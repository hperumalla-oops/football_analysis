from ultralytics import YOLO 

best=r"C:\Users\hperu\fbvision\yolo_inference\models\best.pt"
model = YOLO(best)

path=r"C:\Users\hperu\fbvision\input_vid\08fd33_4.mp4"
results = model.predict(path,save=True,project='my_outputs', name='best_inference')
print(results[0])
print('=====================================')
for box in results[0].boxes:
    print(box)