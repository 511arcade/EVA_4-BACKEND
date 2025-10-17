# Salud Vital - Backend (Django + DRF + PostgreSQL)

Cumple los 14 puntos de la pauta: entorno virtual, comentarios en bloque, estructura, modelos con CHOICES y nueva tabla, CRUD completo (API + templates), filtros/búsqueda, docs, PostgreSQL, rutas/admin, footer en templates.

## Entorno virtual "eva2" (Windows PowerShell)

```
# Crear venv con nombre exacto
python -m venv eva2

# Activar
. .\eva2\Scripts\Activate.ps1

# Actualizar pip (opcional)
python -m pip install --upgrade pip
```

## Instalación

```
cd salud_vital
Copy-Item .env.example .env
pip install -r requirements.txt
python manage.py migrate
python manage.py createsuperuser  # opcional
```

Configura tu PostgreSQL en `.env` (DB_NAME, DB_USER, DB_PASSWORD, DB_HOST, DB_PORT).

## Carga de datos realistas

```
python manage.py loaddata clinica/fixtures/seed.json
```

## Ejecutar servidor

```
python manage.py runserver
```

- Admin: http://127.0.0.1:8000/admin/
- API: http://127.0.0.1:8000/api/
- Docs: http://127.0.0.1:8000/api/docs/

## Rutas API (principales)
- /api/especialidades/
- /api/pacientes/
- /api/medicos/
- /api/tratamientos/
- /api/medicamentos/
- /api/consultas/
- /api/recetas/
- /api/receta-items/

## Rutas Web (templates)
- /especialidades/ (CRUD completo)
- /pacientes/ (CRUD completo)
- /medicos/ (CRUD completo)
- /tratamientos/ (CRUD completo)
- /medicamentos/ (CRUD completo)
- /consultas/ (CRUD completo)
- /recetas/ (CRUD completo)

Todas las páginas incluyen footer con nombre, sección y año.
