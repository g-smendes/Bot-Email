#  Envio de E-mails em Massa com Python

## Descrição
Este script Python automatiza o envio de e-mails em massa utilizando o protocolo SMTP. Ele carrega uma lista de endereços de e-mail a partir de um arquivo CSV, envia mensagens personalizadas em formato HTML com imagem embutida e registra os e-mails enviados com sucesso.

## Requisitos
- Python 3
- Conta de e-mail SMTP (exemplo: Gmail)
- Biblioteca `smtplib` (incluída na biblioteca padrão do Python)
- Biblioteca `email` (incluída na biblioteca padrão do Python)
- Arquivo `senha-email.txt` contendo a senha do e-mail remetente
- Arquivo `lista-email.csv` contendo a lista de destinatários
- Arquivo `image.png` contendo a imagem a ser incorporada no e-mail

## Como Usar
1. **Configurar o e-mail remetente**
   - Substitua `EMAIL` pelo e-mail que será utilizado para enviar as mensagens.
   - Certifique-se de que a conta tem acesso ao envio via SMTP.
   - Caso esteja utilizando Gmail, ative a opção "Senhas de App".
     
2. **Criar o arquivo de senha**
   - Crie um arquivo chamado `senha-email.txt` no mesmo diretório do script.
   - No arquivo, digite apenas a senha do e-mail sem espaços extras ou quebras de linha.

3. **Criar a lista de destinatários**
   - Crie um arquivo `lista-email.csv` contendo os e-mails a serem enviados.
   - Cada linha do CSV deve conter um endereço de e-mail na primeira coluna.

4. **Executar o script**
   - Rode o script utilizando Python:
     ```bash
     python nome_do_script.py
     ```

5. **Verificar os e-mails enviados**
   - Os e-mails enviados com sucesso serão listados no terminal.
   - Um registro será armazenado no arquivo `enviados.csv`.

## Personalização
- **Assunto do e-mail:** Modifique `msg['Subject']` para alterar o título da mensagem.
- **Conteúdo HTML:** Edite a string `html` dentro do script para modificar o corpo do e-mail.
- **Imagem embutida:** Substitua `image.png` pela imagem desejada, garantindo que ela esteja na mesma pasta do script.

## Tratamento de Erros
- O script captura exceções ao enviar e-mails e exibe mensagens de erro no console.
- Caso algum e-mail falhe, ele não será registrado no arquivo `enviados.csv`.

## Observação
Se você estiver utilizando Gmail, pode ser necessário configurar permissões adicionais para permitir o uso de SMTP por aplicativos externos.

## Licença
Este projeto está sob a licença MIT. Sinta-se à vontade para modificar e distribuir conforme necessário.

