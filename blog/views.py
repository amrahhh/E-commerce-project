from product.models import Size
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from blog.models import *
from blog.forms import CommentForm
from django.views.generic.edit import FormMixin
from django.views.generic import (
    ListView, DetailView
)
# Create your views here.

# def blog(request):
#     blogs = Blog_post.objects.all()
#     context = {
#         'blogs':blogs,
#     }
#     return render(request, 'blog.html', context)

# def single_blog(request,id):
#     published_categories = Blog_category.objects.all()
#     recent_post = Blog_post.objects.order_by('-created_at')[:3]
#     single_blogs = Blog_post.objects.filter(id=id)
#     blogs = Blog_post.objects.order_by('-created_at')[:3]
#     blog = Blog_post.objects.get(id = id)
#     parent_comments = Comment.objects.filter(parent_comment__isnull=True, blog_post=blog)
#     form = CommentForm()
#     user = User.objects.get(id=1)
#     print(user)
#     if request.method == 'POST':
#         form = CommentForm(data=request.POST)
#         if form.is_valid():
#             form.instance.blog_post = blog
#             form.instance.author = user
#             form.save()
#             return redirect(reverse_lazy('blog:single_page' , kwargs={'id' : id}))
#     context = {
#         'published_categories':published_categories,
#         'single_blogs':single_blogs,
#         'recent_post': recent_post,
#         'blogs': blogs,
#         'blog' : blog,
#         'form': form,
#         'parent_comments': parent_comments
#     }
#     return render(request, 'single-blog.html', context)


class Blog_postListView(ListView):
    model = Blog_post
    template_name = 'blog.html'
    paginate_by = 6
    context_object_name = 'post_list'
    # queryset = Story.objects.filter(is_published=True)

    def get_queryset(self):
        queryset = super().get_queryset()
        tags = self.request.GET.get('tags')
        queryset = queryset.filter(is_published=True)
        if tags:
            queryset = queryset.filter(tags__id=tags)
        return queryset


class Blog_postDetailView(FormMixin, DetailView):
    model = Blog_post
    form_class = CommentForm
    template_name = 'single-blog.html'
    context_object_name = 'blog_details'
   # queryset = Blog_post.objects.filter(is_published=True)

    def get_success_url(self , **kwargs):
        return reverse_lazy('blog:single_page' , kwargs = {'slug': self.object.slug})

    def get_context_data(self, **kwargs):
        blog = self.object
        context = super().get_context_data(**kwargs)
        context['tags'] = Tag.objects.all()
        context['published_categories'] = Blog_category.objects.all()
        context['recent_blog'] = Blog_post.objects.order_by('-created_at')[:3]
        category = self.object.category
        context['related_post'] = Blog_post.objects.filter(category = category).exclude(id = self.object.id)
        context['parent_comments'] = Comment.objects.filter(parent_comment__isnull = True , blog_post = blog)
        return context

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        form = self.get_form()
        if form.is_valid():
            # <process form cleaned data>
            
            return self.form_valid(form)
        else:
            return self.form_invalid(form)


    def form_valid(self ,form):
        form.instance.blog_post = self.object
        form.instance.author = self.request.user
        form.save()
        return super().form_valid(form)

    def form_invalid(self, form):
        return super().form_invalid(form)


# class ProductDetailView(FormMixin,DetailView):
#     model = Blog
#     form_class = CommentForm
#     template_name = 'item-photo.html'
#     context_object_name = 'blog'
#     def get_success_url(self , **kwargs):
#         return reverse_lazy('product:product_detail' , kwargs = {'pk': self.object.pk})
#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         product = self.object
#         prodspecnames = ProductSpecName.objects.filter(category = product.category)
#         context['parent_comments'] = Review.objects.filter(parent_comment__isnull = True , product = product)
#         context['categories'] = Category.objects.all()
#         context['prodspecnames'] = ProductSpecName.objects.filter(category = product.category)
#         context['productspecdescs'] = ProductSpecDesc.objects.filter(product = product).filter(prod_spec_name__in = prodspecnames)
#         context['products2'] = Product.objects.order_by('-created_at')[:4]
#         return context
#     def post(self, request, *args, **kwargs):
#         self.object = self.get_object()
#         form = self.get_form()
#         print(request.POST)
#         if form.is_valid():
#             # <process form cleaned data>
#             form.instance.product = self.object
#             form.instance.author = request.user
#             form.save()
#             return self.form_valid(form)
#         else:
#             print('invalid form')
#             return self.form_invalid(form)
#         return render(request, self.template_name, {'form': form})