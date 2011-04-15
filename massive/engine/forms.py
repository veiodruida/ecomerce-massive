# -*- coding: utf-8 -*-
from django import forms
from django.forms import widgets
from massive001.massive.engine import models as enginemodels
#from massivecoupon.libs import formutils
from datetime import date
import re
import pdb

r_cep = re.compile(r'^([A-Z][0-9][A-Z])[ -]?([0-9][A-Z][0-9])$', re.I)
r_data = re.compile(r'^(\d\d\d\d)[/-](\d{1,2})[/-](\d{1,2})$')

expira_mes = (
  (1, '1'),
  (2, '2'),
  (3, '3'),
  (4, '4'),
  (5, '5'),
  (6, '6'),
  (7, '7'),
  (8, '8'),
  (9, '9'),
  (10, '10'),
  (11, '11'),
  (12, '12'),
)

expira_ano = (
  (2010, '2010'),
  (2011, '2011'),
  (2012, '2012'),
  (2013, '2013'),
  (2014, '2014'),
  (2015, '2015'),
  (2016, '2016'),
  (2017, '2017'),
  (2018, '2018'),
  (2019, '2019'),
  (2020, '2020'),
)

class EmailSubForm(forms.Form):
    email               = forms.EmailField(help_text="voce@dominio.com", widget=forms.TextInput(attrs={'size':'25'}))
    cidade                = forms.ChoiceField(initial=1, choices=[ (obj.id, obj.nome) for obj in enginemodels.Cidade.objects.all() ])


class CadastrarForm(forms.Form):
    nome_completo           = forms.CharField(max_length=128, widget=forms.TextInput(attrs={'size':'30'}) )
    senha            = forms.CharField(max_length=20, widget=forms.PasswordInput(attrs={'size':'12'}) )
    senha_verifica    = forms.CharField(max_length=20, widget=forms.PasswordInput(attrs={'size':'12'}))
    email               = forms.EmailField(help_text="voce@dominio.com", widget=forms.TextInput(attrs={'size':'30'}))
    


    def clean(self):
        """
        Validate fields to make sure everything's as expected.
        - postalcode is in right format and actually exists
        - service actually exists
        """
        cd = self.cleaned_data

        if 'senha' in cd and 'senha_verifica' in cd:
            if self.cleaned_data['senha'] != self.cleaned_data['senha_verifica']:
                self._errors['senha'] = forms.util.ErrorList(["Senhas incompativeis!"])

        else:
            self._errors['senha'] = forms.util.ErrorList(["Confira sua senha"])

#      raise forms.ValidationError(_(u'Please enter and confirm your password'))


        return cd



class LoginForm(forms.Form):
    email               = forms.EmailField(help_text="voce@dominio.com", widget=forms.TextInput(attrs={'size':'25'}))
    senha            = forms.CharField(max_length=20, widget=forms.PasswordInput(attrs={'size':'12'}) )

    def clean(self):
        # only do further checks if the rest was valid
        if self._errors: return
            
        from django.contrib.auth import login, authenticate
        user = authenticate(username=self.data['email'],
                                password=self.data['senha'])
        if user is not None:
            if user.is_active:
                self.user = user                    
            else:
                raise forms.ValidationError( 'A sua conta esta inativa por favor entre em contato.')
        else:
            raise forms.ValidationError( 'O usuario e/ou a senha nao sao validos')


class OfertaCheckoutForm(forms.Form):
    nome_completo           = forms.CharField(max_length=128, widget=forms.TextInput(attrs={'size':'30'}) )
    senha            = forms.CharField(max_length=20, widget=forms.PasswordInput(attrs={'size':'12'}) )
    senha_verifica     = forms.CharField(max_length=20, widget=forms.PasswordInput(attrs={'size':'12'}))
    email               = forms.EmailField(help_text="voce@dominio.com", widget=forms.TextInput(attrs={'size':'30'}))
    quantidade           = forms.IntegerField(initial=1, widget=forms.TextInput(attrs={'size':'2'}))
    
    nome_titular_cartao     = forms.CharField(max_length=128, widget=forms.TextInput(attrs={'size':'30'}))
    tipo                = forms.ChoiceField( choices = enginemodels.CC_TIPO)
    numero              = forms.CharField(help_text="Coloque o numero do cartao#", max_length=20)
    expira_mes        = forms.ChoiceField(choices=expira_mes, help_text="Coloque o mes do vencimento do cartao")
    expira_ano         = forms.ChoiceField(choices=expira_ano, help_text="Coloque o ano do vencimento do cartao")
    codigo_seguranca           = forms.CharField(help_text="CVV", max_length=5, widget=forms.TextInput(attrs={'size':'5'}))
    #billing_address     = forms.CharField(max_length=256, widget=forms.TextInput(attrs={'size':'30'}))
    #city                = forms.CharField(max_length=25, widget=forms.TextInput(attrs={'size':'30'}))
    #postalcode          = forms.CharField(max_length=7, widget=forms.TextInput(attrs={'size':'7'}))
    #country             = forms.ChoiceField(initial="CA", choices=[ (obj.iso, obj.name) for obj in enginemodels.Country.objects.all() ])

    def clean(self):
        """
        Validate fields to make sure everything's as expected.
        - postalcode is in right format and actually exists
        - service actually exists
        """
        cd = self.cleaned_data

        if 'senha' in cd and 'senha_verifica' in cd:
            if self.cleaned_data['senha'] != self.cleaned_data['senha_verifica']:
                self._errors['senha'] = forms.util.ErrorList(["Senhas incompativeis!"])

        else:
            self._errors['senha'] = forms.util.ErrorList(["Confira sua senha"])

#            raise forms.ValidationError('Por favor confirme sua senha')

        return cd

