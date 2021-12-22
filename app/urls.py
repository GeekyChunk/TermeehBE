from django.urls import path
from app.views import *

urlpatterns = [
    path('item/', ItemList.as_view()),
    path('item/<slug>/', ItemRetrieve.as_view()),
    path('user/', CurrentUser.as_view()),
    path('top/', TopList().as_view()),
    path('top/<pk>/', TopRetrieve.as_view()),
    path('post/', PostList().as_view()),
    path('post/<pk>/', PostRetrieve.as_view()),
    path('highlight/', HighlightList().as_view()),
    path('highlight/<pk>/', HighlightRetrieve.as_view()),
]
