import pickle
import requests as rq
import pymongo

client = pymongo.MongoClient("mongodb+srv://sleepsearch:sleepsearch123@sleepsearchcluster.akq03.mongodb.net/myFirstDatabase?retryWrites=true&w=majority")
db = client.get_database("queryanswers")
queries = db.query

# print(queries.find_one({'tag' : 'insomnia'})["response"]) # THIS ONE

def database_query_label(sentence) : # general purpose

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

  model_0 = pickle.load(open("model_0.pkl", 'rb'))
 
  predict =  model_0.predict([sentence])
  proba = model_0.predict_proba([sentence])
  probability = proba[0][predict][0] * 10

  if predict == [77] and probability < 0.27 : 
    result = "0" # its returning 0 bcs the database cannot found the specified query
  else :
    label = classnames[predict[0]]
    try :
      result = queries.find_one({'tag' : str(label) })["response"]
      result = "(naive bayes) " + str(result)
    except : 
      result = "0"
  return result

# print(database_query_label("kidney cancr ")) # the database still can handle typo
# print(database_query_label("stmch cancer "))
# print(database_query_label("what is python"))
import openai
def gpt_three_query(sentence) : 
  # train data 
  train = f"I am a highly intelligent question answering bot. If you ask me a question that is rooted in truth, I will give you the answer. If you ask me a question that is nonsense, trickery, or has no clear answer, I will respond with \"Unknown\".\n\nQ: What is human life expectancy in the United States?\nA: Human life expectancy in the United States is 78 years.\n\nQ: Who was president of the United States in 1955?\nA: Dwight D. Eisenhower was president of the United States in 1955.\n\nQ: Which party did he belong to?\nA: He belonged to the Republican Party.\n\nQ: What is the square root of banana?\nA: Unknown\n\nQ: How does a telescope work?\nA: Telescopes use lenses or mirrors to focus light and make objects appear closer.\n\nQ: Where were the 1992 Olympics held?\nA: The 1992 Olympics were held in Barcelona, Spain.\n\nQ: How many squigs are in a bonk?\nA: Unknown\n\nQ:{sentence}?\n"
  openai.api_key = "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"
  response = openai.Completion.create(
  engine="davinci",
  prompt= train,
  temperature=0,
  max_tokens=100,
  top_p=1,
  frequency_penalty=0,
  presence_penalty=0,
  stop=["\n"]
  ).choices[0].text
  response = response.split()
  response.pop(0)
  response = " ".join(response)

  if response == "Unknown" :
    response = "0"
  else :
    response = "(gpt3) " + str(response)
  return response

def wolfram_query(sentence) : 
  wolfram_id ="WEXTEU-4LRRU6G988"
  wolfram_url = "http://api.wolframalpha.com/v1/result"
  
  params = {
    'appid': wolfram_id,
    'i': sentence,}

  r = rq.get(wolfram_url, params=params)
  response =  r.text
  
  if response == "Wolfram|Alpha did not understand your input" :
    response = "sorry didnt understand ur input"
  else :
    response = "(wolfram) " + response
  return response 

# print(wolfram_query("what long is normal ruler"))
import wikipedia
def wikipedia_query(sentence) : 
  sentence = sentence.split()

  if sentence[0].lower() == "wikipedia" or sentence[0] == "what" : 
    sentence.pop(0)
    sentence = " ".join(sentence)
    try :
      result = wikipedia.summary(sentence, sentences = 2)
    except : 
      result = "0"
  else :
    result = "0"
  return result

def query(sentence): 
  query_label =  database_query_label(sentence)
  wikipedia_response = wikipedia_query(sentence)
  gpt_response = gpt_three_query(sentence)

  if query_label == "0" : 

    if gpt_response == "0" :
      if wikipedia_response == "0" :
        result = wolfram_query(sentence)
      else :
        result = "(wikipedia) " + str(wikipedia_response)
    else :
      result = gpt_response
  else : 
    # at here we add the mongodb integration
    # that seek our database for answers
    result = query_label

  return result


# query("what is stomach cancer")

# try it right here
# print("~~~")
# print(query("what is insomnia"))
# print(gpt_three_query("How long is a ruler"))

