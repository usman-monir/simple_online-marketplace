from django.shortcuts import render, redirect
from item.models import Item, Category
from .forms import SignupForm, LoginForm

# Create your views here.
def index(request, c = 'all'):
    if c == 'all' or c.isdigit():
        items = Item.objects.all().order_by('created_at')
    else:
        items = Item.objects.filter(category__name = c)
    categories = Category.objects.all()
    total_items = Item.objects.count()
    content = {'items': items, 'categories': categories, 'total_items': total_items}
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
