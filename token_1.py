from gtts import gTTS
import os
TOKEN='7068742322:AAEbQbC-wQ2ZcpOh9VxrOQEidQ3zqS1g7tQ'

def text_to_voice(mytext,lang1):
    myobj=gTTS(text=mytext,lang=lang1,slow=False)
    myobj.save('wordvoice.mp3')