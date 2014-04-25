#!/usr/bin/env python
# vim: ai ts=4 sts=4 et sw=4


from django.db import models
from .utils.modules import try_import, get_classes
from .conf import settings

class MessageTracker(models.Model):
    contact = models.ForeignKey(Contact)
    #: unique identifier for this connection on this backend (e.g. phone
    #: number, email address, IRC nick, etc.)
 

