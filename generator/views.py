from django.shortcuts import render
from django.http import HttpResponse
import random

#Redirección a Home
def home(request):
    return render(request, 'home.html')

#Redirección a Password
def password(request):

    generated_password = ''
    
    # Generamos minúsculas
    characters = list('abcdefghijklmnnñopqrstuvwxyz')
    # Generamos mayúsulas
    if request.GET.get('uppercase'):
        characters.extend(list('ABCDEFGHIJKLMNÑOPQRSTUVWXYZ'))
    # Generamos caracteres especiales
    if request.GET.get('special'):
        characters.extend(list('-_+!@#$%&*()'))
    # Generamos números
    if request.GET.get('numbers'):
        characters.extend(list('0123456789'))

    # Establecemos una longitud
    length = int(request.GET.get('length', 10))

    for x in range(length):
        generated_password += random.choice(characters)


    return render(request, 'password.html', {'password': generated_password})

#Redirección a About
def about(request):
    return render(request, 'about.html')