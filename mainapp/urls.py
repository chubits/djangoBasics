from django.urls import path

from .views import *
from mainapp.apps import MainappConfig

app_name = MainappConfig.name


urlpatterns = [
    path('', MainPageView.as_view(), name='main'),
    path('login/', LoginPageView.as_view(), name='login'),
    path('doc_site/', DocSitePageView.as_view(), name='doc_site'),
    path('contacts/', ContactsPageView.as_view(), name='contacts'),
    path('news/', NewsPageView.as_view(), name='news'),
    # path("news/<int:page>/", views.NewsWithPaginatorView.as_view(), name="news_paginator"),
    path('courses_list/', CoursesListPageView.as_view(), name='courses_list')
]
