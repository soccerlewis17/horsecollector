from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.http import HttpResponse
from .models import Horse
from .forms import FeedingForm

def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def horses_index(request):
    horses = Horse.objects.all()
    return render(request, 'horses/index.html', {'horses': horses})

def horses_detail(request, horse_id):
    horse = Horse.objects.get(id=horse_id)
    feeding_form = FeedingForm()
    return render(request, 'horses/detail.html', {'horse': horse, 'feeding_form': feeding_form})

def add_feeding(request, horse_id):
    form = FeedingForm(request.POST)
    if form.is_valid():
        new_feeding = form.save(commit=False)
        new_feeding.horse_id = horse_id
        new_feeding.save()
    return redirect('detail', horse_id=horse_id)


class HorseCreate(CreateView):
    model = Horse
    fields = '__all__'

class HorseUpdate(UpdateView):
    model = Horse
    fields = ['breed', 'age', 'description']

class HorseDelete(DeleteView):
    model = Horse
    success_url = '/horses/'
