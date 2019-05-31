from django.db import models
from django.utils.timezone import now
from ckeditor.fields import RichTextField

#TESSTTTT SLUGIFY
from django.template import defaultfilters


class Category(models.Model):
    name = models.CharField(max_length=100, verbose_name="Name")
    created = models.DateTimeField(auto_now_add=True, verbose_name="Date of created")
    updated = models.DateTimeField(auto_now=True, verbose_name="Date of edition")

    class Meta:
        verbose_name = "category"
        verbose_name_plural = "categories"
        ordering = ['-created']

    def __str__(self):
        return self.name


class Service(models.Model):

    title = models.CharField(max_length=200, verbose_name="Title")
    subtitle = models.CharField(max_length=200, verbose_name="Subtitle")
    published = models.DateTimeField(verbose_name="Published", default=now)
    finish = models.DateTimeField(verbose_name="Finish", default=now)
    wallet_shop = models.CharField(max_length=100, verbose_name="Address Shop")
    crw_donate = models.IntegerField(verbose_name="Crown needed")
    wallet_donate = models.CharField(null=True, blank=True, max_length=100, verbose_name="Address for donate ")
    amount_donate = models.CharField(null=True, blank=True, max_length=18, verbose_name="Amount donate")
    amount_needed = models.CharField(null=True, blank=True, max_length=18, verbose_name="Amount needed")
    content = RichTextField(verbose_name="Description")
    image = models.ImageField(verbose_name="Image", upload_to="services")
    categories = models.ManyToManyField(Category, verbose_name="Categories", related_name="get_projects")
    progress = models.CharField(null=True, blank=True, max_length=5, verbose_name="Progress")
    created = models.DateTimeField(auto_now_add=True, verbose_name="Date of created")
    updated = models.DateTimeField(auto_now=True, verbose_name="Date of edition")
    completed = models.BooleanField(default=False, verbose_name="Completed")

    class Meta:
        verbose_name = "project"
        verbose_name_plural = "projects"
        ordering = ['-created']

    def __str__(self):
        return self.title


    #TESSTTTT SLUGIFY
    def save(self, *args, **kwargs):
      self.slug = defaultfilters.slugify(self.title)
      super(Service, self).save(*args, **kwargs)

