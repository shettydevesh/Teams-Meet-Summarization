import whisper
from IPython.display import Audio, display


def stt(file):
    display(Audio(file, autoplay=True))
    model = whisper.load_model('medium')
    result = model.transcribe(file)['text']
    print("Transcript done")
    return result


result = stt("pzm34.wav")
print(result)
