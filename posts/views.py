import json
import requests
from django.http import JsonResponse
from django.shortcuts import render


# Create your views here.
from django.urls import reverse


def posts_index(request):
    return render(request, 'posts/index.html')

def posts(request):

    # Get start and end points
    start = int(request.GET.get("start") or 0)
    end = int(request.GET.get("end") or (start + 9))

    # Carregar lista com gifs
    data = []
    for i in range(start, end + 1):
        response = requests.get(
            'https://api.giphy.com/v1/gifs/random?api_key=X7Css4b2G5smBBqmGFiJtMKhKU2WuJH5&tag=children cartoons&rating=g')
        json_data = json.loads(response.text)
        data.append(f"{json_data.get('data').get('images').get('original').get('url')}")


    # Return list of posts
    return JsonResponse({
        "posts": data
    })
