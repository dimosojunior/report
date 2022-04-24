from DimosoApp.models import *
from django.forms import ModelForm
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate



class MyUserForm(UserCreationForm):
    email = forms.EmailField(max_length=255, help_text="Required. Add a valid email address.")
    
    

    class Meta:
        model = MyUser
        fields = (
        "email",
        "username",
        "password1",
        "password2"

        
         )
    def clean_email(self):
        email = self.cleaned_data['email'].lower()
        try:
            myuser = MyUser.objects.get(email=email)
        except Exception as e:
            return email
        raise forms.ValidationError(f"Email {email} is already exist.")

    def clean_username(self):
        username = self.cleaned_data['username']
        try:
            myuser = MyUser.objects.get(username=username)
        except Exception as e:
            return username
        raise forms.ValidationError(f"username {username} is already exist.")

         



         
        
class UserLoginForm(forms.ModelForm):
    password=forms.CharField(
        
        widget = forms.PasswordInput(attrs={'placeholder':'password', 'class':'input'})

    ) 
    email=forms.CharField(
        
        widget = forms.EmailInput(attrs={'placeholder':'email', 'class':'input'})

    )  

    class Meta:
        model=MyUser
        fields=('email', 'password')

    def clean(self):
        if self.is_valid():
            email=self.cleaned_data['email']
            password=self.cleaned_data['password']

            if not authenticate(email=email, password=password):
                raise forms.ValidationError("username or password incorrect")



class ReportIssuesToParentForm(forms.ModelForm):

    
    name = forms.CharField(
            #label=True,
            widget=forms.TextInput(attrs={'id' :'', 'placeholder' : 'Enter Student Name '})
      
       )
    
    
    
    

    class Meta:
        model = ReportIssuesToParent
        fields = [
            "name",
            
            "email",
            "phone",
            
            "send_through_email",
            "send_through_text"
            

        ]














class Form1ReportForm(forms.ModelForm):

    
    name = forms.CharField(
            #label=True,
            widget=forms.TextInput(attrs={'id' :'name', 'placeholder' : 'Enter Student Name To Search'})
      
       )
    phone = forms.CharField(
            #label=True,
            widget=forms.TextInput(attrs={'id' :'phone', 'placeholder' : 'Enter Phone Number Eg: +255628431507'})
      
       )
    email = forms.EmailField(
            #label=True,
            widget=forms.TextInput(attrs={'id' :'phone', 'placeholder' : 'Enter Email '})
      
       )
    
    

    class Meta:
        model = Form1Report
        fields = [
			"name",
            
			"email",
			"phone",
			"body",
			"description"
			

        ]

class Form1StudentsForm(forms.ModelForm):
    
    lname = forms.CharField(
            #label=True,
            widget=forms.TextInput(attrs={'id' :'name', 'placeholder' : 'Enter Student Last Name '})
      
       )
   

    class Meta:
        model = Form1Students
        fields = '__all__'      

#FORM TWO FORM
class Form2ReportForm(forms.ModelForm):

    
    name = forms.CharField(
            #label=True,
            widget=forms.TextInput(attrs={'id' :'name', 'placeholder' : 'Enter Student Name To Search'})
      
       )
    phone = forms.CharField(
            #label=True,
            widget=forms.TextInput(attrs={'id' :'phone', 'placeholder' : 'Enter Phone Number Eg: +255628431507'})
      
       )
    email = forms.EmailField(
            #label=True,
            widget=forms.TextInput(attrs={'id' :'phone', 'placeholder' : 'Enter Email '})
      
       )
    
    

    class Meta:
        model = Form2Report
        fields = [
            "name",
            
            "email",
            "phone",
            "body",
            "description"
            

        ]

class Form2StudentsForm(forms.ModelForm):
    
    lname = forms.CharField(
            #label=True,
            widget=forms.TextInput(attrs={'id' :'name', 'placeholder' : 'Enter Student Last Name '})
      
       )
   

    class Meta:
        model = Form2Students
        fields = '__all__'         




#FORM THREE FORM

class Form3ReportForm(forms.ModelForm):

    
    name = forms.CharField(
            #label=True,
            widget=forms.TextInput(attrs={'id' :'name', 'placeholder' : 'Enter Student Name To Search'})
      
       )
    phone = forms.CharField(
            #label=True,
            widget=forms.TextInput(attrs={'id' :'phone', 'placeholder' : 'Enter Phone Number Eg: +255628431507'})
      
       )
    email = forms.EmailField(
            #label=True,
            widget=forms.TextInput(attrs={'id' :'phone', 'placeholder' : 'Enter Email '})
      
       )
    
    

    class Meta:
        model = Form3Report
        fields = [
            "name",
            
            "email",
            "phone",
            "body",
            "description"
            

        ]

class Form3StudentsForm(forms.ModelForm):
    
    lname = forms.CharField(
            #label=True,
            widget=forms.TextInput(attrs={'id' :'name', 'placeholder' : 'Enter Student Last Name '})
      
       )
   

    class Meta:
        model = Form3Students
        fields = '__all__' 





# FORM FOUR FORM

class Form4ReportForm(forms.ModelForm):

    
    name = forms.CharField(
            #label=True,
            widget=forms.TextInput(attrs={'id' :'name', 'placeholder' : 'Enter Student Name To Search'})
      
       )
    phone = forms.CharField(
            #label=True,
            widget=forms.TextInput(attrs={'id' :'phone', 'placeholder' : 'Enter Phone Number Eg: +255628431507'})
      
       )
    email = forms.EmailField(
            #label=True,
            widget=forms.TextInput(attrs={'id' :'phone', 'placeholder' : 'Enter Email '})
      
       )
    
    

    class Meta:
        model = Form4Report
        fields = [
            "name",
            
            "email",
            "phone",
            "body",
            "description"
            

        ]

class Form4StudentsForm(forms.ModelForm):
    
    lname = forms.CharField(
            #label=True,
            widget=forms.TextInput(attrs={'id' :'name', 'placeholder' : 'Enter Student Last Name '})
      
       )
   

    class Meta:
        model = Form4Students
        fields = '__all__' 
        



#FORM FIVE FORM




# PCM FORM 5 FORM
class PcmForm5ReportForm(forms.ModelForm):

    
    name = forms.CharField(
            #label=True,
            widget=forms.TextInput(attrs={'id' :'name', 'placeholder' : 'Enter Student Name To Search'})
      
       )
    phone = forms.CharField(
            #label=True,
            widget=forms.TextInput(attrs={'id' :'phone', 'placeholder' : 'Enter Phone Number Eg: +255628431507'})
      
       )
    email = forms.EmailField(
            #label=True,
            widget=forms.TextInput(attrs={'id' :'phone', 'placeholder' : 'Enter Email '})
      
       )
    
    

    class Meta:
        model = PcmForm5Report
        fields = [
            "name",
            
            "email",
            "phone",
            "body",
            "description"
            

        ]

class PcmForm5StudentsForm(forms.ModelForm):
    
    lname = forms.CharField(
            #label=True,
            widget=forms.TextInput(attrs={'id' :'name', 'placeholder' : 'Enter Student Last Name '})
      
       )
   

    class Meta:
        model = PcmForm5Students
        fields = '__all__' 


#PCB FORM 5 FORM
class PcbForm5ReportForm(forms.ModelForm):

    
    name = forms.CharField(
            #label=True,
            widget=forms.TextInput(attrs={'id' :'name', 'placeholder' : 'Enter Student Name To Search'})
      
       )
    phone = forms.CharField(
            #label=True,
            widget=forms.TextInput(attrs={'id' :'phone', 'placeholder' : 'Enter Phone Number Eg: +255628431507'})
      
       )
    email = forms.EmailField(
            #label=True,
            widget=forms.TextInput(attrs={'id' :'phone', 'placeholder' : 'Enter Email '})
      
       )
    
    

    class Meta:
        model = PcbForm5Report
        fields = [
            "name",
            
            "email",
            "phone",
            "body",
            "description"
            

        ]

class PcbForm5StudentsForm(forms.ModelForm):
    
    lname = forms.CharField(
            #label=True,
            widget=forms.TextInput(attrs={'id' :'name', 'placeholder' : 'Enter Student Last Name '})
      
       )
   

    class Meta:
        model = PcbForm5Students
        fields = '__all__' 

# PGM FORM 5 FORMS
class PgmForm5ReportForm(forms.ModelForm):

    
    name = forms.CharField(
            #label=True,
            widget=forms.TextInput(attrs={'id' :'name', 'placeholder' : 'Enter Student Name To Search'})
      
       )
    phone = forms.CharField(
            #label=True,
            widget=forms.TextInput(attrs={'id' :'phone', 'placeholder' : 'Enter Phone Number Eg: +255628431507'})
      
       )
    email = forms.EmailField(
            #label=True,
            widget=forms.TextInput(attrs={'id' :'phone', 'placeholder' : 'Enter Email '})
      
       )
    
    

    class Meta:
        model = PgmForm5Report
        fields = [
            "name",
            
            "email",
            "phone",
            "body",
            "description"
            

        ]

class PgmForm5StudentsForm(forms.ModelForm):
    
    lname = forms.CharField(
            #label=True,
            widget=forms.TextInput(attrs={'id' :'name', 'placeholder' : 'Enter Student Last Name '})
      
       )
   

    class Meta:
        model = PgmForm5Students
        fields = '__all__' 


#HGL FORM 5 FORM
class HglForm5ReportForm(forms.ModelForm):

    
    name = forms.CharField(
            #label=True,
            widget=forms.TextInput(attrs={'id' :'name', 'placeholder' : 'Enter Student Name To Search'})
      
       )
    phone = forms.CharField(
            #label=True,
            widget=forms.TextInput(attrs={'id' :'phone', 'placeholder' : 'Enter Phone Number Eg: +255628431507'})
      
       )
    email = forms.EmailField(
            #label=True,
            widget=forms.TextInput(attrs={'id' :'phone', 'placeholder' : 'Enter Email '})
      
       )
    
    

    class Meta:
        model = HglForm5Report
        fields = [
            "name",
            
            "email",
            "phone",
            "body",
            "description"
            

        ]

class HglForm5StudentsForm(forms.ModelForm):
    
    lname = forms.CharField(
            #label=True,
            widget=forms.TextInput(attrs={'id' :'name', 'placeholder' : 'Enter Student Last Name '})
      
       )
   

    class Meta:
        model = HglForm5Students
        fields = '__all__' 


#HGK FORM 5 FORM
class HgkForm5ReportForm(forms.ModelForm):

    
    name = forms.CharField(
            #label=True,
            widget=forms.TextInput(attrs={'id' :'name', 'placeholder' : 'Enter Student Name To Search'})
      
       )
    phone = forms.CharField(
            #label=True,
            widget=forms.TextInput(attrs={'id' :'phone', 'placeholder' : 'Enter Phone Number Eg: +255628431507'})
      
       )
    email = forms.EmailField(
            #label=True,
            widget=forms.TextInput(attrs={'id' :'phone', 'placeholder' : 'Enter Email '})
      
       )
    
    

    class Meta:
        model = HgkForm5Report
        fields = [
            "name",
            
            "email",
            "phone",
            "body",
            "description"
            

        ]

class HgkForm5StudentsForm(forms.ModelForm):
    
    lname = forms.CharField(
            #label=True,
            widget=forms.TextInput(attrs={'id' :'name', 'placeholder' : 'Enter Student Last Name '})
      
       )
   

    class Meta:
        model = HgkForm5Students
        fields = '__all__' 


#CBG FORM 5 FORM
class CbgForm5ReportForm(forms.ModelForm):

    
    name = forms.CharField(
            #label=True,
            widget=forms.TextInput(attrs={'id' :'name', 'placeholder' : 'Enter Student Name To Search'})
      
       )
    phone = forms.CharField(
            #label=True,
            widget=forms.TextInput(attrs={'id' :'phone', 'placeholder' : 'Enter Phone Number Eg: +255628431507'})
      
       )
    email = forms.EmailField(
            #label=True,
            widget=forms.TextInput(attrs={'id' :'phone', 'placeholder' : 'Enter Email '})
      
       )
    
    

    class Meta:
        model = CbgForm5Report
        fields = [
            "name",
            
            "email",
            "phone",
            "body",
            "description"
            

        ]

class CbgForm5StudentsForm(forms.ModelForm):
    
    lname = forms.CharField(
            #label=True,
            widget=forms.TextInput(attrs={'id' :'name', 'placeholder' : 'Enter Student Last Name '})
      
       )
   

    class Meta:
        model = CbgForm5Students
        fields = '__all__' 

#HKL FORM 5 FORM
class HklForm5ReportForm(forms.ModelForm):

    
    name = forms.CharField(
            #label=True,
            widget=forms.TextInput(attrs={'id' :'name', 'placeholder' : 'Enter Student Name To Search'})
      
       )
    phone = forms.CharField(
            #label=True,
            widget=forms.TextInput(attrs={'id' :'phone', 'placeholder' : 'Enter Phone Number Eg: +255628431507'})
      
       )
    email = forms.EmailField(
            #label=True,
            widget=forms.TextInput(attrs={'id' :'phone', 'placeholder' : 'Enter Email '})
      
       )
    
    

    class Meta:
        model = HklForm5Report
        fields = [
            "name",
            
            "email",
            "phone",
            "body",
            "description"
            

        ]

class HklForm5StudentsForm(forms.ModelForm):
    
    lname = forms.CharField(
            #label=True,
            widget=forms.TextInput(attrs={'id' :'name', 'placeholder' : 'Enter Student Last Name '})
      
       )
   

    class Meta:
        model = HklForm5Students
        fields = '__all__' 


#ECA FORM 5 FORM
class EcaForm5ReportForm(forms.ModelForm):

    
    name = forms.CharField(
            #label=True,
            widget=forms.TextInput(attrs={'id' :'name', 'placeholder' : 'Enter Student Name To Search'})
      
       )
    phone = forms.CharField(
            #label=True,
            widget=forms.TextInput(attrs={'id' :'phone', 'placeholder' : 'Enter Phone Number Eg: +255628431507'})
      
       )
    email = forms.EmailField(
            #label=True,
            widget=forms.TextInput(attrs={'id' :'phone', 'placeholder' : 'Enter Email '})
      
       )
    
    

    class Meta:
        model = EcaForm5Report
        fields = [
            "name",
            
            "email",
            "phone",
            "body",
            "description"
            

        ]

class EcaForm5StudentsForm(forms.ModelForm):
    
    lname = forms.CharField(
            #label=True,
            widget=forms.TextInput(attrs={'id' :'name', 'placeholder' : 'Enter Student Last Name '})
      
       )
   

    class Meta:
        model = EcaForm5Students
        fields = '__all__' 












#FORM SIX FORM

















#FORM 6 FORM 6 FORM 6 FORM 6 FORM 6 FORMS


# PCM FORM 6 FORM
class PcmForm6ReportForm(forms.ModelForm):

    
    name = forms.CharField(
            #label=True,
            widget=forms.TextInput(attrs={'id' :'name', 'placeholder' : 'Enter Student Name To Search'})
      
       )
    phone = forms.CharField(
            #label=True,
            widget=forms.TextInput(attrs={'id' :'phone', 'placeholder' : 'Enter Phone Number Eg: +255628431507'})
      
       )
    email = forms.EmailField(
            #label=True,
            widget=forms.TextInput(attrs={'id' :'phone', 'placeholder' : 'Enter Email '})
      
       )
    
    

    class Meta:
        model = PcmForm6Report
        fields = [
            "name",
            
            "email",
            "phone",
            "body",
            "description"
            

        ]

class PcmForm6StudentsForm(forms.ModelForm):
    
    lname = forms.CharField(
            #label=True,
            widget=forms.TextInput(attrs={'id' :'name', 'placeholder' : 'Enter Student Last Name '})
      
       )
   

    class Meta:
        model = PcmForm6Students
        fields = '__all__' 


#PCB FORM 6 FORM
class PcbForm6ReportForm(forms.ModelForm):

    
    name = forms.CharField(
            #label=True,
            widget=forms.TextInput(attrs={'id' :'name', 'placeholder' : 'Enter Student Name To Search'})
      
       )
    phone = forms.CharField(
            #label=True,
            widget=forms.TextInput(attrs={'id' :'phone', 'placeholder' : 'Enter Phone Number Eg: +255628431507'})
      
       )
    email = forms.EmailField(
            #label=True,
            widget=forms.TextInput(attrs={'id' :'phone', 'placeholder' : 'Enter Email '})
      
       )
    
    

    class Meta:
        model = PcbForm6Report
        fields = [
            "name",
            
            "email",
            "phone",
            "body",
            "description"
            

        ]

class PcbForm6StudentsForm(forms.ModelForm):
    
    lname = forms.CharField(
            #label=True,
            widget=forms.TextInput(attrs={'id' :'name', 'placeholder' : 'Enter Student Last Name '})
      
       )
   

    class Meta:
        model = PcbForm6Students
        fields = '__all__' 

# PGM FORM 6 FORMS
class PgmForm6ReportForm(forms.ModelForm):

    
    name = forms.CharField(
            #label=True,
            widget=forms.TextInput(attrs={'id' :'name', 'placeholder' : 'Enter Student Name To Search'})
      
       )
    phone = forms.CharField(
            #label=True,
            widget=forms.TextInput(attrs={'id' :'phone', 'placeholder' : 'Enter Phone Number Eg: +255628431507'})
      
       )
    email = forms.EmailField(
            #label=True,
            widget=forms.TextInput(attrs={'id' :'phone', 'placeholder' : 'Enter Email '})
      
       )
    
    

    class Meta:
        model = PgmForm6Report
        fields = [
            "name",
            
            "email",
            "phone",
            "body",
            "description"
            

        ]

class PgmForm6StudentsForm(forms.ModelForm):
    
    lname = forms.CharField(
            #label=True,
            widget=forms.TextInput(attrs={'id' :'name', 'placeholder' : 'Enter Student Last Name '})
      
       )
   

    class Meta:
        model = PgmForm6Students
        fields = '__all__' 


#HGL FORM 6 FORM
class HglForm6ReportForm(forms.ModelForm):

    
    name = forms.CharField(
            #label=True,
            widget=forms.TextInput(attrs={'id' :'name', 'placeholder' : 'Enter Student Name To Search'})
      
       )
    phone = forms.CharField(
            #label=True,
            widget=forms.TextInput(attrs={'id' :'phone', 'placeholder' : 'Enter Phone Number Eg: +255628431507'})
      
       )
    email = forms.EmailField(
            #label=True,
            widget=forms.TextInput(attrs={'id' :'phone', 'placeholder' : 'Enter Email '})
      
       )
    
    

    class Meta:
        model = HglForm6Report
        fields = [
            "name",
            
            "email",
            "phone",
            "body",
            "description"
            

        ]

class HglForm6StudentsForm(forms.ModelForm):
    
    lname = forms.CharField(
            #label=True,
            widget=forms.TextInput(attrs={'id' :'name', 'placeholder' : 'Enter Student Last Name '})
      
       )
   

    class Meta:
        model = HglForm6Students
        fields = '__all__' 


#HGK FORM 6 FORM
class HgkForm6ReportForm(forms.ModelForm):

    
    name = forms.CharField(
            #label=True,
            widget=forms.TextInput(attrs={'id' :'name', 'placeholder' : 'Enter Student Name To Search'})
      
       )
    phone = forms.CharField(
            #label=True,
            widget=forms.TextInput(attrs={'id' :'phone', 'placeholder' : 'Enter Phone Number Eg: +255628431507'})
      
       )
    email = forms.EmailField(
            #label=True,
            widget=forms.TextInput(attrs={'id' :'phone', 'placeholder' : 'Enter Email '})
      
       )
    
    

    class Meta:
        model = HgkForm6Report
        fields = [
            "name",
            
            "email",
            "phone",
            "body",
            "description"
            

        ]

class HgkForm6StudentsForm(forms.ModelForm):
    
    lname = forms.CharField(
            #label=True,
            widget=forms.TextInput(attrs={'id' :'name', 'placeholder' : 'Enter Student Last Name '})
      
       )
   

    class Meta:
        model = HgkForm6Students
        fields = '__all__' 


#CBG FORM 6 FORM
class CbgForm6ReportForm(forms.ModelForm):

    
    name = forms.CharField(
            #label=True,
            widget=forms.TextInput(attrs={'id' :'name', 'placeholder' : 'Enter Student Name To Search'})
      
       )
    phone = forms.CharField(
            #label=True,
            widget=forms.TextInput(attrs={'id' :'phone', 'placeholder' : 'Enter Phone Number Eg: +255628431507'})
      
       )
    email = forms.EmailField(
            #label=True,
            widget=forms.TextInput(attrs={'id' :'phone', 'placeholder' : 'Enter Email '})
      
       )
    
    

    class Meta:
        model = CbgForm6Report
        fields = [
            "name",
            
            "email",
            "phone",
            "body",
            "description"
            

        ]

class CbgForm6StudentsForm(forms.ModelForm):
    
    lname = forms.CharField(
            #label=True,
            widget=forms.TextInput(attrs={'id' :'name', 'placeholder' : 'Enter Student Last Name '})
      
       )
   

    class Meta:
        model = CbgForm6Students
        fields = '__all__' 

#HKL FORM 6 FORM
class HklForm6ReportForm(forms.ModelForm):

    
    name = forms.CharField(
            #label=True,
            widget=forms.TextInput(attrs={'id' :'name', 'placeholder' : 'Enter Student Name To Search'})
      
       )
    phone = forms.CharField(
            #label=True,
            widget=forms.TextInput(attrs={'id' :'phone', 'placeholder' : 'Enter Phone Number Eg: +255628431507'})
      
       )
    email = forms.EmailField(
            #label=True,
            widget=forms.TextInput(attrs={'id' :'phone', 'placeholder' : 'Enter Email '})
      
       )
    
    

    class Meta:
        model = HklForm6Report
        fields = [
            "name",
            
            "email",
            "phone",
            "body",
            "description"
            

        ]

class HklForm6StudentsForm(forms.ModelForm):
    
    lname = forms.CharField(
            #label=True,
            widget=forms.TextInput(attrs={'id' :'name', 'placeholder' : 'Enter Student Last Name '})
      
       )
   

    class Meta:
        model = HklForm6Students
        fields = '__all__' 


#ECA FORM 6 FORM
class EcaForm6ReportForm(forms.ModelForm):

    
    name = forms.CharField(
            #label=True,
            widget=forms.TextInput(attrs={'id' :'name', 'placeholder' : 'Enter Student Name To Search'})
      
       )
    phone = forms.CharField(
            #label=True,
            widget=forms.TextInput(attrs={'id' :'phone', 'placeholder' : 'Enter Phone Number Eg: +255628431507'})
      
       )
    email = forms.EmailField(
            #label=True,
            widget=forms.TextInput(attrs={'id' :'phone', 'placeholder' : 'Enter Email '})
      
       )
    
    

    class Meta:
        model = EcaForm6Report
        fields = [
            "name",
            
            "email",
            "phone",
            "body",
            "description"
            

        ]

class EcaForm6StudentsForm(forms.ModelForm):
    
    lname = forms.CharField(
            #label=True,
            widget=forms.TextInput(attrs={'id' :'name', 'placeholder' : 'Enter Student Last Name '})
      
       )
   

    class Meta:
        model = EcaForm6Students
        fields = '__all__' 

