import sounddevice

from scipy.io.wavfile import write

fps = 44100


duration = 10

print("recording...")
recording = sounddevice.rec(int(duration*fps), samplerate=fps, channels=2)
sounddevice.wait()
print("done")
write("output.mp3", fps, recording)
