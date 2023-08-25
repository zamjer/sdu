from django.shortcuts import redirect, render
from django.contrib.auth import logout


def taskPage(request):
    context={}
    return render(request, 'app_task/task_list.html', context)
