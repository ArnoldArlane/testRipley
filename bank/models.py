from django.db import models
from django import forms


class Clientes(models.Model):
    fecha_registro = models.DateField(auto_now_add=True)
    nombres = models.CharField(max_length=100)
    apellidos = models.CharField(max_length=100)
    rut = models.CharField(max_length=15, null=True)
    celular = models.CharField(max_length=15)
    email = models.CharField(max_length=50)

    def __int__(self):
        return (self.id)


class ClienteForm(forms.ModelForm):
    class Meta:
        model = Clientes
        fields = ["nombres", "apellidos", "celular", "email"]


class CuentasBancarias(models.Model):
    numero_cuenta = models.CharField(max_length=15, null=True)
    codigo_cliente = models.ForeignKey(
        Clientes, on_delete=models.CASCADE, null=True, blank=False)
    moneda = models.CharField(max_length=15)
    saldo = models.DecimalField(max_digits=15, decimal_places=5, default=0)

    def __int__(self):
        return (self.id)


class TipoTransaccion(models.Model):
    descripcion = models.CharField(max_length=50)

    def __int__(self):
        return (self.id)


class Transacciones(models.Model):
    fecha_transaccion = models.DateField(auto_now_add=True, null=True)    
    cuenta_bancaria = models.ForeignKey(
        CuentasBancarias, on_delete=models.CASCADE, null=True, blank=False)
    origen = models.CharField(max_length=15, null=True)
    tipo_transaccion = models.ForeignKey(
        TipoTransaccion, on_delete=models.CASCADE, null=True, blank=False)
    monto_transaccion = models.DecimalField(max_digits=15, decimal_places=5)

    def __int__(self):
        return (self.id)
