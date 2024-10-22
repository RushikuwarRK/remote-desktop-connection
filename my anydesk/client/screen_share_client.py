import socket
import pickle
import struct
import cv2

# Client setup
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host_ip = 'SERVER_IP_ADDRESS'  # Replace with server IP
port = 9999
client_socket.connect((host_ip, port))

data = b""
payload_size = struct.calcsize("Q")

while True:
    while len(data) < payload_size:
        packet = client_socket.recv(4*1024)  # Receive data in chunks
        if not packet: break
        data += packet
    
    # Unpack frame size
    packed_msg_size = data[:payload_size]
    data = data[payload_size:]
    msg_size = struct.unpack("Q", packed_msg_size)[0]
    
    while len(data) < msg_size:
        data += client_socket.recv(4*1024)
    
    # Deserialize frame data
    frame_data = data[:msg_size]
    data = data[msg_size:]
    
    # Convert back to numpy array
    frame = pickle.loads(frame_data)
    
    # Show the frame using OpenCV
    cv2.imshow("Screen Sharing", frame)
    
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

client_socket.close()
