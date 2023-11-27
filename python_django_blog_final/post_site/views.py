from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from django.urls import reverse_lazy, reverse

from .models import Post, Category, Comment
from .forms import PostForm, EditForm, CategoryForm, CommentForm
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView


def LikeView(request, pk):
    post = get_object_or_404(Post, id=request.POST.get('post_id'))
    if post.likes.filter(id=request.user.id).exists():
        post.likes.remove(request.user)
    else:
        post.likes.add(request.user)
    return HttpResponseRedirect(reverse('article-details', args=[str(pk)]))


class HomeView(ListView):
    model = Post
    template_name = 'post_site/home.html'
    ordering = ['-id']

    def get_context_data(self, *args, **kwargs):
        cat_menu = Category.objects.all()
        contex = super(HomeView, self).get_context_data(*args, **kwargs)
        contex['cat_menu'] = cat_menu

        return contex


def CategoryListView(request):
    cat_menu_list = Category.objects.all()
    return render(request, 'post_site/category_list.html', {'cat_menu_list': cat_menu_list})


def CategoryView(request, cats):
    category_post = Post.objects.filter(category__name=cats.replace('-', ' '))
    return render(request, 'post_site/categories.html',
                  {'cats': cats.title().replace('-', ' '),
                   'category_post': category_post})


class ArticlesDetailView(DetailView):
    model = Post
    template_name = 'post_site/article_details.html'

    def get_context_data(self, *args, **kwargs):
        contex = super(ArticlesDetailView, self).get_context_data()

        stuff = get_object_or_404(Post, id=self.kwargs['pk'])

        liked = False
        if stuff.likes.filter(id=self.request.user.id).exists():
            liked = True
        total_likes = stuff.total_likes()
        contex['total_likes'] = total_likes
        contex['liked'] = liked
        return contex


class AddPostView(CreateView):
    model = Post
    form_class = PostForm
    template_name = 'post_site/add_post.html'


class AddCategoryView(CreateView):
    model = Category
    form_class = CategoryForm
    template_name = 'post_site/add_category.html'


class UpdatePostView(UpdateView):
    model = Post
    form_class = EditForm
    template_name = 'post_site/update_post.html'


class DeletePostView(DeleteView):
    model = Post
    template_name = 'post_site/delete_post.html'
    success_url = reverse_lazy('home')


class AddCommentView(CreateView):
    model = Comment
    form_class = CommentForm
    template_name = 'post_site/add_comment.html'

    def form_valid(self, form):
        form.instance.post_id = self.kwargs['pk']
        return super().form_valid(form)

    success_url = reverse_lazy('home')
