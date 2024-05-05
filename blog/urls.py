from django.urls import path
from .views import ArticleList, ArticleDetail, category
from django.conf import settings
from django.conf.urls.static import static


app_name = "blog"
urlpatterns = [
    path('',ArticleList.as_view(), name="home"),
    path('page/<int:page>',ArticleList.as_view(), name="home"),
    path('article/<slug:slug>',ArticleDetail.as_view(), name="detail"),
    path('category/<slug:slug>',category, name="category"),
    path('category/<slug:slug>/page/<int:page>',category, name="category"),


    
]
urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
