from django.shortcuts import render, redirect
from contact.forms import ContactForm
from django.contrib import messages
from django.urls import reverse_lazy
from django.views.generic import (
    CreateView, 
)
# Create your views here.

# def contact(request):
#     form = ContactForm()
#     if request.method == 'POST':
#         form = ContactForm(data=request.POST)
#         print(request.POST, form.is_valid())
#         if form.is_valid():
#             form.save()
#             return redirect('/')
#     context = {
#         'form': form,
#     }
#     return render(request, "./includes/footer.html", context)

def contact_us(request):
    return render(request, 'contact.html')

class ContactView(CreateView):
    form_class = ContactForm
    #fields = '__all__'
    #model = Contact
    template_name = './includes/footer.html'
    success_url = reverse_lazy('home:home')

    def form_valid(self, form):
        result = super(ContactView, self).form_valid(form)
        messages.success(self.request, 'Sizin muracietiniz qebul edildi.')
        return result