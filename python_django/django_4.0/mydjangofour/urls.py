"""mydjangofour URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
from django.http import HttpResponse

class Test:
    def __init__(self, url):
        self.url = url
    def path(self):
        return self.url

def test(request):
    return HttpResponse("<h1>test</h1>")

def main(request):
    return HttpResponse("<h1>test1</h1>")

def main_page(request):
    return HttpResponse("<h1>test2</h1>")

myurl = Test('test/main/')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('test/', test),
    path(myurl.path(), main),
    path('main_page/home/python', main_page)
]
