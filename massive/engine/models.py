# -*- coding: utf-8 -*-
import datetime

from django.db import models  # Replaced by models in gis package
from django.contrib.auth.models import User
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes import generic
from django.utils.translation import ugettext_lazy as _
from django.utils.dates import WEEKDAYS
from django.core.urlresolvers import reverse
import time
from massive001.massive.photologue.models import TagField

#from massivecoupon.photologue.models import ImageModel
#from massivecoupon.countries.models import Country
#from massive.photologue.models import TagField

OFERTA_IMG = 'ofertas_imagens/'
OFERTA_MINI = 'ofertas_mini/'

STATUS_EMESPERA = 1
STATUS_ATIVO = 2
STATUS_CANCELADO = 3

STATUS = (
  (STATUS_EMESPERA, "Comprado - Em Espera"),
  (STATUS_ATIVO, "Comprado - Pegou o dinheiro"),
  (STATUS_CANCELADO, "Nao efetuada a compra"),
)


CC_VISA = 1
CC_MASTERCARD = 2
CC_AMEX = 3

CC_TIPO = (
  (CC_VISA, 'Visa'),
  (CC_VISA, 'Mastercard'),
  (CC_AMEX, 'American Express'),
)

class Estado(models.Model):
    """
    Localizacao do bairro (latitude, longitude, cep)
    """
    class Meta:
        verbose_name = _('Estado')
        verbose_name_plural = _('Estados')

    nome = models.CharField(verbose_name=_("Nome"), max_length=60)
    #estado = models.ForeignKey("estado.Estado", null=True, blank=True)

    def __unicode__(self):
        return self.nome

class Cidade(models.Model):
    """
     Localizacao do bairro (latitude, longitude, cep)
    """
    class Meta:
        verbose_name = 'Cidade'
        verbose_name_plural = 'Cidades'

    nome = models.CharField(verbose_name=_("Nome"), max_length=60)
    slug = models.SlugField(db_index=True)
    ativo = models.BooleanField(default=False, db_index=True)
    estado = models.ForeignKey("Estado", null=True, blank=True)
    pedido = models.IntegerField(default=0, db_index=True)

    def __unicode__(self):
        return self.nome

    def get_absolute_url(self):
        return reverse('cidade_index', kwargs={'cidade_slug': self.pk})

class Anunciante(models.Model):
    class Meta:
        verbose_name = _('Anunciante')
        verbose_name_plural = _('Anunciantes')

    nome       = models.CharField(max_length=60)
    endereco    = models.CharField(max_length=60)
    cidade       = models.ForeignKey(Cidade)
    cep = models.CharField(max_length=7)
    estado    = models.ForeignKey(Estado)
    telefone      = models.CharField(max_length=25)
    telefone_extra   = models.CharField("Telefone Extra", max_length=6, blank=True)
    celular       = models.CharField(max_length=25)
    fax        = models.CharField(max_length=25)
    contato    = models.CharField(max_length=50, blank=True, help_text="Contato do anunciante")
    email      = models.EmailField(blank=True, help_text="Email do contato")
    website    = models.URLField(blank=True, verbose_name=_('Website'))

    def __str__(self):
        return self.nome
    class Admin:
        list_display = ( "nome", "contato", "email", "telefone" )

class CategoriaOfertas(models.Model):
    """
    Categorias de varias ofertas
    """

    class Meta:
        verbose_name = _('Categoria')
        verbose_name_plural = _('Categorias')

    nome = models.CharField("Categoria", max_length=60)

    def __unicode__(self):
        return self.nome

class OfertaManager(models.Manager):
    def ativa_na_cidade(self, cidade):
        qs = self.get_query_set()

        # Filter by city
        qs = qs.filter(cidade=cidade)

        # Only the active ones
        qs = qs.filter(ativo=True)

        # Only up to date
        qs = qs.filter(finzaliza_em__gte=datetime.datetime.now())

        # Order with the featured deal first
        qs = qs.order_by('-estreando')

        return qs

class Oferta(models.Model):
    """
    Actual services
    """
    class Meta:
        verbose_name = _('Oferta')
        verbose_name_plural = _('Oferta')

    objects = _default_manager = OfertaManager()

    anunciante              = models.ForeignKey(Anunciante)
    cidade                  = models.ForeignKey(Cidade, related_name='ofertas')
    titulo                  = models.CharField(verbose_name=_("Titulo"), max_length=256)
    subtitulo                  = models.CharField(verbose_name=_("SubTitulo"), max_length=256)
    
    slug                    = models.SlugField(db_index=True)

    categoria                = models.ForeignKey(CategoriaOfertas)

    publicado_em            = models.DateTimeField(blank=True, auto_now_add=True, db_index=True)
    inicia_em              = models.DateTimeField(blank=True, null=True, db_index=True)
    # The field 'date_end' could be synchronized with 'auction_duration'
    finzaliza_em                = models.DateTimeField(blank=True, null=True, db_index=True)

    preco_varejo            = models.DecimalField(default=0,decimal_places=2, max_digits=6, help_text='Full retail price')
    preco_oferta              = models.DecimalField(default=0,decimal_places=2, max_digits=6, help_text='Deal (real) Price')

    porcentagem_desconto     = models.DecimalField(default=0,decimal_places=2, max_digits=6, help_text='% Percentage Off retail')
    valor_desconto          = models.DecimalField(default=0,decimal_places=2, max_digits=6, help_text='$ Dollars Off retail')

    duracao_da_oferta        = models.IntegerField(default=24, help_text=_('Deal duration in hours'))
    
    destaque              = models.BooleanField(default=False, db_index=True)
    ativo              = models.BooleanField(default=True, db_index=True)
    estreando                = models.BooleanField(default=False, db_index=True)

    sobre_oferta              = models.TextField()
    destaque_oferta              = models.TextField()

    

    qtd_ofertas_disponiveis           = models.IntegerField(default=1)
    qtd_ofertas_por_pessoa = models.IntegerField(default=1)
    qtd_ofertas_vendidas           = models.IntegerField(default=1)

    descricao_completa             = models.TextField()
    descricao_resumida             = models.TextField()
    
    qtd_fechamento = models.IntegerField(default=0)
    data_fechamento = models.DateTimeField()
    #  reviews                 = models.TextField()

    descricao_compania            = models.TextField()
    #  address                 = models.TextField()

    #  url                     = models.URLField()
   
    imagem                   = models.ImageField(upload_to='ofertas_imagems/', blank=True)
    miniatura                   = models.ImageField(upload_to='ofertas_mini/', blank=True)

    tags                    = TagField(help_text=_("Tags devem ser separados por virgula"), verbose_name=_('Tags'))

    latitude = models.DecimalField(
            verbose_name=_("Latitude (decimal)"),
            max_digits=9,
            decimal_places=6,
            blank=True,
            null=True,
            )
    longitude = models.DecimalField(
            verbose_name=_("Longitude (decimal)"),
            max_digits=9,
            decimal_places=6,
            blank=True,
            null=True,
            )
    meta_keywords = models.CharField("Meta Keywords", max_length=255,
                                     help_text=u'Conjunto delimitado por virgulas de palavras-chave para SEO meta tag')
    meta_description = models.CharField("Meta Description", max_length=255,
                                        help_text=u'Descricao da meta-tag')

    data_entrada              = models.DateTimeField(blank=True, editable=False, null=True, auto_now_add=True)
    data_modificacao              = models.DateTimeField(blank=True, editable=False, null=True, auto_now=True)
    data_exclusao            = models.DateTimeField(blank=True, editable=False, null=True)

    def __unicode__(self):
        return self.titulo
    
    @property
    def num_disponivel(self):
        num_vendido = Cupon.objects.filter(oferta=self.id).count()
        num_disponivel = self.qtd_ofertas - num_vendido
        return num_disponivel
    
    @property
    def num_vendido(self):
        num_vendido = Cupon.objects.filter(oferta=self.id).count()
        return num_vendido
    
    @property
    def percentagem_vendido(self):
        num_vendido = self.num_vendido()
        if num_vendido > self.fecha_em:
            return 100
        elif self.fecha_em:
            return int( ( (num_vendido*1.0) / self.fecha_em) * 100)
        else:
            return 0

    def num_necessario_fechamento(self):
        num_vendido = self.num_vendido()
        if num_vendido > self.fecha_em:
            return 0
        else:
            return self.fecha_em - num_vendido
        
    @property
    def tempo_restante(self):
        agora = datetime.datetime.now()
        expira_em = self.publicado_em + datetime.timedelta(hours=self.duracao_da_oferta)

        if expira_em < agora :
            return "Oferta fechada"

        tempo_expiracao =  expira_em - agora
        horas_tempo_expiracao = int(time.strftime("%H", time.gmtime(tempo_expiracao.seconds)))
        mins_tempo_expiracao = int(time.strftime("%M", time.gmtime(tempo_expiracao.seconds)))

        if tempo_expiracao.days < 1:
            if horas_tempo_expiracao < 1:
                if mins_tempo_expiracao < 1:
                    if tempo_expiracao.seconds < 1:
                        return "Oferta fechada"
                    else:
                        return "%d segundos" % tempo_expiracao.seconds
                else:
                    return "%d minutos" % mins_tempo_expiracao
            else:
                return "%d horas, %d minutos" % (horas_tempo_expiracao, mins_tempo_expiracao)

        else:
            if horas_tempo_expiracao < 1:
                return "%d dias" % (tempo_expiracao.days)
            else:
                return "%d dias, %d horas" % (tempo_expiracao.days, horas_tempo_expiracao)

    def esta_expirado(self):
        agora = datetime.datetime.now()
        expira_em = self.publicado_em + datetime.timedelta(hours=self.duracao_da_oferta)

        if expira_em < agora :
            return True
        else:
            return False

    def get_absolute_url(self):
        return reverse('oferta_detalhe', kwargs={'cidade_slug': self.cidade.slug, 'oferta_slug': self.slug})

    def get_checkout_url(self):
        return reverse('oferta_checkout', kwargs={'cidade_slug': self.cidade.slug, 'oferta_slug': self.slug})

    def get_endereco_completo(self):
        return ','.join(filter(bool, [self.anunciante.endereco, self.anunciante.cidade.nome]))

    def get_telefones(self):
        return ','.join(filter(bool, [self.anunciante.telefone, self.anunciante.telefone_extra]))
 
class EmailInscricao(models.Model):
    class Meta:
        verbose_name = _('Receber Email')
        verbose_name_plural = _('Receber Email')

    email = models.EmailField(blank=True, help_text="Endereco de email")
    cidade = models.ForeignKey(Cidade)

    def __unicode__(self):
        return self.email


class Perfil(models.Model):
    """
    Perfil do usuario
    """

    class Meta:
        verbose_name = _('Perfil')
        verbose_name_plural = _('Perfis')

    email_cad    = models.BooleanField(default=False)
    numero    = models.CharField("Numero", max_length=10)
    endereco          = models.CharField("Nome da Rua", max_length=40)
    apt             = models.CharField("Apartamento #", max_length=20)
    cidade            = models.ForeignKey(Cidade)
    cep      = models.CharField("CEP", max_length=7)
    telefone           = models.CharField(blank=True, max_length=16)
    telefone_extra        = models.CharField("Telefone extra", max_length=6, blank=True)
    celular            = models.CharField("Celular #", blank=True, max_length=16)
    fax             = models.CharField(blank=True, max_length=16)

    def __unicode__(self):
        return self.telefone

class Cupon(models.Model):
    class Meta:
        verbose_name = _('Cupon')
        verbose_name_plural = _('Cupons')

    usuario                    = models.ForeignKey(User)
    oferta                    = models.ForeignKey(Oferta)
    status                  = models.IntegerField(choices=STATUS, default=0, db_index=True)
    data_entrada              = models.DateTimeField(blank=True, editable=False, null=True, auto_now_add=True)
    data_modificacao                = models.DateTimeField(blank=True, editable=False, null=True, auto_now=True)
    data_exclusao            = models.DateTimeField(blank=True, editable=False, null=True)

    def __unicode__(self):
        return str(self.usuario)

# SIGNALS
from django.db.models import signals

def oferta_pre_save(instance, **kwargs):
    if instance.finzaliza_em and instance.inicia_em:
        delta = (instance.finzaliza_em - instance.inicia_em)
        instance.duracao_da_oferta = (delta.days * 24) + (delta.seconds / 60 / 60)
    elif instance.inicia_em and instance.duracao_da_oferta and not instance.finzaliza_em:
        instance.finzaliza_em = instance.inicia_em + datetime.timedelta(seconds=instance.duracao_da_oferta * 60 * 60)

signals.pre_save.connect(oferta_pre_save, sender=Oferta)

