# Customer Experience Automated Detection
Binary text categorization classifier which detects the presence or not of customer experience manifestations in a message.   
    
#### Examples of messages that the classifier will detect as related to CX:   
- I want to give a huge shout out and thanks to @nordstromrack employee #10010692. He processed my return on Monday and made it so pleasant! No judgement or complaining about the task despite a huge box of stuff. He was so friendly! Thank you!
- I had a horrible experience at your store in Weirton WV and I left my groceries and went to Walmart instead. I wish you hired employees that better customer service skills because after 20yrs of shopping their I may as well not go back.
- Followed all advice online on how to fix the 'moisture detected in charge port' error on note8. Keeps coming back for months. Phone hasn't ever been wet. Cannot charge. Sitting in a goddamn car balancing on wireless charging pad.
- Great customer experience!
- Im in love with your store

#### Examples of messages that the classifier will detect as NOT related to CX:   
- Congratulations to Jessica who was hired to work on The Dollar Tree!
- No matter how many times you click, you are forced to watch the dammed tjmaxx commercial! 
- IKEA is calling on the nation to join the Last Straw campaign to ensure it has a lasting impact on the planet
- I want that bag! 
- very chic!

## Algorithm
- Logistic Regression 

## Training 
Trained using 4000 samples of Tweets mentioning brands from the following industries: apparel, bank, big box, book, boutique, convenience, cosmetics, department, electronics, food, furniture, gift shop, jewerly, office supplies, pet, pharmacy, sporting goods, supermarket, warehouse. 

### Training Features
Text transformed to vector space using TF-IDF.

For better results, test must be preprocessed: 
- Removed non-alphabetic characters, emoticons, mentions, URLs.   
- Removed stop words (e.g. from, in, on).   
- Lemmatization

## Results
On a fixed sample of 1000 tweets not used for training:
- **Accuracy**: 0.912    
- **F-Score**: 0.914 

On a fixed sample of 2000 messages from Facebook:
- **Accuracy**: 0.787    


## Reference
- Kuffo, L., Vaca, C., Izquierdo, E., & Bustamante, J. C. (2018, December). Know your customer: Detection of Customer Experience (CX) in Social Platforms using Text Categorization. In 2018 IEEE International Conference on Big Data (Big Data) (pp. 4086-4094). IEEE.
