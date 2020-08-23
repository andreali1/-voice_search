
import webbrowser

import speech_recognition as sr
from gtts import gTTS
import playsound
import gi
import pyaudio
r = sr.Recognizer()

with sr.Microphone() as source:
    print('Dicte donde desea realizarla busqueda : ')
    audio = r.listen(source)
    texto = r.recognize_google(audio, language='es-ES')
    print(texto)
    if texto == "google" or texto == "Google":
        with sr.Microphone() as source:
            print('Dicte lo que desea buscar en {}'.format(texto))
            audio = r.listen(source)
            try:
                text = r.recognize_google(audio, language='es-ES')
                print("estas buscando _ {}".format(text))
                url = 'https://www.google.co.in/search?q='
                search_url = url + text
                webbrowser.open(search_url)
            except:
                print("no se escucho")
    elif texto == "spotify" or texto == "Spotify":
        with sr.Microphone() as source:
            print('Dicte lo que desea buscar en {}'.format(texto))
            audio = r.listen(source)
            try:
                text = r.recognize_google(audio, language='es-ES')
                print("tu estas buscando _ {}".format(text))
                url = 'https://open.spotify.com/search/'
                search_url = url + text
                webbrowser.open(search_url)
            except:
                print("no se escucho")
    elif texto == "youtube" or texto == "Youtube" or texto == 'YouTube':
        with sr.Microphone() as source:
            print('Dicte lo que desea buscar en {}'.format(texto))
            audio = r.listen(source)
            try:
                text = r.recognize_google(audio, language='es-ES')
                print("tu has dicho _ {}".format(text))
                url = 'https://www.youtube.com/results?search_query='
                search_url = url + text
                webbrowser.open(search_url)
            except:
                print("no se escucho")
    elif texto == "facebook" or texto == "Facebook" or texto == 'FaceBook':
        with sr.Microphone() as source:
            print('Dicte lo que desea buscar en {}'.format(texto))
            audio = r.listen(source)
            try:
                text = r.recognize_google(audio, language='es-ES')
                print("tu has dicho _ {}".format(text))
                url = 'https://www.facebook.com/search/top/?q='
                search_url = url + text
                webbrowser.open(search_url)
            except:
                print("no se escucho")
    else:
        print("no se entendio")




