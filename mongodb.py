import pymongo

client = pymongo.MongoClient("mongodb+srv://sleepsearch:sleepsearch123@sleepsearchcluster.akq03.mongodb.net/myFirstDatabase?retryWrites=true&w=majority")
db = client.get_database("queryanswers")
queries = db.query

classnames = ['adobe creative cloud', 'adobe xd', 'airbnb', 'amazon',
        'amazon prime', 'angular', 'apple', 'apple music', 'apple tv',
        'arduino', 'brain cancer', 'breast cancer', 'c', 'c#', 'c++',
        'cancer', 'cat', 'covid19_summary', 'cryptocurrency', 'css',
        'django', 'dog', 'earthquake', 'excessive daytime sleepiness',
        'express', 'facebook', 'flask', 'github', 'gmail', 'google',
        'google cloud', 'google play', 'hackathon', 'heart cancer', 'html',
        'hulu', 'insomnia', 'instagram', 'java', 'javascript',
        'kidney cancer', 'kotlin', 'laravel', 'linkedin', 'liver cancer',
        'lung cancer', 'lyft', 'microsoft', 'microsoft access',
        'microsoft excel', 'microsoft office', 'microsoft onenote',
        'microsoft outlook', 'microsoft powerpoint', 'microsoft word',
        'minecraft', 'mouse', 'narcolepsy', 'netflix', 'node',
        'objective c', 'parasomnia', 'php', 'python', 'rat', 'react',
        'restless legs syndrome', 'revolutions', 'rich people', 'ruby',
        'shift work disorder', 'slack', 'sleep apnea', 'sleeping',
        'spotify', 'stackoverflow', 'stock market', 'stomach cancer',
        'swift', 'tesla', 'travel', 'trello', 'tsunami', 'twilio',
        'twitter', 'uber', 'valorant', 'volcano', 'vue', 'world war 1',
        'world war 2', 'youtube', 'youtube music']


## CHANGE THIS FOR EVERY CLASS ##
# start from the airbnb
new_document = { 
    'tag' : "amazon prime",
    'response' : "Amazon Prime is a paid subscription program from Amazon which is available in various countries and gives users access to additional services otherwise unavailable or available at a premium to other Amazon customers. Services include same, one or two-day delivery of goods and streaming music, video, e-books, gaming and grocery shopping services."
} # dont forget to save it first before commit
try :
    queries.insert_one(new_document)
    print('done inserting')
except : 
    print("something is error")