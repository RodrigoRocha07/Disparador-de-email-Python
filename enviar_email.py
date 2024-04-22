import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from texto import texto

def enviar_email():
    
    corpo_email = texto

    # Criando a mensagem
    msg = MIMEMultipart()
    msg['Subject'] = "Teste de email automatoco"
    msg['From'] = 'devrodrigonunes@gmail.com'  # Coloque seu endereço de e-mail
    msg['To'] = 'rodrigorochafn@gmail.com'  # Coloque o endereço de e-mail do destinatário

    # Adicionando o corpo do e-mail
    msg.attach(MIMEText(corpo_email, 'html'))

    # Configurando o servidor SMTP do Gmail
    smtp_server = 'smtp.gmail.com'
    smtp_port = 587

    # Iniciando uma conexão segura com o servidor
    s = smtplib.SMTP(smtp_server, smtp_port)
    s.starttls()

    # Substitua 'seu_email@gmail.com' e 'sua_senha' com suas credenciais do Gmail
    email = 'devrodrigonunes@gmail.com'
    senha = 'bgqzbkthwouucalx'

    # Faça login no servidor SMTP
    s.login(email, senha)

    # Enviando o e-mail
    s.sendmail(msg['From'], msg['To'], msg.as_string())

    # Encerrando a conexão com o servidor
    s.quit()

    print('E-mail enviado com sucesso.')


