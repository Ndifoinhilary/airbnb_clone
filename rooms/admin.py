from django.contrib import admin
from django.utils.html import mark_safe
# Register your models here.


from . import models


@admin.register(models.RoomType, models.Facility, models.Amenity, models.HouseRule)
class ItemTypeAdmin(admin.ModelAdmin):
    pass


class PhotoAdmin(admin.TabularInline):
    model = models.Photo

class RoomAdmin(admin.ModelAdmin):
    inlines = [
        PhotoAdmin,
    ]
    list_display = [ 'name','country','city','price','address','guests','beds', 'bedroom','check_in','check_out','instance_book','total_rating','count_photos']
    fieldsets = [
        (
           "Room Details",{
               'fields':['name','description','price','beds','bedroom','baths','guests']
           } 
        ),
        ('Time',{
                'fields':['check_in','check_out']
            }
         ),
        ('Address',{
            'fields':['country','city','address']
        }),
        (
            'Owner',{
                'fields':['host',]
            }
        ),
        (
            "Others",{
                'fields':['instance_book','roomtype','amenities','facilities','house_rule']
            }
        )
    ]
    raw_id_fields = ('host',)
    
    def count_photos(self,obj):
        return obj.photos.all().count()
    count_photos.short_description = 'number of photos'
    
    def count_aminities(self,obj):
        return obj.amenities.all()


admin.site.register(models.Room, RoomAdmin)


@admin.register(models.Photo)
class PhotoAdmin(admin.ModelAdmin):
    """photo defination"""
     
    list_display = ['__str__', 'get_thumbnail']
    
    
    def get_thumbnail(self,obj):
        return mark_safe(f'<img width ="50px" src="{obj.file.url}" />')
    
    get_thumbnail.short_description = "thumbnail"