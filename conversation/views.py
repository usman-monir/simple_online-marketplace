from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .forms import MessageForm
from item.models import Item
from .models import Conversation, ConversationMessage

# Create your views here.

@login_required(login_url='/login')
def new(request, item_pk):
    item = get_object_or_404(Item, id=item_pk)

    if item.created_by == request.user:
        return redirect('dashboard:index')

    conversations = Conversation.objects.filter(item=item).filter(members__in=[request.user])

    if conversations:
        return redirect('conversation:detail', pk=conversations.first().id)

    if request.method == 'POST':
        form = MessageForm(request.POST)
        if form.is_valid():
            conversation = Conversation.objects.create(item=item)
            conversation.members.add(request.user)
            conversation.members.add(item.created_by)
            conversation.save()

            conversation_message = form.save(commit=False)
            conversation_message.conversation = conversation
            conversation_message.created_by = request.user
            conversation_message.save()

            return redirect('conversation:inbox')
    form= MessageForm()
    return render(request, 'conversation/new.html', {'form': form})


@login_required
def inbox(request):
    conversations = Conversation.objects.filter(members__in=[request.user])
    return render(request, 'conversation/inbox.html', {'conversations': conversations})

@login_required(login_url='/login')
def detail(request, pk):
    conversation = Conversation.objects.filter(members__in=[request.user]).get(id=pk)
    if request.method == 'POST':
        form = MessageForm(request.POST)
        if form.is_valid():
            conversation_message = form.save(commit=False)
            conversation_message.conversation = conversation
            conversation_message.created_by = request.user
            conversation_message.save()

            return redirect('conversation:detail', pk=pk)
    form = MessageForm()
    return render(request, 'conversation/detail.html', {'conversation': conversation, 'form': form})

