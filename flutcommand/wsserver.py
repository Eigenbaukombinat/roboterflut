from SimpleWebSocketServer import SimpleWebSocketServer, WebSocket
from rc_control import RCControl
from raspi_control import RaspiControl
from registry import BotRegistry
import sys

REGISTRY = BotRegistry()

REGISTRY.add_bot('nilo1', RaspiControl("192.168.0.98", 4210))



class SimpleEcho(WebSocket):

    def handleMessage(self):
        msg = self.data
        botname, cmd = msg.split(';')
        driver = REGISTRY.get_driver(botname)
        if driver is None:
            return
        val = int(cmd[1:])
        if cmd.startswith('t'):
            driver.motor(val)
        elif cmd.startswith('s'):
            driver.steer(val)


    def handleConnected(self):
        print(self.address, 'connected')

    def handleClose(self):
        print(self.address, 'closed')

print("Listening on port 16789...")
server = SimpleWebSocketServer('0.0.0.0', 16789, SimpleEcho)
server.serveforever()
