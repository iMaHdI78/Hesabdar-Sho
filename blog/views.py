from django.views.generic import ListView
from django.views.generic.detail import DetailView
from account.models import User
from django.core.paginator import Paginator
from django.shortcuts import render, get_object_or_404
#from django.http import HttpResponse, Http404
from .models import Article, Category

#Use list view
class ArticleList(ListView):
	queryset = Article.objects.published()
	paginate_by = 3


#Use Detail view
class ArticleDetail(DetailView):
	model = Article
	def get_ibject(self):
		slug = self.kwargs.get('slug')       
		return get_object_or_404(Article.objects.published(), slug=slug)

		
#Use category view
class CategoryList(ListView):
	paginate_by = 3
	template_name = 'blog/category_list.html'
 
	
	def get_queryset(self):
		global category
		slug = self.kwargs.get('slug')
		category = get_object_or_404(Category.objects.active(), slug=slug)
		return category.articles.published()

	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		context['category'] = category
		return context

#Use category view
class AuthorList(ListView):
	paginate_by = 5
	template_name = 'blog/author_list.html'

	def get_queryset(self):
		global author
		username = self.kwargs.get('username')
		author = get_object_or_404(User, username=username)
		return author.articles.published()

	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		context['author'] = author
		return context
