#!/usr/bin/env python
# vim: ai ts=4 sts=4 et sw=4

import django_tables2 as tables
from training_materials.models import TrainingMaterial


class TrainingMaterialTable(tables.Table):
    #id = tables.LinkColumn('training_materials_add', args=[tables.utils.A('pk')])
    title = tables.LinkColumn('training_materials_add', args=[tables.utils.A('pk')])
    assign = tables.LinkColumn('training_materials_assign', args=[tables.utils.A('pk')])

    class Meta:
        model = TrainingMaterial
        exclude = ('tag', 'text', 'id', 'messages', 'messagenum', 'question_1', 'answer_1', 'question_2', 'answer_2', 'question_3', 'answer_3', 'question_4', 'answer_4', 'question_5', 'answer_5',)
        order_by = ('-date', )
        attrs = {
            'class': 'table table-striped table-bordered table-condensed'
        }

		
    def render_identities(self, value, record):
        return ', '.join([x.identity for x in record.connection_set.all()])
