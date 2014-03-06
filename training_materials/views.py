#!/usr/bin/env python
# vim: ai ts=4 sts=4 et sw=4

from django.contrib.auth.decorators import login_required
from django.shortcuts import render

from tables import TrainingMaterialTable
from models import TrainingMaterial
from rapidsms import settings

from django_tables2 import RequestConfig


@login_required
def training_materials(request):
    qset = TrainingMaterial.objects.all()
    #qset = qset.select_related('contact', 'connection__backend')
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
                return HttpResponseRedirect(reverse(registration))
            contact_form = ContactForm(request.POST, instance=tm)
        else:
            contact_form = ContactForm(request.POST)
        if contact_form.is_valid():
            tm = contact_form.save(commit=False)
            connection_formset = ConnectionFormSet(request.POST, instance=tm)
            if connection_formset.is_valid():
                tm.save()
                connection_formset.save()
                messages.add_message(request, messages.INFO, "Added training material")
                return HttpResponseRedirect(reverse(registration))
    return render(request, 'registration/contact_form.html', {
        "tm": tm,
        "contact_form": contact_form,
        "connection_formset": connection_formset,
    })
