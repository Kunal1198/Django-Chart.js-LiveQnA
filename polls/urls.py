from django.conf.urls import url

from .import views 

urlpatterns = [
    #url(r'^$', views.index, name='index'),
    url(r'^login/$', views.user_login, name='user_login'),
    url(r'^logout/$', views.user_logout, name='user_logout'),
    url(r'^register/$', views.register, name='register'),
    url(r'edit_profile/$', views.edit_profile, name="edit_profile"),
    url(r'^question/$', views.page, name='page'),
    url(r'^graph/$', views.hel, name='home'),
    url(r'^api/data/$', views.get_data, name='api-data'),
    url(r'^api/chart/data/$', views.ChartData.as_view(), name='page2'),
]