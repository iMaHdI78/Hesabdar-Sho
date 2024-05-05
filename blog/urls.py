from django.urls import path
from .views import ArticleList, ArticleDetail, CategoryList
from django.conf import settings
from django.conf.urls.static import static


app_name = "blog"
urlpatterns = [
    path('',ArticleList.as_view(), name="home"),
    path('page/<int:page>',ArticleList.as_view(), name="home"),
    path('article/<slug:slug>',ArticleDetail.as_view(), name="detail"),
    path('category/<slug:slug>',CategoryList.as_view(), name="category"),
    path('category/<slug:slug>/page/<int:page>',CategoryList.as_view(), name="category"),


    
]
urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
