#!/usr/bin/env python
# vim: ai ts=4 sts=4 et sw=4

from django.core.exceptions import ValidationError
from django.db import models
from django import forms
from rapidsms.models import Contact, Connection


class TrainingMaterial(models.Model):
    assigned_users = models.ManyToManyField(Contact)
    title = models.CharField(max_length=32)
    tag = models.CharField(max_length=8)
    text = models.TextField()
    date = models.DateTimeField(auto_now=True)
    assign = models.CharField(max_length=8, default='Assign', editable=False)
    #Hidden Processed Text
    messages = models.TextField()
    messagenum = models.IntegerField() 
    #QUIZ
    question_1 = models.TextField(max_length=140)
    answer_1 = models.TextField(max_length=140)
    question_2 = models.TextField(max_length=140)
    answer_2 = models.TextField(max_length=140)
    question_3 = models.TextField(max_length=140)
    answer_3 = models.TextField(max_length=140)
    question_4 = models.TextField(max_length=140)
    answer_4 = models.TextField(max_length=140)
    question_5 = models.TextField(max_length=140)
    answer_5 = models.TextField(max_length=140)

class MessageTracker(models.Model):
    contact = models.ForeignKey(Contact)
    tmorquiz = models.CharField(max_length=8)
    msgnum =  models.IntegerField()
    #forms.ModelMultipleChoiceField(queryset=Contact.objects.all())
                    #models.ForeignKey(Contact, null=True)
    
    def users(self):
	    return ', '.join([a.name for a in self.assigned_users.all()])
    def __unicode__(self):
        return "%s" % (self.title)

