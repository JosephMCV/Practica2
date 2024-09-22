# Practica2
Aqui tendras la siguiente serie de pasos que se utilizaran para ejecutar la aplicación y todos
los demás requisitos necesarios para usarla, como base de datos y etc....


Paso 1- Abrimos windows power shell y nos ubicamos en la carpeta en la que crearemos el entorno


una vez ahi realizaremos el comando python3 -m venv venv

con esto crearemos un entorno virtual en esta carpeta luego nos metemos a ella con

cd ./venv 

aqui adentro haremos ./Scripts/Activate.ps1

con esto activaremos la maquina virtual y ahora volvemos a la carpeta inicial

con cd ..

una vez aqui deberemos instalar las siguientes librerias para continuar, usando el comando

pip install

-pip install fastapi

-pip install docker

-pip install PyMySQL

-pip install pylint

-pip install dark

-pip install pydantic

-pip install peewe

Tenemos que tener en nuestro proyecto configurados los siguientes archivos

En la carpeta FastAPI/Dockerfile -- MySQL/Dockerfile -- Practica2/docker-compose.yml

Ahora tenemos que descargar desde el navegador la app de Docker Desktop y registrarnos

Teniendo estos archivos configurados y la aplicación de docker abierta,volvemos al windows powershell y ejecutamos los siguientes comandos

docker compose build --> Este comando creara la información de nuestro proyecto en la base de datos de docker

Despues de que el docker se buildee, usaremos el comando

docker compose up --> Este comando levantara la base de datos de docker donde podremos ingresar a los contenedores que creamos desde el build, en mi caso usare el localhost:8080 para el adminer
y localhost:8000/docs para el swager

por ultimo verificaremos la calidad del codigo basado en pylint la cual usa el criterio segun pep8

Usamos el comando pylint para ver la calidad, en este caso para la carpeta app

-pylint app

Esto nos dara la calidad del codigo y gracias a black podremos verificar como corregir los errores que recibamos

La calificación en este caso debe ser de 7 hacia arriba
