# app.py
from flask import Flask, request, jsonify, render_template
import requests
import json

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        # 從表單中取得使用者輸入的值
        value = request.form.get('value')

        # 將值傳送到R服務進行計算
        response = requests.post('http://localhost:8002/calculate', json={'value': value})

        # 從R服務的回應中取得結果
        result = response.json()['result']

        # 將結果顯示在網頁上
        return render_template('index.html', result=result)
    else:
        return render_template('index.html')


if __name__ == '__main__':
    app.run(port=5000)
