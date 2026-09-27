import cv2
import numpy as np
from pathlib import Path

from app.alerts.email_alert import send_alert


# -------------------------
# Intrusion Zone
# -------------------------

zone=np.array(

[
[150,100],
[500,100],
[500,400],
[150,400]

],

dtype=np.int32

)


# -------------------------
# Output Folder
# -------------------------

alert_dir=Path(
    "outputs/alerts"
)

alert_dir.mkdir(

    parents=True,

    exist_ok=True

)


saved_ids=set()


# -------------------------
# Main Intrusion Function
# -------------------------

def run_intrusion(

    tracks,

    frame

):

    intrusions=0


    cv2.polylines(

        frame,

        [zone],

        True,

        (0,0,255),

        3

    )


    for track in tracks:


        if "bbox" not in track:

            continue


        tid=track[
            "id"
        ]


        x1,y1,x2,y2=track[
            "bbox"
        ]


        cx=(x1+x2)//2

        cy=(y1+y2)//2


        inside=cv2.pointPolygonTest(

            zone,

            (

                cx,

                cy

            ),

            False

        )


        if inside < 0:

            continue


        intrusions += 1


        # Draw Intrusion Box

        cv2.rectangle(

            frame,

            (x1,y1),

            (x2,y2),

            (0,0,255),

            3

        )


        cv2.putText(

            frame,

            f"ID {tid}",

            (x1,y1-10),

            cv2.FONT_HERSHEY_SIMPLEX,

            0.8,

            (0,0,255),

            2

        )


        cv2.putText(

            frame,

            "INTRUSION",

            (40,50),

            cv2.FONT_HERSHEY_SIMPLEX,

            1,

            (0,0,255),

            3

        )


        if tid not in saved_ids:

            saved_ids.add(
                tid
            )


            filename=alert_dir / f"{tid}.jpg"


            success=cv2.imwrite(

                str(filename),

                frame

            )


            print(

                "SAVE:",

                success,

                filename

            )


            print(
                "EMAIL TRIGGERED"
            )


            try:

                send_alert(

                    str(filename)

                )

                print(
                    "EMAIL SENT"
                )

            except Exception as e:

                print(

                    "EMAIL ERROR:",

                    e

                )


    return {

        "intrusions":

        intrusions

    }