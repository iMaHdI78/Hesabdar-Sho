from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.core.paginator import Paginator
from django.shortcuts import render, get_object_or_404
#from django.http import HttpResponse, Http404
from .models import Article, Category

#Use list view
class ArticleList(ListView):
    queryset = Article.objects.published()
    paginate_by = 3


# def detail (request, slug):
#     context = {
#         "articles" : get_object_or_404(Article.objects.published(), slug=slug)

#     }
#     return render(request,"blog/detail.html", context)

#Use Detail view
class ArticleDetail(DetailView):
    model = Article
    def get_ibject(self):
        slug = self.kwargs.get('slug')       
        return get_object_or_404(Article.objects.published(), slug=slug)
        




def category(request, slug, page=1):
    category = get_object_or_404(Category, slug=slug ,status=True)
    articles_list = category.articles.published()
    paginator = Paginator(articles_list,3)
    articles = paginator.get_page(page)
    context = {
        "category" : category,
        "articles" : articles,

    }
    
    return render(request,"blog/category.html", context)
