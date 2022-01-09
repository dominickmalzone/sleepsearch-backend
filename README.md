# sleepsearch-backend
Introducing sleep search, a web app that return any question you search, especially about health problem like sleep, cancer, etc 

## Inspiration

## What it does
just type any question to search, example : what is stomach cancer, what is insomnia, who is the president of US, what is Indonesia. The model will return any question u search  with a straight answer, so u dont have to surf many-many page in traditional search engine like google

## How it works 
this app contain 5 layers of NLP machine learning, NLP deep learning, and a web scrape api.
1. first we have naive bayes model that determine where should our question passed to
2. second we have a naive bayes model again, to understand nlp input from user, and search our database for the answer. **_btw our database can contain up to 1,000,000 data_**. We use google cloud to host the mongodb
3. third, we have deep learning gpt3 model trained in thousand of data, to answer the question if the naive bayes model not quite sure of the answer.
4. fourth, we have wikipedia api and google web scrape api for the backup plan if all our trained model not quite sure of the answer.
5. and last, we have wolfram api for the backup plan if the question cant be answered on previous layers.

but 90% of the question can be answerred by our model 1st until 3rd layer, so the 4th and 5th model is just for a backup plan if our model still not trained on that data

## How we built it
First, Arnav, Evan, and Dominick working on the front end to make some nice and simple web interface, meanwhile Hazel start to scrape some data to train naive bayes model on google colab **_fun fact : we use naive bayes model for nlp bcs it has the best performance with low resource use, meanwhile the tensorflow model is so heavy as well as slow that it cant be deployed on heroku._** Next Arnav and Hazel start to built the backend flask app and connect it to mongodb on google cloud, meanwhile Dominick start to tweak GPT3 a pretrained model. After that we all work together to connect all the model and the frontend. Then we deploy all of it on heroku

## Challenges we ran into
- scraping the data (solved)
- integrating all layers (solved)
- integrating frontend to backend (solved)

## Accomplishments that we're proud of

## What we learned

## What's next for Sleep Search
- We will train our model periodically so the model will always up to date
- We will add more answers on our database
## Our team
- [Arnav Pandey](https://github.com/Splitxorpio)
- [Dominick](https://github.com/dominickmalzone)
- [Evan](https://github.com/evanstech12345)
- [Hazel Handrata](https://github.com/kittyofheaven)
