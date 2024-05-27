import pyttsx3

engine = pyttsx3.init()
voices = engine.getProperty('voice', id:HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_PT-BR_MARIA_11.0)
for voice in voices:
    print(voice)