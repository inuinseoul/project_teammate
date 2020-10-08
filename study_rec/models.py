from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

# Create your models here.

class Study_list(models.Model) :
    leader = models.ForeignKey(
        User, related_name="leader_s", on_delete=models.CASCADE, null=True
    ) # 팀장
    name = models.CharField(max_length=20) # 팀명 - 입력 받음
    intro = models.TextField() # 팀 소개 - 입력 받음
    state = models.IntegerField(default=0) # 팀상태
    created_date = models.DateTimeField(default=timezone.now)
    

class Study_member(models.Model) : 
    study_id = models.ForeignKey(
        Study_list, related_name="study_id", on_delete=models.CASCADE, null=True
    )
    member = models.ForeignKey(
    User, related_name="study_member", on_delete=models.CASCADE, null=True
    )