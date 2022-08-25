"""aarohi_website URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.shortcuts import redirect
from home.views import error404
handler404 = error404

urlpatterns = [
    path('', lambda req: redirect('/home/')),
    path('payments/', include("payments.urls")),
    path('home/', include("home.urls")),
    path('events/', include("events.urls")),
    path('accounts/', include("accounts.urls")),
    path('mails/', include("mails.urls")),
    path('exhibitions/', include("exhibitions.urls")),
    path('notanadmin/', admin.site.urls),

]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) 
 
