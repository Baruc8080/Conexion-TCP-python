import socket

# Configuración del cliente
HOST = '127.0.0.1'
PORT = 5000

def iniciar_cliente():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client_socket:
        client_socket.connect((HOST, PORT))
        print(f"Conectado al servidor en {HOST}:{PORT}")

        while True:
            
            mensaje = input("Ingrese un mensaje (o 'DESCONEXION' para salir): ")

            # Enviar el mensaje al servidor
            client_socket.sendall(mensaje.encode())

            # Verificar el mensaje "DESCONEXION"
            if mensaje == "DESCONEXION":
                print("Cerrando conexión con el servidor")
                break

            # Recibir respuesta del servidor
            data = client_socket.recv(1024)
            print(f"Respuesta del servidor: {data.decode()}")

if __name__ == "__main__":
    iniciar_cliente()
