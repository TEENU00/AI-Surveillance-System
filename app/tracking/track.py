from ultralytics import YOLO
from deep_sort_realtime.deepsort_tracker import DeepSort

import cv2


model=YOLO(
    "models/yolov8n.pt"
)


tracker=DeepSort(

    max_age=30

)


def run_tracking(
    frame
):

    detections=[]


    results=model(

        frame,

        verbose=False

    )


    for result in results:

        for box in result.boxes:

            cls=int(
                box.cls[0]
            )

            if cls!=0:

                continue


            x1,y1,x2,y2=box.xyxy[
                0
            ]


            conf=float(
                box.conf[0]
            )


            detections.append(

                (

                [

                float(x1),

                float(y1),

                float(x2-x1),

                float(y2-y1)

                ],

                conf,

                "person"

                )

            )


    tracks=tracker.update_tracks(

        detections,

        frame=frame

    )


    people=[]


    for track in tracks:

        if not track.is_confirmed():

            continue


        tid=track.track_id


        x1,y1,x2,y2=map(

            int,

            track.to_ltrb()

        )


        people.append(

            {

            "id":tid,

            "bbox":[

                x1,

                y1,

                x2,

                y2

            ]

            }

        )


    return {

        "tracks":

        people,

        "frame":

        frame

    }