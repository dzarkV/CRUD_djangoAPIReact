from django.conf.urls import url
from CompanyApp import views

from django.conf.urls.static import static
from django.conf import settings

urlpatterns=[

    url(r'^company$',views.companyApi),
    url(r'^company/([0-9]+)$',views.companyApi),

] 