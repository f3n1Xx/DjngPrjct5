
# Register your models here.
from Products import models
from django.contrib import admin

admin.site.register(models.Product)
admin.site.register(models.Variations)
admin.site.register(models.ProductImage)
admin.site.register(models.Category)
admin.site.register(models.ProductFeatured)
