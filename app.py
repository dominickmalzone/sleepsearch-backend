from flask import Flask, render_template, request, jsonify
app = Flask(__name__)
@app.route('/search', methods=['GET','POST'])
def generate_search_results():
    if request.method == "POST":
        data = str(request.json["data"])
        return data
@app.route('/')
def index():
    return render_template("index.html")
if __name__ == "__main__":
    app.run(debug=True)