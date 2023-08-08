from django.shortcuts import render

# Create your views here.
def LandingPageIndex(request):
    context = {}
    return render(request, 'LandingPage/index.html', context)