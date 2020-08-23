import speech_recognition as sr
import webbrowser
from gtts import gTTS

from playsound import playsound
NOMBRE_ARCHIVO = "sonido_generado.mp3"
tts = gTTS('Hola andre en que puedo ayudarte.', lang='es-ES')
# Nota: podríamos llamar directamente a save
with open(NOMBRE_ARCHIVO, "wb") as archivo:
    tts.write_to_fp(archivo)
playsound(NOMBRE_ARCHIVO)
r = sr.Recognizer()
with sr.Microphone() as source:
    print('Dictame en que puedo ayudarte : ')
    audio = r.listen(source)
    texto = r.recognize_google(audio, language='es-ES')
    print(texto)
    if texto == "buscar" or texto == "Buscar" or texto == 'búsqueda':
        NOMBRE_ARCHIVOb = "sonido_generadob.mp3"
        tts = gTTS('En que pagina deseas realizar la busqueda, puedo ayudarte a buscar en google, spotify, youtube, facebook ', lang='es-ES')
        with open(NOMBRE_ARCHIVOb, "wb") as archivob:
            tts.write_to_fp(archivob)
        playsound(NOMBRE_ARCHIVOb)
        r = sr.Recognizer()
        with sr.Microphone() as source:
            print("empezanodo con busquedas")
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





    elif texto == 'nota' or texto == 'Nota' or texto == 'toma nota':
        NOMBRE_ARCHIVOc = "sonido_generadob.mp3"
        tts = gTTS('Tomo nota ', lang='es-ES')
        with open(NOMBRE_ARCHIVOc, "wb") as archivoc:
            tts.write_to_fp(archivoc)
        playsound(NOMBRE_ARCHIVOc)
        r = sr.Recognizer()
        with sr.Microphone() as source:
            print("texto dictado")
            audio = r.listen(source)
            texto = r.recognize_google(audio, language='es-ES')
            print(texto)
            NOMBRE_ARCHIVOd = "sonido_generadod.mp3"
            tts = gTTS('tu has dicho: {}'.format(texto), lang='es-ES')
            with open(NOMBRE_ARCHIVOd, "wb") as archivod:
                tts.write_to_fp(archivod)
            playsound(NOMBRE_ARCHIVOd)










