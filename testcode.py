#  page = int(request.GET.get('page',1) or 1)
#     page_size = 10
#     limit = page * page_size
#     offset = limit - page_size
#     rooms = room_model.Room.objects.all()[offset:limit]
#     page_count = ceil(room_model.Room.objects.count()/page_size)

# def all_rooms(request):
#     page = request.GET.get('page',1)
#     room_list = room_model.Room.objects.all()
#     pagintor = Paginator(room_list,10)
#     try:
#         rooms = pagintor.page(page)
#         context = {
#         'page':rooms,
#         'room_list':room_list
#     }
#         return render(request, 'rooms/home.html', context)

#     except EmptyPage:
#         return redirect('/')



#   city = request.GET.get('city', 'Anywhere')
#     country = request.GET.get('country')
#     room_type = int(request.GET.get('room_type', 0))
#     price = int(request.GET.get('price', 0))
#     guests = int(request.GET.get('guests', 0))
#     beds = int(request.GET.get('beds', 0))
#     bedrooms = int(request.GET.get('bedrooms', 0))
#     baths = int(request.GET.get('baths', 0))
#     instant =  bool(request.GET.get('instant', False))
#     superhost =bool(request.GET.get('superhost', False))
#     s_facilities = request.GET.getlist('facilities')
#     s_amenities = request.GET.getlist('amenities')
#     room_types = room_model.RoomType.objects.all()
#     aminities = room_model.Amenity.objects.all()
#     facilities = room_model.Facility.objects.all()
#     city = str.capitalize(city)
#     form = {'city': city, 's_country': country, 's_room_type': room_type, 'price': price, 'instant': instant, 'super_host': super_host,
#             'guests': guests, 'beds': beds, 'bedrooms': bedrooms, 'baths': baths, 's_facilities': s_facilities, 's_amenities': s_amenities}
#     choice = {'countries': countries,
#               'room_types': room_types,
#               'aminities': aminities,
#               'facilities': facilities,

#               }
   

    # filter_args = {}

    # if city != 'Anywhere':
    #     filter_args['city__startswith'] = city
        
    # filter_args['country'] = country
    
    # if room_type != 0:
    #     filter_args['roomtype__id'] = room_type
        
    # if price != 0:
    #     filter_args['price__gte'] = price
    
    # if guests != 0:
    #     filter_args['guests__gte'] = guests
    
    # if beds != 0:
    #     filter_args['beds__gte'] = beds
    
    # if bedrooms != 0 :
    #     filter_args['bedrooms__gte'] = bedrooms
    
    # if baths != 0 :
    #     filter_args['baths__gte'] = baths
    
    # if instant is True:
    #     filter_args['instance_book'] = True
    
    # if superhost is True:
    #     filter_args['host__superhost'] = True
    
    # if len(s_amenities) > 0 :
    #     for s_amenity in s_amenities:
    #         filter_args['amenities__pk'] = s_amenity
    
    # if len(s_facilities) > 0 :
    #     for s_facility in s_facilities:
    #         filter_args['facilities__pk'] = s_facility  
    
    # rooms = room_model.Room.objects.filter(**filter_args)
    