from sklearn.externals import joblib
import pandas as pd

print "Loading Models..."
# Be aware to use Python 2.7
tfidf = joblib.load("./models/tfidf.pkl")
clf = joblib.load("./models/cx.pkl")

filename = "./data/data.csv" # Your data
column_to_analyze = "text"
output_filename = "./data/prediction.csv"

# Loading data
df = pd.read_csv(filename)
print "Total number of samples: ", len(df)

# Predicting...
tfidf_scores = tfidf.transform(df[column_to_analyze])
prediction = clf.predict(tfidf_scores)
df['prediction'] = prediction
df['prediction'] = df['prediction'].apply(pd.to_numeric)
print "Number of detected CX messages: ", len(df[df['prediction'] == 1])

# Saving results
df.to_csv(output_filename)
