from django.urls import path
from django.conf.urls import url
from . import views

urlpatterns = [

	path('', views.index),
	path('gold', views.gold),
	path('gold.html', views.gold),
	path('<int:treasure_id>',views.detail, name='detail'),
]