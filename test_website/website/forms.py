from .models import Manager, DailyReport
from django import forms


class ManagerForm(forms.ModelForm):
    class Meta:
        model = Manager
        fields = '__all__'


class DailyReportForm(forms.ModelForm):
    class Meta:
        model = DailyReport
        fields = '__all__'
        widgets = {'report_date': forms.TextInput(attrs={'placeholder': '%Y-%m-%d'})}
