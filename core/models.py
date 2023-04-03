from django.db import models
from stdimage.models import StdImageField
import uuid

def get_file_path(instance, filename):
    ext = filename.split('.')[-1]
    filename = f'{uuid.uuid4}.{ext}'
    return filename

# Create your models here.
class Base(models.Model):
    criados = models.DateField('Criação',auto_now_add=True)
    modificacao = models.DateField('Atualização', auto_now=True)
    ativo = models.BooleanField('Ativo', default=True)
    
    class Meta:
        abstract = True


class Recurso(Base):
    ICONE_CHOICECS = (
        ('lni-rocket', 'Foguete'),
        ('lni-laptop-phone',  'Laptop'),
        ('lni-cog', 'Engranagem'),
        ('lni-leaf', 'Folha'),
        ('lni-layers', 'Paginas'),
    )
    
    titulo = models.CharField('Titulo', max_length=100)
    texto = models.CharField('Texto', max_length=150)
    icone = models.CharField('Icone', max_length=17, choices=ICONE_CHOICECS)
    
    class Meta:
        verbose_name = 'Recurso'
        verbose_name_plural = 'Recursos'
    
    def __str__(self):
        return self.titulo


class Servico(Base):
    ICONE_CHOICES = (
        ('lni-cog', 'Engrenagem'),
        ('lni-stats-up', 'Gráfico'),
        ('lni-users', 'Usuários'),
        ('lni-layers', 'Dessign'),
        ('lni-mobile', 'Mobile'),
        ('lni-rocket', 'Foguete'),
    )

    servico = models.CharField('Serviço',max_length=100)
    descricao = models.TextField('Descrição', max_length=200)
    icone = models.CharField('Icone', max_length=12, choices=ICONE_CHOICES)
   

    class Meta:
        verbose_name = 'Serviço'
        verbose_name_plural  = 'Serviços'

    def __str__(self):
        return self.servico


class Cargo(Base):
    cargo = models.CharField('Cargo', max_length=100)

    class Meta:
        verbose_name = 'Cargo'
        verbose_name_plural = 'Cargos'
    
    def __str__(self):
        return self.cargo


class Funcionario(Base):
    nome = models.CharField('Nome', max_length=100)
    cargo = models.ForeignKey('core.Cargo', verbose_name='Cargo', on_delete=models.CASCADE)
    bio = models.TextField('Bio', max_length=200)
    imagem = StdImageField('Imagem',upload_to=get_file_path, variations={'thumb': {'width':480, 'height': 480, 'crop': True}})
    facebook = models.CharField('Facebook', max_length=100, default='#')
    twitter = models.CharField('Facebook', max_length=100, default='#')
    instagram = models.CharField('Facebook', max_length=100, default='#')

    class Meta:
        verbose_name = 'Funcionário'
        verbose_name_plural = 'Funcionários'
    
    def __str__(self):
        return self.nome