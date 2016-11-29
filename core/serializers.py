from rest_framework import serializers
from .models import Dashboard

class DashboardSerializer(serializers.ModelSerializer):

    class Meta:
        model = Dashboard
        fields = ('ano', 'mes', 'rendimento', 'despesa', 'media_gastos', 'saldo', 'saldo_acumulado')
