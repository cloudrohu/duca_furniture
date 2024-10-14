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




@admin_thumbnails.thumbnail('image')
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['title','image_tag','featured_category', 'create_at','update_at']

@admin_thumbnails.thumbnail('image')
class Sub_CategoryAdmin(admin.ModelAdmin):
    list_display = ['title','featured_category', 'image_tag','update_at','create_at']


class BrandAdmin(admin.ModelAdmin):
    list_display = ['title','image_tag','featured_brand','create_at','update_at',]


class ProductAdmin(admin.ModelAdmin):
    list_display = ['id','title','image_tag','featured_project', 'Top_Deals_Of_The_Day','Top_Selling_Products','Recommended_For_You', 'slug', 'create_at','update_at',]
    list_filter = ['category']
    list_editable = ['featured_project', 'Top_Deals_Of_The_Day','Top_Selling_Products','Recommended_For_You']
    inlines = [ProductImageInline,]

admin.site.register(Product,ProductAdmin)
admin.site.register(Category,CategoryAdmin)
admin.site.register(Sub_Category,Sub_CategoryAdmin)
admin.site.register(Brand,BrandAdmin)
admin.site.register(Size)
admin.site.register(Room_Type)
admin.site.register(Type)
admin.site.register(Seat_Depth)
admin.site.register(Item_Shape)
admin.site.register(Assembly)
admin.site.register(Seat_Back_Interior_Height)
admin.site.register(Arm_Style)
admin.site.register(Height)
admin.site.register(Width)
admin.site.register(Material)
admin.site.register(Depth)
admin.site.register(Back_Style)
admin.site.register(Embellishment_Feature)
admin.site.register(Quality_Certification)
admin.site.register(Images)
admin.site.register(Comment)



