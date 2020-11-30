from django.views.generic import TemplateView


# Create your views here.
class ProductList(TemplateView):
    template_name = 'products/index.html'
