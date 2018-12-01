from django.urls import path
from cms import views


app_name = 'cms'
urlpatterns = [

    path('recoman_top/', views.recoman_top, name='recoman_top'),   # top
    path('recoman_top/recommend', views.recommend, name='recoman_recommend'),  # recommend
    path('recoman_top/history', views.recoman_history, name='recoman_history'),  # history
]