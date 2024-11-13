Cliente y Servidor TCP en Python

Este proyecto implementa un servidor y un cliente TCP en Python que se comunican a través de un puerto en localhost. El objetivo es permitir la interacción entre el cliente y el servidor para enviar y recibir mensajes de manera simple en este pequeño ejercicio.

Objetivo

1. El servidor escucha conexiones en localhost en el puerto 5000.
2. El cliente se conecta al servidor y envía mensajes.
3. Si el cliente envía el mensaje "hola servidor", el servidor responde "HOLA CLIENTE".
4. Para cualquier otro mensaje, el servidor responde con el mensaje en mayúsculas.
5. Si el cliente envía el mensaje "DESCONEXION", el servidor cierra la conexión con el cliente.

Archivos del Proyecto

servidor_tcp.py: Script que implementa el servidor TCP.

cliente_tcp.py: Script que implementa el cliente TCP.

Instrucciones de Ejecución

1. Ejecutar el Servidor

En una terminal, ejecuta el servidor con el 
siguiente comando: python servidor_tcp.py

El servidor comenzará a escuchar conexiones en 127.0.0.1:5000.

2. Ejecutar el Cliente

En otra terminal, ejecuta el cliente con el 
siguiente comando: python cliente_tcp.py

El cliente intentará conectarse al servidor en 127.0.0.1:5000.

Pruebas Manuales

Mensaje Regular:
En el cliente, escriba un mensaje como hola servidor y verifica que el servidor responde con "HOLA CLIENTE".

Mensaje de Desconexión:
En el cliente, escriba DESCONEXION y verifica que el servidor y el cliente cierren la conexión correctamente.

Autor
Baruc López - Ejercicio Técnico en Python