import subprocess
from iocbuilder import Device, AutoSubstitution,Device,Xml
from iocbuilder.modules.streamDevice import AutoProtocol
from iocbuilder.arginfo import *


class _d2tsfTemplate(AutoSubstitution):
    TemplateFile = "d2tsf.db"


class d2tsf(Device, AutoProtocol):
    ## Parse this template file for macros
    ProtocolFiles = ['d2tsf.proto']

    def __init__(self, name, device, STREAMS_PORT):
        self.name = name
        self.device = device
        self.STREAMS_PORT = STREAMS_PORT

        _d2tsfTemplate(device=self.device, STREAMS_PORT=self.STREAMS_PORT)

    ArgInfo = makeArgInfo(__init__,
        name = Simple("name", str),
        device = Simple("PV prefix", str),
        STREAMS_PORT = Ident("Asyn Port", str)
    )
