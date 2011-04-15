# -*- coding: utf-8 -*-

from django.contrib import admin
from models import CategoriaOfertas,Anunciante,Cidade,Cupon,EmailInscricao,Estado,Oferta,Perfil

class AnuncianteAdmin(admin.ModelAdmin):
    """admin class"""

class CategoriaOfertasAdmin(admin.ModelAdmin):
    """admin class"""

class OfertaAdmin(admin.ModelAdmin):
    prepopulated_fields = {
        'slug': ( 'titulo', )
    }


class PerfilAdmin(admin.ModelAdmin):
    """admin class"""

class EmailInscricaoAdmin(admin.ModelAdmin):
   """admin class"""

class CuponAdmin(admin.ModelAdmin):
    """admin class"""
    list_display = ['usuario', 'oferta', 'status']
    list_filter = ('usuario', 'oferta')
    list_per_page = 100
    search_fields = ['usuario', 'oferta']


class CidadeAdmin(admin.ModelAdmin):
    """admin class"""
    list_display = ['nome', 'estado', 'ativo']
    list_per_page = 100
    search_fields = ['nome']
    prepopulated_fields = {
        'slug': ( 'nome', )
    }


admin.site.register(CategoriaOfertas, CategoriaOfertasAdmin)
admin.site.register(Oferta, OfertaAdmin)
admin.site.register(Estado)
admin.site.register(Cidade, CidadeAdmin)
admin.site.register(Perfil, PerfilAdmin)
admin.site.register(Cupon, CuponAdmin)
admin.site.register(Anunciante, AnuncianteAdmin)
admin.site.register(EmailInscricao, EmailInscricaoAdmin)
