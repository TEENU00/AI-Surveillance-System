def run_crowd(
    tracks
):

    people=0


    confirmed_tracks=[]


    for track in tracks:

        # DeepSORT object
        if hasattr(
            track,
            "is_confirmed"
        ):

            if not track.is_confirmed():

                continue


            confirmed_tracks.append(
                track
            )

        else:

            confirmed_tracks.append(
                track
            )


    people=len(
        confirmed_tracks
    )


    crowd="LOW"


    if people>=3:

        crowd="MEDIUM"


    if people>=6:

        crowd="HIGH"


    density="NORMAL"


    if people>=10:

        density="DENSE"


    if people>=20:

        density="CRITICAL"


    return {

        "people":

        people,

        "crowd":

        crowd,

        "density":

        density

    }