import whisper
import pyaudio
import wave
import zhconv
from whisper.tokenizer import get_tokenizer

model = whisper.load_model("base")

# result = model.transcribe("audio.mp3", language="en")
result = model.transcribe("D:\伟境音乐台\许巍 - 生活不止眼前的苟且.flac", language="zh")
print("\n".join([zhconv.convert(i["text"], 'zh-hans') for i in result["segments"] if i is not None]))
print(result["text"])