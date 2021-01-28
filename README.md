![voz](https://user-images.githubusercontent.com/51414398/106074608-e6756880-60ea-11eb-8bbd-e6fa20e03378.jpg)

<h1 align="center">Speech Recogntion</h1>

<p align="center">Speech recognition with Python language and the speech_recognition library.</p>

## About the project

This project was created to see how speech recognition works using the Python language.

## How it works?

The user will say something in the microphone, and Python will understand and write what the user is saying.

## Why?

Just to practice my Python skills more and and see how the library works.

## Prerequisites

- pip install SpeechRecognition.

- You need to install Pyaudio compatible with your computer at this link: https://www.lfd.uci.edu/~gohlke/pythonlibs/#pyaudio.

- And finally, just install the file you downloaded like this: pip install (the file you downloaded).

## The code

```
# Importando a biblioteca 
import speech_recognition as sr
# Criando uma instância da classe "Recognizer"
r = sr.Recognizer()
# Utilizando Microfone
with sr.Microphone() as fonte:
    # Eliminando ruidos
    r.adjust_for_ambient_noise(fonte, duration=3) 
    print('Diga algo: ')
    # Capturando o audio
    audio = r.listen(fonte)
    try:
        # Transformando o audio em texto
        print('Você disse: ' + r.recognize_google(audio, language='pt-BR')) 
    except:
        print('Não foi possivel compreender o áudio')
```
