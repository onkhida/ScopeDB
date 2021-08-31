from django.urls import path
from . import views

urlpatterns = [
    path('', views.project_list, name='projects'),
    path('<int:id>/', views.project_detail, name='project'),
    # path('file/<int:id>/', views.show_file, name='show-file')
]