from django import forms
from django.core.mail.message import EmailMessage

# Isso aqui é para criação de formulário para encaminhar e-mail.

class ContatoForm(forms.Form):
    nome = forms.CharField(label='Nome', max_length=100)
    emai = forms.EmailField(label='E-mail', max_length=100)
    assunto = forms.CharField(label='Assunto', max_length=100)
    mensagem = forms.CharField(label='Mensagem', widget=forms.Textarea())
    
    def send_email(self):
        nome = nome.cleaned_data['nome']
        email = email.cleaned_data['email']
        assunto = assunto.cleaned_data['assunto']
        mensagem = mensagem.cleaned_data['mensagem']
        
        conteudo = f'Nome: {nome}\nE-mail: {email}\nAssuunto: {assunto}\nMensagem: {mensagem}'
        
        mail = EmailMessage(
            subject=assunto,
            body=conteudo,
            from_email='pedroteste@gmailf.com.br',
            to=['pedroteste@gmailf.com.br',],
            headers={'Reply-To': email}
        )
        
        mail.send()