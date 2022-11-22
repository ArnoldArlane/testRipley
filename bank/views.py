# Create your views here.
from datetime import datetime
from decimal import Decimal
from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from bank.models import Clientes
from bank.models import CuentasBancarias
from bank.models import TipoTransaccion
from bank.models import Transacciones
from django.conf import settings
import json
from fpdf import FPDF, HTMLMixin
from PIL import Image
from PIL import ImageFont
from PIL import ImageDraw
import requests


LISTA_MESES_EQ = ["Enero", "Febreo", "Marzo", "Abril",
                  "Mayo", "Junio", "Julio", "Agosto",
                  "Setiembre", "Octubre", "Noviembre",
                  "Diciembre"]


class MyFPDF(FPDF, HTMLMixin):
    """Clase para crear PDF.

    Args:
        FPDF (str): Tipo orientacion
        HTMLMixin (str): HTMLMixin
    """
    pass


class Mindicador:
    def __init__(self, indicador, date_i):
        self.indicador = indicador
        self.date_i = date_i

    def InfoApi(self):
        url = f'https://mindicador.cl/api/{self.indicador}/{self.date_i}'
        response = requests.get(url)
        data = json.loads(response.text.encode("utf-8"))
        return data


def read_json():
    list_client = []
    list_cue_ban = []
    list_tip_tra = []
    list_tra = []
    f = open('bank/data.json')
    data = json.load(f)
    for cli in data['clientes']:
        o_c = Clientes(
            id=cli['id'], fecha_registro=cli['fecha_registro'],
            nombres=cli['nombres'], apellidos=cli['apellidos'],
            rut=cli['rut'], celular=cli['celular'],
            email=cli['email'])
        o_c.save()
        list_client.append(o_c)
    for cue in data['cuentas_bancarias']:
        cli = Clientes.objects.get(pk=int(cue['codigo_cliente']))
        o_c = CuentasBancarias(
            id=cue['id'], numero_cuenta=cue['numero_cuenta'],
            codigo_cliente=cli, moneda=cue['moneda'],
            saldo=Decimal(cue['saldo']))
        o_c.save()
        list_cue_ban.append(o_c)
    for tip in data['tipo_transaccion']:
        o_t = TipoTransaccion(
            id=tip['id'], descripcion=tip['descripcion'])
        o_t.save()
        list_tip_tra.append(o_t)
    for tra in data['transaccion']:
        cue = CuentasBancarias.objects.get(pk=int(tra['cuenta_bancaria']))
        tip = TipoTransaccion.objects.get(pk=int(tra['tipo_transaccion']))
        o_t = Transacciones(
            id=tra['id'], fecha_transaccion=tra['fecha_transaccion'],
            cuenta_bancaria=cue,
            origen=tra['origen'], tipo_transaccion=tip,
            monto_transaccion=tra['monto_transaccion'])
        o_t.save()
        list_tra.append(o_t)
    f.close()
    return list_client, list_cue_ban, list_tip_tra, list_tra


@login_required
def consulta_saldo(request):
    title = "Consulta tu Saldo"
    return render(request, 'home/consulta_saldo.html', locals())


@login_required
def consultar_saldo_pro(request):
    title = "Consulta tu Saldo"
    (list_client, list_cue_ban,
     list_tip_tra, list_tra) = read_json()
    nombres_lideres_lecciones = ''
    rut_a = ''
    if request.method == 'GET':
        rut_a = request.GET['rut']
    cli = Clientes.objects.filter(rut=rut_a).first()
    cue = ''
    if cli:
        cue = CuentasBancarias.objects.filter(codigo_cliente=cli).first()
    return render(request, 'home/consulta_saldo_res.html', locals())


@login_required
def transferencia(request):
    title = "Realizar Transferencia"
    return render(request, 'home/transferencia.html', locals())


def f_date(fec):
    return str(fec.strftime("%Y-%m-%d"))


def export_db():
    lis_cli_db = Clientes.objects.all()
    lis_cue_db = CuentasBancarias.objects.all()
    lis_tip_db = TipoTransaccion.objects.all()
    lis_tra_db = Transacciones.objects.all()
    lis_cli = []
    lis_cue = []
    lis_tip = []
    lis_tra = []
    for c in lis_cli_db:
        lis_cli.append(
            {"id": c.id,
             "fecha_registro": f_date(c.fecha_registro),
             "nombres": c.nombres,
             "apellidos": c.apellidos,
             "rut": c.rut,
             "celular": c.celular,
             "email": c.email})
    for cu in lis_cue_db:
        lis_cue.append(
            {"id": cu.id,
             "numero_cuenta": cu.numero_cuenta,
             "codigo_cliente": cu.codigo_cliente.id,
             "moneda": cu.moneda,
             "saldo": str(cu.saldo)})
    for t in lis_tip_db:
        lis_tip.append(
            {"id": t.id,
             "descripcion": t.descripcion}
        )
    for tr in lis_tra_db:
        lis_tra.append(
            {"id": tr.id,
             "fecha_transaccion": f_date(tr.fecha_transaccion),
             "cuenta_bancaria": tr.cuenta_bancaria.id,
             "origen": tr.origen,
             "tipo_transaccion": tr.tipo_transaccion.id,
             "monto_transaccion": str(tr.monto_transaccion)})

    data_json = {
        'clientes': lis_cli,
        'cuentas_bancarias': lis_cue,
        'tipo_transaccion': lis_tip,
        'transaccion': lis_tra}
    json_object = json.dumps(data_json, indent=4)

    with open("bank/data.json", "w") as outfile:
        outfile.write(json_object)


@login_required
def transferencia_pro(request):
    title = "Realizar Transferencia"
    msj_cue_o = ''
    msj_cue_d = ''
    msj_mon_t = ''
    (list_client, list_cue_ban,
     list_tip_tra, list_tra) = read_json()
    nombres_lideres_lecciones = ''
    cue_o = ''
    cue_d = ''
    mon_t = ''
    template_dir = (str(settings.STATICFILES_DIRS[0]) +
                    "/assets/img/template_vou.jpg")
    filename = 'voucher.pdf'
    jgp_gen = str(settings.STATICFILES_DIRS[0]) + '/assets/img/voucher.jpg'
    dir_archivo = str(settings.STATICFILES_DIRS[0]) + '/assets/img/' + filename
    succ_trans = False
    if request.method == 'GET':
        cue_o = request.GET['cue_o']
        cue_d = request.GET['cue_d']
        mon_t = Decimal(request.GET['mon_t'])
    o_cue_o = CuentasBancarias.objects.filter(numero_cuenta=cue_o).first()
    o_cue_d = CuentasBancarias.objects.filter(numero_cuenta=cue_d).first()
    if o_cue_o:
        msj_cue_o = ''
        if o_cue_o.saldo > mon_t:
            msj_mon_t = ''
            if o_cue_d:
                msj_cue_d = ''
                # registrar salida
                new_t = Transacciones()
                new_t.cuenta_bancaria = o_cue_o
                new_t.origen = "transferencia salida"
                new_t.tipo_transaccion = TipoTransaccion.objects.get(pk=2)
                new_t.monto_transaccion = mon_t
                new_t.save()
                o_cue_o.saldo = o_cue_o.saldo - mon_t
                o_cue_o.save()
                # registrar ingreso
                new_t_i = Transacciones()
                new_t_i.cuenta_bancaria = o_cue_d
                new_t_i.origen = cue_o
                new_t_i.tipo_transaccion = TipoTransaccion.objects.get(pk=1)
                new_t_i.monto_transaccion = mon_t
                new_t_i.save()
                o_cue_d.saldo = o_cue_d.saldo + mon_t
                o_cue_d.save()
                succ_trans = True
                img = Image.open(template_dir)
                draw = ImageDraw.Draw(img)
                font = ImageFont.truetype("ARLRDBD.TTF", 30)
                txt_f1 = ("Hola " + o_cue_o.codigo_cliente.nombres + ' ' +
                          o_cue_o.codigo_cliente.apellidos)
                txt_f2 = "Realizaste una transferencia exitosa:"
                txt_f3 = "Cuenta Origen: " + cue_o
                txt_f4 = "Cuenta Destino: " + cue_d
                txt_f5 = "Monto transferido: " + str(mon_t)
                txt_f6 = "Tu saldo es: $ " + str(o_cue_o.saldo)
                draw.text((270, 540), txt_f1, (0, 0, 0), font=font)
                draw.text((270, 640), txt_f2, (0, 0, 0), font=font)
                draw.text((270, 740), txt_f3, (0, 0, 0), font=font)
                draw.text((270, 840), txt_f4, (0, 0, 0), font=font)
                draw.text((270, 940), txt_f5, (0, 0, 0), font=font)
                draw.text((270, 1040), txt_f6, (0, 0, 0), font=font)
                img.save(jgp_gen)
                pdf = MyFPDF('P', 'mm', 'A4')
                x, y, w, h = 0, 0, 210, 297
                pdf.add_page()
                pdf.image(jgp_gen, x, y, w, h)
                pdf.output(dir_archivo, "F")
                export_db()
            else:
                msj_cue_d = 'No se encontró el numero de cuenta Destino,\
                            favor verificar.'
        else:
            msj_mon_t = 'Monto insuficiente'
    else:
        msj_cue_o = 'No se encontró el numero de cuenta Origen,\
                    favor verificar.'
    return render(request, 'home/transferencia_res.html', locals())


@login_required
def consulta_ind(request):
    title = "Consulta de indicadores"
    today = datetime.now()
    today_f = str(today.strftime("%d-%m-%Y"))
    ind_dol = Mindicador('dolar', today_f)
    lis_ind_dol = ind_dol.InfoApi()
    val_ind_dol = lis_ind_dol['serie'][0]['valor']
    ind_utm = Mindicador('utm', today_f)
    lis_ind_utm = ind_utm.InfoApi()
    val_ind_utm = lis_ind_utm['serie'][0]['valor']
    ind_uf = Mindicador('uf', today_f)
    lis_ind_uf = ind_uf.InfoApi()
    val_ind_uf = lis_ind_uf['serie'][0]['valor']
    return render(request, 'home/consulta_ind.html', locals())
