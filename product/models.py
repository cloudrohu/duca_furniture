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
    class Meta:
        verbose_name_plural='5. Category'

    def __str__(self):
        return self.title
    

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
    class Meta:
        verbose_name_plural='3. Sub_Category'
    
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
        
    class Meta:
        verbose_name_plural='4. Brand'

    def __str__(self):
        return self.title
class Size(models.Model):
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

    sub_category = models.ForeignKey(Sub_Category, on_delete=models.CASCADE) #many to one relation with Brand
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE) #many to one relation with Brand

    size = models.ForeignKey(Size, blank=True, null=True , on_delete=models.CASCADE) #many to one relation with Brand
    special_features = models.ManyToManyField(Special_Features, blank=True,) #many to one relation with Brand
    title = models.CharField(max_length=150)
    keywords = models.CharField(max_length=1255)
    description = models.TextField(max_length=1255)
    image=models.ImageField(upload_to='images/',null=False)
    price=models.IntegerField(default=0)
    discount=models.IntegerField(default=3)
    detail=RichTextUploadingField()

    featured_project = models.BooleanField(default=False)
    Top_Deals_Of_The_Day = models.BooleanField(default=False)
    Top_Selling_Products = models.BooleanField(default=False)
    Recommended_For_You = models.BooleanField(default=False)

    slug = models.SlugField(null=True,blank=True, unique=True)
    status=models.CharField(max_length=10,choices=STATUS)
    create_at=models.DateTimeField(auto_now_add=True)
    update_at=models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.category.title +'--'+ self.title

    class Meta:
        verbose_name_plural='1. Product'


    ## method to create a fake table field in read only mode
    def image_tag(self):
        if self.image.url is not None:
            return mark_safe('<img src="{}" height="50" />'.format(self.image.url))
        else:
            return ""

    def get_absolute_url(self):
        from django.urls import reverse
        return reverse("product_details",kwargs={'slug':self.slug})

    class Meta:
        db_table = "product_Product"


    

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

def create_slug(instance, new_slug=None):
    slug = slugify(instance.title)
    if new_slug is not None:
        slug = new_slug
    qs = Product.objects.filter(slug=slug).order_by('-id')
    exists = qs.exists()
    if exists:
        new_slug = "%s-%s" % (slug, qs.first().id)
        return create_slug(instance, new_slug=new_slug)
    return slug

def pre_save_post_reciver(sender, instance, *args, **kwargs):
    if not instance.slug:
        instance.slug = create_slug(instance)
pre_save.connect(pre_save_post_reciver, Product)

class Additional_Information(models.Model):
    product=models.ForeignKey(Product,on_delete=models.CASCADE)

    Additional_Type = (
        ('Quality_Certification', 'Quality_Certification'),
        ('Embellishment_Feature', 'Embellishment_Feature'),
        ('Back_Style', 'Back_Style'),
        ('Depth', 'Depth'),
        ('Material', 'Material'),
        ('Width', 'Width'),
        ('Height', 'Height'),
        ('Arm_Style', 'Arm_Style'),
        ('Seat_Back_Interior_Height', 'Seat_Back_Interior_Height'),
        ('Assembly', 'Assembly'),
        ('Item_Shape', 'Item_Shape'),
        ('Seat_Depth', 'Seat_Depth'),
        ('Type', 'Type'),
        ('Room_Type', 'Room_Type'),
        ('Size', 'Size'),
        ('Others', 'Others'),
    )
    additional_type=models.CharField(max_length=100,choices=Additional_Type)

    title = models.CharField(max_length=50)    
    def __str__(self):
        return self.title


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
