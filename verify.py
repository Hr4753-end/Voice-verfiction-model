import os
import pickle
from sklearn.metrics.pairwise import cosine_similarity

from Audio_Utils import get_embedding


DATABASE = "embeddings.pkl"
THRESHOLD = 0.75


def _to_2d_numpy(tensor_embedding):
    arr = tensor_embedding.squeeze(0).detach().cpu().numpy()
    if arr.ndim == 1:
        arr = arr.reshape(1, -1)
    return arr


def verify_user(username, audio_path):
    if not os.path.exists(DATABASE):
        return f"Database not found: {DATABASE}"

    if not os.path.exists(audio_path):
        return f"Audio file not found: {audio_path}"

    with open(DATABASE, "rb") as f:
        db = pickle.load(f)

    if username not in db:
        return "User not found"

    stored_embedding = db[username]
    new_embedding = get_embedding(audio_path)

    similarity = cosine_similarity(
        _to_2d_numpy(stored_embedding),
        _to_2d_numpy(new_embedding),
    )[0][0]

    print("Similarity:", similarity)
    if similarity > THRESHOLD:
        return "VERIFIED"
    return "NOT VERIFIED"
