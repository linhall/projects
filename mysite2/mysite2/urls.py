from django.conf.urls import include, url
from django.contrib import admin
from mysite2.views import hello, current_datetime, hours_ahead, contact
from books import views

urlpatterns = [
    # Examples:
    # url(r'^$', 'mysite2.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^hello/$', hello),
    url(r'^time/$', current_datetime),
    url(r'^time/plus/(\d{1,2})/$', hours_ahead),
    url(r'^search/$', views.search),
    url(r'^contact/$', contact),
]
