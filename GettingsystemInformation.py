import platform

pMachine = platform.machine()
pSystem = platform.system()
pProcessor = platform.processor()
if pMachine == 'AMD64':
	print 'Machine : 64 Bit'
print 'System :', pSystem
print 'Processor:', pProcessor