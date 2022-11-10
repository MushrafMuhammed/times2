from django.urls import path
from . import views

app_name = 'homepage'

urlpatterns = [ 
    path('index/',views.indexfun, name='index'),
    path('about/',views.aboutfun, name='about'),
    path('news/',views.newsfun, name='news'),
    path('work/',views.workfun, name='work'),
    path('academics/',views.academicsfun, name='academics'),
    path('resources/',views.resourcesfun, name='resources'),
    path('getinvolved/',views.getinvolvedfun, name='getinvolved')
]