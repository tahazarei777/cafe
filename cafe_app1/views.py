from django.shortcuts import render
from django.views import View
from .models import Category
from django.views.generic import TemplateView

class list_products(View):
    def get (self,request):
        categorys = Category.objects.prefetch_related('products').all()
        context ={
            "categorys":categorys
        }
        return render(request, "index.html" ,context)
    


class home(TemplateView):
    template_name = "index.html"