from django import forms

#all the labels in the forms must correspond with the ones in models.py
class PersonForm(forms.ModelForm):
    class Meta:
    	model = Person
    	fields = ('lastname', 'firstname')