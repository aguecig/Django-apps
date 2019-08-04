from django.urls import path
from . import views



urlpatterns = [
        path('',views.home,name='app-home'),
        path('test/',views.test,name='test'),
        path('quadquiz/',views.quadratics_quiz,name='quad_quiz',),
        path('quadinfo/',views.quadratics_info,name='quad_info',),
        ]
