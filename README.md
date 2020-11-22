# Definiciones Aleatorias 

Repositorio del proyecto de vistas CRUD de Definiciones Eng/Esp

La finalidad de este proyecto es la de tener un herramienta que sirva de complemento para el aprendizaje de otra lengua, como por ejemplo el idioma inglés en este caso. Con este proyecto se pueden ir guardando las palabras que te interese recordar con sus definiciones, las cuales luego puedes estudiar usando un selector de palabras aleatorias, el cual te mostrara todas las definiciones de la palabra elegida aleatoriamente. Las definiciones pueden ser modificadas o eliminadas. 

## Funcionamiento 👇

El proyecto tiene 4 páginas principales:

1)En la **primera página** tú puedes apretar un botón que te eligirá una palabra aleatoria en ingles que tú hayas ingresado previamente

![Pagina palabra aleatoria](/Readme_images/page1_1.png)

Luego tú puedes apretar el botón de **pista** para poder ver ejemplos de esta palabra o puedes apretar el botón **me rindo** para ver todos los campos. 

![Pagina palabra aleatoria](/Readme_images/page1_2.png)

**PD:** Los datos de las palabras que se ven en este ejemplo fueron sacadas de [WordReference](https://www.wordreference.com/es/)

2)En la **segunda página** tú tienes el formulario para poder ingresar una nueva definición

![Pagina palabra aleatoria](/Readme_images/page2.png)

3)En la **tercera página** tú puedes buscar una palabra en inglés y actualizar o borrar sus definiciones

![Pagina palabra aleatoria](/Readme_images/page3.png)

4)En la **cuarta página** tú puedes ver las categorías que se han ido insertando y también puedes actualizar su nombre.

![Pagina palabra aleatoria](/Readme_images/page4.png)

### Requisitos 📋

Para este proyecto se usó **Django 3.1.3** y **Python 3.8.5**, por lo que los requisitos serían:

- Django 3.1.3

Puedes configurar un entorno virtual usando **Conda**. A continuación se muestra un ejemplo de cómo puedes configurar uno de nombre **django31** para **Python 3.8**

```
conda create --name django31 python=3.8
```

Una vez ya creado el entorno debes ingresar en él, lo cual se haría de la siguiente manera 

```
conda activate django31
```

Entonces ya dentro del entorno virtual instalas **Django 3.1.3**

```
pip install Django==3.1.3
```

Con esto deberías tener lista la configuración inicial

### Instalación 🔧

Una vez ya tienes todos los requisitos solo debes configurar la base de datos y para ello solo debes hacer:

```
python manage.py migrate
```

Con esto ya deberías poder probar el proyecto haciendo un

```
python manage.py runserver
```

## Construido con 🛠️

* [Django](https://www.djangoproject.com) - Framework web
* [w3schools](https://www.w3schools.com/w3css/w3css_templates.asp) - Plantilla de estilos CSS


## Autor✒️

* **Eduardo A. Barrios** - *Trabajo Inicial* - [GTXs4](https://github.com/gtxs4)
