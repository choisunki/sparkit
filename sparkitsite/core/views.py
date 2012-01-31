# -*- coding: utf-8 -*-
from annoying.decorators import render_to
from templated_emails.utils import send_templated_email
from forms import SparkCampForm

@render_to('core/index.html')
def index(request):
    return locals()

@render_to('core/camp.html')
def spark_camp(request):
	form = SparkCampForm(request.POST or None)
	if form.is_valid():
		TO_EMAIL = ['victor@sparkit.com.br']

		nome_projeto 	= form.cleaned_data['nome_projeto']
		url_projeto 	= form.cleaned_data['url_projeto']
		desc_projeto 	= form.cleaned_data['desc_projeto']
		time 			= form.cleaned_data['time']
		email 			= form.cleaned_data['email']
		celular 		= form.cleaned_data['celular']

		send_templated_email(TO_EMAIL, 'emails/spark-campus', locals())

	return locals()