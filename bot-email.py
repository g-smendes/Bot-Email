import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
import csv

# Configurações do e-mail e servidor SMTP
EMAIL = "e-mail a ser utilizado"
SMTP_SERVER = "smtp.gmail.com"
SMTP_PORT = 465

# Lendo a senha do arquivo
with open('senha-email.txt') as f:
    senha_do_email = f.readline().strip()

# Lendo os e-mails do arquivo CSV
with open('lista-email.csv', newline='') as csvfile:
    leitor_csv = csv.reader(csvfile)
    emails = [linha[0] for linha in leitor_csv]  # Assume que o e-mail está na primeira coluna

# Lista para armazenar os e-mails enviados com sucesso
enviados = []

# Criando e enviando e-mails para cada endereço
for destinatario in emails:
    # Criando a mensagem
    msg = MIMEMultipart("related")
    msg['Subject'] = 'Titulo'
    msg['From'] = EMAIL
    msg['To'] = destinatario

    # Corpo do e-mail com HTML
    html = f"""
    <html>
        <body>
            <p><strong>Prezado<strong>,</p>
            <p>Mensagem</p>
            <p>Baixe o app <p>
            <p><strong>ANDROID</strong></p>
            <p><a href="https://exemple.com" target="_blank">Clique aqui para acessar</a></p>
            <p><strong>IOS</strong></p>
            <p><a href="https://exemple.com" target="_blank">Clique aqui para acessar</a></p>
            <div style="text-align: center;">
            <img src="cid:image.png" alt="Mural" style="width:100%; max-width:600px;" />
            </div>
        </body>
    </html>
    """
    msg.attach(MIMEText(html, "html"))

    # Embutir a imagem no corpo do e-mail
    with open("image.png", "rb") as img_file:
        img = MIMEImage(img_file.read())
        img.add_header("Content-ID", "<cartao-virtual.png>")
        img.add_header("Content-Disposition", "inline", filename="image.png")
        msg.attach(img)

    # Enviando o e-mail
    try:
        with smtplib.SMTP_SSL(SMTP_SERVER, SMTP_PORT) as smtp:
            smtp.login(EMAIL, senha_do_email)
            smtp.send_message(msg)
        print(f"E-mail enviado para {destinatario}")
    except Exception as e:
        print(f"Erro ao enviar e-mail para {destinatario}: {e}")
        
# Verificar se há e-mails enviados com sucesso
if enviados:
    print(f"E-mails enviados com sucesso: {enviados}")

    # Adicionar os e-mails enviados ao arquivo enviados.csv
    with open('enviados.csv', mode='a', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerows(enviados)
    print("E-mails enviados registrados no arquivo 'enviados.csv'.")
else:
    print("Nenhum e-mail foi enviado com sucesso.")