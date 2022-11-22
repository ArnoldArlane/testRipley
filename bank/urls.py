from django.urls import path
from . import views

app_name = 'bank'

urlpatterns = [
    path('consulta_saldo/', views.consulta_saldo, name='consulta_saldo'),
    path('consultar_saldo_pro/', views.consultar_saldo_pro,
         name='consultar_saldo_pro'),
    path('transferencia/', views.transferencia, name='transferencia'),
    path('transferencia_pro/', views.transferencia_pro,
         name='transferencia_pro'),
    path('consulta_ind/', views.consulta_ind, name='consulta_ind')
]
