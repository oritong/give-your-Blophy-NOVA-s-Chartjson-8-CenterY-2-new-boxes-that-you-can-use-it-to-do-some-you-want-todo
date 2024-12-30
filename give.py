import json
import os

# 获取当前脚本所在的文件夹路径
current_folder = os.path.dirname(os.path.realpath(__file__))

# 强制将工作目录设置为脚本所在目录
os.chdir(current_folder)

# 定义要插入的 boxEvents 数据
new_box_event = {
    "boxEvents": {
        "speed": [{"startBeats": {"integer": 0, "molecule": 0, "denominator": 1, "currentBPM": 0.0, "ThisStartBPM": 0.0},
                   "endBeats": {"integer": 1, "molecule": 0, "denominator": 1, "currentBPM": 0.0, "ThisStartBPM": 1.0},
                   "startValue": 3.0, "endValue": 3.0, "curveIndex": 0, "IsSelected": False}],
        "moveX": [{"startBeats": {"integer": 0, "molecule": 0, "denominator": 1, "currentBPM": 0.0, "ThisStartBPM": 0.0},
                   "endBeats": {"integer": 1, "molecule": 0, "denominator": 1, "currentBPM": 0.0, "ThisStartBPM": 1.0},
                   "startValue": 0.0, "endValue": 0.0, "curveIndex": 0, "IsSelected": False}],
        "moveY": [{"startBeats": {"integer": 0, "molecule": 0, "denominator": 1, "currentBPM": 0.0, "ThisStartBPM": 0.0},
                   "endBeats": {"integer": 1, "molecule": 0, "denominator": 1, "currentBPM": 0.0, "ThisStartBPM": 1.0},
                   "startValue": 0.0, "endValue": 0.0, "curveIndex": 0, "IsSelected": False}],
        "rotate": [{"startBeats": {"integer": 0, "molecule": 0, "denominator": 1, "currentBPM": 0.0, "ThisStartBPM": 0.0},
                    "endBeats": {"integer": 1, "molecule": 0, "denominator": 1, "currentBPM": 0.0, "ThisStartBPM": 1.0},
                    "startValue": 0.0, "endValue": 0.0, "curveIndex": 0, "IsSelected": False}],
        "alpha": [{"startBeats": {"integer": 0, "molecule": 0, "denominator": 1, "currentBPM": 0.0, "ThisStartBPM": 0.0},
                   "endBeats": {"integer": 1, "molecule": 0, "denominator": 1, "currentBPM": 0.0, "ThisStartBPM": 1.0},
                   "startValue": 1.0, "endValue": 1.0, "curveIndex": 0, "IsSelected": False}],
        "scaleX": [{"startBeats": {"integer": 0, "molecule": 0, "denominator": 1, "currentBPM": 0.0, "ThisStartBPM": 0.0},
                    "endBeats": {"integer": 1, "molecule": 0, "denominator": 1, "currentBPM": 0.0, "ThisStartBPM": 1.0},
                    "startValue": 2.7, "endValue": 2.7, "curveIndex": 0, "IsSelected": False}],
        "scaleY": [{"startBeats": {"integer": 0, "molecule": 0, "denominator": 1, "currentBPM": 0.0, "ThisStartBPM": 0.0},
                    "endBeats": {"integer": 1, "molecule": 0, "denominator": 1, "currentBPM": 0.0, "ThisStartBPM": 1.0},
                    "startValue": 2.7, "endValue": 2.7, "curveIndex": 0, "IsSelected": False}],
        "centerX": [{"startBeats": {"integer": 0, "molecule": 0, "denominator": 1, "currentBPM": 0.0, "ThisStartBPM": 0.0},
                     "endBeats": {"integer": 1, "molecule": 0, "denominator": 1, "currentBPM": 0.0, "ThisStartBPM": 1.0},
                     "startValue": 0.5, "endValue": 0.5, "curveIndex": 0, "IsSelected": False}],
        "centerY": [{"startBeats": {"integer": 0, "molecule": 0, "denominator": 1, "currentBPM": 0.0, "ThisStartBPM": 0.0},
                     "endBeats": {"integer": 1, "molecule": 0, "denominator": 1, "currentBPM": 0.0, "ThisStartBPM": 1.0},
                     "startValue": 2.0, "endValue": 2.0, "curveIndex": 0, "IsSelected": True}],
        "lineAlpha": [{"startBeats": {"integer": 0, "molecule": 0, "denominator": 1, "currentBPM": 0.0, "ThisStartBPM": 0.0},
                       "endBeats": {"integer": 1, "molecule": 0, "denominator": 1, "currentBPM": 0.0, "ThisStartBPM": 1.0},
                       "startValue": 0.0, "endValue": 0.0, "curveIndex": 0, "IsSelected": False}],
        "LengthSpeed": 1, "LengthMoveX": 1, "LengthMoveY": 1, "LengthRotate": 1, "LengthAlpha": 1,
        "LengthScaleX": 1, "LengthScaleY": 1, "LengthCenterX": 1, "LengthCenterY": 1, "LengthLineAlpha": 1
    },
    "lines": [{"onlineNotes": [], "onlineNotesLength": -1, "offlineNotes": [], "offlineNotesLength": -1, "OnlineNotesLength": 0, "OfflineNotesLength": 0}]
}

def add_new_box_events():
    # 读取现有的 Chart.json 文件
    chart_file_path = os.path.join(current_folder, 'Chart.json')
    with open(chart_file_path, 'r') as f:
        chart_data = json.load(f)
    
    # 获取 boxes 列表
    boxes = chart_data.get("boxes", [])
    
    # 向 boxes 列表中添加 8 个新的 boxEvents
    for _ in range(8):
        boxes.append(new_box_event)
    
    # 保存更新后的数据回 Chart.json
    with open(chart_file_path, 'w') as f:
        json.dump(chart_data, f, indent=4)

    print(f"Successfully added 8 new boxEvents to {chart_file_path}")

# 调用函数
add_new_box_events()
