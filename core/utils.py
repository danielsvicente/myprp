from django.core.files import File
from django.conf import settings
from .models import Transaction, Category, Dashboard
from decimal import *
import csv
import codecs
from io import TextIOWrapper

"""
This function opens the account statement file,
parse the data to be imported and insert into the
table Transaction.

Account statement CSV file layout:
Column 0: Date
Column 1: Category name
Column 2: Category ID
Column 3: Description
Column 4: Document
Column 5: Value
"""
def account_statement(name):
	csv.register_dialect('semicolon', delimiter=';')
	f = open(settings.DATA_ROOT + '/' + name, 'r')
	try:
	    reader = csv.reader(f, dialect='semicolon')

	    for row in reader:
	    	t = Transaction()
	    	t.date = format_date(row[0])
	    	if row[2]:
		    	category_id = int(row[2])
		    	t.category = Category.objects.get(pk=category_id)
	    	t.description = row[3]
	    	t.document = row[4]
	    	t.value = format_value(row[5])
	    	t.save()

	    print('IMPORTAÇÃO REALIZADA COM SUCESSO!')
	#except ValueError:
	#	print(ValueError, name)
	finally:
		f.close()


"""
Processo de carga na tabela de transacoes

Solucao para problema na leitura do arquivo importado:
stackoverflow.com/questions/16243023/how-to-resolve-iterator-should-return-strings-not-bytes#answer-16243182
"""
def carga_extrato(f):
	csv.register_dialect('semicolon', delimiter=';')
	csvfile = TextIOWrapper(f.file)

	#Metodo anterior para abrir arquivo direto da pasta
	#f = open(settings.DATA_ROOT + '/' + name, 'r')

	try:
		reader = csv.reader(csvfile, dialect='semicolon')
		for row in reader:
			t = Transaction()
			t.date = format_date(row[0])
			t.description = row[2]
			t.document = row[3]
			t.value = format_value(row[4])
			if row[1]:
				category_id = int(row[1])
				t.category = Category.objects.get(pk=category_id)
			t.saldo = format_value(row[5])
			t.save()
			print('Nova transacao: ' + t.date + ' ' + t.value)

			#Processo de atualizacao na tabela do dashboard
			try:
				dashboard_data = Dashboard.objects.get(ano=t.date[0:4], mes=t.date[5:7]) #[0:4]=ano [5:7]=mes
			except Dashboard.DoesNotExist:
				dashboard_data = Dashboard()
				dashboard_data.ano = int(t.date[0:4])
				dashboard_data.mes = int(t.date[5:7])
				dashboard_data.rendimento = Decimal(0.00)
				dashboard_data.despesa = Decimal(0.00)
				dashboard_data.media_gastos = Decimal(0.00)
				dashboard_data.saldo = Decimal(0.00)
				dashboard_data.saldo_acumulado = Decimal(0.00)
				dashboard_data.save()
				print('Novo registro no Dashboard: ' + str(dashboard_data.ano) + '/' + str(dashboard_data.mes))

			if Decimal(t.value) > Decimal(0.00):
				dashboard_data.rendimento += Decimal(t.value)
			else:
				dashboard_data.despesa += abs(Decimal(t.value))
			dashboard_data.media_gastos = dashboard_data.despesa / int(t.date[8:10])
			dashboard_data.saldo = dashboard_data.rendimento - dashboard_data.despesa
			dashboard_data.saldo_acumulado = t.saldo

			print('DASHBOARD...: ' + str(dashboard_data.ano) + '/' + str(dashboard_data.mes))
			print('Rendimento..: ' + str(dashboard_data.rendimento))
			print('Despesa.....: ' + str(dashboard_data.despesa))
			print('Media gastos: ' + str(dashboard_data.media_gastos))
			print('Saldo.......: ' + str(dashboard_data.saldo))
			print('Saldo acum..: ' + str(dashboard_data.saldo_acumulado))

			dashboard_data.save()

		print('IMPORTAÇÃO REALIZADA COM SUCESSO!')
	except Exception as e:
		print('ALGUM ERRO OCORREU...')
		raise
	finally:
		f.close()


"""
Format date to aaaa-mm-dd format
"""
def format_date(date):
	dd = date[0:2]
	mm = date[3:5]
	aaaa = date[6:10]
	formated_date = aaaa + '-' + mm + '-' + dd
	return formated_date

"""
Format value
"""
def format_value(value):
	aux_value = value.replace('.', '')
	formated_value = aux_value.replace(',', '.')
	#if formated_value[0] is '-':
	#	return formated_value[1:]
	#else:
	return formated_value
