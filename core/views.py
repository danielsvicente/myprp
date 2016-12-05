from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, JsonResponse, HttpResponseRedirect
from datetime import date, timedelta
from django.core import serializers
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Transaction, Dashboard
from .forms import TransactionForm, UploadFileForm
from .serializers import DashboardSerializer
from .utils import carga_extrato
from datetime import datetime
from decimal import *


def home(request):
	today = datetime.today()
	dashboard_infos = Dashboard.objects.last()
	context = {'dashboard_infos': dashboard_infos}
	return render(request, 'home.html', context)

def extrato(request):
	template_name = 'extrato.html'
	end_date = date.today()
	start_date = end_date - timedelta(days=7)

	if request.method == 'GET':
		data_inicial = request.GET.get('dataInicial')
		data_final = request.GET.get('dataFinal')
		tipo_transacao = request.GET.get('tipoTransacao')
		if tipo_transacao == 'Rendimentos':
			print('RENDIMENTOS')
			transactions = Transaction.objects.filter(date__range=[data_inicial, data_final], value__gte=0)
		elif tipo_transacao == 'Despesas':
			transactions = Transaction.objects.filter(date__range=[data_inicial, data_final], value__lte=0)
		else:
			transactions = Transaction.objects.filter(date__range=[data_inicial, data_final])
		'''
		if data_inicial and data_final:
			start_day = data_inicial[0:2]
			start_mouth = data_inicial[3:5]
			start_year = data_inicial[6:10]
			end_day = data_final[0:2]
			end_mouth = data_final[3:5]
			end_year = data_final[6:10]
			start_date = start_year + '-' + start_mouth + '-' + start_day
			end_date = end_year + '-' + end_mouth + '-' + end_day
	transactions = Transaction.objects.filter(date__range=[start_date, end_date])
	'''
	soma_rendimentos = Decimal(0.00)
	soma_despesas = Decimal(0.00)
	for transaction in transactions:
		if transaction.value > 0.00:
			soma_rendimentos += transaction.value
		else:
			soma_despesas += transaction.value

	context = {
		'transactions': transactions,
		'soma_rendimentos': soma_rendimentos,
		'soma_despesas': soma_despesas
	}
	return render(request, template_name, context)
"""
def extrato(request):
	template_name = 'extrato.html'
	end_date = date.today()
	start_date = end_date - timedelta(days=7)

	if request.method == 'GET':
		input_date = request.GET.get('range')
		if input_date:
			start_mouth = input_date[0:2]
			start_day = input_date[3:5]
			start_year = input_date[6:10]
			end_mouth = input_date[13:15]
			end_day = input_date[16:18]
			end_year = input_date[19:]
			start_date = start_year + '-' + start_mouth + '-' + start_day
			end_date = end_year + '-' + end_mouth + '-' + end_day
		elif request.GET.get('jan'):
			start_date = str(date.today().year) + '-01-01'
			end_date = str(date.today().year) + '-01-31'
		elif request.GET.get('fev'):
			start_date = str(date.today().year) + '-02-01'
			end_date = str(date.today().year) + '-02-29'
		elif request.GET.get('mar'):
			start_date = str(date.today().year) + '-03-01'
			end_date = str(date.today().year) + '-03-31'
		elif request.GET.get('abr'):
			start_date = str(date.today().year) + '-04-01'
			end_date = str(date.today().year) + '-04-30'
		elif request.GET.get('mai'):
			start_date = str(date.today().year) + '-05-01'
			end_date = str(date.today().year) + '-05-31'
		elif request.GET.get('jun'):
			start_date = str(date.today().year) + '-06-01'
			end_date = str(date.today().year) + '-06-30'
		elif request.GET.get('jul'):
			start_date = str(date.today().year) + '-07-01'
			end_date = str(date.today().year) + '-07-31'
		elif request.GET.get('ago'):
			start_date = str(date.today().year) + '-08-01'
			end_date = str(date.today().year) + '-08-31'
		elif request.GET.get('set'):
			start_date = str(date.today().year) + '-09-01'
			end_date = str(date.today().year) + '-09-30'
		elif request.GET.get('out'):
			start_date = str(date.today().year) + '-10-01'
			end_date = str(date.today().year) + '-10-31'
		elif request.GET.get('nov'):
			start_date = str(date.today().year) + '-11-01'
			end_date = str(date.today().year) + '-11-30'
		elif request.GET.get('dez'):
			start_date = str(date.today().year) + '-12-01'
			end_date = str(date.today().year) + '-12-31'
	transactions = Transaction.objects.filter(date__range=[start_date, end_date])
	context = {
		'transactions': transactions
	}
	return render(request, template_name, context)
"""

def carga(request):
	if request.method == 'POST':
		print('POST')
		form = UploadFileForm(request.POST, request.FILES)
		if form.is_valid():
			carga_extrato(request.FILES['file'])
			return HttpResponseRedirect('/extrato/')
	else:
		print('GET')
		form = UploadFileForm()
		return render(request, 'carga_extrato.html', {'form': form})

def asimport(request):
	#import2db.account_statement(name='extrato.csv')
	import2db.carga_extrato(name='extrato_ago_nov.csv')
	return redirect(extrato)

def transaction_edit(request, pk):
	template_name = 'transaction_form.html'
	transaction = Transaction(pk=pk)
	form = TransactionForm(transaction)
	context = {
		'form': form
	}
	return render(request, template_name, context)

def dashboard_data(request):
	#all_data = serializers.serialize('json', Dashboard.objects.all())
	#return JsonResponse(all_data, safe=False)
	data = Dashboard.objects.all()
	serializer = DashboardSerializer(data, many=True)
	return JsonResponse(serializer.data, safe=False)
