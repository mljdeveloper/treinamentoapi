from django.contrib import admin
from .models import Frequency

# Register your models here.


class FrequencyAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'days',   'create_at',
                    'updated_at', 'display', 'username')
    list_display_links = ('id', 'name')
    list_per_page = 200
    search_fields = ('id', 'name',)
    list_editable = ('display',)
    exclude = ['username', ]

    def get_queryset(self, request):
        qs = super(FrequencyAdmin, self).get_queryset(request)
        return qs.filter(username=request.user)

    def save_model(self, request, obj, form, change):
        obj.username = request.user
        super().save_model(request, obj, form, change)


admin.site.register(Frequency, FrequencyAdmin)
