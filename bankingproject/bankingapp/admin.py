from django.contrib import admin


# Register your models here.

from .models import Registration,Branch,Personnal


class RegisterAdmin(admin.ModelAdmin):
    list_display = ['username', 'password']


admin.site.register(Registration, RegisterAdmin)


class BranchAdmin(admin.ModelAdmin):
    list_display = ['name', 'district', 'wikipedia_link']


admin.site.register(Branch, BranchAdmin)


class PersonalAdmin(admin.ModelAdmin):
    list_display = ['name', 'dob', 'age', 'gender', 'phonenumber', 'mailid', 'address', 'district', 'branch',
                    'account_type', 'materials_provide']
    list_editable = ['account_type','materials_provide']
    list_per_page = 20


admin.site.register(Personnal, PersonalAdmin)
