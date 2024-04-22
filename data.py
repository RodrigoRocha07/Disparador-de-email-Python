import datetime
import time
from enviar_email import *

# Definição de datas:
hoje = datetime.date.today()
dia_especifico = hoje + datetime.timedelta(days=3)
segunda_feira = 0
terca_feira = 1
quarta_feira = 2
quinta_feira = 3
sexta_feira = 4
sabado = 5
domingo = 6

# Transformando datas em strings:
hoje_stg = hoje.strftime("%d/%m/%Y")
dia_especifico_stg = dia_especifico.strftime("%d/%m/%Y")


# Definindo o horário de envio desejado
horario_de_envio = datetime.datetime.combine(hoje, datetime.time(14, 6))

# Mensagem de email que será enviada
def mensagem(hoje, dia_especifico):
    print(f"Olá, a data de hoje é {hoje_stg}, tenha um bom dia! \n Dia {dia_especifico_stg} será lançada a cobrança!")
    


while True:
    if hoje.weekday() == domingo:
        while True:
            # Obtendo o horário atual
            horario_atual = datetime.datetime.now()

            # Definir uma tolerância
            tolerancia = datetime.timedelta(minutes=0.1)

            # Verificar se o horário atual está dentro da tolerância do horário de envio
            horario_antes = horario_de_envio - tolerancia
            horario_depois = horario_de_envio + tolerancia


            if horario_antes <= horario_atual <= horario_depois:
                mensagem(hoje, dia_especifico)
                enviar_email()
                print(horario_atual)
                break
    time.sleep(60)

