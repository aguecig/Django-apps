from django.urls import path
from . import views

from .views import FunctionCreateView, FunctionListView, FunctionDetailView, FunctionDeleteView

urlpatterns = [
        path('',views.home,name='app-home'),
        # calculus tool urls
        path('calculus_tool/',FunctionListView.as_view(),name='calculus_tool'),
        path('calculus_tool/function/',FunctionCreateView.as_view(),name='function-create'),
        path('calculus_tool/<int:pk>/',FunctionDetailView.as_view(),name='function-detail'),
        path('calculus_tool/<int:pk>/delete/',FunctionDeleteView.as_view(),name='function-delete'),
        ]
