from django.contrib import admin
from .models import Article, Category

# Register your models here.
def make_published(modeladmin, request, queryset):
		rows_updated = queryset.update(status='p')
		if rows_updated == 1:
			message_bit = "منتشر شد."
		else:
			message_bit = "منتشر شدند."
		modeladmin.message_user(request, "{} مقاله {}".format(rows_updated, message_bit))
make_published.short_description = "انتشار مقالات انتخاب شده"


def make_draft(modeladmin, request, queryset):
        rows_updated = queryset.update(status='d')
        if rows_updated == 1:
            message_bit = "پیش‌نویس شد."
        else:
            message_bit = "پیش‌نویس شدند."
        modeladmin.message_user(request, "{} مقاله {}".format(rows_updated, message_bit))
make_draft.short_description = "پیش‌نویس شدن مقالات انتخاب شده"




class CategoryAdmin(admin.ModelAdmin):
	list_display = (
		'position',
		'title',
		'slug',
		'parent',
		'status',
		
	)
	
	list_filter = (
		['status']
		
	)

	search_fields = (
		'title',
		'slug',
	)
	
	prepopulated_fields = {'slug' : ('title',)} #برای اینکه فیلد اسلاک از فیلد تایتل به صورت خودکار پر شود
	
admin.site.register(Category,CategoryAdmin)

class ArticleAdmin(admin.ModelAdmin):
	list_display = (
		'title',
		'slug',
		'jpublish',
		'status',
		'category_to_str',
		
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
	actions = [
     	make_published, 
            make_draft,
            ]
	
	def category_to_str(self, obj):
		return ", ".join([category.title for category in obj.category_published()])
	category_to_str.short_description = 'دسته بندی'   
			 
admin.site.register(Article,ArticleAdmin)
