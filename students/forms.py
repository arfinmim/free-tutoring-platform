from django import forms
from .models import Student, Tutor, Contact


class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = '__all__'


class TutorForm(forms.ModelForm):
    class Meta:
        model = Tutor
        fields = '__all__'


class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ['name', 'email', 'message']