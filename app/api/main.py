from fastapi import FastAPI
import cv2

from app.tracking.track import run_tracking
from app.tracking.crowd_count import run_crowd
from app.tracking.intrusion import run_intrusion
from app.detection.fire_detection import run_fire

app = FastAPI()


@app.get("/")

def home():

    return {

        "status":"running"

    }


@app.get("/analyze")

def analyze():

    VIDEO_SOURCE="videos/test.mp4"

    cap=cv2.VideoCapture(
        VIDEO_SOURCE
    )

    if not cap.isOpened():

        return {

            "status":"error",

            "message":"video failed"

        }

    results={

        "frames":0,

        "intrusions":0,

        "max_people":0,

        "fire":False,

        "total_tracks":0

    }

    while True:

        ret,frame=cap.read()

        if not ret:

            break


        # -------------------
        # TRACKING
        # -------------------

        tracking=run_tracking(
            frame
        )

        tracks=tracking[
            "tracks"
        ]


        # -------------------
        # CROWD
        # -------------------

        crowd=run_crowd(
            tracks
        )


        # -------------------
        # INTRUSION
        # -------------------

        intrusion=run_intrusion(

            tracks,

            frame

        )


        # -------------------
        # FIRE
        # -------------------

        fire=run_fire(
            frame
        )


        results["frames"] += 1

        results["intrusions"] += intrusion[
            "intrusions"
        ]

        results["max_people"]=max(

            results["max_people"],

            crowd[
                "people"
            ]

        )

        results["total_tracks"] += len(
            tracks
        )

        if fire["fire"]:

            results["fire"]=True


    cap.release()


    return results