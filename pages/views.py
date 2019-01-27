from django.http import HttpResponse # importar isso
from django.shortcuts import render # já vem importado

# Create your views here.
def home_view(request, *args, **kwargs): #args e kwargs são do python. Parece que, com o request, não precisa dos outros parâm.
    print(args, kwargs)
    print(request.user) # muito útil para autenticação, etc
    # return HttpResponse("<h1>Hello World</h1>") # string of HTML code python (comentamos esse response simples para poder testar a outra forma, que usa os templates e o render)
    return render(request, "home.html",  {}) # são necessários os 3 argumentos, sendo o segundo o nome do template que iremos usar e o terceiro o contexto, que, nesse caso, preenchemos com o empty dictionarty

def about_view(request, *args, **kwargs):
    my_context = {
        "my_text": "this is about Denise",
        "my_number": 123,
        "my_list": [456, 788, "abc"],
    }
    # return HttpResponse("<h1>About us</h1>")
    return render(request, "about.html",  my_context)

def contact_view(request, *args, **kwargs):
    # return HttpResponse("<h1>Keep in touch</h1>")
    return render(request, "contact.html",  {})