from django.contrib import admin
from .models import Funcao

# Register your models here.


class FuncaoAdmin(admin.ModelAdmin):
    list_display = ('id', 'nomefuncao', 'create_at',
                    'updated_at', 'mostrar', 'parent_id')
    list_display_links = ('id', 'nomefuncao')
    list_per_page = 200
    search_fields = ('id', 'nomefuncao',)
    list_editable = ('mostrar',)
    exclude = ['username', ]

    def get_queryset(self, request):
        qs = super(FuncaoAdmin, self).get_queryset(request)
        return qs.filter(username=request.user)

    def save_model(self, request, obj, form, change):
        obj.username = request.user
        super().save_model(request, obj, form, change)


admin.site.register(Funcao, FuncaoAdmin)
