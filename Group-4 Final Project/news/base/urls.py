from django.urls import path
from . import views
 
urlpatterns=[ 
    path('',views.home,name="HOME"),
    path('summarize/<str:pk1>/<str:pk2>',views.summarize,name="summarizer"),
    path('entertainment/', views.entertainmentNews, name='news-entertainment'),
    path('health/', views.healthNews, name='news-health'),
    path('science/', views.scienceNews, name='news-science'),
    path('sports/', views.sportsNews, name='news-sports'),
    path('technology/', views.technologyNews, name='news-technology'),
    path('business/', views.businessNews, name='news-business'),
]