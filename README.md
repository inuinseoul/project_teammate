# project_teammate
자신의 부족한 점을 보완해주는 최고의 팀메이트를 추천해주는 서비스

# 1. 목표
-	추천시스템을 통해 참여자에게 자신과 팀메이트의 후보를 뽑아준다.
-	참여자는 단점을 보완하고 장점을 살려줄 팀메이트를 구할 수 있다.
-	주최자는 합리적인 팀매칭으로 교육 혹은 공모전에서 더 나은 아웃풋을 도모할 수 있다.

<br>

# 2. 사용기술
-	코사인유사도 기반 추천시스템<br>
-	django를 활용한 페이지 구성<br>
- django를 활용한 회원가입 및 로그인 구성<br>
- sqlite 기반 각종 모델 구성

<br>

# 3. 실행방법

```
pipenv shell
pipenv install django
python manage.py runserver
```

<br>

# 4. 실행결과화면

![image](https://user-images.githubusercontent.com/70463738/104844280-ba9bfb00-5912-11eb-8828-92f95b444ebc.png)

- 회원가입 시 각종정보를 입력받는다.
- 입력된 회원들의 정보를 기반으로 회원들에게 가장 잘 맞는 팀원, 스터디메이트를 추천해준다.
- 관심정보를 기반으로 뉴스레터도 보여준다.

