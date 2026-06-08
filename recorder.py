import sounddevice as sd
from scipy.io.wavfile import write

def record_audio(filename, duration, fs):
    print("Recording...")
    audio = sd.rec(
        int(duration * fs),
            samplerate=fs,
            channels=2
    )
    
    sd.wait()
    
    write(filename, fs, audio)
    print("Recording finished and saved as", filename)
