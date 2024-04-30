from django.contrib import admin
from .models import Article

# Register your models here.
class ArticleAdmin(admin.ModelAdmin):
    list_display = (
        'title',
        'slug',
        'publish',
        'status',
        
    )
    
    list_filter = (
        'publish',
        'status',
        
    )

    search_fields = (
        'title',
        'description',
    )
    
    prepopulated_fields = {'slug' : ('title',)} #برای اینکه فیلد اسلاک از فیلد تایتل به صورت خودکار پر شود
    
    ordering = [
        '-status',
        '-publish',
    ]
admin.site.register(Article,ArticleAdmin)
