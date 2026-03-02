# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _

# Create your models here.

class UserProfile(models.Model):

    user = models.OneToOneField(User, on_delete=models.CASCADE)

    #__PROFILE_FIELDS__

    #__PROFILE_FIELDS__END

    def __str__(self):
        return self.user.username
    
    class Meta:
        verbose_name        = _("UserProfile")
        verbose_name_plural = _("UserProfile")

#__MODELS__
class Projeto(models.Model):

    #__Projeto_FIELDS__
    codigo = models.CharField(max_length=255, null=True, blank=True)
    descricao = models.CharField(max_length=255, null=True, blank=True)
    cliente = models.CharField(max_length=255, null=True, blank=True)

    #__Projeto_FIELDS__END

    class Meta:
        verbose_name        = _("Projeto")
        verbose_name_plural = _("Projeto")


class Conceitos(models.Model):

    #__Conceitos_FIELDS__
    contratacao = models.IntegerField(null=True, blank=True)
    ingressos = models.IntegerField(null=True, blank=True)

    #__Conceitos_FIELDS__END

    class Meta:
        verbose_name        = _("Conceitos")
        verbose_name_plural = _("Conceitos")



#__MODELS__END
