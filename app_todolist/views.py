from django.shortcuts import redirect, render
from django.contrib.auth import logout


def todolistPage(request):
    # logout(request)
    context={}
    # return redirect("app_course:course")
    return render(request, 'app_todolist/todo_list.html', context)
