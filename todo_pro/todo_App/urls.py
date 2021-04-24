
from django.urls import path

from todo_App import views

urlpatterns=[
     path('',views.show,name='show'),
    path('delete/<int:task_id>/',views.delete,name='delete'),
    path('update/<int:id>/', views.update, name='update'),
    path('cbvtask/',views.TaskListview.as_view(),name='cbvtask'),
    path('cbvdetail/<int:pk>/', views.TaskDetailView.as_view(), name='cbvdetail'),
path('cbvupdate/<int:pk>/', views.TaskUpdateView.as_view(), name='cbvupdate'),
path('cbvdelete/<int:pk>/', views.TaskDeleteView.as_view(), name='cbvdelete')


]