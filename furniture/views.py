from django.http import HttpResponse, HttpResponseNotFound, Http404
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView
from django.contrib.auth.mixins import LoginRequiredMixin

from .forms import *
from .models import *
from .utils import *



class FurnitureHome(DataMixin, ListView):
    model = Furniture
    template_name = 'furniture/index.html'
    context_object_name = 'posts'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title="Главная страница")
        return context | c_def

    def get_queryset(self):
        return Furniture.objects.filter(is_published=True)


# def index(request):
#     posts = Furniture.objects.all()
#
#     context = {
#         'posts': posts,
#         'menu': menu,
#         'title': 'Главная страница',
#         'cat_selected': 0,
#     }
#
#     return render(request, 'furniture/index.html', context=context)

def about(request):
    return render(request, 'furniture/about.html', {'menu': menu, 'title': 'Про сайт'})

class AddPage(LoginRequiredMixin, DataMixin, CreateView):
    form_class = AddPostForm
    template_name = 'furniture/addpage.html'
    success_url = reverse_lazy('home')
    login_url = reverse_lazy('home')
    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title="Добавление статьи")
        return context | c_def

# def addpage(request):
#     if request.method == 'POST':
#         form = AddPostForm(request.POST, request.FILES)
#         if form.is_valid():
#                 form.save()
#                 return redirect('home')
#     else:
#         form = AddPostForm()
#     return render(request, 'furniture/addpage.html', {'form': form, 'menu':menu, 'title': 'Добавление статьи'})

def contact(request):
    return HttpResponse("Обратная связь")

def login(request):
    return HttpResponse("Авторизация")

def pageNotFound(request, exception):
    return HttpResponseNotFound("<h1>Сторінку не знайдена</h1")

# def show_post(request, post_slug):
#     post = get_object_or_404(Furniture, slug=post_slug)
#
#     context = {
#         'post': post,
#         'menu': menu,
#         'title': post.title,
#         'cat_selected': post.cat_id,
#     }
#
#     return render(request, 'furniture/post.html', context=context)

class ShowPost(DataMixin, DetailView):
    model = Furniture
    template_name = 'furniture/post.html'
    slug_url_kwarg = 'post_slug'
    context_object_name = 'post'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title=context['post'])
        return context | c_def


# def show_category(request, cat_slug):
#     posts = Furniture.objects.filter(cat__slug=cat_slug)
#
#     dict = {'title': 'Отображение по рубрикам',
#             'posts': posts,
#             'cat_selected': cat_slug
#             }
#
#     return render(request, 'furniture/index.html', context=dict)


class FurnitureCategory(DataMixin, ListView):
    model = Furniture
    template_name = 'furniture/index.html'
    context_object_name = 'posts'
    allow_empty = False

    def get_queryset(self):
        return Furniture.objects.filter(cat__slug=self.kwargs['cat_slug'], is_published=True)
    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title='Категория - ' + str(context['posts'][0].cat),
                                      cat_selected=context['posts'][0].cat_id)
        return context | c_def
# Create your views here.
