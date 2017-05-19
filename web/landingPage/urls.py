from django.conf.urls import url
from landingPage import views

urlpatterns = [
    url(r'^$', views.HomePageView.as_view()),
]
