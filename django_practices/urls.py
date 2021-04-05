"""django_practices URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

import helloworld.views as helloworldviews
import emaillist01.views as emaillist01views
import guestbook01.views as guestbook01views

urlpatterns = [
    path('', helloworldviews.main), # main은 url을 안주면 됨
    path('form/', helloworldviews.form),
    path('join', helloworldviews.join), # POST 방식으로 할 때는 join으로 설정하고, #GET 방식으로 할때는 join/으로 함
    path('hello1/', helloworldviews.hello1),
    path('tags/', helloworldviews.tags),

    path('emaillist01/', emaillist01views.index),
    path('emaillist01/form', emaillist01views.form),
    path('emaillist01/add', emaillist01views.add),

    path('guestbook01/', guestbook01views.index),

    path('admin/', admin.site.urls),
]
