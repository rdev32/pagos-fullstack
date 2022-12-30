''' ESTAS RUTAS SON SOLO PARA SERVIR LAS PAGINAS HTML '''
''' CADA PAGINA TIENE UN SCRIPT ASINCRONO QUE HACE LAS PETICIONES A LA API '''
from django.shortcuts import render

# home routing
def page_not_found_view(request, exception):
    return render(request, '404.html', status=404)

def index(request):
    return render(request, 'index.html', status=200)

def terms(request):
    return render(request, 'terms.html', status=200)

def privacy(request):
    return render(request, 'privacy.html', status=200)

def user_login(request):
    return render(request, 'login.html', status=200)

def user_register(request):
    return render(request, 'register.html', status=200)

# user dashboard routing
def user_dashboard(request):
    return render(request, 'customer/index.html', status=200)

def user_create(request):
    return render(request, 'customer/add.html', status=200)

# manager dashboard routing
def manager_dashboard(request):
    return render(request, 'management/index.html', status=200)
