import asyncio
import speech_recognition as sr
from googletrans import Translator

async def listen_and_translate():
    recognizer = sr.Recognizer()
    translator = Translator()

    while True:
        with sr.Microphone() as source:
            print("Listening...")
            audio = recognizer.listen(source)

        try:
            print("Recognizing...")
            text = recognizer.recognize_google(audio, language="en-US")
            print("You said:", text)

            translated_text = await asyncio.get_event_loop().run_in_executor(None, translator.translate, text, {'src': 'en', 'dest': 'pt'})
            print("Translated to Portuguese:", translated_text.text)

        except sr.UnknownValueError:
            print("Sorry, I could not understand what you said.")
        except sr.RequestError as e:
            print("Could not request results; {0}".format(e))
        except Exception as e:
            print("Error:", e)

if __name__ == "__main__":
    asyncio.run(listen_and_translate())
