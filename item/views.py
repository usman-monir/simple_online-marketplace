from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from .models import Item
from .forms import NewItemForm, EditItemForm

# Create your views here.
def detail(request, pk):
    item = get_object_or_404(Item, pk= pk)
    related_items = Item.objects.filter(is_sold = False, category = item.category).exclude(pk=pk)[0:3]
    content = {'item': item, 'related_items': related_items}
    return render(request, 'item/detail.html', content)


@login_required(login_url='/login')
def new(request):
    if request.method == 'POST':
        form = NewItemForm(request.POST, request.FILES)
        if form.is_valid():
            item= form.save(commit=False)
            item.created_by = request.user
            item.save()
            print('item created',item)
            return redirect(reverse('item:detail', args=[item.pk]))
    form = NewItemForm()
    content = {'form': form}
    print('form......')
    return render(request, 'item/new.html', content)


@login_required(login_url='/login')
def edit(request, pk):
    if request.method == 'POST':
        item = get_object_or_404(Item, pk=pk)
        form = EditItemForm(request.POST, request.FILES, instance=item)
        if form.is_valid():
            form.save()
            return redirect('item:detail', pk=pk)
        else:
            print('invalid form ')
    print('edit', pk)
    item = get_object_or_404(Item, pk=pk)
    form = EditItemForm(instance=item)
    content = {'form': form, 'pk': pk}
    return render(request, 'item/edit.html', content)



@login_required(login_url='/login')
def delete(request, pk):
    item = get_object_or_404(Item, pk=pk)
    item.delete()
    return redirect('/')
