#!/usr/bin/env python
# vim: ai ts=4 sts=4 et sw=4

from django.shortcuts import render

from rapidsms import settings

from django_tables2 import RequestConfig


#@login_required
def analytics(request):

    return render(request, "analytics/index.html", {
    })
