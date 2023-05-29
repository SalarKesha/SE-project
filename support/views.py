from django.contrib.auth.decorators import login_required
from django.http import Http404
from django.shortcuts import render
from support.models import Message
from account.models import CustomUser


@login_required(login_url='/login/')
def message(request, pk):
    user = CustomUser.objects.filter(id=pk).first()
    if user != request.user:
        raise Http404
    if request.method == 'POST':
        title = request.POST.get('title')
        content = request.POST.get('content')
        Message.objects.create(
            user=user,
            title=title,
            content=content
        )
    messages = user.messages.all()
    return render(request, 'support/support.html', {'tickets': messages})
