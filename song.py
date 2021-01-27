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
