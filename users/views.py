from django.shortcuts import render, redirect
from .models import Customer, Domain, Score, Role, Study
from django.contrib.auth.models import User
from django.contrib import auth

ERROR_MSG = {
    "ID_EXIST": "이미 사용 중인 아이디 입니다.",
    "ID_NOT_EXIST": "존재하지 않는 아이디 입니다.",
    "ID_PW_MISSING": "아이디와 비밀번호를 다시 한번 확인해주세요.",
    "PW_CHECK": "비밀번호가 일치하지 않습니다.",
}


ERROR_MSG2 = {
    "error": "10개의 하트를 제대로 베팅하지않으셨습니다. 값을 다시확인해주세요!!",
    "error2": "null값이 존재합니다. 입력값을 다시 한번 확인해주세요!!!",
}

# 회원가입
def signup(request):
    context = {"error": {"state": False, "msg": ""}}

    if request.method == "POST":

        user_id = request.POST["user_id"]
        user_pw = request.POST["user_pw"]
        user_pw_check = request.POST["user_pw_check"]
        name = request.POST["name"]
        email = request.POST["email"]
        phone_num = request.POST["phone_num"]
        intro = request.POST["intro"]

        if user_id and user_pw:
            user = User.objects.filter(username=user_id)
            if len(user) == 0:
                if user_pw == user_pw_check:

                    created_user = User.objects.create_user(
                        username=user_id, password=user_pw
                    )

                    customer = Customer.objects.create(
                        user=created_user,
                        name=name,
                        email=email,
                        phone_num=phone_num,
                        intro=intro,
                    )

                    Domain.objects.create(
                        foreignkey=customer,
                    )

                    Score.objects.create(
                        foreignkey=customer,
                    )

                    Role.objects.create(
                        foreignkey=customer,
                    )

                    Study.objects.create(
                        foreignkey=customer,
                    )

                    auth.login(request, created_user)

                    return render(request, "users/signup2.html")
                else:
                    context["error"]["state"] = True
                    context["error"]["msg"] = ERROR_MSG["PW_CHECK"]
            else:
                context["error"]["state"] = True
                context["error"]["msg"] = ERROR_MSG["ID_EXIST"]
        else:
            context["error"]["state"] = True
            context["error"]["msg"] = ERROR_MSG["ID_PW_MISSING"]

    return render(request, "users/signup.html", context)


# 회원가입2 - 흥미(건강~기술)
def signup2(request, customer_pk):
    context = {"error": {"state": False, "msg": ""}}
    if request.method == "POST":
        health = request.POST["health"]
        economy = request.POST["economy"]
        culture_art = request.POST["culture_art"]
        education = request.POST["education"]
        society = request.POST["society"]
        technology = request.POST["technology"]

        if (
            len(health)
            and len(economy)
            and len(culture_art)
            and len(education)
            and len(society)
            and len(technology)
        ):
            if (
                int(health)
                + int(economy)
                + int(culture_art)
                + int(education)
                + int(society)
                + int(technology)
                == 10
            ):

                customer = Customer.objects.get(pk=customer_pk)

                Domain.objects.filter(foreignkey=customer).update(
                    health=health,
                    economy=economy,
                    culture_art=culture_art,
                    education=education,
                    society=society,
                    technology=technology,
                    domain_sum=10,
                )

                return render(request, "users/signup3.html")
            else:
                context["error"]["state"] = True
                context["error"]["msg"] = ERROR_MSG2["error"]
        else:
            context["error"]["state"] = True
            context["error"]["msg"] = ERROR_MSG2["error2"]

    return render(request, "users/signup2.html", context)


# 회원가입3 - 실력테스트(각분야에대한 점수)
def signup3(request, customer_pk):
    context = {"error": {"state": False, "msg": ""}}
    if request.method == "POST":
        web = request.POST["web"]
        design = request.POST["design"]
        machine_learning = request.POST["machine_learning"]
        statistics = request.POST["statistics"]
        deep_learning = request.POST["deep_learning"]
        algorithm = request.POST["algorithm"]
        nlp = request.POST["nlp"]

        if (
            len(web)
            and len(design)
            and len(machine_learning)
            and len(statistics)
            and len(deep_learning)
            and len(algorithm)
            and len(nlp)
        ):
            web = round(float(web))
            design = round(float(design))
            machine_learning = round(float(machine_learning))
            statistics = round(float(statistics))
            deep_learning = round(float(deep_learning))
            algorithm = round(float(algorithm))
            nlp = round(float(nlp))
            data_score = round(int(web) * 0.5 + int(design) * 0.5)
            modeling_score = round(
                int(machine_learning) * 0.25
                + int(deep_learning) * 0.25
                + int(algorithm) * 0.25
                + int(nlp) * 0.25
            )

            customer = Customer.objects.get(pk=customer_pk)

            Score.objects.filter(foreignkey=customer).update(
                web=web,
                design=design,
                machine_learning=machine_learning,
                statistics=statistics,
                deep_learning=deep_learning,
                algorithm=algorithm,
                nlp=nlp,
                data_score=data_score,
                modeling_score=modeling_score,
                score_sum=int(web)
                + int(design)
                + int(machine_learning)
                + int(statistics)
                + int(deep_learning)
                + int(algorithm)
                + int(nlp)
                + int(data_score)
                + int(modeling_score),
            )

            return render(request, "users/signup4.html")
        else:
            context["error"]["state"] = True
            context["error"]["msg"] = ERROR_MSG2["error2"]

    return render(request, "users/signup3.html", context)


# 회원가입4 - 선호역할
def signup4(request, customer_pk):
    context = {"error": {"state": False, "msg": ""}}
    if request.method == "POST":
        analysis_hearts = request.POST["analysis_hearts"]
        web_hearts = request.POST["web_hearts"]
        design_hearts = request.POST["design_hearts"]
        modeling_hearts = request.POST["modeling_hearts"]

        if (
            len(analysis_hearts)
            and len(web_hearts)
            and len(design_hearts)
            and len(modeling_hearts)
        ):
            if (
                int(analysis_hearts)
                + int(web_hearts)
                + int(design_hearts)
                + int(modeling_hearts)
                == 10
            ):

                customer = Customer.objects.get(pk=customer_pk)

                Role.objects.filter(foreignkey=customer).update(
                    analysis_hearts=analysis_hearts,
                    web_hearts=web_hearts,
                    design_hearts=design_hearts,
                    modeling_hearts=modeling_hearts,
                    role_sum=10,
                )

                return render(request, "users/signup5.html")
            else:
                context["error"]["state"] = True
                context["error"]["msg"] = ERROR_MSG2["error"]
        else:
            context["error"]["state"] = True
            context["error"]["msg"] = ERROR_MSG2["error2"]

    return render(request, "users/signup4.html", context)


# 관심있는 스터디
def signup5(request, customer_pk):
    context = {"error": {"state": False, "msg": ""}}
    if request.method == "POST":
        customer = Customer.objects.get(pk=customer_pk)

        foreignkey = customer
        web_hearts = request.POST["web_hearts"]
        design_hearts = request.POST["design_hearts"]
        machine_learning_hearts = request.POST["machine_learning_hearts"]
        statistics_hearts = request.POST["statistics_hearts"]
        deep_learning_hearts = request.POST["deep_learning_hearts"]
        algorithm_hearts = request.POST["algorithm_hearts"]
        nlp_hearts = request.POST["nlp_hearts"]
        basic_python_hearts = request.POST["basic_python_hearts"]
        data_analysis_hearts = request.POST["data_analysis_hearts"]
        voice_recog_hearts = request.POST["voice_recog_hearts"]
        computer_vision_hearts = request.POST["computer_vision_hearts"]
        rec_system_hearts = request.POST["rec_system_hearts"]
        reinforcement_hearts = request.POST["reinforcement_hearts"]

        if (
            len(web_hearts)
            and len(design_hearts)
            and len(machine_learning_hearts)
            and len(statistics_hearts)
            and len(deep_learning_hearts)
            and len(algorithm_hearts)
            and len(nlp_hearts)
            and len(basic_python_hearts)
            and len(data_analysis_hearts)
            and len(voice_recog_hearts)
            and len(computer_vision_hearts)
            and len(rec_system_hearts)
            and len(reinforcement_hearts)
        ):
            if (
                int(web_hearts)
                + int(design_hearts)
                + int(machine_learning_hearts)
                + int(statistics_hearts)
                + int(deep_learning_hearts)
                + int(algorithm_hearts)
                + int(nlp_hearts)
                + int(basic_python_hearts)
                + int(data_analysis_hearts)
                + int(voice_recog_hearts)
                + int(computer_vision_hearts)
                + int(rec_system_hearts)
                + int(reinforcement_hearts)
                == 10
            ):
                Study.objects.filter(foreignkey=customer).update(
                    web_hearts=web_hearts,
                    design_hearts=design_hearts,
                    machine_learning_hearts=machine_learning_hearts,
                    statistics_hearts=statistics_hearts,
                    deep_learning_hearts=deep_learning_hearts,
                    algorithm_hearts=algorithm_hearts,
                    nlp_hearts=nlp_hearts,
                    basic_python_hearts=basic_python_hearts,
                    data_analysis_hearts=data_analysis_hearts,
                    voice_recog_hearts=voice_recog_hearts,
                    computer_vision_hearts=computer_vision_hearts,
                    rec_system_hearts=rec_system_hearts,
                    reinforcement_hearts=reinforcement_hearts,
                    study_sum=10,
                )

                return redirect("home")
            else:
                context["error"]["state"] = True
                context["error"]["msg"] = ERROR_MSG2["error"]
        else:
            context["error"]["state"] = True
            context["error"]["msg"] = ERROR_MSG2["error2"]

    return render(request, "users/signup5.html", context)


# 로그인
def login(request):
    context = {"error": {"state": False, "msg": ""}}
    if request.method == "POST":

        user_id = request.POST["user_id"]
        user_pw = request.POST["user_pw"]

        if user_id and user_pw:
            user = User.objects.filter(username=user_id)

            if len(user) != 0:

                user = auth.authenticate(username=user_id, password=user_pw)

                if user != None:

                    auth.login(request, user)

                    return redirect("home")
                else:
                    context["error"]["state"] = True
                    context["error"]["msg"] = ERROR_MSG["PW_CHECK"]
            else:
                context["error"]["state"] = True
                context["error"]["msg"] = ERROR_MSG["ID_NOT_EXIST"]
        else:
            context["error"]["state"] = True
            context["error"]["msg"] = ERROR_MSG["ID_PW_MISSING"]

    return render(request, "users/login.html", context)


# 로그아웃
def logout(request):
    auth.logout(request)

    return redirect("home")
