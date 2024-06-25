from django.contrib import admin
from django.urls import path
from . import views
# from .views import *
from . import test
# from django.conf.urls import url

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.index),
    path('home',views.home, name = "homie"),
    path(r'^$', test.button),
    # raw string
    path(r'^prediction', test.prediction,name="script"),
]

# urlpatterns = [
#     path('', home),
#     # path('test_py/',test_py,name = "test"),

#         # 'livefe' -> function from views
#         # 'live_camera' -> name at index.html>img src="{% url 'live_camera' %}[p-=]
#     ]