from django.shortcuts import render, get_object_or_404
from .models import Guide

def guide_list(request):
    guides = Guide.objects.all()
    return render(request, 'guide/guide_list.html', {'guides': guides})

def guide_detail(request, pk):
    guide = get_object_or_404(Guide, pk=pk)
    return render(request, 'guide/guide_detail.html', {'guide': guide})

# guide/views.py

from django.shortcuts import render, get_object_or_404, redirect
from .models import Guide
from .forms import GuideForm

def guide_list(request):
    guides = Guide.objects.all()
    return render(request, 'guide/guide_list.html', {'guides': guides})

def guide_detail(request, pk):
    guide = get_object_or_404(Guide, pk=pk)
    return render(request, 'guide/guide_detail.html', {'guide': guide})

def guide_create(request):
    if request.method == 'POST':
        form = GuideForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('guide_list')
    else:
        form = GuideForm()
    return render(request, 'guide/guide_form.html', {'form': form})

def guide_update(request, pk):
    guide = get_object_or_404(Guide, pk=pk)
    if request.method == 'POST':
        form = GuideForm(request.POST, request.FILES, instance=guide)
        if form.is_valid():
            form.save()
            return redirect('guide_detail', pk=guide.pk)
    else:
        form = GuideForm(instance=guide)
    return render(request, 'guide/guide_form.html', {'form': form})

def guide_delete(request, pk):
    guide = get_object_or_404(Guide, pk=pk)
    if request.method == 'POST':
        guide.delete()
        return redirect('guide_list')
    return render(request, 'guide/guide_confirm_delete.html', {'guide': guide})
