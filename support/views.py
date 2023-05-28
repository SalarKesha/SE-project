from django.contrib.auth.decorators import login_required
from django.shortcuts import render

from account.models import CustomUser
from patient.models import Patient
from support.models import Message


@login_required(login_url='/login/')
def message(request, pk):
    user = CustomUser.objects.filter(id=pk).first()
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
