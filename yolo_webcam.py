import cv2
import time
import pyttsx3
import threading
from ultralytics import YOLO

model = YOLO("yolov8n.pt")


def say(texto):
    threading.Thread(target=_say, args=(texto,), daemon=True).start()


def _say(text):
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()
    engine.stop()


cam = cv2.VideoCapture(0)

if not cam.isOpened():
    raise Exception("Não foi possível abrir a webcam")

while True:
    print("▶ Iniciando análise por 3 segundos...")

    inicio = time.time()
    ultimo_objeto = None

    while time.time() - inicio < 3:
        ok, frame = cam.read()
        if not ok:
            print(" Erro ao capturar frame")
            break

        results = model.predict(frame, verbose=False)

        for r in results:
            for box in r.boxes:
                cls_id = int(box.cls)
                nome = r.names[cls_id]
                conf = float(box.conf)

                ultimo_objeto = nome
                print(f"Objeto detectado: {nome} ({conf:.2f})")

        cv2.imshow("Webcam", frame)
        if cv2.waitKey(1) == 27:
            break

    print("⏹ Encerrando análise.")

    if ultimo_objeto:
        print(f"🔊Falando: {ultimo_objeto}")
        say(f"Objeto detectado: {ultimo_objeto}")

    print("Aguardando 10 segundos...")
    time.sleep(10)
