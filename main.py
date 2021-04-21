#Import libs
import datetime
import speech_recognition as sr 
r =sr.Recognizer()
with sr.Microphone() as source:
    #
    audio=r.listen(source)
text = r.recognize_google(audio)

if str(text).lower()== "What time is":
    print(datetime.datetime.now().strftime('%b-%d-%I%M%p-%G'))
    break
