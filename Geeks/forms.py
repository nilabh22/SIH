from  django import forms

from Geeks.models import Details, Department, IndividualForm

class student(forms.ModelForm):
    nameleader=forms.CharField(widget=forms.TextInput(attrs=
            {'class':'form-control','placeholder':'Enter your Name'}),
                required=True,max_length=100)
    name1=forms.CharField(widget=forms.TextInput(attrs=
            {'class':'form-control','placeholder':'Enter First Member Name'}),
                required=True,max_length=100)
    name2=forms.CharField(widget=forms.TextInput(attrs=
            {'class':'form-control','placeholder':'Enter Second Member Name'}),
                required=True,max_length=100)
    name3=forms.CharField(widget=forms.TextInput(attrs=
            {'class':'form-control','placeholder':'Enter Third Member Name'}),
                required=True,max_length=100)
    name4=forms.CharField(widget=forms.TextInput(attrs=
            {'class':'form-control','placeholder':'Enter Fourth Member Name'}),max_length=100,
            required=False)
    name5=forms.CharField(widget=forms.TextInput(attrs=
            {'class':'form-control','placeholder':'Enter Fifth Member Name'}),max_length=100,
            required=False)
    email=forms.EmailField(widget=forms.EmailInput(attrs=
            {'class':'form-control','placeholder':'Enter your Email'}),
                    required=True,max_length=100)
    contact=forms.IntegerField(widget=forms.NumberInput(attrs=
            {'class':'form-control','placeholder':'Enter your number'}),
                    required=True)
    rollno=forms.IntegerField(widget=forms.NumberInput(attrs=
            {'class':'form-control','placeholder':'Enter your Roll Number'}),
                required=True)
    rollno1=forms.IntegerField(widget=forms.NumberInput(attrs=
            {'class':'form-control','placeholder':'Enter your Roll Number'}),
                required=True)
    rollno2=forms.IntegerField(widget=forms.NumberInput(attrs=
            {'class':'form-control','placeholder':'Enter your Roll Number'}),
                required=True)
    rollno3=forms.IntegerField(widget=forms.NumberInput(attrs=
            {'class':'form-control','placeholder':'Enter your Roll Number'}),
                required=True)

    rollno4=forms.IntegerField(widget=forms.NumberInput(attrs=
            {'class':'form-control','placeholder':'Enter your Roll Number'}),
            required=False)
    rollno5=forms.IntegerField(widget=forms.NumberInput(attrs=
            {'class':'form-control','placeholder':'Enter your Roll Number'}),
            required=False)
    department=forms.ModelChoiceField(queryset=Department.objects.all())
    gitLinkedinLink=forms.URLField(widget=forms.URLInput(attrs=
            {'class':'form-control','placeholder':'Enter your Github Link'}),
                required=True,max_length=10000)

    class Meta():
         model=Details
         fields='__all__'


class IndividualForm(forms.ModelForm):
    name=forms.CharField(widget=forms.TextInput(attrs=
            {'class':'form-control','placeholder':'Enter your Name'}),
                required=True,max_length=100)
    email=forms.EmailField(widget=forms.EmailInput(attrs=
            {'class':'form-control','placeholder':'Enter your Email'}),
                    required=True,max_length=100)
    rollno=forms.IntegerField(widget=forms.NumberInput(attrs=
            {'class':'form-control','placeholder':'Enter your Roll Number'}),
                required=True)
    contact=forms.IntegerField(widget=forms.NumberInput(attrs=
            {'class':'form-control','placeholder':'Enter your number'}),
                    required=True)
    department=forms.ModelChoiceField(queryset=Department.objects.all())
    gitLinkedinLink=forms.URLField(widget=forms.URLInput(attrs=
            {'class':'form-control','placeholder':'Enter your Github Link'}),
                required=True,max_length=10000)
    class Meta():
         model=IndividualForm
         fields='__all__'
