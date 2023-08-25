from django.shortcuts import redirect, render
from django.contrib.auth import logout


def coursePage(request):
    # logout(request)
    context={}
    # return redirect("app_course:course")
    return render(request, 'app_course/course-list.html', context)
