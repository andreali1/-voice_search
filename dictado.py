import speech_recognition as sr
r = sr.Recognizer()
with sr.Microphone() as source:
    print('Dicte donde desea realizarla busqueda : ')
    audio = r.listen(source)
    texto = r.recognize_google(audio, language='es-ES')
    print(texto)