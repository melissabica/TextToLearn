#!/usr/bin/env python
# vim: ai ts=4 sts=4 et sw=4

from django.core.exceptions import ValidationError
from django.db import models, forms
from rapidsms.models import Contact, Connection


class TrainingMaterial(models.Model):
    title = models.TextField()
    tag = models.TextField()
    text = models.TextField()
    date = models.DateTimeField(auto_now=True)
    assigned_users = forms.ModelMultipleChoiceField(queryset=Contact.objects.all())
                    #models.ForeignKey(Contact, null=True)

