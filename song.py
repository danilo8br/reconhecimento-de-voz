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
