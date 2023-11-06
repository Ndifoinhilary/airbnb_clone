from django.db import models
from django.core.validators import MaxValueValidator,MinValueValidator

from core import models as core_model
# Create your models here.


class Review(core_model.TimeStampModel):
    """Review model """
    
    review = models.TextField()
    accuracy =models.IntegerField(validators=[MinValueValidator(1),MaxValueValidator(5)], default=1)
    communication = models.IntegerField(validators=[MinValueValidator(1),MaxValueValidator(5)], default=1)
    cleanliness = models.IntegerField(validators=[MinValueValidator(1),MaxValueValidator(5)], default=1)
    location = models.IntegerField(validators=[MinValueValidator(1),MaxValueValidator(5)], default=1)
    check_in = models.IntegerField(validators=[MinValueValidator(1),MaxValueValidator(5)], default=1)
    value = models.IntegerField(validators=[MinValueValidator(1),MaxValueValidator(5)], default=1)
    user = models.ForeignKey('users.User',related_name='review_user', on_delete=models.CASCADE)
    room = models.ForeignKey('rooms.Room',related_name='review_room', on_delete=models.CASCADE)
    
    
    def __str__(self):
        return f'{self.review}-----{self.room}'
    def rating_average(self):
        avg= (self.accuracy + self.communication + self.cleanliness + self.location + self.check_in + self.value)/6
        
        return round(avg, 2)