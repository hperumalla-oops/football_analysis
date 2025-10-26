# from roboflow import Roboflow
# rf = Roboflow(api_key="pVcVwRAHEiX6pBCrIcZX")
# project = rf.workspace("roboflow-jvuqo").project("football-players-detection-3zvbc")
# version = project.version(1)
# dataset = version.download("yolov8")
                

import shutil

shutil.move('football-players-detection-1/train',
            'football-players-detection-1/football-players-detection-1/train'
            )

shutil.move('football-players-detection-1/test',
            'football-players-detection-1/football-players-detection-1/test'
            )

shutil.move('football-players-detection-1/valid',
            'football-players-detection-1/football-players-detection-1/valid'
            )

