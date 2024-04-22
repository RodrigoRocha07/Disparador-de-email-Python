import datetime

# Data de hoje
hoje = datetime.date.today()
# Data de inicio
inicio = hoje + datetime.timedelta(days=7)
# Fim da semana (6 dias após a data de hoje)
fim_semana = hoje + datetime.timedelta(days=13)
# Dois dias após a data de hoje
dia_max = hoje + datetime.timedelta(days=2)

# Formatar para exibir apenas dia/mês
hoje_formatado = hoje.strftime('%d/%m')
inicio_formatado = inicio.strftime('%d/%m')
fim_semana_formatado = fim_semana.strftime('%d/%m')
dia_max_formatado = dia_max.strftime('%d/%m')

texto = f"""  
<!-- HTML USADO PARA TESTAR A MENSAGEM QUE SERÁ ENVIADA NO EMAIL -->
<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Solicitação de Pagamento</title>
</head>
<body style="margin: 0; padding: 0; background-color: #f9f9f9; font-family: Arial, sans-serif;">

<div style="max-width: 600px; margin: 20px auto; padding: 20px; background-color: #fff; border-radius: 10px; box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);">

    <div style="float: right; width: 200px;">
        <img src="https://i.imgur.com/1EHt8ny.jpeg" alt="Logo da Empresa" style="max-width: 100%; height: auto; display: block; border-radius: 10px;">
    </div>
    
    <h1 style="text-align: center; color: #333;">Programação de Pagamentos</h1>

    <div style="margin-top: 20px; border-top: 1px solid #ddd; padding-top: 10px;">
        <p>Bom dia!</p>
        <p>Solicito que as entregas dos pagamentos referentes à semana de <strong>{inicio_formatado} a {fim_semana_formatado} </strong> sejam enviadas até as 18:00 da <strong> QUARTA-FEIRA, dia {dia_max_formatado} </strong>.</p>
        <p>Reforçando que as entregas incluem  <strong>autorizações da diretoria </strong> (Dr. André Guanabara) e  <strong>boletos de pagamentos </strong>, salvo pagamentos recorrentes do mês.</p>
    </div>
    
    <div style="margin-top: 20px; text-align: center;">
        <p>Atenciosamente,</p>
        <p>Setor Financeiro</p>
    </div>
</div>

</body>
</html>





    """