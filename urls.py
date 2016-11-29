"""myprp URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
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
from django.conf.urls import url
from django.contrib import admin
from myprp.core import views as myprp_views



urlpatterns = [
	url(r'^$', myprp_views.home, name='home'),
	url(r'^extrato/', myprp_views.extrato, name='extrato'),
    url(r'^carga/', myprp_views.carga, name='carga'),
    url(r'^asimport/', myprp_views.asimport, name='asimport'),
    url(r'^transaction_edit/(?P<pk>[0-9]+)/$', myprp_views.transaction_edit, name='transaction_edit'),
    url(r'^dashboard_data/', myprp_views.dashboard_data, name='dashboard_data'),
    url(r'^admin/', admin.site.urls, name='admin'),
]
