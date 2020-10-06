from django.urls import path
from . import views

app_name = "alarm"
urlpatterns = [
    path("alarm_list/<int:customer_pk>", views.alarm_list, name="alarm_list"),
    path("del_alarm/<int:message_pk>", views.del_alarm, name="del_alarm"),
    path("check_info/<int:message_pk>", views.check_info, name="check_info"),
    path("join_team/<int:message_pk>", views.join_team, name="join_team")
]