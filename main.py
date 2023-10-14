import speech_recognition as sr
import pyttsx3
import datetime
import wikipedia
import pywhatkit
from tkinter import *

#Interface (Front-end)
master = Tk()
master.title('Paula, sua assistente')
master.geometry('500x800+470+4')
master.resizable(width=1, height=1)

img_fundo = PhotoImage(file='imagens\\fundoo.png')
img_botao = PhotoImage(file='imagens\\botao.png')

lab_fundo = Label(master, image=img_fundo)
lab_fundo.pack()


bt_entrar = Button(master, bd=0, image=img_botao, command= master.destroy)
bt_entrar.place(width=253, height=75, x=125, y=241)

master.mainloop()

audio = sr.Recognizer()
maquina = pyttsx3.init()

def executa_comando():
    try:
        with sr.Microphone() as source:
            print('Estou te ouvindo!')
            voz = audio.listen(source)
            comando = audio.recognize_google(voz, language='pt-BR')
            comando = comando.lower()
            if 'paula' in comando:
                comando = comando.replace('paula', '')
                maquina.say(comando)
                maquina.runAndWait()

    except:
        print('Microfone não está funcionando. Tente novamente')

    return comando

def comando_voz_usuario():
    comando = executa_comando()
    if 'horas' in comando:
        hora = datetime.datetime.now().strftime('%H:%M')
        maquina.say('Agora são' + hora)
        maquina.runAndWait()
    elif 'pesquise por' in comando:
        procurar = comando.replace('pesquise por', '')
        wikipedia.set_lang('pt')
        resultado = wikipedia.summary(procurar,2)
        print(resultado)
        maquina.say(resultado)
        maquina.runAndWait()
    elif 'tocar' in comando:
        musica = comando.replace('tocar','')
        resultado = pywhatkit.playonyt(musica)
        maquina.say('Tocando música')
        maquina.runAndWait()


comando_voz_usuario()
