# 🎙️ Voice Verification Demo

A Python-based Speaker Verification System built using the ECAPA-TDNN architecture and SpeechBrain. This project demonstrates how voice biometrics can be used for secure user authentication by comparing speaker embeddings generated from voice recordings.

---

## 🚀 Features

* User Enrollment
* Speaker Verification
* Voice Embedding Generation
* Cosine Similarity Matching
* Modular Project Structure
* Pretrained ECAPA-TDNN Model
* FastAPI Integration Ready
* Easy to Extend and Customize

---

## 📂 Project Structure

```text
voice-verification-demo/
│
├── app/
│   ├── enroll.py
│   ├── verify.py
│   ├── recorder.py
│   ├── audio_utils.py
│   ├── model.py
│   └── database/
│       └── embeddings.pkl
│
├── samples/
│
├── requirements.txt
├── main.py
└── README.md
```

---

## 🧠 How It Works

```text
Voice Input
     ↓
Audio Recording
     ↓
Feature Extraction
     ↓
ECAPA-TDNN Model
     ↓
Speaker Embedding
     ↓
Cosine Similarity
     ↓
Verification Decision
```

### Enrollment Phase

1. Record user's voice.
2. Generate speaker embedding.
3. Store embedding in database.

### Verification Phase

1. Record new voice sample.
2. Generate embedding.
3. Compare with stored embedding.
4. Return VERIFIED or NOT VERIFIED.

---

## 🛠️ Technologies Used

* Python
* PyTorch
* SpeechBrain
* ECAPA-TDNN
* Librosa
* SoundDevice
* NumPy
* Scikit-Learn
* FastAPI

---

## 📦 Installation

Clone the repository:

```bash
git clone https://github.com/yourusername/voice-verification-demo.git
cd voice-verification-demo
```

Create virtual environment:

```bash
python -m venv venv
```

Activate environment:

### Windows

```bash
venv\Scripts\activate
```

### Linux/Mac

```bash
source venv/bin/activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

---

## ▶️ Running the Project

Start the application:

```bash
python main.py
```

Choose:

```text
1. Enroll
2. Verify
```

Follow the prompts to record audio and test verification.

---

## 📊 Verification Method

The project uses cosine similarity to compare speaker embeddings.

A similarity score above a predefined threshold indicates that both recordings belong to the same speaker.

---

## 🔒 Future Improvements

* Anti-Spoofing Detection
* Deepfake Voice Detection
* Noise Reduction
* Real-Time Streaming Verification
* Web Dashboard
* Database Integration
* Multi-User Management
* Cloud Deployment

---

## 🎯 Learning Outcomes

This project helps understand:

* Speaker Verification
* Voice Biometrics
* Deep Learning for Audio
* Embedding Generation
* Cosine Similarity
* Model Deployment
* API Development

---

## 📜 License

This project is released under the MIT License.

---

## 👨‍💻 Author

Developed as an internship project to demonstrate practical implementation of speaker verification using deep learning and modern voice biometric technologies.
