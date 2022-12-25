from .models import Client
from django.forms import ModelForm
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Column, Layout, Row, Submit

class ClientForm(ModelForm):

    def __init__(self, *args, **kwargs):
        super(ClientForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.layout = Layout(
            Row(
                Column(css_class='form-group col-md-2 mx-auto'),
                Column('name', css_class='form-group col-md-3 mx-auto'),
                Column('email', css_class='form-group col-md-3 mx-auto'),
                Column(css_class='form-group col-md-2 mx-auto'),
                css_class='form-row'
            ),
            Row(
                Column(css_class='form-group col-md-2 mx-auto'),
                Column('grade_level', css_class='form-group col-md-3 mx-auto'),
                Column('subject', css_class='form-group col-md-3 mx-auto'),
                Column(css_class='form-group col-md-2 mx-auto'),
                css_class='form-row'
            ),
            Row(
                Column(css_class='form-group col-md-2 mx-auto'),
                Column('comment', css_class='form-group col-md-6 mx-auto'),
                Column(css_class='form-group col-md-2 mx-auto'),
                css_class='form-row'
            ),
            Row(
                Column(css_class='form-group col-md-4 mx-auto'),
                Submit('submit', 'Submit', css_class='form-group col-md-2 mx-auto'),
                Column(css_class='form-group col-md-4 mx-auto'),
                css_class='form-row'
            ),
        )
    
    class Meta:
        model = Client
        fields = "__all__"
