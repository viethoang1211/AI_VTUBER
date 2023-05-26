import argparse
import os
import subprocess
import soundfile as sf
import pydub
import numpy as np
import noisereduce as nr
def collect_training_data(youtube_link, output_folder):
    # TODO: Implement data collection from YouTube video
    # pass
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    # Extract audio from YouTube video using youtube-dl
    # command = ['youtube-dl', '--extract-audio', '--audio-format', 'wav', '-o', f'{output_folder}/%(id)s.%(ext)s', youtube_link]
    command = ['yt-dlp', '-o', f'{output_folder}/%(title)s.%(ext)s','-x','--audio-format','wav', youtube_link]
    subprocess.call(command)

    print("Training data collected successfully.")

# def remove_noise_and_music(processed_file):
#     '''
#     Removes background noise and music from an audio file, using pydub's noise filter
#     '''

# ver 1
# def remove_noise_and_music(audio_segment):
#     # Convert the audio segment to a numpy array
#     audio_data = np.array(audio_segment.get_array_of_samples())

#     # Perform noise reduction using noisereduce
#     reduced_noise = nr.reduce_noise(y=audio_data, sr=audio_segment.frame_rate)

#     # Convert the reduced noise audio back to an AudioSegment object
#     reduced_noise_segment = pydub.AudioSegment(
#         data=reduced_noise.tobytes(),
#         sample_width=audio_segment.sample_width,
#         frame_rate=audio_segment.frame_rate,
#         channels=audio_segment.channels
#     )
    
#     # Detect non-silent parts using pydub's silence detection
#     non_silent_parts = pydub.silence.detect_nonsilent(reduced_noise_segment, min_silence_len=500, silence_thresh=-50)
#     voice_segments = [reduced_noise_segment[start:end] for start, end in non_silent_parts]
#     # Concatenate the non-silent segments to obtain the author's voice
#     voice_segment = pydub.AudioSegment.empty()
#     for segment in voice_segments:
#         voice_segment += segment

#     return voice_segment
# def preprocess_data(input_folder, output_folder):
#     # TODO: Implement data preprocessing
#     pass

# ver 1
# def preprocess_data(input_folder, output_folder):
#     if not os.path.exists(output_folder):
#         os.makedirs(output_folder)

#     # Iterate over the audio files in the input folder
#     for filename in os.listdir(input_folder):
#         input_file = os.path.join(input_folder, filename)
#         # output_file = os.path.join(output_folder, filename)
#         if filename.endswith('.wav') or filename.endswith('.mp3'):
#             processed_file = pydub.AudioSegment.from_wav(os.path.join(input_folder, filename))
#             result = remove_noise_and_music(processed_file)
#             output_folder_path = os.path.join(output_folder, os.path.splitext(os.path.basename(filename))[0] + ".processed.wav")
#             result.export(output_folder_path,format='wav')
            
            
#     print("Data preprocessing completed.")


from matplotlib import pyplot as plt
from wavfile import read

def preprocess_data(input_folder, output_folder):
    for file_name in os.listdir(input_folder):
        with open(os.path.join(input_folder, file_name), 'rb') as file:
            wav_data = read(file)
        # Remove background noise and music
        noise_freq_list = []
        for sample in wav_data:
            if np.abs(sample).any():
                noise_freq = wav_data[sample-32768]
                noise_freq_list.append(noise_freq)
        wav_data = np.delete(wav_data, np.nonzero(wav_data == noise_freq_list))
        music_freq_list = []
        for sample in wav_data:
            if np.abs(sample).all():
                music_freq = wav_data[sample-2048,:]
                music_freq_list.append(music_freq)
        wav_data = np.delete(wav_data, np.nonzero(wav_data == music_freq_list))
        np.savetxt(os.path.join(output_folder, file_name), wav_data)



def train_voice_model(input_folder, output_model):
    # TODO: Implement voice model training
    pass

def clone_voice(input_text, input_model, output_file):
    # TODO: Implement voice cloning
    pass

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    subparsers = parser.add_subparsers(dest='command')

    # Data collection command
    collect_parser = subparsers.add_parser('collect', help='Collect training data from YouTube')
    collect_parser.add_argument('-yl', '--youtube_link', type=str, help='YouTube video link')
    collect_parser.add_argument('-of', '--output_folder', type=str, help='Output folder for training data')

    # Data preprocessing command
    preprocess_parser = subparsers.add_parser('preprocess', help='Preprocess training data')
    preprocess_parser.add_argument('-if', '--input_folder', type=str, help='Input folder containing training data')
    preprocess_parser.add_argument('-of', '--output_folder', type=str, help='Output folder for preprocessed data')

    # Model training command
    train_parser = subparsers.add_parser('train', help='Train voice cloning model')
    train_parser.add_argument('-if', '--input_folder', type=str, help='Input folder containing preprocessed data')
    train_parser.add_argument('-om', '--output_model', type=str, help='Output file for trained model')

    # Voice cloning command
    clone_parser = subparsers.add_parser('clone', help='Clone voice')
    clone_parser.add_argument('-it', '--input_text', type=str, help='Input text to be cloned')
    clone_parser.add_argument('-im', '--input_model', type=str, help='Input trained model file')
    clone_parser.add_argument('-of', '--output_file', type=str, help='Output file for cloned voice')

    args = parser.parse_args()

    if args.command == 'collect':
        collect_training_data(args.youtube_link, args.output_folder)
    elif args.command == 'preprocess':
        preprocess_data(args.input_folder, args.output_folder)
    elif args.command == 'train':
        train_voice_model(args.input_folder, args.output_model)
    elif args.command == 'clone':
        clone_voice(args.input_text, args.input_model, args.output_file)
    else:
        parser.print_help()