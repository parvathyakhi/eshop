from django.urls import path,include
from . import views
urlpatterns = [
    path('reg', views.reg,name='reg'),

]