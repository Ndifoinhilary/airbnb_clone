from django.db import models
from django.utils import timezone
from core import models as core_model
# Create your models here.

class Reservation(core_model.TimeStampModel):
    """reservation model"""
    
    STATUS_CHOISE = (
        ('PENDING','Pending'),
        ('CONFIRM','Comfirm'),
        ('CANCELED', 'Cancelled')
    )
    
    status= models.CharField(max_length=10, choices=STATUS_CHOISE, default='PENDING')
    check_in = models.DateField(auto_now=False, auto_now_add=False)
    check_out = models.DateField(auto_now=False, auto_now_add=False)
    guest = models.ForeignKey('users.User',related_name='reservation', on_delete=models.CASCADE)
    room  = models.ForeignKey('rooms.Room',related_name='room_reservation' ,on_delete=models.CASCADE)
    
    
    def __str__(self):
        return f'{self.room}'
    
    def in_progress(self):
        now = timezone.now().date()
        return now >= self.check_in and now <= self.check_out
    in_progress.boolean = True
    
    def is_complete(self):
        now = timezone.now().date()
        return now > self.check_out
    is_complete.boolean = True
    
    
    def to_start(self):
        now = timezone.now().date()
        return now < self.check_in
    to_start.boolean = True
    
    