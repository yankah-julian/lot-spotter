import cv2
import boto3
import json
import time
from sensor import UltrasonicSensor
from sync import DynamoSync

# Initialize
cap = cv2.VideoCapture(0)
sensor = UltrasonicSensor(trig_pin=23, echo_pin=24)
db = DynamoSync()

# Load pre-trained vacancy classifier
net = cv2.dnn.readNetFromONNX('models/vacancy_classifier.onnx')

LOT_ID = "lot_ksu_main"
SPACES = 48


def classify_frame(frame):
    """Run inference on a parking lot frame."""
    blob = cv2.dnn.blobFromImage(frame, 1/255.0, (224, 224), swapRB=True)
    net.setInput(blob)
    output = net.forward()
    return output[0]  # confidence scores per space


def main():
    print(f"[LotSpotter] Starting detection for {LOT_ID}...")
    while True:
        ret, frame = cap.read()
        if not ret:
            continue

        scores = classify_frame(frame)
        distance = sensor.read()

        occupancy = {
            f"space_{i}": bool(scores[i] > 0.5)
            for i in range(SPACES)
        }

        db.update_lot(LOT_ID, occupancy, distance)
        print(f"[LotSpotter] Updated: {sum(occupancy.values())}/{SPACES} occupied")
        time.sleep(2)


if __name__ == "__main__":
    main()
