from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from DimosoApp.models import *

# Register your models here.

class MyUserAdmin(BaseUserAdmin):
    list_display=('username', 'email', 'company_name', 'profile_image', 'date_joined', 'last_login', 'is_admin', 'is_active')
    search_fields=('email', 'first_name', 'last_name')
    readonly_fields=('date_joined', 'last_login')
    filter_horizontal=()
    list_filter=('last_login',)
    fieldsets=()

    add_fieldsets=(
        (None,{
            'classes':('wide'),
            'fields':('email', 'username', 'first_name', 'middle_name', 'last_name', 'company_name', 'phone', 'profile_image', 'password1', 'password2'),
        }),
    )

    ordering=('email',)
class Form1StudentsAdmin(admin.ModelAdmin):
	list_display = ["fname", "sname", "lname", "gender", "age",  "post_date"]
	#prepopulated_fields={'slug':('name',)}
class Form1ReportAdmin(admin.ModelAdmin):
	list_display = ["name", "post_date"]


class Form2StudentsAdmin(admin.ModelAdmin):
	list_display = ["fname", "sname", "lname", "gender", "age",  "post_date"]
	#prepopulated_fields={'slug':('name',)}
class Form2ReportAdmin(admin.ModelAdmin):
	list_display = ["name", "post_date"]


class Form3StudentsAdmin(admin.ModelAdmin):
	list_display = ["fname", "sname", "lname", "gender", "age",  "post_date"]
	#prepopulated_fields={'slug':('name',)}
class Form3ReportAdmin(admin.ModelAdmin):
	list_display = ["name", "post_date"]


class Form4StudentsAdmin(admin.ModelAdmin):
	list_display = ["fname", "sname", "lname", "gender", "age",  "post_date"]
	#prepopulated_fields={'slug':('name',)}
class Form4ReportAdmin(admin.ModelAdmin):
	list_display = ["name", "post_date"]


class Form5StudentsAdmin(admin.ModelAdmin):
	list_display = ["fname", "sname", "lname", "gender", "age",  "post_date"]
	#prepopulated_fields={'slug':('name',)}
class Form5ReportAdmin(admin.ModelAdmin):
	list_display = ["name", "post_date"]

class PcmForm5StudentsAdmin(admin.ModelAdmin):
	list_display = ["fname", "sname", "lname", "gender", "age",  "post_date"]
	#prepopulated_fields={'slug':('name',)}
class PcmForm5ReportAdmin(admin.ModelAdmin):
	list_display = ["name", "post_date"]


class PcbForm5StudentsAdmin(admin.ModelAdmin):
	list_display = ["fname", "sname", "lname", "gender", "age",  "post_date"]
	#prepopulated_fields={'slug':('name',)}
class PcbForm5ReportAdmin(admin.ModelAdmin):
	list_display = ["name", "post_date"]

class PgmForm5StudentsAdmin(admin.ModelAdmin):
	list_display = ["fname", "sname", "lname", "gender", "age",  "post_date"]
	#prepopulated_fields={'slug':('name',)}
class PgmForm5ReportAdmin(admin.ModelAdmin):
	list_display = ["name", "post_date"]


class HglForm5StudentsAdmin(admin.ModelAdmin):
	list_display = ["fname", "sname", "lname", "gender", "age",  "post_date"]
	#prepopulated_fields={'slug':('name',)}
class HglForm5ReportAdmin(admin.ModelAdmin):
	list_display = ["name", "post_date"]


class HgkForm5StudentsAdmin(admin.ModelAdmin):
	list_display = ["fname", "sname", "lname", "gender", "age",  "post_date"]
	#prepopulated_fields={'slug':('name',)}
class HgkForm5ReportAdmin(admin.ModelAdmin):
	list_display = ["name", "post_date"]

class CbgForm5StudentsAdmin(admin.ModelAdmin):
	list_display = ["fname", "sname", "lname", "gender", "age",  "post_date"]
	#prepopulated_fields={'slug':('name',)}
class CbgForm5ReportAdmin(admin.ModelAdmin):
	list_display = ["name", "post_date"]


class HklForm5StudentsAdmin(admin.ModelAdmin):
	list_display = ["fname", "sname", "lname", "gender", "age",  "post_date"]
	#prepopulated_fields={'slug':('name',)}
class HklForm5ReportAdmin(admin.ModelAdmin):
	list_display = ["name", "post_date"]

class EcaForm5StudentsAdmin(admin.ModelAdmin):
	list_display = ["fname", "sname", "lname", "gender", "age",  "post_date"]
	#prepopulated_fields={'slug':('name',)}
class EcaForm5ReportAdmin(admin.ModelAdmin):
	list_display = ["name", "post_date"]






#form 6 form 6 form 6

class PcmForm6StudentsAdmin(admin.ModelAdmin):
	list_display = ["fname", "sname", "lname", "gender", "age",  "post_date"]
	#prepopulated_fields={'slug':('name',)}
class PcmForm6ReportAdmin(admin.ModelAdmin):
	list_display = ["name", "post_date"]

class PcbForm6StudentsAdmin(admin.ModelAdmin):
	list_display = ["fname", "sname", "lname", "gender", "age",  "post_date"]
	#prepopulated_fields={'slug':('name',)}
class PcbForm6ReportAdmin(admin.ModelAdmin):
	list_display = ["name", "post_date"]

class PgmForm6StudentsAdmin(admin.ModelAdmin):
	list_display = ["fname", "sname", "lname", "gender", "age",  "post_date"]
	#prepopulated_fields={'slug':('name',)}
class PgmForm6ReportAdmin(admin.ModelAdmin):
	list_display = ["name", "post_date"]

class HglForm6StudentsAdmin(admin.ModelAdmin):
	list_display = ["fname", "sname", "lname", "gender", "age",  "post_date"]
	#prepopulated_fields={'slug':('name',)}
class HglForm6ReportAdmin(admin.ModelAdmin):
	list_display = ["name", "post_date"]

class HgkForm6StudentsAdmin(admin.ModelAdmin):
	list_display = ["fname", "sname", "lname", "gender", "age",  "post_date"]
	#prepopulated_fields={'slug':('name',)}
class HgkForm6ReportAdmin(admin.ModelAdmin):
	list_display = ["name", "post_date"]

class CbgForm6StudentsAdmin(admin.ModelAdmin):
	list_display = ["fname", "sname", "lname", "gender", "age",  "post_date"]
	#prepopulated_fields={'slug':('name',)}
class CbgForm6ReportAdmin(admin.ModelAdmin):
	list_display = ["name", "post_date"]


class HklForm6StudentsAdmin(admin.ModelAdmin):
	list_display = ["fname", "sname", "lname", "gender", "age",  "post_date"]
	#prepopulated_fields={'slug':('name',)}
class HklForm6ReportAdmin(admin.ModelAdmin):
	list_display = ["name", "post_date"]

class EcaForm6StudentsAdmin(admin.ModelAdmin):
	list_display = ["fname", "sname", "lname", "gender", "age",  "post_date"]
	#prepopulated_fields={'slug':('name',)}
class EcaForm6ReportAdmin(admin.ModelAdmin):
	list_display = ["name", "post_date"]








class DarasaAdmin(admin.ModelAdmin):
	list_display = ["name", "idadi"]

class CombinationAdmin(admin.ModelAdmin):
	list_display = ["name", "idadi"]

admin.site.register(MyUser, MyUserAdmin)

admin.site.register(Darasa, DarasaAdmin)
admin.site.register(Combination, CombinationAdmin)
admin.site.register(ReportIssuesToParent)

#form one
admin.site.register(Form1Students, Form1StudentsAdmin)
admin.site.register(Form1Report, Form1ReportAdmin)

#form two
admin.site.register(Form2Students, Form2StudentsAdmin)
admin.site.register(Form2Report, Form2ReportAdmin)

#form three
admin.site.register(Form3Students, Form3StudentsAdmin)
admin.site.register(Form3Report, Form3ReportAdmin)

#form four
admin.site.register(Form4Students, Form4StudentsAdmin)
admin.site.register(Form4Report, Form4ReportAdmin)


#form five
admin.site.register(Form5Students, Form5StudentsAdmin)
admin.site.register(Form5Report, Form5ReportAdmin)

#pcm form five
admin.site.register(PcmForm5Students, PcmForm5StudentsAdmin)
admin.site.register(PcmForm5Report, PcmForm5ReportAdmin)

#pcb form five
admin.site.register(PcbForm5Students, PcbForm5StudentsAdmin)
admin.site.register(PcbForm5Report, PcbForm5ReportAdmin)

#Pgm form five
admin.site.register(PgmForm5Students, PgmForm5StudentsAdmin)
admin.site.register(PgmForm5Report, PgmForm5ReportAdmin)


#hgl form five
admin.site.register(HglForm5Students, HglForm5StudentsAdmin)
admin.site.register(HglForm5Report, HglForm5ReportAdmin)

#Hgk form five
admin.site.register(HgkForm5Students, HgkForm5StudentsAdmin)
admin.site.register(HgkForm5Report, HgkForm5ReportAdmin)

#Cbg form five
admin.site.register(CbgForm5Students, CbgForm5StudentsAdmin)
admin.site.register(CbgForm5Report, CbgForm5ReportAdmin)

#Hkl form five
admin.site.register(HklForm5Students, HklForm5StudentsAdmin)
admin.site.register(HklForm5Report, HklForm5ReportAdmin)

#Eca form five
admin.site.register(EcaForm5Students, EcaForm5StudentsAdmin)
admin.site.register(EcaForm5Report, EcaForm5ReportAdmin)









#FORM 6 FORM 6 FORM6 FORM 6


admin.site.register(PcmForm6Students, PcmForm6StudentsAdmin)
admin.site.register(PcmForm6Report, PcmForm6ReportAdmin)

admin.site.register(PcbForm6Students, PcbForm6StudentsAdmin)
admin.site.register(PcbForm6Report, PcbForm6ReportAdmin)

admin.site.register(PgmForm6Students, PgmForm6StudentsAdmin)
admin.site.register(PgmForm6Report, PgmForm6ReportAdmin)

admin.site.register(HglForm6Students, HglForm6StudentsAdmin)
admin.site.register(HglForm6Report, HglForm6ReportAdmin)

admin.site.register(HgkForm6Students, HgkForm6StudentsAdmin)
admin.site.register(HgkForm6Report, HgkForm6ReportAdmin)

admin.site.register(CbgForm6Students, CbgForm6StudentsAdmin)
admin.site.register(CbgForm6Report, CbgForm6ReportAdmin)

admin.site.register(HklForm6Students, HklForm6StudentsAdmin)
admin.site.register(HklForm6Report, HklForm6ReportAdmin)

admin.site.register(EcaForm6Students, EcaForm6StudentsAdmin)
admin.site.register(EcaForm6Report, EcaForm6ReportAdmin)


