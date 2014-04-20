#!/usr/bin/env python
# vim: ai ts=4 sts=4 et sw=4

from django import forms
from models import TrainingMaterial
from rapidsms.router import send
from selectable.forms import AutoCompleteSelectMultipleField
from messaging.lookups import ConnectionLookup



"""class TMFormSetBase(forms.models.BaseInlineFormSet):
    def __init__(self, *args, **kwargs):
        super(TMFormSetBase, self).__init__(*args, **kwargs)
        self.forms[0].empty_permitted = False
        for form in self.forms:
            if not form.initial:
                form.fields['DELETE'].widget = forms.widgets.HiddenInput()
"""                


class TMForm(forms.ModelForm):
	type = forms.models.modelform_factory(TrainingMaterial)
	class Meta:
		model = TrainingMaterial
		exclude = ('assign',)
        #widgets = {'assigned_users': forms.CheckboxSelectMultiple()}


class AssignForm(forms.ModelForm):
    type = forms.models.modelform_factory(TrainingMaterial)
    connections = AutoCompleteSelectMultipleField(lookup_class=ConnectionLookup)
    class Meta:
        model = TrainingMaterial
        exclude = ('assign',)
        #widgets = {'assigned_users': forms.CheckboxSelectMultiple()}
    def send(self):
        message = self.cleaned_data['text']
        connections = self.cleaned_data['connections']
        return send(message, connections)
		
		

"""	def save(self):
		instance = forms.ModelForm.save(self)
		instance.trainingmaterial_set.clear()
		for trainingmaterial in self.cleaned_data['trainingmaterials']:
		    instance.trainingmaterial_set.add(trainingmaterial)
	"""
#	= forms.ModelMultipleChoiceField(widget=forms.CheckboxSelectMultiple, queryset=Category.objects.all())

"""TMFormSet = forms.models.inlineformset_factory(
    TrainingMaterial,
    formset = TMFormSetBase,
)


# the built-in FileField doesn't specify the 'size' attribute, so the
# widget is rendered at its default width -- which is too wide for our
# form. this is a little hack to shrink the field.
class SmallFileField(forms.FileField):
    def widget_attrs(self, widget):
        return {"size": 10}
"""