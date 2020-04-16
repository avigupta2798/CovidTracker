from django import forms
from home.models import  Covid


class CovidForm(forms.ModelForm):
    class Meta():
        model = Covid
        fields = ('patient_number', 'age', 'backup_notes', 'current_status', 'date_announced', 'city', 'district', 'state', 'gender', 'nationality', 'notes', 'source1', 'source2', 'source3', 'statecode', 'status_change_date', 'type_of_transmission')