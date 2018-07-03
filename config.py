# Air Quality Sensing

# credentials
APP_EUI = ''
APP_KEY = ''
NWK_KEY = ''
APP_SWKEY = ''
DEV_ADDR = ''

# max number of connection attemps to TTN
MAX_JOIN_ATTEMPT = const(50)
INT_SAMPLING = 10    # number of sec between each reading
# number of packets to be transmit with the same data  (retries)
# default is 3
N_TX = const(0)

# data rate used to send message via LoRaWAN:
# 1 (slowest - longest range) to 4 (fastest - smallest range)
DATA_RATE = const(4)