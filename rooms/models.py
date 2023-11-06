from django.db import models
from django.core.validators import MaxValueValidator,MinValueValidator
# `from django_countries.fields import CountryField` is importing the `CountryField` class from the
# `django_countries.fields` module. This field is used to store and validate country data in Django
# models.
from django_countries.fields import CountryField
from django.urls import reverse
from core import models as core_model
from users import models as user_model
# Create your models here.


class AbstractItem(core_model.TimeStampModel):
    """Abstract item"""

    name = models.CharField(max_length=150)

    class Meta:
        abstract = True

    def __str__(self):
        return self.name


class RoomType(AbstractItem):
    """"Room type"""
    class Meta:
        verbose_name = 'RoomType'


class Facility(AbstractItem):
    """Facility"""

    class Meta:
        verbose_name_plural = 'Facilities'


class HouseRule(AbstractItem):
    """House rule"""
    class Meta:
        verbose_name = 'House Rule'


class Amenity(AbstractItem):

    class Meta:
        verbose_name_plural = 'Amenities'


class Photo(core_model.TimeStampModel):
    """Photo model"""
    
    caption = models.CharField(max_length=100)
    file = models.ImageField(upload_to='photos')
    room= models.ForeignKey('Room',related_name= 'photos', on_delete=models.CASCADE)
    def __str__(self):
        return self.caption



class Room(core_model.TimeStampModel):
    """Room model """

    name = models.CharField(max_length=140)
    description = models.TextField()
    country = CountryField()
    city = models.CharField(max_length=255)
    price = models.PositiveIntegerField()
    address = models.CharField(max_length=255)
    guests = models.IntegerField(validators=[MinValueValidator(1),MaxValueValidator(5)], default=1)
    beds = models.IntegerField(validators=[MinValueValidator(1),MaxValueValidator(5)], default=1)
    bedroom = models.IntegerField(validators=[MinValueValidator(1),MaxValueValidator(5)], default=1)
    baths = models.IntegerField(validators=[MinValueValidator(1),MaxValueValidator(5)], default=1)
    check_in = models.TimeField()
    check_out = models.TimeField()
    instance_book = models.BooleanField(default=False)
    host = models.ForeignKey(user_model.User,related_name='rooms', on_delete=models.CASCADE)
    roomtype = models.ForeignKey(
        RoomType,related_name='room_type', on_delete=models.SET_NULL, null=True)
    amenities = models.ManyToManyField(Amenity, blank=True)
    facilities = models.ManyToManyField(Facility, blank=True)
    house_rule = models.ManyToManyField(HouseRule, blank=True)
    
    
    
    def save(self, *args, **kwargs):
       self.city = str.capitalize(self.city)
       super(Room, self).save(*args, **kwargs) # Call the real save() method 
    
    def get_absolute_url(self):
        return reverse("rooms:detail", kwargs={"pk": self.pk})
    

    def __str__(self):
        return self.name
    def total_rating(self):
        all_review = self.review_room.all()
        all_rating = 0
        try:
            for review in all_review:
                all_rating +=review.rating_average()
            return round(all_rating/len(all_review), 2)
        except Exception as e:
            return 0