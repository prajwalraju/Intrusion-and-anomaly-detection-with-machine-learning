import socket

def send_command(command, host, port):
    try:
        
        client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        client_socket.connect((host, port))
        client_socket.send(command.encode())
        output = client_socket.recv(1024).decode()
        print(output)
        client_socket.close()
    except Exception as e:
        print(str(e))

# Example usage
# send_command('ls', '127.0.0.1', 9991)

bots = [
    {'host': '127.0.0.1', 'port': 9991},
    {'host': '127.0.0.1', 'port': 9992}
]

command = 'ls -all'
for bot in bots:
    host = bot['host']
    port = bot['port']
    send_command(command, host, port)