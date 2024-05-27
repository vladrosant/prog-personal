import customtkinter
import pyttsx3

from twitchio.ext import commands

customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("dark-blue")

root = customtkinter.CTk()
root.geometry('500x350')

# https://twitchapps.com/tmi/ for the oauth token
class MyBot(commands.Bot):

    def __init__(self):
        super().__init__(token='qb9x82gr01nw2w8i501urt6hj2cpxn',
                         client_id='xxhssc8t01wngo1ejsx7lia8p53rq2',
                         nick='VamPipo',
                         prefix='',
                         initial_channels=['VamPipo'])
        self.engine = pyttsx3.init()
        self.engine.setProperty('volume', 1)
        self.engine.setProperty('voice', 'HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_PT-BR_MARIA_11.0')
        self.engine.setProperty('rate', 130)

    async def event_message(self, message):
        message_text = message.content
        self.engine.say(message_text)
        self.engine.runAndWait()


if __name__ == '__main__':
    bot = MyBot()
    bot.run()

frame = customtkinter.CTk.frame(master=root)
frame.pack(pady=20, padx=60, fill='both', expand=True)

label = customtkinter.CTkLabel(master=frame, text="TTS Bot", text_font=('Roboto, 24'))
label.pack(pady=12, padx=10)

entry1 = customtkinter.CTkEntry(master=frame, placeholder_text="Twitch username")
entry1.pack(pady=12, padx=10)

entry2 = customtkinter.CTkEntry(master=frame, placeholder_text="Twich TOKEN", show="*")
entry2.pack(pady=12, padx=10)

entry3 = customtkinter.CTkEntry(master=frame, placeholder_text="Twitch Client ID", show="*")
entry3.pack(pady=12, padx=10)

volume_slider = customtkinter.CTkSlider(master=frame, text="Volume", from_=0, to=2)
speed_slider = customtkinter.CTkSlider(master=frame, text="Speed", from_=0, to=300)
button = customtkinter.CTkButton(master=frame, text="Login", command=__init__)
