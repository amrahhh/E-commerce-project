from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from product.models import *
from django.contrib import messages
from product.forms import ReviewForm
from django.views.generic.edit import FormMixin
from checkout.models import OrderItem
from django.views.generic import (
    ListView, DetailView, CreateView
)

# Create your views here.

# def product(request):
#     product = Product.objects.all()[:5]
#     image = Product_image.objects.all()
#     context = {
#         'product':product,
#         'image': image,

#     }
#     return render(request, 'product-list.html', context)

class ProductListView(ListView):
    model = Product
    template_name = 'product-list.html'
    paginate_by = 4
    context_object_name = 'product_list'
    
    # queryset = Story.objects.filter(is_published=True)
    def get_queryset(self):
        queryset = super().get_queryset()
        tags = self.request.GET.get('tags')
        queryset = queryset.filter(is_published=True)
        if tags:
            queryset = queryset.filter(tags__id=tags)
        return queryset
    

class ProductDetailView(FormMixin, DetailView):
    model = Product
    form_class = ReviewForm
    template_name = 'single-product.html'
    context_object_name = 'product_details'
   # queryset = Blog_post.objects.filter(is_published=True)

    def get_success_url(self , **kwargs):
        return reverse_lazy('product:single_prod', kwargs = {'slug': self.object.slug})

    def get_context_data(self, **kwargs):
        product = self.object
        context = super().get_context_data(**kwargs)
        context['tags'] = Product_tag.objects.all()
        context['recent_blog'] = Product.objects.order_by('-created_at')[:3]
        category = self.object.category
        context['related_post'] = Product.objects.filter(category = category).exclude(id = self.object.id)
        context['parent_reviews'] = Review.objects.filter(parent_review__isnull = True, product=product)
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
        form.instance.product = self.object
        form.instance.author = self.request.user
        form.save()
        return super().form_valid(form)

    def form_invalid(self, form):
        return super().form_invalid(form)





# class CreateProductView(LoginRequiredMixin, CreateView):
#     form_class = ProductForm
#     template_name = 'add_product.html'

#     def form_valid(self, form):
#         result = super(CreateProductView, self).form_valid(form)
#         form.instance.author = self.request.user
#         messages.success(self.request, 'Sizin mehsulunuz elave olundu.')
#         return result

# def single_product(request, id):
#     product = Product.objects.filter(id=id)
#     image = Product_image.objects.all()
#     prod = Product.objects.all()
#     related_prod = Product.objects.order_by('-created_at')[:4]
#     blog = Product.objects.get(id = id)
#     form = ReviewForm()
#     user = User.objects.get(id=1)
#     if request.method == 'POST':
#         form = ReviewForm(data=request.POST)
#         if form.is_valid():
#             form.instance.product = blog
#             form.instance.author = user
#             form.save()
#             return redirect(reverse_lazy('product:single-prod', kwargs={'id' : id}))
#     context = {
#         'product':product,
#         'image': image,
#         'related_prod': related_prod,
#         'form': form,
#         'blog':blog,
#         'prod': prod,
#     }
#     return render(request, 'single-product.html', context)