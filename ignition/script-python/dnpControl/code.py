DEVICE = "SEL-751"

PULSE_ON  = 1

TCC = 0
COUNT = 1

PULSE_MS = 2000

def pulse(dnp, index):
	return dnp.directOperateBinary(DEVICE, index, TCC, PULSE_ON, COUNT, PULSE_MS, PULSE_MS)