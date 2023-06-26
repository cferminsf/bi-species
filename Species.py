# Modulos requeridos para utilizar el script 
#pip install requests
#pip install pypyodbc
#pip install sqlalchemy
#pip install pyodbc

# Importacion de librerias
import json
import requests as reqs
import pandas as pd
import pypyodbc as pyodbc
import pyodbc

#Sql
# Definicion de variables para la conexion de SQL Server.
# Consta de crendenciales, enlaces, y el nombre del driver de la conexion.
DRIVER_NAME = 'SQL Server' # Nombre del driver
SERVER_NAME = '10.0.2.26\DataWH,8699' # Url de conexion
DATABASE_NAME = 'UnoSof' # Base de datos
USERNAME = 'porellana' # Usuario
PASSWORD = 'SQusPo2023$' # Contraseña

# Variable que contiene la informacion de conexion a SQL Server.
conexion = f"""
  DRIVER={{{DRIVER_NAME}}};
  SERVER={SERVER_NAME};
  DATABASE={DATABASE_NAME};
  Trust_Connection=yes;
  uid=porellana;
  pwd=SQusPo2023$;
"""

# Pyodbc es el paquete que realiza la conexion de la base.
conn = pyodbc.connect(conexion)
c = conn.cursor()

# Metodo para consultar los datos desde un archivo JSON y guardarlos dentro de la tabla de SQL Server.
def saveData():

  # Url que se obtiene del metodo para obtener las Especies (Unosof).
  url = 'https://malimamaster.unosof.com/api/v1/products/getSpecies?parentPage=Products2.List'

  # Parametros que se van a ingresar dentro de la cabecera, solo esta la ApiKey.
  payload={}
  headers = {
    'apikey': '9e3da560-3d17-47b2-a1d3-5f4a817be433'
  }

  # Llama al metodo GET del request URL.
  response = reqs.request("GET", url, headers=headers, data=payload)

  # Se crea una variable en la cual lee los datos Json como texto.
  data = json.loads(response.text)

  # Variable que contienen la normalizacion de los datos que se necesitan.
  species = pd.json_normalize(data["data"]["DISTINCTSPECIES"])

  # Bucle que sirve para utilizar la clausula Insert dentro de la base, ademas recorre todas las columnas que se necesitan
  # para ingresar dentro de la base de T_Species
  for row in species.itertuples():
      c.execute('''
                INSERT INTO T_Species (gu_option, nm_option, od_option, tx_code_1, id_venture, tx_code_commercial, tx_code_hts)
                VALUES (?,?,?,?,?,?,?)
                ''',
                row.gu_option,
                row.nm_option,
                row.od_option,
                row.tx_code_1,
                row.id_venture,
                row.tx_code_commercial,
                row.tx_code_hts
              )
      
  # Commit para guardar los datos del insert.
  conn.commit()
  # Cierra la conexion del driver. 
  c.close()

#Llama al metodo para guardar datos.
saveData()