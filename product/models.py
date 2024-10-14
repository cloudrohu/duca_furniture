from ckeditor_uploader.fields import RichTextUploadingField
from django.contrib.auth.models import User
from django.db import models
from django.utils.html import mark_safe
# Create your models here.
from django.db.models import Avg, Count
from django.forms import ModelForm
from django.urls import reverse
from django.utils.safestring import mark_safe
from django.db.models.signals import pre_save

from django.utils.text import slugify
# Create your models here.

class Category(models.Model):
    title = models.CharField(max_length=50)
    image=models.ImageField(upload_to='images/')
    featured_category = models.BooleanField(default=False)
    create_at=models.DateTimeField(auto_now_add=True)
    update_at=models.DateTimeField(auto_now=True)

    def image_tag(self):
        if self.image.url is not None:
            return mark_safe('<img src="{}" height="50"/>'.format(self.image.url))
        else:
            return ""

    def __str__(self):
        return self.title + '--' + self.main_category.title
class Sub_Category(models.Model):
    title = models.CharField(max_length=50)
    category = models.ForeignKey(Category,on_delete=models.CASCADE)
    image=models.ImageField(upload_to='images/')
    featured_category = models.BooleanField(default=False)
    create_at=models.DateTimeField(auto_now_add=True)
    update_at=models.DateTimeField(auto_now=True)

    def image_tag(self):
        if self.image.url is not None:
            return mark_safe('<img src="{}" height="50"/>'.format(self.image.url))
        else:
            return ""

    def __str__(self):
        return self.title + '--' + self.category.title
class Brand(models.Model):
    title = models.CharField(max_length=50)
    image=models.ImageField(upload_to='images/')
    featured_brand = models.BooleanField(default=False)
    create_at=models.DateTimeField(auto_now_add=True)
    update_at=models.DateTimeField(auto_now=True)

    def image_tag(self):
        if self.image.url is not None:
            return mark_safe('<img src="{}" height="50"/>'.format(self.image.url))
        else:
            return ""

    def __str__(self):
        return self.title
class Size(models.Model):
    title = models.CharField(max_length=50)
    create_at=models.DateTimeField(auto_now_add=True)
    update_at=models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.title
class Room_Type(models.Model):
    title = models.CharField(max_length=50)
    create_at=models.DateTimeField(auto_now_add=True)
    update_at=models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.title
class Type(models.Model):
    title = models.CharField(max_length=50)
    create_at=models.DateTimeField(auto_now_add=True)
    update_at=models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.title
class Seat_Depth(models.Model):
    title = models.CharField(max_length=50)
    create_at=models.DateTimeField(auto_now_add=True)
    update_at=models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.title
class Item_Shape(models.Model):
    title = models.CharField(max_length=50)
    create_at=models.DateTimeField(auto_now_add=True)
    update_at=models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.title
class Assembly(models.Model):
    title = models.CharField(max_length=50)
    create_at=models.DateTimeField(auto_now_add=True)
    update_at=models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.title
class Seat_Back_Interior_Height(models.Model):
    title = models.CharField(max_length=50)
    create_at=models.DateTimeField(auto_now_add=True)
    update_at=models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.title
class Arm_Style(models.Model):
    title = models.CharField(max_length=50)
    create_at=models.DateTimeField(auto_now_add=True)
    update_at=models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.title
class Height(models.Model):
    title = models.CharField(max_length=50)
    create_at=models.DateTimeField(auto_now_add=True)
    update_at=models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.title
class Width(models.Model):
    title = models.CharField(max_length=50)
    create_at=models.DateTimeField(auto_now_add=True)
    update_at=models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.title
class Material(models.Model):
    title = models.CharField(max_length=50)
    create_at=models.DateTimeField(auto_now_add=True)
    update_at=models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.title
class Depth(models.Model):
    title = models.CharField(max_length=50)
    create_at=models.DateTimeField(auto_now_add=True)
    update_at=models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.title

class Embellishment_Feature(models.Model):
    title = models.CharField(max_length=50)
    create_at=models.DateTimeField(auto_now_add=True)
    update_at=models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.title
class Quality_Certification(models.Model):
    title = models.CharField(max_length=50)
    create_at=models.DateTimeField(auto_now_add=True)
    update_at=models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.title
class Upholstery_Color(models.Model):
    title = models.CharField(max_length=50)
    create_at=models.DateTimeField(auto_now_add=True)
    update_at=models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.title
class Fill_Material(models.Model):
    title = models.CharField(max_length=50)
    create_at=models.DateTimeField(auto_now_add=True)
    update_at=models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.title
class Back_Style(models.Model):
    title = models.CharField(max_length=50)
    create_at=models.DateTimeField(auto_now_add=True)
    update_at=models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.title
class Color(models.Model):
    name = models.CharField(max_length=20)
    code = models.CharField(max_length=10, blank=True,null=True)
    def __str__(self):
        return self.name
    def color_tag(self):
        if self.code is not None:
            return mark_safe('<p style="background-color:{}">Color </p>'.format(self.code))
        else:
            return ""
class Item_Width_Side_to_Side(models.Model):
    title = models.CharField(max_length=50)
    create_at=models.DateTimeField(auto_now_add=True)
    update_at=models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.title
class Item_Depth_Front_to_Back(models.Model):
    title = models.CharField(max_length=50)
    create_at=models.DateTimeField(auto_now_add=True)
    update_at=models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.title
class Height_Base_to_Top(models.Model):
    title = models.CharField(max_length=50)
    create_at=models.DateTimeField(auto_now_add=True)
    update_at=models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.title
class Included_Components(models.Model):
    title = models.CharField(max_length=50)
    create_at=models.DateTimeField(auto_now_add=True)
    update_at=models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.title
class Pattern(models.Model):
    title = models.CharField(max_length=50)
    create_at=models.DateTimeField(auto_now_add=True)
    update_at=models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.title
class Special_Features(models.Model):
    title = models.CharField(max_length=50)
    create_at=models.DateTimeField(auto_now_add=True)
    update_at=models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.title

class Product(models.Model):    
    STATUS = (
        ('True', 'True'),
        ('False', 'False'),
    )

    category = models.ForeignKey(Sub_Category, on_delete=models.CASCADE) #many to one relation with Brand
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE) #many to one relation with Brand

    size = models.ForeignKey(Size, blank=True, null=True , on_delete=models.CASCADE) #many to one relation with Brand
    room_type = models.ManyToManyField(Room_Type, blank=True,) #many to one relation with Brand
    type = models.ForeignKey(Type, blank=True, null=True , on_delete=models.CASCADE) #many to one relation with Brand
    seat_depth = models.ForeignKey(Seat_Depth, blank=True, null=True , on_delete=models.CASCADE) #many to one relation with Brand
    item_shape = models.ForeignKey(Item_Shape, blank=True, null=True , on_delete=models.CASCADE) #many to one relation with Brand
    assembly = models.ForeignKey(Assembly, blank=True, null=True , on_delete=models.CASCADE) #many to one relation with Brand
    seat_back_interior_height = models.ForeignKey(Seat_Back_Interior_Height, blank=True, null=True , on_delete=models.CASCADE) #many to one relation with Brand
    arm_style = models.ForeignKey(Arm_Style, blank=True, null=True , on_delete=models.CASCADE) #many to one relation with Brand
    height = models.ForeignKey(Height, blank=True, null=True , on_delete=models.CASCADE) #many to one relation with Brand
    width = models.ForeignKey(Width, blank=True, null=True , on_delete=models.CASCADE) #many to one relation with Brand
    material = models.ForeignKey(Material, blank=True, null=True , on_delete=models.CASCADE) #many to one relation with Brand
    depth = models.ForeignKey(Depth, blank=True, null=True , on_delete=models.CASCADE) #many to one relation with Brand
    embellishment_feature = models.ForeignKey(Embellishment_Feature, blank=True, null=True , on_delete=models.CASCADE) #many to one relation with Brand
    quality_certification = models.ForeignKey(Quality_Certification, blank=True, null=True , on_delete=models.CASCADE) #many to one relation with Brand
    upholstery_color = models.ForeignKey(Upholstery_Color, blank=True, null=True , on_delete=models.CASCADE) #many to one relation with Brand
    fill_material = models.ForeignKey(Fill_Material, blank=True, null=True , on_delete=models.CASCADE) #many to one relation with Brand
    back_style = models.ForeignKey(Back_Style, blank=True, null=True , on_delete=models.CASCADE) #many to one relation with Brand
    color = models.ManyToManyField(Color, blank=True,) #many to one relation with Brand
    item_width_side_to_side = models.ForeignKey(Item_Width_Side_to_Side, blank=True, null=True , on_delete=models.CASCADE) #many to one relation with Brand
    item_depth_front_to_back = models.ForeignKey(Item_Depth_Front_to_Back, blank=True, null=True , on_delete=models.CASCADE) #many to one relation with Brand
    height_base_to_top = models.ForeignKey(Height_Base_to_Top, blank=True, null=True , on_delete=models.CASCADE) #many to one relation with Brand
    included_components = models.ManyToManyField(Included_Components, blank=True,) #many to one relation with Brand
    pattern = models.ForeignKey(Pattern, blank=True, null=True , on_delete=models.CASCADE) #many to one relation with Brand
    special_features = models.ManyToManyField(Special_Features, blank=True,) #many to one relation with Brand


    title = models.CharField(max_length=150)
    keywords = models.CharField(max_length=1255)
    description = models.TextField(max_length=1255)
    image=models.ImageField(upload_to='images/',null=False)
    price=models.IntegerField(default=0)
    discount=models.IntegerField(default=3)
    detail=RichTextUploadingField()
    slug = models.SlugField(null=True,blank=True, unique=True)
    status=models.CharField(max_length=10,choices=STATUS)
    featured_project = models.BooleanField(default=False)
    Top_Deals_Of_The_Day = models.BooleanField(default=False)
    Top_Selling_Products = models.BooleanField(default=False)
    Recommended_For_You = models.BooleanField(default=False)
    create_at=models.DateTimeField(auto_now_add=True)
    update_at=models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural='1. Product'


    ## method to create a fake table field in read only mode
    def image_tag(self):
        if self.image.url is not None:
            return mark_safe('<img src="{}" height="50"/>'.format(self.image.url))
        else:
            return ""

    def save(self , *args , **kwargs):
        self.slug = slugify(self.title)
        super(Product ,self).save(*args , **kwargs)


    def get_absolute_url(self):
        return reverse('PRODUCT_DETAILS', kwargs={'slug': self.slug})

    def avaregereview(self):
        reviews = Comment.objects.filter(product=self, status='True').aggregate(avarage=Avg('rate'))
        avg=0
        if reviews["avarage"] is not None:
            avg=float(reviews["avarage"])
        return avg

    def countreview(self):
        reviews = Comment.objects.filter(product=self, status='True').aggregate(count=Count('id'))
        cnt=0
        if reviews["count"] is not None:
            cnt = int(reviews["count"])
        return cnt

class Images(models.Model):
    product=models.ForeignKey(Product,on_delete=models.CASCADE)
    title = models.CharField(max_length=50,blank=True)
    image = models.ImageField(blank=True, upload_to='images/')

    def __str__(self):
        return self.title

class Comment(models.Model):
    STATUS = (
        ('New', 'New'),
        ('True', 'True'),
        ('False', 'False'),
    )
    product=models.ForeignKey(Product,on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    subject = models.CharField(max_length=50, blank=True)
    comment = models.CharField(max_length=250,blank=True)
    rate = models.IntegerField(default=1)
    ip = models.CharField(max_length=20, blank=True)
    status=models.CharField(max_length=10,choices=STATUS, default='New')
    create_at=models.DateTimeField(auto_now_add=True)
    update_at=models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.subject
    
    class Meta:
        verbose_name_plural='2. Comment'

class CommentForm(ModelForm):
    class Meta:
        model = Comment
        fields = ['subject', 'comment', 'rate']
