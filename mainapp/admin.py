from django.contrib import admin
from .models import Post, Comment,Category, Tag
# Register your models here.
admin.site.register(Post)
admin.site.register(Comment)
class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name', )}

admin.site.register(Category, CategoryAdmin)


class TagAdmin(admin.ModelAdmin):
    pass
    # prepopulated_fields = {'slug': ('name', )}
admin.site.register(Tag, TagAdmin)