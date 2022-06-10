import speech_recognition as sr

rec = sr.Recognizer()       # INSTANCIANDO O RECONHECEDOR DE VOZ

# print(sr.Microphone().list_microphone_names()) --> AQUI PRINTAMOS NO CONSOLE A LISTA DE MICROFONES CONECTADOS QUE QUEREMOS USAR

with sr.Microphone() as mic:        # CONTROLANDO O MICROFONE
	rec.adjust_for_ambient_noise(mic)       # INDINCANDO QUAL TIPO DE SOM DESEJAMOS CAPTURAR - NO NOSSO CASO O (mic)
	print("Gravando audio...")       # PRINTA UMA MENSAGEM ANTES DE GRAVAR
	audio = rec.listen(mic)         # OUVINDO O AUDIO 
	texto = rec.recognize_google(audio, language="pt-BR")        # AQUI ESCOLHEMOS QUAL RECONHECEDOR VAMOS USAR, NESTE CASO O DO GOOGLE, E DEFINIMOS A LÍNGUA TBM
	print(texto)        # POR FIM PRINTAMOS O QUE FOI DITO NO CONSOLE