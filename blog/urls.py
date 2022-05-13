from django.urls import path
from . import views

urlpatterns = [
    path('films/', views.filmsList.as_view()),
    path('films/<int:pk>/', views.filmsDetail.as_view()),
    path('actors/', views.actorstList.as_view()),
    path('actors/<int:pk>/', views.actorsDetail.as_view()),
    path('category/', views.categorytList.as_view()),
    path('category/<int:pk>/', views.categoryDetail.as_view()),
]
