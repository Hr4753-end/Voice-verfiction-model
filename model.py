from speechbrain.inference.speaker import SpeakerRecognition
from speechbrain.utils.fetching import LocalStrategy


def load_verification_model():
    # COPY avoids Windows symlink permission failures during HF model fetch.
    return SpeakerRecognition.from_hparams(
        source="speechbrain/spkrec-ecapa-voxceleb",
        savedir="pretrained_models",
        local_strategy=LocalStrategy.COPY,
    )


verification = load_verification_model()
print("Model loaded successfully.")
