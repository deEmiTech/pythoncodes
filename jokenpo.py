from random import choice
from time import sleep

print('{:=^40}'.format('PEDRA PAPEL TESOURA'))

comp = choice(['pedra', 'papel', 'tesoura'])
jog = int(input('''ja escolhi, agora e sua vez.
	[1] pedra
	[2] papel
	[3] tesoura
	sua opcao:'''))

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

print('{:=^40}'.format('QUEM É QUEM'))
sleep(0.35)
print('JO')
sleep(0.5)
print('KEN')
sleep(0.35)
print('PO')
sleep(1)
print('computador:',comp,'\njogador:',jog)
sleep(3)
print('{:=^40}'.format('O GRANDE VENCEDOR'))
print(win)
sleep(7)
