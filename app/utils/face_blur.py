import cv2

face_cascade = cv2.CascadeClassifier(

    cv2.data.haarcascades +

    "haarcascade_frontalface_default.xml"

)

def blur_faces(frame):

    gray=cv2.cvtColor(
        frame,
        cv2.COLOR_BGR2GRAY
    )

    faces=face_cascade.detectMultiScale(

        gray,

        1.1,

        4

    )

    for x,y,w,h in faces:

        roi=frame[
            y:y+h,
            x:x+w
        ]

        roi=cv2.GaussianBlur(

            roi,

            (99,99),

            30

        )

        frame[
            y:y+h,
            x:x+w
        ]=roi

    return frame