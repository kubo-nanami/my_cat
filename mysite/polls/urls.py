from django.urls import path

from . import views
from django.views.generic import TemplateView


app_name = 'polls'
urlpatterns = [
    path('', TemplateView.as_view(template_name='polls/index.html'), name='index'),
    path('inquiry/', views.InquiryView.as_view(), name="inquiry"),
    path('management/', views.DiaryListView.as_view(), name="management_list"),
    path('diary-detail/<int:pk>/', views.DiaryDetailView.as_view(), name="diary_detail"),
    path('page-create/', views.DiaryCreateView.as_view(), name=",management_create"),
    path('management-update/<int:pk>/', views.DiaryUpdateView.as_view(), name="management_update"),
    path('page-delete/<int:pk>/', views.DiaryDeleteView.as_view(), name="diary_delete"),
]