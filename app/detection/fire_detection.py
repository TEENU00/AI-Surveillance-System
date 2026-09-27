# from ultralytics import YOLO
# import cv2
# import time

# model = YOLO(r"models/fire_smoke.pt")

# cap = cv2.VideoCapture(0)

# last_alert = 0

# while True:

#     ret,frame = cap.read()

#     if not ret:
#         break

#     results = model(
#         frame
#     )

#     fire_detected=False

#     for result in results:

#         boxes=result.boxes

#         for box in boxes:

#             cls=int(
#                 box.cls[0]
#             )

#             conf=float(
#                 box.conf[0]
#             )

#             x1,y1,x2,y2=map(
#                 int,
#                 box.xyxy[0]
#             )

#             label=model.names[
#                 cls
#             ]

#             if label.lower() in [
#                 "fire",
#                 "smoke"
#             ]:

#                 fire_detected=True

#                 cv2.rectangle(
#                     frame,
#                     (x1,y1),
#                     (x2,y2),
#                     (0,0,255),
#                     2
#                 )

#                 cv2.putText(
#                     frame,
#                     f"{label}:{conf:.2f}",
#                     (x1,y1-10),
#                     cv2.FONT_HERSHEY_SIMPLEX,
#                     0.7,
#                     (0,0,255),
#                     2
#                 )

#     if fire_detected:

#         cv2.putText(
#             frame,
#             "DANGER",
#             (30,50),
#             cv2.FONT_HERSHEY_SIMPLEX,
#             1.2,
#             (0,0,255),
#             3
#         )

#         if time.time()-last_alert>20:

#             print(
#                 "FIRE ALERT"
#             )

#             last_alert=time.time()

#     cv2.imshow(
#         "Fire Detection",
#         frame
#     )

#     if cv2.waitKey(1)==ord(
#         "q"
#     ):
#         break

# cap.release()

# cv2.destroyAllWindows()

def run_fire(frame):

    return {

        "fire":False

    }