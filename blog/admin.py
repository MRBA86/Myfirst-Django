from django.contrib import admin
from blog.models import Post , Category

class PostAdmin(admin.ModelAdmin):
    date_hierarchy = 'created_date'
    empty_value_display = 'خالی'
    list_display =  ('title', 'author','status', 'counted_views', 'created_date','published_date','updated_date')
    list_filter = ('status','author')
    search_fields = ['title', 'content']

admin.site.register(Category)
admin.site.register(Post,PostAdmin)

# Register your models here.
