from django.contrib import admin
import admin_thumbnails

from .models import *
# Register your models here.

@admin_thumbnails.thumbnail('image')
class ProductImageInline(admin.TabularInline):
    list_display = ['id']
    model = Images
    readonly_fields = ('id',)
    extra = 1

class Additional_InformationInline(admin.TabularInline):
    list_display = ['id']
    model = Additional_Information
    readonly_fields = ('id',)
    extra = 1

@admin_thumbnails.thumbnail('image')
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['id', 'title','image_tag','featured_category', 'create_at','update_at']
    list_editable = ['featured_category',]


@admin_thumbnails.thumbnail('image')
class Sub_CategoryAdmin(admin.ModelAdmin):
    list_display = ['id','title', 'category', 'featured_category', 'image_tag','update_at','create_at']
    list_editable = ['featured_category',]


class BrandAdmin(admin.ModelAdmin):
    list_display = ['title','image_tag','featured_brand','create_at','update_at',]



class ProductAdmin(admin.ModelAdmin):
    list_display = ['id','title','image_tag','featured_project', 'Top_Deals_Of_The_Day','Top_Selling_Products','Recommended_For_You', 'slug', 'create_at','update_at',]
    list_filter = ['sub_category']
    list_editable = ['featured_project', 'Top_Deals_Of_The_Day','Top_Selling_Products','Recommended_For_You']
    inlines = [ProductImageInline,Additional_InformationInline]


class CommentAdmin(admin.ModelAdmin):
    list_display = ['id','product','user','subject', 'rate','ip','status', 'create_at','update_at',]
    list_filter = ['status']
    list_editable = ['status',]


admin.site.register(Product,ProductAdmin)
admin.site.register(Category,CategoryAdmin)
admin.site.register(Sub_Category,Sub_CategoryAdmin)
admin.site.register(Brand,BrandAdmin)

admin.site.register(Size)

admin.site.register(Additional_Information)

admin.site.register(Images)
admin.site.register(Comment,CommentAdmin)



