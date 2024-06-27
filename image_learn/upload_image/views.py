from django.shortcuts import render

from .models import MyModel

def display(request):
    fm = MyModel.objects.all()
    return render(request, 'display.html', {'form': fm})
