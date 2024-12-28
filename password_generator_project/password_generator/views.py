from django.shortcuts import render
import random

def home(request):
    return render(request, 'home.html')

def generate_password(request):
    length = int(request.GET.get('length', 12))
    include_uppercase = request.GET.get('uppercase') == 'on'
    include_lowercase = request.GET.get('lowercase') == 'on'
    include_numbers = request.GET.get('numbers') == 'on'
    include_symbols = request.GET.get('symbols') == 'on'

    characters = ''

    if include_uppercase:
        characters += 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    if include_lowercase:
        characters += 'abcdefghijklmnopqrstuvwxyz'
    if include_numbers:
        characters += '0123456789'
    if include_symbols:
        characters += '!@#$%^&*()-_=+[]{}|;:,.<>?'

    if not characters:
        characters = 'abcdefghijklmnopqrstuvwxyz'

    password = ''.join(random.choice(characters) for _ in range(length))

    return render(request, 'password.html', {'password': password})
