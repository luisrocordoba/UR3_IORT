#LIBRERIAS A UTILIZAR
import pypyodbc as odbc 
import pandas as pd
#USUARIO Y CONTRASEÑA DE LA BASE DE DATOS
username = 'luis'
password = 'Superman04'

#DIRECCIÓN DEL SERVIDOR
server =  'sqldatabaseur3.database.windows.net'
#NOMBRE DE LA BASE DE DATOS
database = 'Pruebadb'

#CADENA DE CONEXION Y CONEXION A BASE DE DATOS
connection_string = 'DRIVER={ODBC Driver 18 for SQL Server};SERVER='+server+';DATABASE='+database+';ENCRYPT=yes;UID='+username+';Pwd='+password
conn = odbc.connect(connection_string)

#COMANDO SQL
sql= """
	SELECT *
	FROM tblObjetos
"""
#CREACIÓN DE CURSOS
cursor = conn.cursor()
cursor.execute(sql)
#CONVERSIÓN A DATAFRAME
dataset = cursor.fetchall()
columns=[column[0] for column in cursor.description]
df= pd.DataFrame(dataset, columns=columns)

print(df)
valor = df.iloc[-1]['nombre'].upper()
print(valor)