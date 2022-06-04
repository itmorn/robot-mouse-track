from flask import Flask,render_template,request
from flask import jsonify
import json
from flask_cors import CORS  # 导入模块
app = Flask(__name__)
CORS(app, supports_credentials=True)  # 设置跨域


@app.route('/sendAjax2', methods=['POST'])
def sendAjax2():
    # password = request.form.get('password')
    # username = request.args.get('username')

    data = json.loads(request.form.get('data'))
    username = data['username']
    password = data['username']
    print(username)
    print(password)
    return "46575"

if __name__ == '__main__':
    app.run()