#!/usr/bin/env python


"""

Rayed Alrashed  2013-10-09

AgentX sub agent library

To help debugging run snmpd in foreground debug mode:
sudo /usr/sbin/snmpd -f -Lsd  -Dagentx -Le -u snmp -g snmp -I -smux -p /var/run/snmpd.pid


snmpget  -v2c -c public localhost .1.3.6.1.3.9999.100.1.0
snmpwalk -v2c -c public localhost .1.3.6.1.3.9999.100

"""

import logging

import agentx
from agentx.pdu import PDU
from agentx.agent import Agent



class MyAgent(Agent):

    def setup(self):
        self.register('1.3.6.1.3.9999.100', self.update)
        self.register('1.3.6.1.3.9999.200', self.update2, 10)

    def update(self):
        self.append('1.3.6.1.3.9999.100.1.0', agentx.TYPE_COUNTER32, 1000)
        self.append('1.3.6.1.3.9999.100.2.0', agentx.TYPE_COUNTER32, 2000)
        self.append('1.3.6.1.3.9999.100.3.0', agentx.TYPE_OCTETSTRING, "Hola Dora")

    def update2(self):
        self.append('1.3.6.1.3.9999.200.1.0', agentx.TYPE_COUNTER32, 1000)
        self.append('1.3.6.1.3.9999.200.2.0', agentx.TYPE_COUNTER32, 2000)
        self.append('1.3.6.1.3.9999.200.3.0', agentx.TYPE_OCTETSTRING, "Hola Dora")


def setup_login():
    logger = logging.getLogger('agentx')
    logger.setLevel(logging.DEBUG)
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    ch = logging.StreamHandler()
    ch.setLevel(logging.DEBUG)
    ch.setFormatter(formatter)
    logger.addHandler(ch)

def main():
    setup_login()
    a = MyAgent()
    a.start()


if __name__=="__main__":
    main()