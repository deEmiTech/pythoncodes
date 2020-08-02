from random import choice
from time import sleep

comp = choice(['pedra', 'papel', 'tesoura'])
jog = int(input('''ja escolhi, agora e sua vez.
	[1] pedra
	[2] papel
	[3] tesoura
	[sua opcao]'''))


if jog == 1:
	jog = 'pedra'
elif jog == 2:
	jog = 'papel'
elif jog == 3:
	jog = 'tesoura'	
print('computador:',comp,'jogador',jog)
sleep(1)