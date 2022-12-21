from django.shortcuts import render

from django.http import HttpResponse


class Horse:  # Note that parens are optional if not inheriting from another class
  def __init__(self, name, breed, description, age):
    self.name = name
    self.breed = breed
    self.description = description
    self.age = age

horses = [
  Horse('Vroom', 'Mustang', 'very fast but not great with kids', 4),
  Horse('Big Ben', 'Clydesdale', 'towers over everything but very loveable personality', 2),
  Horse('Aspen', 'American Quarter Horse', 'just born a few weeks ago', 0)
]


# Create your views here.
def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def horses_index(request):
    return render(request, 'horses/index.html', {'horses': horses})