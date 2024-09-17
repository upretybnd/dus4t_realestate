from django.db import models
from django.urls import reverse

from category.models import Category
from decimal import Decimal
from PIL import Image


class Post(models.Model):
    post_name = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True)
    description = models.TextField(max_length=100000, blank=True)

    # Location Fields
    district = models.CharField(max_length=50, default='Unknown')
    city = models.CharField(max_length=100, default='Unknown')
    place = models.CharField(max_length=200, default='Unknown')

    # Price Field
    price = models.DecimalField(max_digits=12, decimal_places=2, default=Decimal('0.00'))

    # Size of the property
    size = models.CharField(max_length=100, blank=True)  # Can be in square feet or meters

    # Additional Fields
    is_available = models.BooleanField(default=True)
    listing_type = models.CharField(max_length=50, choices=[('sale', 'For Sale'), ('rent', 'For Rent')], default='sale')

    # ForeignKey to Category
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    # Date and Time
    created_date = models.DateTimeField(auto_now_add=True)
    modified_date = models.DateTimeField(auto_now=True)

    def get_url(self):
        return reverse('post_detail', args=[self.category.slug, self.slug])


    def __str__(self):
        return self.post_name


class PostImage(models.Model):
    post = models.ForeignKey(Post, related_name='images', on_delete=models.CASCADE)
    image = models.ImageField(upload_to='photos/properties')

    def save(self, *args, **kwargs):
        # Save the instance first to get the image path
        super().save(*args, **kwargs)

        # Open the image
        img = Image.open(self.image.path)

        # Define the target size (800x600)
        target_size = (800, 600)

        # Resize the image if it's larger than the target size
        if img.size != target_size:
            img = img.resize(target_size, Image.Resampling.LANCZOS)  # Updated resampling method

            # Save the resized image
            img.save(self.image.path)


    def __str__(self):
        return f"{self.post.post_name} Image"
