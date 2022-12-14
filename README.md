# Prueba T茅cnica Ripley

Construya una p谩gina web que permita realizar 3 acciones:
- 馃殌 Consulta de saldo
- 馃殌 Realizar transferencia bancaria
- 馃殌Consulta de indicadores econ贸micos
 
### Desaf铆o:
-	馃殌 Desarrolle un proyecto en Python como lenguaje de programaci贸n (puede utilizar cualquier framework):

    -	Para la consulta de saldo, se debe solicitar el RUT del cliente y se espera como resultado el saldo de su cuenta bancaria.

    - Para realizar una transferencia bancaria, se deben solicitar las cuentas de origen y destino, adem谩s el monto a transferir. Se espera un mensaje que indique el resultado de la transferencia (ejemplo: transferencia realizada, saldo insuficiente o que la cuenta de destino no existe).

    - Para la consulta de indicadores econ贸micos consuma un API REST externo y p煤blico (ejemplo: https://mindicador.cl/) para obtener los valores reales del D贸lar, UTM y UF.

- 馃殌 Utilice y maneje como base de datos un archivo JSON donde tendr谩 los datos de clientes y cuentas bancarias.

- 馃殌 Renderice una vista para que el usuario seleccione la intenci贸n y obtenga los datos generados.

- 馃殌 Es bienvenida toda funcionalidad adicional (ejemplo: Al realizar una transferencia bancaria, que nos entregue un documento PDF como comprobante).

- 馃殌 Orden y calidad de c贸digo ser谩n considerados, incluya un archivo README con las instrucciones de ejecuci贸n.


## Start the app

> **Step 1** - Download the code from the GH repository (using `GIT`) 

```bash
$ git clone https://github.com/ArnoldArlane/testRipley.git
$ cd testRipley-main
```

<br />

### 馃憠 Set Up for `Windows` 

> Install modules via `VENV` (windows) 

```
$ virtualenv env
$ .\env\Scripts\activate
$ pip3 install -r requirements.txt
```

<br />

> Set Up Database

```bash
$ python manage.py makemigrations
$ python manage.py migrate
```

<br />

> Start the app

```bash
$ python manage.py runserver
```

At this point, the app runs at `http://127.0.0.1:8000/`. 

<br />

## 鉁? Create Users

```bash
python manage.py createsuperuser
```

Con este usuario podr谩 ingresar al sistema.

