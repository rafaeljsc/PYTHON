import os
import time
import ctypes
os.system('cls||clear')

work = int(input("Foco(min): "))
rest = int(input("Pausa(min): "))

def pomodoro(min,action):
    while(min > 0):
        os.system('cls||clear')
        print(f'Faltam {min} minuto(s) para {action}.')
        time.sleep(60)
        min-=1    
    print(f'{action.upper()}!')
    ctypes.windll.user32.MessageBoxW(0, 'Momento de ' + action + '.', 'Pomodoro', 64)

while(True):
    pomodoro(work,'pausa') #minutos até a pausa (tempo focado)
    pomodoro(rest,'retornar') #minutos até o retorno (tempo de descanso)