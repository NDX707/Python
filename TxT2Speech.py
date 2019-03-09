from gtts import gTTS
import os

location = os.system('pwd')
#print(location)

while True:

    userInput = input('Type: ')
    if userInput == "quit":
        break
    
    tts = gTTS(userInput)
    tts.save('Response.mp3')

    os.environ['PATH'] += os.pathsep + 'location'
    os.system('play Response.mp3')
