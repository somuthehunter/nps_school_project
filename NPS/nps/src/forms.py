from django import forms
from .models import *
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout , Submit

class studetPayment(forms.ModelForm):
    class Meta:
        model = StudentsPayment
        fields = "__all__"
    
    def __init__(self,*args,**kwargs):
        super().__init__(*args,**kwargs)
        self.helper = FormHelper(self)
        self.helper.layout = Layout(
            'name',
            'amount',
            Submit('submit','Submit',css_class='button white btn-block btn-primary')

        )
