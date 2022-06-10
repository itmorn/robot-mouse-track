from flask import Flask
from flask import request
from flask_cors import CORS  # 导入模块

app = Flask(__name__)
CORS(app, supports_credentials=True)  # 设置跨域
from mouse_track import MouseTrack
import matplotlib.pyplot as plt


@app.route("/predict", methods=["POST"])
def index():
    trace = request.get_json()
    print(trace)
    mouse_track = MouseTrack(trace)
    mouse_track.show_track()

    lst_derivative_to_xy = mouse_track.get_feature_dev(order=2)

    for idx,arr_feature in enumerate(lst_derivative_to_xy):
        plt.figure()
        plt.plot(mouse_track.arr_time[:len(arr_feature)], arr_feature[:, 0])
        plt.show()


    return "ok"


if __name__ == '__main__':
    app.run()
