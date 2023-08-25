from django.shortcuts import redirect, render
from django.contrib.auth import logout


def assessmentPage(request):
    # logout(request)
    context={}
    # return redirect("app_course:course")
    return render(request, 'app_assessment/assessment.html', context)
