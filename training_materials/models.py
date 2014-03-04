#!/usr/bin/env python
# vim: ai ts=4 sts=4 et sw=4

from django.core.exceptions import ValidationError
from django.db import models
from rapidsms.models import Contact, Connection


class TrainingMaterial(models.Model):
    INCOMING = "I"
    OUTGOING = "O"
    DIRECTION_CHOICES = (
        (INCOMING, "Incoming"),
        (OUTGOING, "Outgoing"),
    )
	
    title = models.TextField()
    date = models.DateTimeField()
    assigned_users = models.ForeignKey(Contact, null=True)

