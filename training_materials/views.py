#!/usr/bin/env python
# vim: ai ts=4 sts=4 et sw=4

from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.contrib import messages
from django.core.urlresolvers import reverse
from django.db import transaction
from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django_tables2 import RequestConfig
from tables import TrainingMaterialTable
from models import TrainingMaterial
from forms import TMForm
from rapidsms import settings

from django_tables2 import RequestConfig


@login_required
def training_materials(request):
    qset = TrainingMaterial.objects.all()
    template = "django_tables2/bootstrap-tables.html"

    training_materials_table = TrainingMaterialTable(qset, template=template)

    paginate = {"per_page": settings.PAGINATOR_OBJECTS_PER_PAGE}
    RequestConfig(request, paginate=paginate).configure(training_materials_table)

    return render(request, "training_materials/index.html", {
        "training_materials_table": training_materials_table,
    })
	
@login_required
def training_materials_add(request, pk=None):
    if pk:
        tm = get_object_or_404(TrainingMaterial, pk=pk)
    else:
        tm = TrainingMaterial()
    tm_form = TMForm(instance=tm)
    if request.method == 'POST':
        data = {}
        for key in request.POST:
            val = request.POST[key]
            if isinstance(val, basestring):
                data[key] = val
            else:
                try:
                    data[key] = val[0]
                except (IndexError, TypeError):
                    data[key] = val
        # print repr(data)
        del data
        if pk:
            if request.POST["submit"] == "Delete Training Material":
                tm.delete()
                messages.add_message(request, messages.INFO, "Deleted training material")
                return HttpResponseRedirect(reverse(training_materials_add))
            tm_form = TMForm(request.POST, instance=tm)
        else:
            tm_form = TMForm(request.POST)
        if tm_form.is_valid():
            tm = tm_form.save(commit=False)
            tm.save()
            messages.add_message(request, messages.INFO, "Added contact")
            return HttpResponseRedirect(reverse(training_materials_add))
    return render(request, 'training_materials/tm_form.html', {
        "tm": tm,
        "tm_form": tm_form,
    })
