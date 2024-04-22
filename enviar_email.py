import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from texto import texto


destinatarios = ['rodrigorochafn@gmail.com',
                 'administrativo@drandreguanabara.com.br',
                'dp@drandreguanabara.com.br',
                'compras@drandreguanabara.com.br',
                'supervisaocomercial@drandreguanabara.com.br',
                'taywan@wakeperformance.com.br',
                'operacoes@drandreguanabara.com.br',
                'fernanda.maias92@gmail.com']


def enviar_email(destinatario):
    
    corpo_email = texto

    # Criando a mensagem
    msg = MIMEMultipart()
    msg['Subject'] = "Programação de pagamentos da semana"
    msg['From'] = 'financeiro@drandreguanabara.com.br'  # Coloque seu endereço de e-mail
    msg['To'] =(destinatario)


    # Adicionando o corpo do e-mail
    msg.attach(MIMEText(corpo_email, 'html'))

    # Configurando o servidor SMTP do Gmail
    smtp_server = 'smtp.gmail.com'
    smtp_port = 587

    # Iniciando uma conexão segura com o servidor
    s = smtplib.SMTP(smtp_server, smtp_port)
    s.starttls()

    # Substitua 'seu_email@gmail.com' e 'sua_senha' com suas credenciais do Gmail
    #email = 'devrodrigonunes@gmail.com'
    #senha = 'bgqzbkthwouucalx'
    email = 'financeiro@drandreguanabara.com.br'
    senha = 'cjnnseuuwtheamak'

    # Faça login no servidor SMTP
    s.login(email, senha)

    # Enviando o e-mail
    s.sendmail(msg['From'], msg['To'], msg.as_string())

    # Encerrando a conexão com o servidor
    s.quit()

    print(f'E-mail enviado com sucesso. {destinatario}')

#for destinatario in destinatarios:
    #enviar_email(destinatario)

