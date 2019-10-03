from flask import Flask, render_template, jsonify, request
app = Flask(__name__)

import requests
from bs4 import BeautifulSoup

from pymongo import MongoClient
client = MongoClient('localhost', 27017)
db = client.dbsparta

## HTML을 주는 부분
@app.route('/')
def home():
   return 'This is Home!'

@app.route('/mypage')
def mypage():
   return render_template('index.html')


## API 역할을 하는 부분
@app.route('/post', methods=['POST'])
def post():
   url_receive = request.form['url_give']  # 클라이언트로부터 url을 받는 부분
   comment_receive = request.form['comment_give']  # 클라이언트로부터 comment를 받는 부분

   headers = {
      'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}
   data = requests.get(url_receive, headers=headers)

   soup = BeautifulSoup(data.text, 'html.parser')

   og_image = soup.select_one('meta[property="og:image"]')
   og_title = soup.select_one('meta[property="og:title"]')
   og_description = soup.select_one('meta[property="og:description"]')

   url_image = og_image['content']
   url_title = og_title['content']
   url_description = og_description['content']

   article = {'url': url_receive, 'comment': comment_receive, 'image': url_image, 'title': url_title, 'desc': url_description}

   db.articles.insert_one(article)

   return jsonify({'result': 'success'})

@app.route('/post', methods=['GET'])
def view():
   posts = db.articles.find({},{'_id':0})
   return jsonify({'result':'success', 'articles':list(posts)})

if __name__ == '__main__':
   app.run('0.0.0.0',port=5000,debug=True)