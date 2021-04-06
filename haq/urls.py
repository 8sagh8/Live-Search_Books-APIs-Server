from django.urls import path, include
from django.conf.urls import url

from . import views

app_name = "haq"
               
urlpatterns = [
    path('logout', views.LogOutView, name="logout"),
    # JSON Files routes
    path('', views.CreateJSONView, name="createJSON"),
    path('postJSON', views.PostJSONView, name="postJSON"),
    path('addNeed', views.AddNeedView, name="addName"),
    path('deleteNeed', views.DeleteNeedView, name="addName"),

    #  other ways to write route
    # path('getTopic/', views.GetTopicView, name="getTopic"),
    # url(r'^getPersonRef/(?P<person_id>[0-9]+)/$', views.GetPersonRefView, name="getPersonRef"),
    # url(r'^getTopic/(?P<topic_id>[0-9]+)/$', views.GetTopicView, name="getTopic"),
    # url(r'^getCategoriesBooks/(?P<category_id>[0-9]+)/$', views.GetCategoriesBooksView, name="getCategoriesBooks"),
    # path(r'^getCategoriesBooks/(?P<category_id>\d+)/$', views.GetCategoriesBooksView, name="getCategoriesBooks"),
    # url(r'^getStatusBooks/(?P<status_id>[0-9]+)/$', views.GetStatusBooksView, name="getStatusBooks"),
    # url(r'^getReligiousBooks/(?P<sect_id>[0-9]+)/$', views.GetReligiousBooksView, name="getReligiousBooks"),
    # url(r'^getNeedBooks/(?P<need_id>[0-9]+)/$', views.GetNeedBooksView, name="getNeedBooks"),
    # url(r'getLanguagesBooks/(?P<language_id>[0-9]+)/$', views.GetLanguagesBooksView, name="getLanguagesBooks"),
    # url(r'^getTopic/(?P<topic_id>\d+)/', views.GetTopicView, name="getTopic"),
    # path(r'getPersonRef/<int:person_id>/', views.GetPersonRefView, name="getPersonRef"),
]


