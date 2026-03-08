# 📦 Sistema de Ventas Django

## 🔹 Descripción

Este proyecto es un **sistema de gestión de ventas** desarrollado con **Django** y **Bootstrap**. Permite gestionar:

* **Departamentos**: Crear, listar, editar y eliminar.
* **Productos**: Asociados a departamentos, con precios, IVA y stock.
* **Clientes**: Gestión de clientes con nombre, email y teléfono.
* **Ventas**: Registro de ventas incluyendo código automático, cliente, producto, precio, cantidad y fecha.

Todas las listas utilizan **paginación** y las plantillas están diseñadas con **Bootstrap 5** para una interfaz moderna y responsiva.

---

## ⚙️ Instalación y ejecución

1. **Clonar el repositorio**

```bash
git clone <URL-del-repositorio>
cd DjangoProject
```

2. **Crear y activar un entorno virtual**

* Windows:

```bash
python -m venv .venv
.venv\Scripts\activate
```

* Linux / MacOS:

```bash
python -m venv .venv
source .venv/bin/activate
```

3. **Instalar dependencias**

```bash
pip install django
pip install -r requirements.txt  # si existe
```

4. **Crear y aplicar migraciones**

```bash
python manage.py makemigrations
python manage.py migrate
```

> 🔹 Esto crea las tablas necesarias en la base de datos según tus modelos.

5. **Crear superusuario (opcional)**

```bash
python manage.py createsuperuser
```

6. **Ejecutar el servidor de desarrollo**

```bash
python manage.py runserver
```

Abrir en el navegador: [http://127.0.0.1:8000](http://127.0.0.1:8000)

---

## 🔹 Relanzar Django en caso de falla

Si el servidor se detiene o falla:

1. **Detener procesos de Django antiguos**

* Windows:

```bash
taskkill /F /IM python.exe
```

* Linux / Mac:

```bash
pkill -f runserver
```

2. **Reactivar el entorno virtual**

```bash
.venv\Scripts\activate  # Windows
source .venv/bin/activate  # Linux/Mac
```

3. **Reaplicar migraciones si hay cambios**

```bash
python manage.py makemigrations
python manage.py migrate
```

4. **Reiniciar el servidor**

```bash
python manage.py runserver
```

5. **Ver errores**

* Revisar la consola por mensajes de error.
* Comprobar dependencias: `pip list`
* Verificar `settings.py` y la base de datos.

---

## 🌐 Notas adicionales

* Todos los formularios y tablas están diseñados con **Bootstrap 5**.
* El código de venta se genera automáticamente combinando **3 letras del mes actual + últimos 5 dígitos del timestamp UNIX**.
* Paginación activa en todos los listados.
* Compatible con Django ≥ 5.1 y Python ≥ 3.11.
---
