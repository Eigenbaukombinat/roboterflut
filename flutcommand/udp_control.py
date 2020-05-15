import socket
from struct import pack



class UdpControl(object):
    """Driver base class for using an udp socket for sending commands to the bot."""
    def __init__(self, host, port):
            self.sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
            self.addr = (host, port)

    def send(self, cmd, val):
            packet = pack('ii', cmd, val)
            self.sock.sendto(packet, self.addr)

