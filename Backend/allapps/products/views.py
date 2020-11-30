from django.views.generic import TemplateView


# Create your views here.
class ProductsView(TemplateView):
    template_name = 'products/index.html'
