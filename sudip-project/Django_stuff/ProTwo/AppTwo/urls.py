from django.conf.urls import url
from AppTwo import views

urlpatterns = [
        url(r'^$',views.index,name="second_app"),
        url(r'^espanyol/',views.intro,name="intro"),
        ]
