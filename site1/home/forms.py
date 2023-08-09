from django import forms
from .models import Todo

class TodoCreateForm(forms.Form):
    title = forms.CharField()
    body = forms.CharField()
    created = forms.DateTimeField(label='created date' , required=False)

class TodoUpdateForm(forms.ModelForm):
    class Meta:
        model = Todo
        fields = ('title' , 'body' , 'created')