from django.contrib import admin
from .models import Course

# Register your models here.


class CourseAdmin(admin.ModelAdmin):
    list_display = ('id', 'coursename', 'create_at',
                    'updated_at', 'display', 'username')
    list_display_links = ('id', 'coursename')
    list_per_page = 200
    search_fields = ('id', 'coursename',)
    list_editable = ('display',)
    exclude = ['username', ]

    def get_queryset(self, request):
        qs = super(CourseAdmin, self).get_queryset(request)
        return qs.filter(username=request.user)

    def save_model(self, request, obj, form, change):
        obj.username = request.user
        super().save_model(request, obj, form, change)


admin.site.register(Course, CourseAdmin)
