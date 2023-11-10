from django.db import models
from django.core.mail import send_mail
from django.conf import settings
import uuid

# Create your models here.
from django.contrib.auth.models import AbstractUser



class User(AbstractUser):
    """Custom User model"""
    GENDER = (
        ('MALE', 'Male'),
        ('FAMALE', 'Female'),
        ('OTHER', 'Other')
    )
    CURRENCY = (
        ('USD', 'USD'),
        ('EUR', 'EUR'),
        ('GBP', 'GBP')
    )
    LANGUEGES = (
        ('en', 'English'),
        ('fr', 'French'),
        ('ru', 'Russian'),
        ('zh', 'Chinese'),
        ('KRW','Korean')
    )
    bio = models.TextField()
    avatar = models.ImageField(blank=True, null=True, upload_to='avatar')
    gender = models.CharField(max_length=10, choices=GENDER)
    date_of_birth = models.DateField(null = True , blank=True)
    languages = models.CharField(choices=LANGUEGES, max_length=4, default ='en')
    currency = models.CharField(choices=CURRENCY, max_length=4, default='USD')
    superhost = models.BooleanField(default=False)
    email_verify = models.BooleanField(default=False)
    email_secret =models.CharField(max_length = 120, default = "",blank =True )
    
    
    def verify_email(self):
        if self.email_verify is False:
            secret = uuid.uuid4().hex[:20]
            self.email_secret = secret
            send_mail("Verify your Airbnb account",
                f"Verify acount, this it your secret code {secret}", 
                settings.EMAIL_HOST_USER, 
                [self.email],
                fail_silently=True)
            