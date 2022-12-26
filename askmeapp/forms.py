from django.forms import ModelForm
from .models import AskmeModel

class AskmeForm(ModelForm):
    class Meta:
        model = AskmeModel
        fields = ['title', 'detail', 'urgent']
        