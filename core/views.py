#Esse de baixo é quando usa somente os templates e buscando dados de fora.
#from django.views.generic import TemplateView

#FormView é com formulário tipo do e-mail
from django.views.generic import FormView
from django.urls import reverse_lazy
from django.contrib import messages

from .models import Servico, Funcionario, Recurso
from .forms import ContatoForm

# Create your views here.

class IndexView(FormView):
    template_name = 'index.html'
    
    #Aqui envolve e-mail
    form_class =  ContatoForm
    success_url = reverse_lazy('index')
    
    
    def get_context_data(self, **kwargs):
        context = super(IndexView, self).get_context_data(**kwargs)
        context['servicos'] = Servico.objects.order_by('?').all()
        context['funcionarios'] = Funcionario.objects.all()
        context['recursos1'] = Recurso.objects.all()[:3]
        context['recursos2'] = Recurso.objects.all()[3:6]
        return context
    
    #Validando o formulário de e-mail
    def form_valid(self, form, *args, **kwargs):
        form.send_mail()
        messages.success(self.request, 'E-mail enviado com sucesso.')
        return super(IndexView, self).form_valid(form, *args, **kwargs)
    
    def form_invalid(self, form, *args, **kwargs ):
        messages.error(self.request, 'Error ao enviar e-mail.')
        return super(IndexView, self).form_valid(form, *args, **kwargs)
        


