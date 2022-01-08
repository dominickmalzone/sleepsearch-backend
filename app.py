from flask import Flask, render_template, request, jsonify
from flask_restful import Api, Resource, reqparse
from flask import jsonify
from flask_mongoengine import MongoEngine
import requests
from bs4 import BeautifulSoup
import wikipedia
import pymongo
client = pymongo.MongoClient("mongodb+srv://evans:Bellwood30@cluster0.luckw.mongodb.net/myFirstDatabase?retryWrites=true&w=majority")
app = Flask(__name__)
api = Api(app)
app.config['MONGODB_SETTINGS'] = {
    'db': 'sleepSearch',
    'host': 'localhost',
    'port': 27017
}
db = MongoEngine()
db.init_app(app)

search_put_args = reqparse.RequestParser()
search_put_args.add_argument('data', type=str, help="insert search data here", required = True)

# @app.route('/search', methods=['GET','POST'])
# def generate_search_results():
#     if request.method == "POST":
#         data = str(request.json["data"])
#         print(data)
#         return data



def query(user_query):
    URL = "https://www.google.co.in/search?q=" + user_query

    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.90 Safari/537.36 Edg/89.0.774.57'
    }
    page = requests.get(URL, headers=headers)
    soup = BeautifulSoup(page.content, 'html.parser')
    if soup.find(class_='Z0LcW') != None:
        result = soup.find(class_='Z0LcW').get_text()
    elif soup.find(class_='thODed') != None:
        result = soup.find(class_='thODed').get_text()
    else:
        result = "sorry no result found"
    result = result.encode('ascii', 'ignore').decode('ascii')
    return result



def search_engine(search_data : str) : 
    pass


class Search(Resource) : 
    def post(self): 
        args = dict(search_put_args.parse_args())
        search_data = args['data'] 
        print(search_data)
        result = query(search_data)
        print(result)
        json_result = jsonify({"result" : result})
        return json_result
        # return "result : " + result
    
    def get(self): 
        args = dict(search_put_args.parse_args())
        search_data = args['data'] 
        print(search_data)
        result = query(search_data)
        print(result)
        return "result : " +result

@app.route('/')
def index():
    return render_template("index.html")

api.add_resource(Search,"/search")

if __name__ == "__main__":
    app.run(debug=True)