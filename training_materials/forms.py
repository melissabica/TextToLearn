#!/usr/bin/env python
# vim: ai ts=4 sts=4 et sw=4

from django import forms
from models import TrainingMaterial
from rapidsms.router import send
from selectable.forms import AutoCompleteSelectMultipleField
from .lookups import ConnectionLookup
from rapidsms.models import Contact, Connection


"""class TMFormSetBase(forms.models.BaseInlineFormSet):
    def __init__(self, *args, **kwargs):
        super(TMFormSetBase, self).__init__(*args, **kwargs)
        self.forms[0].empty_permitted = False
        for form in self.forms:
            if not form.initial:
                form.fields['DELETE'].widget = forms.widgets.HiddenInput()
"""                


class TMForm(forms.ModelForm):
    c = 20
    r = 2
    type = forms.models.modelform_factory(TrainingMaterial)
    question_1 = forms.CharField(widget=forms.Textarea(attrs={'cols': c, 'rows': r}), required=False)
    question_2 = forms.CharField(widget=forms.Textarea(attrs={'cols': c, 'rows': r}), required=False)
    question_3 = forms.CharField(widget=forms.Textarea(attrs={'cols': c, 'rows': r}), required=False)
    question_4 = forms.CharField(widget=forms.Textarea(attrs={'cols': c, 'rows': r}), required=False)
    question_5 = forms.CharField(widget=forms.Textarea(attrs={'cols': c, 'rows': r}), required=False)
    
    answer_1 = forms.CharField(widget=forms.Textarea(attrs={'cols': c, 'rows': r}), required=False)
    answer_2 = forms.CharField(widget=forms.Textarea(attrs={'cols': c, 'rows': r}), required=False)
    answer_3 = forms.CharField(widget=forms.Textarea(attrs={'cols': c, 'rows': r}), required=False)
    answer_4 = forms.CharField(widget=forms.Textarea(attrs={'cols': c, 'rows': r}), required=False)
    answer_5 = forms.CharField(widget=forms.Textarea(attrs={'cols': c, 'rows': r}), required=False)
    
    
    class Meta:
        model = TrainingMaterial
        exclude = ('assign','assigned_users', 'messages', 'messagenum')
        # widgets = {
            # 'question_1': forms.Textarea(attrs={'rows':2, 'cols':20}, required=False),
        # }
    def createMessages(self):
        msgLen = 160 - len(self.cleaned_data['tag']) - len(" -Reply NEXT ")
        i = 0
        text = self.cleaned_data['text']
        message = ""
        l = len(text)
        if(l < msgLen):
            #if(self.cleaned_data['question_1'] != "")
            message = text
        while(l > msgLen):
            message +=text[msgLen*i:msgLen+msgLen*i]
            message += " -Reply NEXT %s" % self.cleaned_data['tag']
            l -= msgLen
            i += 1
        message += text[msgLen*i:]
        if self.cleaned_data[question_1] == "":
            message += " (end)"
        else:
            message += "-Reply QUIZ %s" % tag
        return (message, i+1)
    def extraValidation(self):
        if TrainingMaterial.objects.get(tag = self.cleaned_data['tag'].upper().replace(" ", "")):
            raise forms.ValidationError("Tag must be unique.")

class AssignForm(forms.ModelForm):
    type = forms.models.modelform_factory(TrainingMaterial)

    class Meta:
        model = TrainingMaterial
        exclude = ('assign','messages','messagenum','title','tag','text','question_1','answer_1','question_2','answer_2','question_3','answer_3','question_4','answer_4','question_5','answer_5')
        widgets = {'assigned_users': forms.CheckboxSelectMultiple()}
    """def __init__(self, *args, **kwargs):  
        super(AssignForm, self).__init__(*args, **kwargs)
        self.fields["assigned_users"].widget = forms.CheckboxSelectMultiple()"""  



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