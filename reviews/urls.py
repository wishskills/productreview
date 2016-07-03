from django.conf.urls import url
from . import views

urlpatterns = [
    # ex: /
    url(r'^$', views.review_list, name='review_list'),
    # ex: /review/1/
    url(r'review/(?P<review_id>[0-9]+)/$', views.review_detail, name='review_detail'),
    # ex: /laptop/
    url(r'laptop$', views.laptop_list, name='laptop_list'),
    # ex: /laptop/1
    url(r'laptop/(?P<laptop_id>[0-9]+)/$', views.laptop_detail, name='laptop_detail'),
    url(r'^review/(?P<laptop_id>[0-9]+)/add_review/$', views.add_review, name='add_review'),
    url(r'^review/user/$', views.user_review_list, name='user_review_list'),
]
