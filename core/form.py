from django.forms import ModelForm, TextInput, BooleanField

from .models import Todo

class TodoForm(ModelForm):
    class Meta:
        model = Todo
        fields = {'title','description','important'}
        # widgets ={
        #     'title':TextInput(attrs={
        #         'class':"form_title",
        #     }),
        #     'description':TextInput(attrs={
        #         'class':"form_description",
        #     }),
        # }