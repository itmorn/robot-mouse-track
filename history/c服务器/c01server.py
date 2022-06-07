import json

from flask import Flask
from flask import request
from flask_cors import CORS  # 导入模块

app = Flask(__name__)
CORS(app, supports_credentials=True)  # 设置跨域
from d轨迹检测.d01轨迹检测 import MouseTrajectoryAnalyzer
import matplotlib.pyplot as plt


@app.route("/predict", methods=["POST"])
def index():
    trace = request.get_json()

    mta = MouseTrajectoryAnalyzer(trace)
    mta.show_track()

    lst_derivative_to_xy = mta.get_feature_dev_partial(order=2)

    for idx,arr_dev_order in enumerate(lst_derivative_to_xy):
        plt.figure()
        plt.plot(arr_dev_order[:, -1], arr_dev_order[:, 0])#, "*"
        plt.ylabel(f"x order {idx}")
        plt.show()

    for idx,arr_dev_order in enumerate(lst_derivative_to_xy):
        plt.figure()
        plt.plot(arr_dev_order[:, -1], arr_dev_order[:, 1])#, "*"
        plt.ylabel(f"y order {idx}")
        plt.show()

    return "ok"


if __name__ == '__main__':
    app.run()
