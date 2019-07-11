##import speech_recognition as sr
##s=sr.Recognizer()
##with sr.Microphone() as source:
##    print("Please speak")
### NLP
### Label
### Clustering
### Always Work In Online Mode
##
##
##    audio=s.listen(source)
##    print(audio)
##    s.adjust_for_ambient_noise
##data=s.recognize_google(audio)
##print(data)
##
##if('time' in data):
##    print(time.ctime())
##
##elif(data=='Hello'):
##    print("Hii")
##else:
##    print("Bye")
##
##



import speech_recognition as sr
s=sr.Recognizer()
with sr.Microphone() as source:
    print("Please speak")
# NLP
# Label
# Clustering
# Always Work In Online Mode


    audio=s.listen(source)
    print(audio)
    s.adjust_for_ambient_noise

try:
    data=s.recognize_google(audio)

except UnKnownValueError:
    print("Please Speak Properly")

except RequestError:
    print("Please Check Your Internet Connection")

except Exception as e:
    print("Some Errors are There")
print(data)

if('time' in data):
    print(time.ctime())

elif(data=='Hello'):
    print("Hii")
else:
    print("Bye")



