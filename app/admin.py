from django.contrib import admin
from .models import Group , Post

class PostAdmin(admin.ModelAdmin):
	prepopulated_fields = {'slug': ('title',)}

class GroupAdmin(admin.ModelAdmin):
	prepopulated_fields = {'slug': ('name',)}

admin.site.register(Post, PostAdmin)
admin.site.register(Group , GroupAdmin)

