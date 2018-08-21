
import os
import struct

########################################################################    
## extractHeader(start, size, ifile, ofile):
#  \param self self
#  \param pos where to start reading the header
#  \param ifile the input ROM file
#  \param ofile the output header file
#
########################################################################
def extractHeader(start, size, ifile, ofile):
    try:
        os.remove(ofile)
    except OSError:
        pass
        
    with open(ofile, "wb+") as fwrite:
        with open(ifile, "rb") as fread:
            fread.seek(start, 0)
            readBytes = fread.read(size)
            fwrite.write(readBytes)

def getrom(mode):
    if mode == 'gen':
        return genesis.genesis()
    elif mode == 'sms':
        return sms.sms()
    elif mode == 'snes':
        return snes.snes()

    return None

########################################################################    
## byteSwap(self, ifile, ofile):
#  \param self self
#  \param ifile
#  \param ofile
#
########################################################################
def byteSwap(ifile, ofile):
    
    fileSize = os.path.getsize(ifile)
    pos = 0
    
    try:
        os.remove(ofile)
    except OSError:
        pass
        
    with open(ofile, "wb+") as fwrite:
        with open(ifile, "rb") as fread:
            while(pos < fileSize):  
                badEndian = fread.read(2)
                revEndian = struct.pack('<h', *struct.unpack('>h', badEndian))
                fwrite.write(revEndian)
                pos += 2


from . import genesis, sms, snes
