# Prueba Técnica Ripley

Construya una página web que permita realizar 3 acciones:
- 🚀 Consulta de saldo
- 🚀 Realizar transferencia bancaria
- 🚀Consulta de indicadores económicos
 
### Desafío:
-	🚀 Desarrolle un proyecto en Python como lenguaje de programación (puede utilizar cualquier framework):

    -	Para la consulta de saldo, se debe solicitar el RUT del cliente y se espera como resultado el saldo de su cuenta bancaria.

    - Para realizar una transferencia bancaria, se deben solicitar las cuentas de origen y destino, además el monto a transferir. Se espera un mensaje que indique el resultado de la transferencia (ejemplo: transferencia realizada, saldo insuficiente o que la cuenta de destino no existe).

    - Para la consulta de indicadores económicos consuma un API REST externo y público (ejemplo: https://mindicador.cl/) para obtener los valores reales del Dólar, UTM y UF.

- 🚀 Utilice y maneje como base de datos un archivo JSON donde tendrá los datos de clientes y cuentas bancarias.

- 🚀 Renderice una vista para que el usuario seleccione la intención y obtenga los datos generados.

- 🚀 Es bienvenida toda funcionalidad adicional (ejemplo: Al realizar una transferencia bancaria, que nos entregue un documento PDF como comprobante).

- 🚀 Orden y calidad de código serán considerados, incluya un archivo README con las instrucciones de ejecución.


## Start the app

> **Step 1** - Download the code from the GH repository (using `GIT`) 

```bash
$ git clone https://github.com/ArnoldArlane/testRipley.git
$ cd challenge_ripley
```

<br />

### 👉 Set Up for `Windows` 

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

## ✨ Create Users

```bash
python manage.py createsuperuser
```

Con este usuario podrá ingresar al sistema.

