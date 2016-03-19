import socket
import time
import psutil

soket_udp = socket.socket(socket.AF_INET, socket.SOCK_DGRAM);
alamat_server = ('localhost', 8080)
penyimpanan = psutil.virtual_memory()
memory = penyimpanan.percent
cpu = psutil.cpu_percent()

for i in range(10):
	soket_udp.sendto("("+ time.ctime()+")"+" "+"CPU = "+str(cpu)+"%"+" "+"MEMORY = "+str(memory)+"%"+" ", alamat_server)
	proses,dari_server = soket_udp.recvfrom(2048)
	print proses
	time.sleep(1)
soket_udp.close()