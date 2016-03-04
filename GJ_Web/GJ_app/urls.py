from django.conf.urls import url
from . import views
from . import menu_controller


app_name = 'GJ_app'
urlpatterns = [ 
	# Users
	# ex: /GJ_app/
    url(r'^$', views.index, name='index'),
    # ex: /GJ_app/5/
   # url(r'^(?P<question_id>[0-9]+)/$', views.detail, name='detail'),
    # ex: /GJ_app/5/results/
   # url(r'^(?P<question_id>[0-9]+)/results/$', views.results, name='results'),
    # ex: /GJ_app/5/vote/
  #  url(r'^(?P<question_id>[0-9]+)/vote/$', views.vote, name='vote'),
    # ex: /GJ_app/signup/
    url(r'^profile/',views.profile, name='profile'),
    url(r'^signup/', views.signup, name='signup'),
    # ex: /GJ_app/login/
    url(r'^login/', views.login, name='login'),
    # ex: /GJ_app/logout/
    url(r'^logout/', views.logout, name='logout'),
	
	# App Data
	# /GJ_app/data/customer/menu/ 
    url(r'^data/customer/menu/', views.menu_json, name='menu_json'),
    url(r'^data/', views.data),
	
	# Menus page
	# /GJ_app/menu/mcdonalds
	# url(r'^menu/(?P<comp_name>\w+)/$', menu_controller.index, name='index')
	
	# for testing purposes , we are going to do it with company_id
	url(r'^menu/(?P<comp_id>[0-9]+)/$', menu_controller.index, name='index'),
	    url(r'^pricing/', views.pricing, name='pricing'),

	

]

