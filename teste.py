import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from texto import texto


def enviar_email(lista_destinatarios, email_remetente, senha, assunto, texto):
    # Criar a mensagem de email
    msg = MIMEMultipart()
    msg['Subject'] = assunto
    msg['From'] = email_remetente
    msg['To'] = ", ".join(lista_destinatarios)  # Concatenar a lista para exibição

    # Adicionar o corpo do email
    msg.attach(MIMEText(texto, 'html'))  # Conteúdo do email em HTML

    # Configurar o servidor SMTP (neste exemplo, usando Gmail)
    smtp_server = 'smtp.gmail.com'
    smtp_port = 587

    # Criar uma conexão segura com o servidor
    server = smtplib.SMTP(smtp_server, smtp_port)
    server.starttls()

    # Fazer login com as credenciais do remetente
    server.login(email_remetente, senha)

    # Enviar para todos os destinatários na lista
    server.sendmail(email_remetente, lista_destinatarios, msg.as_string())

    # Encerrar a conexão
    server.quit()

    print("E-mail enviado com sucesso.")

# Lista de destinatários
lista_destinatarios = ['rodrigorochafn@gmail.com',
                 'suporteti@drandreguanabara.com.br',
                ]


# Informações do remetente e assunto

#email = 'devrodrigonunes@gmail.com'
#senha = 'bgqzbkthwouucalx'
email_remetente = 'financeiro@drandreguanabara.com.br'
senha = 'cjnnseuuwtheamak'
assunto = 'Programação de pagamentos da semana'

# Enviar email para todos os destinatários da lista
enviar_email(lista_destinatarios, email_remetente, senha, assunto, texto)



