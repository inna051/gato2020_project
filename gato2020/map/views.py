from django.shortcuts import render, redirect
from .models import City
from .forms import CityForm
import folium


def map_view(request):
    cities = City.objects.all()
    map = folium.Map(location=[42, 25], zoom_start=6)

    for city in cities:
        folium.Marker([city.latitude, city.longitude], popup=city.name, icon=folium.Icon(color='red')).add_to(map)

    map = map._repr_html_()
    return render(request, 'map/map.html', {'map': map})


def add_city_view(request):
    if request.method == 'POST':
        form = CityForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('map:map')
    else:
        form = CityForm()
    return render(request, 'map/add_city.html', {'form': form})