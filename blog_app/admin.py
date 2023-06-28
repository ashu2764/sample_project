from django.contrib import admin
from .models import Category,Post
# Register your models here.


# for configration of Category admin
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('title','description','add_date',)
    search_fields=('title',)
    list_filter=('title',)




#  post admin

class PostAdmin(admin.ModelAdmin):
    list_display=('title','cat',)
    search_fields=('title','cat',)
    list_filter=('cat',)
    list_per_page=5



admin.site.register(Category, CategoryAdmin)
admin.site.register(Post, PostAdmin)
