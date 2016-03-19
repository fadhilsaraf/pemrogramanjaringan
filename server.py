import socket

soket_udp = socket.socket(socket.AF_INET, socket.SOCK_DGRAM);
alamat_feeder = ('', 8080)
soket_udp.bind(alamat_feeder)

while True:
    try:
        proses, dari_feeder = soket_udp.recvfrom(2048)
        print dari_feeder, " ", proses
        soket_udp.sendto(proses +"", dari_feeder)
    except KeyboardInterrupt:
        break
soket_udp.close()
