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
    contact = models.ForeignKey(Contact, null=True)
    connection = models.ForeignKey(Connection, null=True)
    direction = models.CharField(max_length=1, choices=DIRECTION_CHOICES)
    date = models.DateTimeField()