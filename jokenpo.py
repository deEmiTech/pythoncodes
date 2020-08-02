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

if jog == comp:
	win = 'empate'
elif jog =='pedra' and comp == 'tesoura' or jog == 'papel' and comp == 'pedra' or jog == 'tesoura' and comp == 'papel':
	win = 'jogador'
elif comp =='pedra' and jog == 'tesoura' or comp == 'papel' and jog == 'pedra' or comp == 'tesoura' and jog == 'papel':
	win = 'computador'	
print('computador:',comp,'jogador:',jog)
sleep(1)
print(win)
sleep(3)


