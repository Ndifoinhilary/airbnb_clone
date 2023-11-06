from django.db import models
from core import models as core_model
# Create your models here.


class List(core_model.TimeStampModel):
    """List model"""
    name= models.CharField(max_length=50)
    
    user = models.ForeignKey('users.User', related_name='user_list', on_delete=models.CASCADE)
    rooms = models.ManyToManyField('rooms.Room',blank=True)
    
    
    def __str__(self):
        return self.name
    
    def count_rooms(self):
        return self.rooms.count()
    count_rooms.short_description = 'Number of rooms'