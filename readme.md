# Django Practices

## 장고프로젝트(django_practices) 만들기

### 1. pycham에서 프로젝트 생성

### 2. django library 설치 (Terminal 에서)

```shell
(env) # pip install django
``` 

### 3. mysqlclient library 설치
```shell
(env) # pip install mysqlclient
```

### 4. 장고 프로젝트 생성
```shell
(env) # django-admin startproject django_practices
```

### 5. 디렉토리 정리(pycharm 프로젝트랑 장고 프로젝트를 일치시켜주기)

### 6. 초기설정(settings.py)
1) time zone 설정
```python
Time_Zone = 'Asia/Seoul'
```
2) database 설정
```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'webdb',
        'USER': 'webdb',
        'PASSWORD': 'webdb',
        'HOST': 'localhost',
        'PORT': 3306
    }
}
```

### 7. 장고 프로젝트 관리 어플리케이션(기본설치)이 사용하는 DB 생성하기
```shell
(env) # python manage.py migrate -- 워크밴치에 테이블 생성됨.
```
* mysql5.1x인 경우 오류가 발생하면, manage.py에 다음 코드를 추가하고 다시 실행
```python
from django.db.backends.mysql.base import DatabaseWrapper
DatabaseWrapper.data_types['DateTimeField'] = 'datetime'
```

### 8. 프로젝트(사이트) 관리 계정 만들기 (damin 계정)
```shell
(env) # python manage.py createsuperuser

Username (leave blank to use 'user'): admin
Email address: hj5730@naver.com
Password:
Password (again):
Superuser created successfully.
```

### 9. 지금까지 작업 내용 확인
1) 서버 시작하기
```shell
(env) # python manage.py runserver 0.0.0.0:9999
```
2) 브라우저로 접근하기
url http://localhost:9999 로 접근
   
------------------------------------------

### 2. 프로젝트(django_practices)에 Apprlcation 추가하기

#### 1. Application들의 통합 template 디렉토리 templates 만들기
1) 디렉토리 생성
django_practices
|--- templates
   
2) template 디렉토리 설정(settings.py)
```python
import os

'DIRS': [os.path.join(BASE_DIR, 'templates')]
```


### 2. helloworld application 만들기
1) application 생성
```shell (터미널에서 하라는 뜻)
(venv) # python manage.py startapp helloworld
```

2) application 등록(settings.py)
```python
INSTALLED_APPS = [
    'helloworld',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
]
```
* 맨위의 helloworld를 추가해주면 됨.
  (새로 만들 application 이름)

3) applcation의 template 디렉토리 생성
django_practices
|---templates
       |--- helloworld
   

4) urls.py 에 URL 등록하고 views.py 에 요청 처리 함수 만들고 template(html) 연결하고.... (반복반복)

### 3. emaillist01 application 만들기
1) application 생성
```shell (터미널에서 하라는 뜻)
(venv) # python manage.py startapp emaillist01
```

2) application 등록(settings.py)
```python
INSTALLED_APPS = [
    'emaillist01',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
]
```
* 맨위의 helloworld를 추가해주면 됨.
  (새로 만들 application 이름)

3) applcation의 template 디렉토리 생성
django_practices
|---templates
       |--- emaillist01
   
   

4) urls.py 에 URL 등록하고 views.py 에 요청 처리 함수 만들고 template(html) 연결하고.... (반복반복)

### 4. guestbook01 application 만들기
1) application 생성
```shell (터미널에서 하라는 뜻)
(venv) # python manage.py startapp guestbook01
```

2) application 등록(settings.py)
```python
INSTALLED_APPS = [
    'guestbook01',
    'emaillist01',
    'helloworld',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
]
```
* 맨위에 guestbook01를 추가해주면 됨.
  (새로 만들 application 이름)

3) applcation의 template 디렉토리 생성
django_practices
|---templates
       |--- guestbook01
       |--- emaillist01
       |--- helloworld
   

4) urls.py 에 URL 등록하고 views.py 에 요청 처리 함수 만들고 template(html) 연결하고.... (반복반복)