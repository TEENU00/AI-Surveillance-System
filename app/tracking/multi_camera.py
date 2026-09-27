from ultralytics import YOLO
import cv2
import threading

model=YOLO(r"models/yolov8n.pt")

# cameras
sources=[
    0,
    0
]

def process_camera(
        cam_id,
        source
):

    cap=cv2.VideoCapture(
        source
    )

    while True:

        ret,frame=cap.read()

        if not ret:

            print(
                f"Camera {cam_id} failed"
            )

            break

        results=model(
            frame
        )

        frame=results[
            0
        ].plot()

        cv2.putText(
            frame,
            f"CAM {cam_id}",
            (20,40),
            cv2.FONT_HERSHEY_SIMPLEX,
            1,
            (0,255,0),
            2
        )

        cv2.imshow(
            f"Camera {cam_id}",
            frame
        )

        if cv2.waitKey(1)==ord(
            "q"
        ):
            break

    cap.release()


threads=[]

for i,src in enumerate(
    sources
):

    t=threading.Thread(
        target=process_camera,
        args=(i,src)
    )

    t.start()

    threads.append(t)

for t in threads:

    t.join()

cv2.destroyAllWindows()