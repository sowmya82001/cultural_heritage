from django.shortcuts import render, get_object_or_404
from .models import Place

def place_list(request):
    places = Place.objects.all()
    return render(request, 'places/place_list.html', {'places': places})

def place_detail(request, pk):
    place = get_object_or_404(Place, pk=pk)
    return render(request, 'places/place_detail.html', {'place': place})

# places/views.py

from django.shortcuts import render, get_object_or_404, redirect
from .models import Place
from .forms import PlaceForm

def place_list(request):
    places = Place.objects.all()
    return render(request, 'places/place_list.html', {'places': places})

def place_detail(request, pk):
    place = get_object_or_404(Place, pk=pk)
    return render(request, 'places/place_detail.html', {'place': place})

def place_create(request):
    if request.method == 'POST':
        form = PlaceForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('place_list')
    else:
        form = PlaceForm()
    return render(request, 'places/place_form.html', {'form': form})

def place_update(request, pk):
    place = get_object_or_404(Place, pk=pk)
    if request.method == 'POST':
        form = PlaceForm(request.POST, request.FILES, instance=place)
        if form.is_valid():
            form.save()
            return redirect('place_detail', pk=place.pk)
    else:
        form = PlaceForm(instance=place)
    return render(request, 'places/place_form.html', {'form': form})

def place_delete(request, pk):
    place = get_object_or_404(Place, pk=pk)
    if request.method == 'POST':
        place.delete()
        return redirect('place_list')
    return render(request, 'places/place_confirm_delete.html', {'place': place})
