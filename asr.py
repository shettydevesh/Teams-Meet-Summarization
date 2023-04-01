from vosk import Model, KaldiRecognizer
from pydub import AudioSegment
import json

FRAME_RATE = 16000
CHANNELS = 1

model = Model(
    "D:/STM/deepblue/server/python/vosk-model-en-us-0.22/vosk-model-en-us-0.22")
rec = KaldiRecognizer(model, FRAME_RATE)
rec.SetWords(True)


def stt(file):
    mp3 = AudioSegment.from_wav(file)
    mp3 = mp3.set_channels(1)
    mp3 = mp3.set_frame_rate(16000)

    rec.AcceptWaveform(mp3.raw_data)
    result = json.loads(rec.Result())["text"]
    # cased = subprocess.check_output(
    #     "python D:\STM\deepblue\server\python\vosk-recasepunc-en-0.22\vosk-recasepunc-en-0.22\recasepunc.py predict D:\STM\deepblue\server\python\vosk-recasepunc-en-0.22\vosk-recasepunc-en-0.22\checkpoint", shell=True, text=True, input=result)
    return result
