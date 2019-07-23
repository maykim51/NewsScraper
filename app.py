from flask import Flask, jsonify, request, render_template

app = Flask(__name__)

articles = [

]
count  = 0


## HTML을 주는 부분
@app.route('/')
def home():
    return 'This is Home!'

@app.route('/mypage')
def mypage():
    return render_template('index.html')



@app.route('/post', methods=['POST'])
def post():
    global articles            # 이 함수 안에서 나오는 articles 글로벌 변수를 가리킵니다.
    global count

    url_receive = request.form['url']          # 클라이언트로부터 url을 받는 부분
    comment_receive = request.form['comment']  # 클라이언트로부터 comment를 받는 부분

    count += 1
    article = {'url':url_receive,'comment':comment_receive, 'index': count} # 받은 걸 딕셔너리로 만들고,

    articles[count] = article   # 넣는다

    return jsonify({'result':'success'})



@app.route('/post', methods = ['GET'])
def view():
    print(articles)
    return jsonify({'result': 'success', 'articles': articles})


@app.route('/post', methods = ['GET'])
def view_article():
    index = request.args.get('index')


@app.route('/post', methods=['DELETE'])
def delete_order():
    global articles
    received_index = request.form['index']
    print("received {}".format(received_index))

    for article in orders:
        if str(order['index']) == str(received_index):
            articles.remove(article)
            return jsonify({'result': 'success', 'orders': articles})

    return jsonify({'result': 'fail'})



#run app
if __name__ == '__main__':
    app.run('0.0.0.0', port=5000, debug = True)