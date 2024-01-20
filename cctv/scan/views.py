from django.http.response import StreamingHttpResponse
from django.shortcuts import render

from scan.models import Mail

# News Import
from scan.utils import gen, VideoCamera


def Scan(request):
    return StreamingHttpResponse(gen(VideoCamera(), request),
                                 content_type='multipart/x-mixed-replace; boundary=frame')


def Home(request):
    return render(request, 'scan/home.html', {})


def History(request):
    msg = Mail.objects.all()
    print(msg)
    return render(request, 'scan/History.html', {"messages":msg})
