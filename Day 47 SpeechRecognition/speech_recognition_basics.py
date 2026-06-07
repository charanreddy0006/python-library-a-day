import speech_recognition as sr

# Create recognizer
recognizer = sr.Recognizer()

# Use microphone
with sr.Microphone() as source:

    print("Speak something...")

    audio = recognizer.listen(source)

try:
    
    text = recognizer.recognize_google(audio)

    print("You said:", text)

except Exception as e:

    print("Error:", e)