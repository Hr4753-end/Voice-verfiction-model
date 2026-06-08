import os
import pickle

from Audio_Utils import get_embedding


DATABASE = "embeddings.pkl"


def enroll_user(username, audio_path):
    if not os.path.exists(audio_path):
        return f"Audio file not found: {audio_path}"

    if os.path.exists(DATABASE):
        with open(DATABASE, "rb") as f:
            db = pickle.load(f)
    else:
        db = {}

    db[username] = get_embedding(audio_path)

    with open(DATABASE, "wb") as f:
        pickle.dump(db, f)

    return f"User '{username}' enrolled successfully."
