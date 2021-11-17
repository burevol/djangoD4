from django.views.generic import ListView, UpdateView, CreateView, DetailView, \
    DeleteView

from .forms import NewsForm
from .models import Post


# Create your views here.
class PostList(ListView):
    model = Post
    template_name = 'posts.html'
    context_object_name = 'posts'
    queryset = Post.objects.order_by('-date')
    paginate_by = 10


class PostDetail(DetailView):
    model = Post
    template_name = 'post.html'
    context_object_name = 'post'


class PostCreateView(CreateView):
    template_name = 'post_create.html'
    form_class = NewsForm


class PostUpdateView(UpdateView):
    template_name = 'post_create.html'
    form_class = NewsForm

    def get_object(self, **kwargs):
        id = self.kwargs.get('pk')
        return Post.objects.get(pk=id)


class PostDeleteView(DeleteView):
    template_name = 'post_delete.html'
    queryset = Post.objects.all()
    success_url = '/news/'


class PostSearchView(ListView):
    model = Post
    template_name = 'products_search.html'
