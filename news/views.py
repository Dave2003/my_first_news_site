from django.shortcuts import render, redirect
from .models import Articles
from .forms import ArticlesForm
from django.views.generic import DetailView, UpdateView

# Create your views here.


def news(request):
    news = Articles.objects.order_by('-date')
    return render(request, 'news/newshome.html', {'news': news})


class NewsDetailView(DetailView):
    model = Articles
    template_name = 'news/detail_wiews.html'
    context_object_name = 'article'


class NewsUpdateView(UpdateView):
    model = Articles
    template_name = 'news/create.html'
    form_class = ArticlesForm


def crete(request):
    error = ''
    if request.method == 'POST':
        form = ArticlesForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
        else:
            error = 'Yalnyslyk bar'

    form = ArticlesForm
    data = {
        'form': form,
        'error': error
    }
    return render(request, 'news/create.html', data)
