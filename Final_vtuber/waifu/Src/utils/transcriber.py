import utils.audio
import utils.vtube_studio

import openai, requests, urllib, os, wave, io,torch,whisper

VOICEVOX_URL = os.environ.get("VOICEVOX_URL")
HAS_OPENAI = os.environ.get("OPENAI_CHECK")

audio_model =None
# for non openai key
if not HAS_OPENAI:
    model ="medium.en"
    audio_model =whisper.load_model(model)

# model= "medium.en"
# audio_model = whisper.load_model(model)
# end


print("model loaded successfully")
VOICEVOX_LOCAL_FILE = "test.wav"
def transcribe(filename):
    global HAS_OPENAI, audio_model
    audio = open(filename, "rb")
    # for non openai key
    # result = audio_model.transcribe(filename, fp16=torch.cuda.is_available())
    # transcript = result['text'].strip()
    # message=transcript

    #  for openai key
    if HAS_OPENAI:
        transcript = openai.Audio.transcribe("whisper-1", audio)
        message = transcript.text
    else:
        result = audio_model.transcribe(filename, fp16=torch.cuda.is_available())
        transcript = result['text'].strip()
        message=transcript
        # pass

    if message is None or len(message.strip()) == 0:
        return None
    
    return message

def speak_jp(text, speaker=46):
    global VOICEVOX_URL, VOICEVOX_LOCAL_FILE
    params_encoded = urllib.parse.urlencode({'text': text, 'speaker': speaker})
    request = requests.post(f'{VOICEVOX_URL}/audio_query?{params_encoded}')
    params_encoded = urllib.parse.urlencode({'speaker': 46, 'enable_interrogative_upspeak': True})
    request = requests.post(f'{VOICEVOX_URL}/synthesis?{params_encoded}', json=request.json())
    with io.BytesIO(request.content) as memfile:
        utils.audio.play_wav(memfile, utils.vtube_studio.set_audio_level)
    