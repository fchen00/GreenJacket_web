from django.conf.urls import url
from . import views

app_name = 'GJ_app'
urlpatterns = [ 
	# ex: /GJ_app/
    url(r'^$', views.index, name='index'),
    # ex: /GJ_app/5/
    url(r'^(?P<question_id>[0-9]+)/$', views.detail, name='detail'),
    # ex: /GJ_app/5/results/
    url(r'^(?P<question_id>[0-9]+)/results/$', views.results, name='results'),
    # ex: /GJ_app/5/vote/
    url(r'^(?P<question_id>[0-9]+)/vote/$', views.vote, name='vote'),
    # ex: /GJ_app/signup/
    url(r'^signup/', views.signup, name='signup')
]

