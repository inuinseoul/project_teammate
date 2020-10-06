# chat/views.py
from django.shortcuts import render
from django.utils.safestring import mark_safe
import json
from team_rec.models import Team_list, Team_member

#테스트
def index(request):
    team_list = Team_list.objects.all
    team_member = Team_member.objects.all


    context = {
        'team_list' : team_list,
        'team_member' : team_member
        }

    return render(request, 'chat/index.html', context)

def room(request, room_name):
    user = request.user
    context = {
        'room_name_json': mark_safe(json.dumps(room_name)),
        'room_name':room_name,
    }

    return render(request, 'chat/room.html', context)