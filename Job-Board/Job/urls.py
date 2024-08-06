
from . import views
from django.urls import path , include
urlpatterns = [
    path('', views.job_list, name='job_list'),  # This is the main URL for the application.
    # path('<int:job_id>/', views.job_detail, name='job_detail'),  # This URL pattern will match when we have a URL like '/jobs/1/'.
]
