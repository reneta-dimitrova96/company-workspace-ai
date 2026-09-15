from django.contrib import admin

from companies.models import Company


class CompanyAdmin(admin.ModelAdmin):
    list_display = ('name', 'created_at', 'updated_at')


admin.site.register(Company, CompanyAdmin)
