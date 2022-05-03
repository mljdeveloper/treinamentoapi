from django.contrib import admin
from .models import Zipcode

# Register your models here.


class ZipcodeAdmin(admin.ModelAdmin):
    list_display = ('id', 'zipcode', 'address',
                    'address1', 'county', 'city', 'st',)
    list_display_links = ('id', 'zipcode')
    list_per_page = 200
    search_fields = ('id', 'zipcode',)

    def get_queryset(self, request):
        qs = super(ZipcodeAdmin, self).get_queryset(request)
        return qs

    def save_model(self, request, obj, form, change):
        super().save_model(request, obj, form, change)


admin.site.register(Zipcode, ZipcodeAdmin)
