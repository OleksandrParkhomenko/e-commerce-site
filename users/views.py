from django.shortcuts import render


def register(request):
    context = {
    }
    return render(request, 'users/register.html', context)
