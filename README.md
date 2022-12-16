# Approval-API-crediclub
API que abrueba o rechaza un credito construido en python con fastAPI y SQLAlchemy

1. Crear DB: /dbcreate.sql
1.1 Verificar credenciales para la conexión a la db en /config/db.py 
2. Compilar app.py en el entorno virtuar (en particular se utilizó Anaconda) con el objeto app.
 	> uvicorn app:app --reload
3. Correr el servidor local
4. Para realizar una consulta, hacer una petición Post en http://127.0.0.1:8000/users
    Ejemplo de datos a ingresar (JSON):
    {
      "PRIMER_NOMBRE": "Maria",
      "APELLIDO_PAT": "Gomez",
      "APELLIDO_MAT": "Palacio",
      "FECHA_NAC": "2000-11-30",
      "INGRESOS_MENSUALES": 17000,
      "DEPENDIENTES": 2,
    }
    
6. Respuesta 
{
    "ID": 44,
    "RFC": "GOPM001130",
    "APROBADO": "Aprobado"
}
