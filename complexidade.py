velocidade = 61 #velocidade atual do carro 
local_carro = 90

RADAR_1 = 61 #velocidade maxima do radar 1
LOCAL_1 = 100 #local onde o radar 1 está 
RADAR_RANGE = 1 # a distancia onde o radar pega 

vel_carro_pass_radar_1 = velocidade > RADAR_1

if vel_carro_pass_radar_1:
    print("Velocidade carro passou do radar 1")

if local_carro >= (LOCAL_1 - RADAR_RANGE) and \
   local_carro <= (LOCAL_1 + RADAR_RANGE) and \
    vel_carro_pass_radar_1:
  print('Carro multado em radar 1')
