from django.shortcuts import render, redirect
from users.models import Customer, Domain, Score, Role
from alarm.models import Message
from team_rec.models import Team_member,Team_list
from django.http import JsonResponse

# 알림 리스트 보기
def alarm_list(request, customer_pk):
    customer = Customer.objects.get(pk=customer_pk)
    message_list_team = Message.objects.filter(kind="team").filter(recipient=customer)
    message_list_study = Message.objects.filter(kind="study").filter(recipient=customer)

    context = {
        "message_list_team": message_list_team,
        "message_list_study": message_list_study,
    }

    return render(request, "alarm/alarm_list.html", context)


# 알림삭제(팀메이트)
def del_alarm(request, message_pk):
    message = Message.objects.get(pk=message_pk)
    customer = message.recipient
    message.delete()

    message_list_team = Message.objects.filter(kind="team").filter(recipient=customer)
    message_list_study = Message.objects.filter(kind="study").filter(recipient=customer)

    context = {
        "message_list_team": message_list_team,
        "message_list_study": message_list_study,
    }

    return render(request, "alarm/alarm_list.html", context)


# 팀원제의 받은사람이 팀원제의한 사람의 정보를 볼수있게
def check_info(request, message_pk):
    message = Message.objects.get(pk=message_pk)
    customer = Customer.objects.get(name=message.sender)
    domain = Domain.objects.get(foreignkey=customer)
    score = Score.objects.get(foreignkey=customer)
    role = Role.objects.get(foreignkey=customer)

    context = {
        "customer": customer,
        "domain": domain,
        "score": score,
        "role": role,
    }

    return render(request, "alarm/check_info.html", context)

def join_team(request, message_pk):
    message = Message.objects.get(pk=message_pk)    
    team = Team_list.objects.get(pk=message.invite_team.pk)

    customer = message.recipient
    message.delete()

    message_list_team = Message.objects.filter(kind="team").filter(recipient=customer)
    message_list_study = Message.objects.filter(kind="study").filter(recipient=customer)

    context = {
        "message_list_team": message_list_team,
        "message_list_study": message_list_study,
        "error_state" : False
    }

    if not (Team_member.objects.filter(team_id=team).filter(member=request.user)):
        Team_member.objects.create(
            team_id=team,
            member=request.user
        )
        context["error_state"] = True
        context["error_message"] = team.name + "팀에 가입되었습니다."
    else:
        context["error_state"] = True
        context["error_message"] = "이미 해당 팀에 가입하셨거나 해당 팀이 존재하지 않습니다."

    return render(request, "alarm/alarm_list.html", context)