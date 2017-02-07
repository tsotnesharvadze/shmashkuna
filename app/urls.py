from django.conf.urls import url, include
from .views import *

app_name = 'app'



urlpatterns = [
	url(r'^$', Index.as_view(), name='index'),

]