from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('courseDetails/<int:myid>', views.courseDetails, name='courseDetails'),
    path('enroll/<int:myid>', views.courseEnroll, name='courseEnroll'),
    path('course/', views.course, name='course'),
    path('about/', views.aboutus, name='about'),
    path('contact/', views.contact, name='contact'),
    path('search', views.search, name='search'),
    path('gallery', views.gallery, name='gallery'),
    path('studentReg/<int:myid>', views.studentReg, name='studentReg'),
    path('termsAndConditions', views.terms, name='termsAndConditions'),
    path('premiumcourse', views.premiumreg, name='premiumcourse'),
]
