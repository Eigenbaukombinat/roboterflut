from udp_control import UdpControl


STEER_SCALE = 0.1 


class RaspiControl(UdpControl):
    def steer(self, value):
            # 0-180
            # 90 means center
            # map -200-200 to 0-180
            val = int((180/400.0) * (200-value)) 
            # invert because picture is also inverted
            val = 180-val
            # scale
            # val = int((val * STEER_SCALE) + (90*(1-STEER_SCALE)))
            if val > 180:
                val = 180
            if val < 0:
                val = 0
            self.send(2, val)

    def motor(self, value):
            # 0-180
            # 90 means center
            # map -200-200 to 0-180
            val = int((180/400.0) * (200-value)) 
            # invert because picture is also inverted
            val = 180-val
            
            if val > 180:
                val = 180
            if val < 0:
                val = 0
            print(val)
            self.send(1, val)

