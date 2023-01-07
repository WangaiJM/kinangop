from django.forms import ModelForm
from .models import online_registration

class registrationForm(ModelForm):
    class Meta:
        model = online_registration
        fields = "__all__"