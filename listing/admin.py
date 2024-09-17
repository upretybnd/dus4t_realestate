from django.contrib import admin
from .models import Post, PostImage


class PostImageInline(admin.TabularInline):
    model = PostImage
    extra = 1


class PostAdmin(admin.ModelAdmin):
    list_display = ('post_name', 'category', 'price', 'is_available', 'listing_type', 'created_date', 'modified_date')
    prepopulated_fields = {'slug': ('post_name',)}
    list_filter = ('category', 'is_available', 'listing_type', 'created_date')
    search_fields = ('post_name', 'district', 'city', 'place')
    inlines = [PostImageInline]


admin.site.register(Post, PostAdmin)
