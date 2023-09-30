from django.urls import path
from .views import *

urlpatterns = [
    path('', home, name="home"),
    path('login/', login_view, name="login_view"),
    path('register/', register_view, name="register_view"),
    path('add-article/', add_article, name="add_article"),
    path('article-detail/<slug>', article_detail, name="article_detail"),
    path('see-article/', see_article, name="see_article"),
    path('article-delete/<id>', article_delete, name="article_delete"),
    path('article-update/<slug>/', article_update, name="article_update"),
    path('logout-view/', logout_view, name="logout_view"),
    path('verify/<token>/', verify, name="verify")
]
