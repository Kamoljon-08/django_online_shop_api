from django.db import models

# Create your models here.

class CustomUser (models.Model):
    block = models.BooleanField(name='block', default=False)
    created_at = models.DateTimeField(name="created_at", auto_now_add=True)
    phone = models.CharField(name='phone', max_length=30, blank=False, unique=True)
    email = models.CharField(name='email', max_length=30, blank=False, unique=True)
    image = models.ImageField(name='image', upload_to='user/', default='images/user.png')
    
    def __str__ (self) -> str:
        return str(self.phone)