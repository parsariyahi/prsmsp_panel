from django.forms import ModelForm

from app.models import Sms, SmsPanel


class SmsPanelForm(ModelForm):

    def __init__(self, *args, **kwargs):
        super(SmsPanelForm, self).__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control'

    class Meta:
        model = SmsPanel
        fields = "__all__"