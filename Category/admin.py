from django.contrib import admin
from .models import Category

# Register your models here.


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'categoryname', 'create_at',
                    'updated_at', 'display', 'username')
    list_display_links = ('id', 'categoryname')
    list_per_page = 200
    search_fields = ('id', 'categoryname',)
    list_editable = ('display',)
    exclude = ['username', ]

    def get_queryset(self, request):
        qs = super(CategoryAdmin, self).get_queryset(request)
        return qs.filter(username=request.user)

    def save_model(self, request, obj, form, change):
        obj.username = request.user
        super().save_model(request, obj, form, change)


admin.site.register(Category, CategoryAdmin)
