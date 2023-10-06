from django.contrib import admin
from blog.models import Post , Category , Comment
from django_summernote.admin import SummernoteModelAdmin

class PostAdmin(SummernoteModelAdmin):
    date_hierarchy = 'created_date'
    empty_value_display = 'خالی'
    list_display =  ('title', 'author','status', 'counted_views', 'created_date','published_date','updated_date')
    list_filter = ('status','author')
    search_fields = ['title', 'content']
    summernote_fields = ('content',)

class CommentAdmin(admin.ModelAdmin):
    date_hierarchy = 'created_date'
    empty_value_display = 'خالی'
    list_display =  ('name','post','subject', 'approved', 'created_date','updated_date')
    list_filter = ('post','approved','email','name')
    search_fields = ['subject', 'message']
    #summernote_fields = ('content',)

admin.site.register(Comment,CommentAdmin)
admin.site.register(Category)
admin.site.register(Post,PostAdmin)

# Register your models here.
