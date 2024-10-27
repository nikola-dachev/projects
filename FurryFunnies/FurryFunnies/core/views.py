
from django.shortcuts import render
from django.views.generic import ListView

from FurryFunnies.authors.models import Author
from FurryFunnies.posts.models import Post


# Create your views here.

def index(request):
    author = Author.objects.first()
    context = {
        'author': author,
    }

    return render(request,'core/index.html', context)


class ListDashboardView(ListView):
    model = Post
    template_name = 'core/dashboard.html'


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['author'] = Author.objects.first()
        return context
