from django.shortcuts import render
from django.http import HttpResponse
from django.views import View
from django.views.generic import ListView
from .models import Rating

# Create your views here.

class SimpleView(View):
    def get(self, request):
        return HttpResponse('Hello, world')
    
# class SimpleFormView(View):
#     form_class = SimpleForm
#     initial = {'foo': 'initional value'}
#     template_name = 'form_template.html'

#     def get(self, request, *args, **kwargs):
#         form = self.form_class(initional=self.initional)
#         return render(request, self.template_name, {'form': form})

class RatingsListView(ListView):
    model = Rating










