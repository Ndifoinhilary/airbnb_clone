from django.shortcuts import render, redirect
from django.views import generic
from django.urls import reverse
from django_countries.fields import countries
from django.core.paginator import Paginator
from rooms import models as room_model
from .forms import SearchForm
# Create your views here.


class HomeView(generic.ListView):
    """Home view Definition"""

    model = room_model.Room
    paginate_by = 10
    paginate_orphans = 5

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context


# def DetailRoomView(request,pk):
#    try:
#     room = room_model.Room.objects.get(pk=pk)
#     context = {
#         'room':room
#     }
#     return render(request, 'rooms/detail.html',context)
#    except room_model.Room.DoesNotExist:
#     return redirect(reverse('core:home'))


class DetailRoomView(generic.DetailView):
    model = room_model.Room


class SearchView(generic.View):
    """rooms application SearchView Class
    Display list of rooms searched by city

    Inherit             : View
    Templates name      : rooms/search.html
    """

    def get(self, request):
        country = request.GET.get("country")

        if country:
            form = SearchForm(request.GET)

            if form.is_valid():
                city = form.cleaned_data.get("city")
                country = form.cleaned_data.get("country")
                room_type = form.cleaned_data.get("room_type")
                price = form.cleaned_data.get("price")
                guests = form.cleaned_data.get("guests")
                bedrooms = form.cleaned_data.get("bedrooms")
                beds = form.cleaned_data.get("beds")
                baths = form.cleaned_data.get("baths")
                instant_book = form.cleaned_data.get("instant_book")
                is_superhost = form.cleaned_data.get("is_superhost")
                amenities = form.cleaned_data.get("amenities")
                facilities = form.cleaned_data.get("facilities")

                filter_args = {}

                if city != "Anywhere":
                    filter_args["city__startswith"] = city

                filter_args["country"] = country

                if room_type is not None:
                    filter_args["room_type"] = room_type

                if price is not None:
                    filter_args["price__lte"] = price

                if guests is not None:
                    filter_args["guests__gte"] = guests

                if bedrooms is not None:
                    filter_args["bedrooms__gte"] = bedrooms

                if beds is not None:
                    filter_args["beds__gte"] = beds

                if baths is not None:
                    filter_args["baths__gte"] = baths

                if instant_book is True:
                    filter_args["instant_book"] = True

                if is_superhost is True:
                    filter_args["host__is_superhost"] = True

                for amenity in amenities:
                    filter_args["amenities"] = amenity

                for facility in facilities:
                    filter_args["facilities"] = facility

                qs = room_model.Room.objects.filter(**filter_args).order_by('-created')
                paginator = Paginator(qs,10,orphans=5)
                page = request.GET.get('page',1)
                rooms = paginator.get_page(page)                
                return render(
                    request, "rooms/search.html", {"form": form, "rooms": rooms}
                )

        else:
            form = SearchForm()

        return render(request, "rooms/search.html", {"form": form})
