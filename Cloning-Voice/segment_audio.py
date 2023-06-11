import librosa
import os
import soundfile as sf
def segment_audio(audio_path, clip_duration, output_dir):
    # Load audio file
    audio, sr = librosa.load(audio_path, sr=None)

    # Calculate clip duration in samples
    clip_duration_samples = int(clip_duration * sr)

    # Determine the number of clips
    num_clips = len(audio) // clip_duration_samples

    # Create the output directory if it doesn't exist
    os.makedirs(output_dir, exist_ok=True)

    # Segment the audio into clips
    for i in range(num_clips):
        clip_start = i * clip_duration_samples
        clip_end = clip_start + clip_duration_samples

        # Extract the clip
        clip = audio[clip_start:clip_end]

        # Save the clip as a new audio file
        clip_output_path = os.path.join(output_dir, f"clip{i+1}.wav")
        sf.write(clip_output_path, clip, sr)

    print("Audio segmentation completed.")

# Example usage
audio_path = "vocals.wav"
clip_duration = 20  # Duration of each clip in seconds
output_dir = "data/train_segment/countonme"

segment_audio(audio_path, clip_duration, output_dir)
