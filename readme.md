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
(env) # python manage.py migrate
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