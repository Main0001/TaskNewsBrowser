from django.shortcuts import render, redirect
from django.urls import reverse_lazy

from .models import *
from .forms import *
from django.views.generic import DetailView, UpdateView, DeleteView


class NewsUpdateView(UpdateView):
    model = Articles
    template_name = 'news/create.html'

    form_class = ArticlesForm


class NewsDeleteView(DeleteView):
    model = Articles
    success_url = reverse_lazy('home')
    template_name = 'news/news-delete.html'


class NewsDetailView(DetailView):
    model = Articles
    template_name = 'news/details_view.html'
    context_object_name = 'article'


def news_home(request):
    news = Articles.objects.all()
    return render(request, 'news/news_home.html', {'news': news})


def create(request):
    error = ''
    if request.method == 'POST':
        form = ArticlesForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
        else:
            error = 'Ошибка зполнения формы'
    form = ArticlesForm()
    context = {
        'form': form,
        'error': error
    }
    return render(request, 'news/create.html', context=context)