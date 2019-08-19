from django.urls import path
from . import views
from .views import FunctionCreateView, FunctionListView, FunctionDetailView, FunctionDeleteView



urlpatterns = [
        path('',views.home,name='home'),
        path('database/',FunctionListView.as_view(),name='database'),
        # The default html doc this path will look for is function_form.html
        path('database/function/',FunctionCreateView.as_view(),name='function-create'),
        path('database/<int:pk>/',FunctionDetailView.as_view(),name='function-detail'),
        path('database/<int:pk>/delete/',FunctionDeleteView.as_view(),name='function-delete'),
        path('database/matrix/',views.get_matrix,name='matrix'),
        ]