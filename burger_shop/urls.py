
from django.conf.urls import url
from django.contrib import admin
from core import views as menu_views
from django.contrib.auth import views as auth_views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^menu/$', menu_views.show_menu, name='menu'),
    url(r'^login/$', auth_views.login, {'template_name': 'login.html'}, name='login'),
    url(r'^logout/$', auth_views.logout, {'next_page': 'login'}, name='logout'),
    url(r'^signup/$', menu_views.signup, name='signup'),
]
