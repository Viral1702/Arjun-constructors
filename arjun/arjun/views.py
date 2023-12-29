from django.http import Http404
from django.shortcuts import render
from contectus.models import Contectus


def home(request):
    try:
        pass
    except:
        pass
    if request.method == 'POST':
        names = request.POST.get('name')
        emails = request.POST.get('email')
        massages = request.POST.get('massage')
        data = Contectus(name=names,email=emails,massage=massages)
        data.save()
    return render(request, "index.html")
def aboutus(request):
    try:
        pass
    except:
        pass
    return render(request,"about.html")