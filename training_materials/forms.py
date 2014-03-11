#!/usr/bin/env python
# vim: ai ts=4 sts=4 et sw=4

from django import forms
from models import TrainingMaterial


class ConnectionFormSetBase(forms.models.BaseInlineFormSet):
    def __init__(self, *args, **kwargs):
        super(ConnectionFormSetBase, self).__init__(*args, **kwargs)
        self.forms[0].empty_permitted = False
        for form in self.forms:
            if not form.initial:
                form.fields['DELETE'].widget = forms.widgets.HiddenInput()


TMForm = forms.models.modelform_factory(TrainingMaterial)

TMFormSet = forms.models.inlineformset_factory(
    TrainingMaterial,
    extra=1,
    formset=ConnectionFormSetBase,
)


# the built-in FileField doesn't specify the 'size' attribute, so the
# widget is rendered at its default width -- which is too wide for our
# form. this is a little hack to shrink the field.
class SmallFileField(forms.FileField):
    def widget_attrs(self, widget):
        return {"size": 10}
