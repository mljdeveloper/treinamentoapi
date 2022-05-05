from django.contrib import admin
from .models import Position

# Register your models here.


class PositionAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'create_at',
                    'updated_at', 'mostrar', 'username')
    list_display_links = ('id', 'name')
    list_per_page = 200
    search_fields = ('id', 'name',)
    list_editable = ('mostrar',)
    exclude = ['username', ]

    def get_queryset(self, request):
        qs = super(PositionAdmin, self).get_queryset(request)
        return qs.filter(username=request.user)

    def save_model(self, request, obj, form, change):
        obj.username = request.user
        super().save_model(request, obj, form, change)


admin.site.register(Position, PositionAdmin)
