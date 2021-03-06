from django.shortcuts import get_object_or_404, redirect, render
from django.db.models import Q
from django.views import View
from inbox.forms import MessageForm, ThreadForm
from django.contrib.auth.models import User
from inbox.models import MessageModel, ThreadModel
from django.contrib import messages

class CreateThread(View):
  def get(self, request, pk, *args, **kwargs):

    newthreaduser= get_object_or_404(User, pk=pk)
    initial_data={
        'username': newthreaduser.username
    }   
    if newthreaduser == request.user:
      form = ThreadForm()
    else:
      form = ThreadForm(initial=initial_data)
    context = {
      'form': form
    }
    return render(request, 'inbox/createThread.html', context)
    
  def post(self, request, pk, *args, **kwargs):
   
    newthreaduser= get_object_or_404(User, pk=pk)
    initial_data={
        'username': newthreaduser.username
    }
    form = ThreadForm()

    if request.method == 'POST':
      form = ThreadForm(request.POST)
      username = request.POST.get('username')
      try:
        receiver = User.objects.get(username=username)
        if ThreadModel.objects.filter(user=request.user, receiver=receiver).exists():
          thread = ThreadModel.objects.filter(user=request.user, receiver=receiver)[0]
          return redirect('thread', pk=thread.pk)
       
        elif ThreadModel.objects.filter(receiver=request.user, user=receiver).exists():
          thread = ThreadModel.objects.filter(receiver=request.user, user=receiver)[0]
          return redirect('thread', pk=thread.pk)
        if form.is_valid():
          sender_thread = ThreadModel(
            user=request.user,
            receiver=receiver
          )
          sender_thread.save()
          thread_pk = sender_thread.pk
          return redirect('thread', pk=thread_pk)
      except:
        return redirect('create-thread', pk)
    else:
        form=ThreadForm(initial=initial_data)
    return render(request, 'inbox/createThread.html', {'form': form})

  def post(self, request, pk, *args, **kwargs):
    form = ThreadForm(request.POST)
    username = request.POST.get('username')
    try:
      receiver = User.objects.get(username=username)
      if ThreadModel.objects.filter(user=request.user, receiver=receiver).exists():
        thread = ThreadModel.objects.filter(user=request.user, receiver=receiver)[0]
        return redirect('thread', pk=thread.pk)

      elif ThreadModel.objects.filter(receiver=request.user, user=receiver).exists():
          thread = ThreadModel.objects.filter(receiver=request.user, user=receiver)[0]
          return redirect('thread', pk=thread.pk)
      
      if form.is_valid():
        sender_thread = ThreadModel(
          user=request.user,
          receiver=receiver
        )
      sender_thread.save()
      thread_pk = sender_thread.pk
      return redirect('thread', pk=thread_pk)
    except:
      messages.error(request, 'Nutzer nicht gefunden.')
      return redirect('create-thread', pk)

class ListThreads(View):
  def get(self, request, *args, **kwargs):
      threads = ThreadModel.objects.filter(Q(user=request.user) | Q(receiver=request.user))
      context = {
      'threads': threads
      }
      return render(request, 'inbox/threadList.html', context)

class CreateMessage(View):
  def post(self, request, pk, *args, **kwargs):
    form = MessageForm(request.POST, request.FILES)
    thread = ThreadModel.objects.get(pk=pk)
    if thread.receiver == request.user:
      receiver = thread.receiver
      message = MessageModel(
        thread=thread,
        sender_user=thread.receiver,
        receiver_user=thread.user,
        body=request.POST.get('message'),
      )
    else:
      receiver = thread.receiver
      message = MessageModel(
        thread=thread,
        sender_user=request.user,
        receiver_user=receiver,
        body=request.POST.get('message'),
      )
    if form.is_valid() and thread.receiver == request.user:
      message = form.save(commit=False)
      message.thread = thread
      message.sender_user = receiver
      message.receiver_user = request.user
      message.save()
    elif form.is_valid():
      message = form.save(commit=False)
      message.thread = thread
      message.sender_user = request.user
      message.receiver_user = receiver
      message.save()
    return redirect('thread', pk=pk)

class ThreadView(View):
  def get(self, request, pk, *args, **kwargs):
    form = MessageForm()
    thread = ThreadModel.objects.get(pk=pk)
    message_list = MessageModel.objects.filter(thread__pk__contains=pk)
    context = {
      'thread': thread,
      'form': form,
      'message_list': message_list
    }
    return render(request, 'inbox/thread.html', context)

def deleteThread(request, pk, *args, **kwargs):

  entrytodelete = get_object_or_404(ThreadModel, pk=pk)

  if request.method == 'POST':

    entrytodelete.delete()
    return redirect("inbox")
    
  return render(request, "inbox/deleteThread.html", {'entrytodelete': entrytodelete})
