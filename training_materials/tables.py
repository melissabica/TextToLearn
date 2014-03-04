#!/usr/bin/env python
# vim: ai ts=4 sts=4 et sw=4

import django_tables2 as tables
from training_materials.models import TrainingMaterial


class TrainingMaterialTable(tables.Table):

    class Meta:
        model = TrainingMaterial
        exclude = ('id', )
        order_by = ('-date', )
        attrs = {
            'class': 'table table-striped table-bordered table-condensed'
        }
