# chat/views.py
from django.shortcuts import render
from django.utils.safestring import mark_safe
import json

def index(request):
    context = {'team_list' : ['ai','good']}

    return render(request, 'chat/index.html', context)

def room(request, room_name):
    user = request.user
    context = {
        'room_name_json': mark_safe(json.dumps(room_name))

    }

    return render(request, 'chat/room.html', context)