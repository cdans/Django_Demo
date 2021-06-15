from django.contrib import admin

from demo.models import Book, BookNumber, Character, Author

admin.site.register(BookNumber)
admin.site.register(Character)
admin.site.register(Author)

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    # fields = ['title', 'description']
    list_display = ['title', 'price']
    list_filter = ['is_published']
    search_fields = ['title']
