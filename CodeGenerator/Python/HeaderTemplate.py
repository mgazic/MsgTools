#    <OUTPUTFILENAME>
#    Created <DATE> from:
#        Messages = <INPUTFILENAME>
#        Template = <TEMPLATEFILENAME>
#        Language = <LANGUAGEFILENAME>
#
#                     AUTOGENERATED FILE, DO NOT EDIT
import struct
import ctypes
from Messaging import Messaging
import Messaging as msg

class <MSGNAME> :
    SIZE = <MSGSIZE>
    FIELDINFOS = <FIELDINFOS>

    @staticmethod
    def Create() :
        bytes = ctypes.create_string_buffer(<MSGNAME>.SIZE)
        <INIT_CODE>
        return bytes

    @staticmethod
    def MsgName():
        return "<MSGNAME>"
    # Enumerations
    <ENUMERATIONS>
    # Accessors
    <ACCESSORS>
