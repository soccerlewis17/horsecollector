from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView
from django.http import HttpResponse
from .models import Horse, Toy
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
    toys_horse_doesnt_have = Toy.objects.exclude(id__in = horse.toys.all().values_list('id'))
    feeding_form = FeedingForm()
    return render(request, 'horses/detail.html', {'horse': horse, 'feeding_form': feeding_form, 'toys': toys_horse_doesnt_have})

def add_feeding(request, horse_id):
    form = FeedingForm(request.POST)
    if form.is_valid():
        new_feeding = form.save(commit=False)
        new_feeding.horse_id = horse_id
        new_feeding.save()
    return redirect('detail', horse_id=horse_id)

def assoc_toy(request, horse_id, toy_id):
  # Note that you can pass a toy's id instead of the whole object
  Horse.objects.get(id=horse_id).toys.add(toy_id)
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

class ToyList(ListView):
  model = Toy

class ToyDetail(DetailView):
  model = Toy

class ToyCreate(CreateView):
  model = Toy
  fields = '__all__'

class ToyUpdate(UpdateView):
  model = Toy
  fields = ['name', 'color']

class ToyDelete(DeleteView):
  model = Toy
  success_url = '/toys/'
