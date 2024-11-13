import socket

# Configuración del servidor
HOST = '127.0.0.1'
PORT = 5000

def iniciar_servidor():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server_socket:
        server_socket.bind((HOST, PORT))
        server_socket.listen()
        print(f"Servidor TCP escuchando en {HOST}:{PORT}")

        while True:
            # Conexión del cliente
            client_socket, client_address = server_socket.accept()
            print(f"Conexión establecida con {client_address}")
            with client_socket:
                while True:
                    # Recibir mensaje del cliente
                    data = client_socket.recv(1024)
                    if not data:
                        break

                    mensaje = data.decode()
                    print(f"Cliente envía: {mensaje}")

                    # Mensaje de "hola servidor"
                    if mensaje.lower() == "hola servidor":
                        respuesta = "HOLA CLIENTE"
                    elif mensaje == "DESCONEXION":
                        print("Cerrando conexión con el cliente")
                        break
                    else:
                        # Responder con el mensaje en mayúsculas por defecto
                        respuesta = mensaje.upper()
                    
                    # Enviar respuesta al cliente
                    client_socket.sendall(respuesta.encode())
                    print(f"Servidor responde: {respuesta}")

if __name__ == "__main__":
    iniciar_servidor()
