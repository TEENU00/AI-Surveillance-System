import streamlit as st
import os
import glob
from pathlib import Path
import cv2
import time

st.set_page_config(
    page_title="AI Surveillance Dashboard",
    layout="wide"
)

st.title("AI Surveillance Dashboard")

placeholder = st.empty()

while True:

    BASE_DIR = Path(__file__).resolve().parents[2]

    alerts_path = BASE_DIR / "outputs" / "alerts"

    BASE_DIR = Path(__file__).resolve().parents[2]

    alerts_path = BASE_DIR / "outputs" / "alerts"

    alert_images = glob.glob(
        str(alerts_path / "*.jpg")
    )

    intrusion_count = len(
        alert_images
    )

    with placeholder.container():

        col1,col2,col3=st.columns(3)

        col1.metric(
            "Intrusions",
            intrusion_count
        )

        col2.metric(
            "Saved Evidence",
            intrusion_count
        )

        col3.metric(
            "System",
            "RUNNING"
        )

        st.subheader(
            "Recent Alerts"
        )

        latest=sorted(
            alert_images,
            reverse=True
        )[:5]

        cols=st.columns(5)

        for i,img_path in enumerate(latest):

            cols[i].image(
                img_path,
                use_container_width=True
            )

    time.sleep(2)