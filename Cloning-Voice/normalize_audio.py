import librosa
import numpy as np
import soundfile as sf
def normalize_audio(audio_path):
    # Load audio file
    audio, sr = librosa.load(audio_path, sr=None)

    # Normalize the audio
    normalized_audio = librosa.util.normalize(audio)

    # Scale the audio to 16-bit integers
    normalized_audio = (normalized_audio * 32767).astype(np.int16)

    return normalized_audio, sr

# Example usage
audio_path = "data/train/lopi.wav"

normalized_audio, sample_rate = normalize_audio(audio_path)

# Save the normalized audio as a new file
output_path = "data/train1/normalized_lopi.wav"
sf.write(output_path, normalized_audio,sample_rate)