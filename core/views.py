from django.shortcuts import render, redirect
from item.models import Item, Category
from .forms import SignupForm, LoginForm

# Create your views here.
def index(request):
    items = Item.objects.all()
    categories = Category.objects.all()
    content = {'items': items, 'categories': categories}
    return render(request, 'core/index.html', content)

def signup(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        print('form', form)
        if form.is_valid():
            print('valid', form)
            form.save()
            return redirect('/login/')
    else:
        form = SignupForm()
    content = {'form': form}
    return render(request, 'core/signup.html', content)

def login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            print('login form', form)
            return redirect('/')
    form = LoginForm()
    content = {'form': form}
    return render(request, 'core/login.html', content)
