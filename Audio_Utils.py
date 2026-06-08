import torch
from scipy.io import wavfile
from scipy.signal import resample_poly

from model import verification

TARGET_SAMPLE_RATE = 16000


def get_embedding(audio_path):
    sample_rate, waveform_np = wavfile.read(audio_path)

    if waveform_np.ndim > 1:
        waveform_np = waveform_np.mean(axis=1)

    waveform_np = waveform_np.astype("float32")
    peak = max(abs(waveform_np).max(), 1.0)
    waveform_np = waveform_np / peak

    if sample_rate != TARGET_SAMPLE_RATE:
        waveform_np = resample_poly(
            waveform_np, TARGET_SAMPLE_RATE, sample_rate
        ).astype("float32")

    waveform = torch.from_numpy(waveform_np).unsqueeze(0)

    # encode_batch expects shape [batch, time].
    embedding = verification.encode_batch(waveform)
    return embedding
