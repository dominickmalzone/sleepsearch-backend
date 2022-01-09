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
github_document = { 
    'tag' : "github",
    'response' : "GitHub, Inc. is a provider of Internet hosting for software development and version control using Git. It offers the distributed version control and source code management functionality of Git, plus its own features. It provides access control and several collaboration features such as bug tracking, feature requests, task management, continuous integration and wikis for every project. Headquartered in California, it has been a subsidiary of Microsoft since 2018."
} # dont forget to save it first before commit
gmail_document = {
    'tag' : "gmail",
    'response' : "Gmail is a free email service provided by Google. As of 2019, it had 1.5 billion active users worldwide. A user typically accesses Gmail in a web browser or the official mobile app. Google also supports the use of email clients via the POP and IMAP protocols."
}
google_document = {
    'tag' : "google",
    'response' : "Google LLC is an American multinational technology company that specializes in Internet-related services and products, which include online advertising technologies, a search engine, cloud computing, software, and hardware."
}
google_cloud_document = {
    'tag' : "google cloud",
    'response' : "Google Cloud Platform, offered by Google, is a suite of cloud computing services that runs on the same infrastructure that Google uses internally for its end-user products, such as Google Search, Gmail, Google Drive, and YouTube."
}
google_play_document = {
    'tag' : "google play",
    'response' : "Google Play, also branded as the Google Play Store and formerly Android Market, is a digital distribution service operated and developed by Google. It serves as the official app store for certified devices running on the Android operating system and its derivatives as well as Chrome OS, allowing users to browse and download applications developed with the Android software development kit (SDK) and published through Google. Google Play also serves as a digital media store, offering music, books, movies, and television programs."
}
hackathon_document = {
    'tag' : "hackathon",
    'response' : "A hackathon is a design sprint-like event; often, in which computer programmers and others involved in software development, including graphic designers, interface designers, project managers, domain experts, and others collaborate intensively on software projects."
}
heart_cancer_document = {
    'tag' : "heart cancer",
    'response' : "Heart cancer occurs when diseased cells grow out of control on or near the heart. These cells form a tumor. Cancer that begins in the heart is primary heart cancer. This form of heart cancer is extremely rare."
}
html_document = {
    'tag' : "html",
    'response' : "The HyperText Markup Language, or HTML is the standard markup language for documents designed to be displayed in a web browser. It can be assisted by technologies such as Cascading Style Sheets and scripting languages such as JavaScript."
}
hulu_document = {
    'tag' : "hulu",
    'response' : "Hulu is an American streaming platform. Launched on October 29, 2007, it offers a library of films and television series from networks such as CBS, ABC, NBC, or FX, as well as Hulu original content. Hulu is currently only available in the United States."
}
try :
    queries.insert_one(github_document)
    queries.insert_one(gmail_document)
    queries.insert_one(google_document)
    queries.insert_one(google_cloud_document)
    queries.insert_one(google_play_document)
    queries.insert_one(hackathon_document)
    queries.insert_one(heart_cancer_document)
    queries.insert_one(html_document)
    print('done inserting')
except : 
    print("something is error")