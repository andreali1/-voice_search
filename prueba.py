import speech_recognition as sr
import webbrowser
from gtts import gTTS

from playsound import playsound

# rguarado el archivo quqe genera el sonido
NOMBRE_ARCHIVO = "sonido_generado.mp3"
# primer texto q se guiarda en el MP3 y luego se reproduyce --- lang es paa el idioma
tts = gTTS('Hola andre en que puedo ayudarte.', lang='es-ES')
# Nota: podríamos llamar directamente a save
# abriendo archivo donde se guarda el texto para convertirlo a audio
# y creando el archivo MP3
with open(NOMBRE_ARCHIVO, "wb") as archivo:
    tts.write_to_fp(archivo)
# reproduciendo el archivo  de audio creado desde el textos
playsound(NOMBRE_ARCHIVO)

# empezando a habalr con la maquina
# objeto para implementar el reconocimientyo de voz

r = sr.Recognizer()
# encendiendo y usando el microfono para el guardar el dictadop
with sr.Microphone() as source:
    print('Dictame en que puedo ayudarte : ')
    audio = r.listen(source)
    # reconocieno el texto dictado
    texto = r.recognize_google(audio, language='es-ES')
    print(texto)

    # ----------------------------------------
    # primer accion  busuqeda en navegador
    # ---------------------------------------

    # validando el texto dicatado para mas acciones
    if texto == "buscar" or texto == "Buscar" or texto == 'búsqueda':
        # creando el archivo para audio del asistente con el texto de abajo
        NOMBRE_ARCHIVOb = "sonido_generadob.mp3"
        tts = gTTS(
            'En que pagina deseas realizar la busqueda, puedo ayudarte a buscar en google, spotify, youtube, facebook ',
            lang='es-ES')
        # abriendo el archivo donde se va guaradar el texto ingresado
        with open(NOMBRE_ARCHIVOb, "wb") as archivob:
            tts.write_to_fp(archivob)
        # reproduciendo el archivo
        playsound(NOMBRE_ARCHIVOb)
        # objeto para reconocimiento de voz
        r = sr.Recognizer()
        # iniciando microfono
        with sr.Microphone() as source:
            print("empezando con busquedas")
            # emepzando el reconocimiento de voz
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

    # ----------------------------------------
    # primer accion  busuqeda en navegador
    # ---------------------------------------

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
#cambios