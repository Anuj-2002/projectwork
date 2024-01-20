from django.urls import path, include

# from smart import urls as SmartUrl
from scan import views as ScanViews

urlpatterns = [
    path('', ScanViews.Home),
    path('scan/', ScanViews.Scan, name='video'),
    path('history/', ScanViews.History, name='History'),
]
