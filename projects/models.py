from django.db import models
from django.contrib.auth.models import User
from djrichtextfield.models import RichTextField
from cloudinary.models import CloudinaryField


CATEGORIES = (
    ('art', 'Art'),
    ('decorative', 'Decorative'),
    ('diy_gifts', 'DIY Gifts'),
    ('fashion', 'Fashion'),
    ('garden', 'Garden'),
    ('jewellery', 'Jewellery'),
    ('kids', 'Kids'),
    ('misc', 'Misc'),
    ('woodworking', 'Woodworking'),
)


# Create your models here.
class Project(models.Model):
    author = models.ForeignKey(User, related_name='project_author', on_delete=models.CASCADE)
    title = models.CharField (max_length=255, unique=True, blank=False, null=False)
    slug = models.SlugField (max_length=255, unique=True, null=False)
    description = models.CharField (max_length=600, blank=False, null=False)
    materials = RichTextField(max_length=10000, blank=False, null=False)
    steps = RichTextField(max_length=10000, blank=False, null=False)
    image = CloudinaryField ('image', default='placeholder')
    published_on = models.DateTimeField(auto_now_add=True)
    category = models.CharField( choices=CATEGORIES, max_length=75, default='art' )

    class Meta:
        ordering = ['-published_on']

    def __string__(self):
        return str(self.title)