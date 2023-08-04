from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from item.models import Item,Category

# Create your views here.
@login_required(login_url='/login')
def index(request, c = 'all'):
    if c == 'all' or c.isdigit():
        items = Item.objects.filter(created_by=request.user).order_by('created_at')
    else:
        items = Item.objects.filter(category__name = c , created_by=request.user).order_by('created_at')
    categories = Category.objects.filter()
    total_items = Item.objects.filter(created_by=request.user).count()
    content = {'items': items, 'categories': categories, 'total_items': total_items}
    return render(request, 'dashboard/index.html', content)

