from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('courseDetails/<int:myid>', views.courseDetails, name='courseDetails'),
    path('course/', views.course, name='course'),
    path('about/', views.aboutus, name='about'),

]