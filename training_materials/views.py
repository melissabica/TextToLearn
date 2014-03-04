# Create your views here.


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
    qset = qset.select_related('contact', 'connection__backend')
    template = "django_tables2/bootstrap-tables.html"

    training_materials_table = TrainingMaterialTable(qset, template=template)

    paginate = {"per_page": settings.PAGINATOR_OBJECTS_PER_PAGE}
    RequestConfig(request, paginate=paginate).configure(training_materials_table)

    return render(request, "training_materials/index.html", {
        "training_materials_table": training_materials_table,
    })
