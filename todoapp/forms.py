from django import forms
from .models import Task
from jalali_date.fields import JalaliDateField
from jalali_date.widgets import AdminJalaliDateWidget



class taskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = '__all__'
        exclude = ('created_at','completed_at','completed',)

    def __init__(self, *args, **kwargs):
        super(taskForm, self).__init__(*args, **kwargs)
        self.fields['deadline'] = JalaliDateField( label=('DeadLine'), widget=AdminJalaliDateWidget )