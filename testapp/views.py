from django.shortcuts import render

# Create your views here.


def form(request):
    return render(request, 'form.html')

def result(request):
    return render(request, 'result.html')