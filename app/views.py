# from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.shortcuts import render, redirect, get_object_or_404
# from django.conf import settings
# from django.http import Http404, HttpResponse, JsonResponse
# from django.utils.translation import ugettext_lazy as _
# from django.utils.translation import get_language
from django.views.generic import TemplateView ,DetailView , ListView ,FormView
# from user.forms import UserUpForm ,UserInForm ,AddressForm
# from django.http import JsonResponse
# from django.views.decorators.csrf import csrf_exempt
# from django.core.mail import send_mail
from .models import PhotoModel


class Index(ListView):
	template_name = 'index.html'
	model = PhotoModel
	# object =None

	# def get_context_data(self, **kwargs):
	# 	context = super().get_context_data(**kwargs)
	# 	context['form'] = BanerForm(instance = self.object)
	# 	# print(self.object.txt1)
	# 	return context


