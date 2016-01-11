"""Dandelion URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include, patterns
from django.contrib import admin
from goals import views
from newyears import views
from django.views.generic import TemplateView
from django.contrib.auth.decorators import login_required, permission_required


urlpatterns = [
	url(r'^$', login_required(TemplateView.as_view(template_name="landing.html"))),
    url(r'^admin/', admin.site.urls),
	# include all the default authentication views. more info at
	# https://docs.djangoproject.com/es/1.9/topics/auth/default/#module-django.contrib.auth.views
	url(r'^user/', include('django.contrib.auth.urls')),
	url(r'^goals/', include('goals.urls')),
	url(r'^newyears/', include('newyears.urls')),
]
