from django.db import models

class TransactionType(models.Model):
	name = models.CharField('Name', max_length=50)
	create_time = models.DateTimeField('Create time', auto_now_add=True)
	update_time = models.DateTimeField('Update time', auto_now=True, null=True)

	def __str__(self):
		return self.name

class Category(models.Model):
	name = models.CharField('Name', max_length=50)
	transaction_type = models.ForeignKey(
		'TransactionType', on_delete=models.CASCADE, related_name='types'
	)
	create_time = models.DateTimeField('Create time', auto_now_add=True)
	update_time = models.DateTimeField('Update time', auto_now=True, null=True)

	def __str__(self):
		return self.name

class Transaction(models.Model):
	date = models.DateField('Date of transaction')
	description = models.CharField('Description', max_length=100)
	document = models.CharField('Document', max_length=10)
	value = models.DecimalField('Value', max_digits=12, decimal_places=2)
	category = models.ForeignKey(
		'Category', on_delete=models.CASCADE, related_name='categories', null=True
	)
	saldo = models.DecimalField('Saldo', max_digits=12, decimal_places=2)
	create_time = models.DateTimeField('Create time', auto_now_add=True)
	update_time = models.DateTimeField('Update time', auto_now=True, null=True)

	def __str__(self):
		return self.description

class Dashboard(models.Model):
	ano = models.IntegerField('Ano', max_length=4)
	mes = models.IntegerField('Mês', max_length=2)
	rendimento = models.DecimalField('Rendimento', max_digits=12, decimal_places=2)
	despesa = models.DecimalField('Despesa', max_digits=12, decimal_places=2)
	media_gastos = models.DecimalField('Média de gasto diário', max_digits=12, decimal_places=2)
	saldo = models.DecimalField('Saldo', max_digits=12, decimal_places=2)
	saldo_acumulado = models.DecimalField('Saldo acumulado', max_digits=12, decimal_places=2)
	create_time = models.DateTimeField('Create time', auto_now_add=True)
	update_time = models.DateTimeField('Update time', auto_now=True, null=True)

	def __str__(self):
		return str(self.ano) + '/' + str(self.mes)
