from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from .functions import *
import json


def landing(request):
    return render(request, 'index.html')


def generate_key(request):
    if request.method == "POST":
        body = json.loads(request.body)
        seed_str = body.get('seed', '')
        seed_bytes = seed_str.encode('utf-8') if seed_str else None

        key = generate_fernet_key(seed_bytes)
        return JsonResponse({'generated_key': key.decode('utf-8')})
    else:
        return render(request, 'generate-key.html')


def hide_message(request):
    if request.method == "POST":
        # Check if request is JSON (from AJAX)
        if request.content_type == 'application/json':
            data = json.loads(request.body)
            key = data.get('key')
            secret_message = data.get('s_message')
            cover_message = data.get('c_message')
        else:
            key = request.POST['key']
            secret_message = request.POST['s_message']
            cover_message = request.POST['c_message']

        combined_message = hide(key, secret_message, cover_message)
        
        # Return JSON if AJAX
        if request.content_type == 'application/json':
            return JsonResponse({'combined_message': combined_message})
        
        # Otherwise fallback to normal page render
        return render(request, 'hide-message.html', context={'combined_message': combined_message})
    
    else:
        return render(request, 'hide-message.html')


# def extract_message(request):
#     if request.method == 'POST':
#         key = request.POST['key']
#         combined_message = request.POST['combined_message']
#         hidden_message = extract(key, combined_message)
#         return JsonResponse({'message': hidden_message})
#     else:
#         return render(request, 'extract-message.html')


def extract_message(request):
    if request.method == 'POST':
        if request.content_type == 'application/json':
            data = json.loads(request.body)
            key = data.get('key')
            combined_message = data.get('combined_message')
        else:
            key = request.POST['key']
            combined_message = request.POST['combined_message']

        hidden_message = extract(key, combined_message)

        if request.content_type == 'application/json':
            return JsonResponse({'message': hidden_message})

        return render(request, 'extract-message.html', context={'message': hidden_message})
    else:
        return render(request, 'extract-message.html')