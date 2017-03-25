from django import forms
from .models import Dotaz

class DotazForm(forms.ModelForm):
     class Meta:
         model = Dotaz
         fields = ('jmeno', 'prijmeni', 'email', 'mobil', 'zprava')
         labels = {
            'jmeno': "Jméno",
            'prijmeni': "Příjmení",
            'email': "Email",
            'mobil': "Telefon",
            'zprava': "Text vzkazu",
         }
