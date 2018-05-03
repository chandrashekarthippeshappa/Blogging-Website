from django.contrib import admin
from .models import Blog,Other



class BlogAdmin(admin.ModelAdmin):
	list_display = ['title','author','published']
	search_fields = ['title']
	list_filter = ['published']

admin.site.register(Blog,BlogAdmin)
admin.site.register(Other)
