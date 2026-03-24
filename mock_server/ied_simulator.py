# data source, 作用：模拟保护继电器（IED）, 61850 接口数据上报电流值

from flask import Flask, jsonify
import random

app = Flask(__name__)

# 模拟 61850 MMS 报文数据 (MMS: Manufacturing Message Specification)
# 这是工业设备传输实时数据最常用的协议
@app.route('/mms/dataset/read', methods=['GET'])
def read_protocol_data():
    # 模拟电流值 (Current Value)
    current_val = round(random.uniform(10.5, 12.0), 2)
    return jsonify({
        "Reference": "LD0/MMXU1.A.phsA", # 61850 逻辑节点路径
        "Value": current_val,
        "Unit": "A",
        "Quality": "Good" # 信号质量 (Signal Quality)
    })

if __name__ == '__main__':
    # 模拟设备运行在 5000 端口
    app.run(port=5000)
