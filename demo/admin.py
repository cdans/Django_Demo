from django.contrib import admin

from demo.models import Book

# admin.site.register(Book)
@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    # fields = ['title', 'description']
    list_display = ['title', 'price']
    list_filter = ['is_published']
    search_fields = ['title']