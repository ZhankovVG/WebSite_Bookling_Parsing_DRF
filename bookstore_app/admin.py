from django.contrib import admin
from .models import *
from django.utils.safestring import mark_safe


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'url')
    prepopulated_fields = {'url' : ('name', )}
    list_display_links = ('name', )


class ReviewInline(admin.StackedInline):
    model = Reviews
    readonly_fields = ('name', 'email')
    extra = 1


@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ('name', )
    list_display_links = ('name', )


@admin.register(Books)
class BooksAdmin(admin.ModelAdmin):
    list_display = (
        'name', 
        'code', 
        'price',
        'get_image', 
        'description',
        'draft',
        )
    list_filter = ('name', 'price', 'draft')
    list_editable = ('draft', )
    prepopulated_fields = {'url' : ('name', )}
    list_display_links = ('name', )
    inlines = [ReviewInline]

    def get_image(self, object):
        return mark_safe(f"<img src={object.image.url} width='50' heigh='50' ")
    
    get_image.short_description = 'Изображение'


@admin.register(Reting)
class RetingAdmin(admin.ModelAdmin):
    list_display = ('ip', 'star', 'book')


admin.site.register(RatingsStar)


@admin.register(Reviews)
class ReviewsAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'email', 'parent', 'book')
    readonly_fields = ('name', 'email')
    list_display_links = ('name', )