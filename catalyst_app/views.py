from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.


def upload_file(request):
    if request.method == "POST":
        file = request.FILES.get('file')
        return HttpResponse("Done")
    else:
        return render(request, 'submit_file.html')