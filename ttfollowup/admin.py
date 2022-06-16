from django.contrib import admin
from .models import TTfollowup

# Register your models here.


class TTFollowupAdmin(admin.ModelAdmin):
    list_display = ('id', 'lead', 'username', 'description', 'create_at',)
    list_display_links = ('id', 'lead')
    list_per_page = 200
    search_fields = ('id', 'lead',)

    def get_queryset(self, request):
        qs = super(TTFollowupAdmin, self).get_queryset(request)
        return qs.filter()

    def save_model(self, request, obj, form, change):
        obj.username = request.user
        super().save_model(request, obj, form, change)


admin.site.register(TTfollowup, TTFollowupAdmin)
