import json

from flask import Flask
from flask import request
from flask_cors import CORS  # 导入模块
app = Flask(__name__)
CORS(app, supports_credentials=True)  # 设置跨域


@app.route("/predict", methods=["POST"])
def index():
    jsn = request.get_json()
    print(jsn)
    return "ok"


if __name__ == '__main__':
    app.run()
