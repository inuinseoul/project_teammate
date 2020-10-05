# chat/views.py
from django.shortcuts import render
from django.utils.safestring import mark_safe
import json

#테스트
def index(request):
    context = {
        'team_list' : ['팀메이트','멋쟁이사자처럼','솔트룩스','에이림'],
        }

    return render(request, 'chat/index.html', context)

def room(request, room_name):
    user = request.user
    context = {
        'room_name_json': mark_safe(json.dumps(room_name)),
        'room_name':room_name,
    }

    return render(request, 'chat/room.html', context)