from django.conf.urls import url, patterns

from crudapp import views

urlpatterns = patterns('',
    url(r'^$', views.UserList, name = "user_list"),
    url(r'^new$', views.CreateUser, name = "user_new"),
    url(r'^edit/(?P<pk>\d+)$', views.UpdateUser, name = "user_edit"),
    url(r'^delete/(?P<pk>\d+)$', views.DeleteUser, name = "user_delete"),
)