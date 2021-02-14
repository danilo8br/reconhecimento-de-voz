![1_OCPpp4VdniwJxlWKn63Zcg](https://user-images.githubusercontent.com/51414398/106143998-579c3680-6152-11eb-86db-084c64ae8a65.jpeg)

<h1 align="center">Speech Recogntion</h1>

<p align="center">Speech recognition with Python language and the speech_recognition library.</p>

## :rocket: About the project 

This project was created to see how speech recognition works using the Python language.

## :wrench: How it works?

The user will say something in the microphone, and Python will understand and write what the user is saying.

## :thinking:  Why?

Just to practice my Python skills more and and see how the library works.

## :warning: Prerequisites

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
while True:
    with sr.Microphone() as fonte:
        # Eliminando ruidos
        r.adjust_for_ambient_noise(fonte, duration=3) 
        print('Diga algo: ')
        # Capturando o audio
        audio = r.listen(fonte)
        try:
            # Transoformando o audio em texto
            text = r.recognize_google(audio, language='pt-BR')
            print(f'Você disse: {text}')       
        except:
            print('Não foi possivel compreender o áudio')
        if 'parar' in text:
            break
```
