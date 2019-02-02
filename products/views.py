from django.shortcuts import render

from .models import Product
# Create your views here.
def product_detail_view(request):
    obj = Product.objects.get(id=1)
    # inicialmente passamos dessa forma, mas, para ficar mais fácil caso haja uma alteração, adotamos a segunda opção e chamamos o .title, etc no template
    # context = {
    #     "title": obj.title,
    #     "description": obj.description
    # }
    context = {
        "object": obj
    }
    # return render(request, "product/detail.html", context) # esse foi o caminho para quando criei o template dentro de templates
    return render(request, "products/product_detail.html", context) # esse é o caminho para o template criado dentro do app products