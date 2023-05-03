from flask import Flask,request
from bs4 import BeautifulSoup 
app = Flask(__name__)

@app.route("/",methods=['GET'])
def hello():
    return "Hello, World!"

@app.route("/",methods=['POST'])
def query():
    linked_in = request.get('linked_in')
    page_content = requests.get(linked_in)
    soup = BeautifulSoup(page_content.content,'html.parser') 


if __name__ == '__main__':
    app.run(debug=True)