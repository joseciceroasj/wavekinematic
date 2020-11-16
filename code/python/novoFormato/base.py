import PySimpleGUI as sg
import math
from math import pi, cos, sqrt, sin, cosh, sinh
import numpy as np
import matplotlib.pyplot as plt

from airy import Airy

class Tela:
    def __init__(self):
        # layout
        layout = [
            [sg.Text('Insira o valor da altura da onda:'),
             sg.Input(size=(15, 0), key='altura')],
            [sg.Text('Insira o valor do período da onda:'), sg.Input(
                size=(15, 0), key='periodo')],
            [sg.Text('Insira o valor da Profundidade da água:'), sg.Input(
                size=(15, 0), key='profundidade')],
            [sg.Text('Insira o valor da posição de onda:'), sg.Input(
                size=(15, 0), key='posicao')],
            [sg.Text('Insira o valor de tempo:'), sg.Input(
                size=(15, 0), key='tempo')],
            [sg.Text('Qual teoria de onda você vai usar?')],
            [sg.Radio('Airy', 'teoria', key='airy', default='True'),
             sg.Radio('Stokes', 'teoria', key='stokes')],
            [sg.Text('As propriedades serão analisadas ao longo:')],
            [sg.Radio('Do Tempo', 'tipo', key='choice_tempo', default='True'), sg.Radio(
                'Da Profundidade', 'tipo', key='choice_profundidade')],
            [sg.Text('Selecione qual propriedade será analisada')],
            [sg.Checkbox('Velocidade Horizontal', key='vel_horizontal'), sg.Checkbox(
                'Velocidade Vertical', key='vel_vertical'), sg.Checkbox('Aceleração Horizontal', key='ac_horizontal'), sg.Checkbox('Aceleração Vertical', key='ac_vertical')],
            [sg.Button('Processar dados')],
            #[sg.Output()]
        ]
        # janela
        self.janela = sg.Window('Wave Kinematics').layout(layout)
    def iniciar(self):
        while True:
            # Extrair dados da tela
            self.button, self.values = self.janela.Read()
            H = float(self.values['altura'])
            T = float(self.values['periodo'])
            d = float(self.values['profundidade'])
            x = float(self.values['posicao'])
            t = float(self.values['tempo'])
            airy = self.values['airy']
            stokes = self.values['stokes']
            vel_horizontal = self.values['vel_horizontal']
            vel_vertical = self.values['vel_vertical']
            ac_horizontal = self.values['ac_horizontal']
            ac_vertical = self.values['ac_vertical']
            choice_tempo = self.values['choice_tempo']
            choice_profundidade = self.values['choice_profundidade']
            
            print('Entrou no While true')
            
            if airy == True and stokes == False:
                # Calculo percentual das velocidades e acelerações
                # Nomear variaveis de acordo com cada função criada, após isso criar as variáveis percentuais
                wave1 = Airy(d,H,T)
                uhL0 = wave1.VelHorizontal(t, x, 0.0)
                uhL2 = wave1.VelHorizontal(t, x, -wave1.L/2)
                #uhL0 = wave1.airy_vel_horizontal(t, g, k, H, w, 0.0, d, c, x)
                #uhL2 = wave1.airy_vel_horizontal(t, g, k, H, w, -L/2, d, c, x)
                uvL0 = wave1.VelVertical(t, x, 0.0)
                uvL2 = wave1.VelVertical(t, x, -wave1.L/2)
                #uvL0 = wave1.airy_vel_vertical(t, g, k, H, w, 0.0, d, c, x)
                #uvL2 = wave1.airy_vel_vertical(t, g, k, H, w, -L/2, d, c, x)
                #AvL0 = wave1.airy_ac_vertical(t, g, k, H, w, 0.0, d, c, x)
                #AvL2 = wave1.airy_ac_vertical(t, g, k, H, w, -L/2, d, c, x)
                #AhL0 = wave1.airy_ac_horizontal(t, g, k, H, w, 0.0, d, c, x)
                #AhL2 = wave1.airy_ac_horizontal(t, g, k, H, w, -L/2, d, c, x)
                PVh = 100*(uhL2/uhL0)
                PVv = 100*(uvL2/uvL0)
                #PAv = 100*(AvL2/AvL0)
                #PAh = 100*(AhL2/AhL0)
                print(PVh)
                print(PVv)
                print(
                    f'Variáveis percentuais: \nVelocidade Horizontal: {PVh} \nVelocidade Vertical: {PVv}')
                    #f'Variáveis percentuais: \nVelocidade Horizontal: {PVh} \nVelocidade Vertical: {PVv} \nAceleração Horizontal: {PAh} \nAceleração Vertical: {PAv}')
                # Criação de gráficos
                if choice_tempo == True and choice_profundidade == False:
                    # Plotando ao longo do tempo
                    t1 = np.arange(0, 100, 1)
                    vel_airy_horizontal_t = np.zeros(100)
                    vel_airy_vertical_t = np.zeros(100)
                    ac_airy_horizontal_t = np.zeros(100)
                    ac_airy_vertical_t = np.zeros(100)
                    for i in t1:
                        vel_airy_horizontal_t[i] = wave1.VelHorizontal(i, x, 0.0)
                        vel_airy_vertical_t[i] = wave1.VelVertical(i, x, 0.0)
                    plt.clf()
                    plt.title('Teoria de Airy')
                    if vel_horizontal == True:
                        plt.plot(t1, vel_airy_horizontal_t, 'b', label='Velocidade Horizontal')
                    else:
                        pass
                    if vel_vertical == True:
                        plt.plot(t1, vel_airy_vertical_t, 'g', label='Velocidade Vertical')
                    else:
                        pass
#                    if ac_horizontal == True:
#                        plt.plot(t1, ac_airy_horizontal_t, 'r', label='Aceleração Horizontal')
#                    else:
#                        pass
#                    if ac_vertical == True:
#                        plt.plot(t1, ac_airy_vertical_t, 'k', label='Aceleração Vertical')
                    #else:
                    #    pass
                    plt.legend()
                    plt.show()
#                else:
#                    # Plotando ao longo da profundidade
#                    z = int(d)
#                    z1 = np.arange(0, z, 1)
#                    vel_airy_horizontal_z = np.zeros(z)
#                    vel_airy_vertical_z = np.zeros(z)
#                    ac_airy_horizontal_z = np.zeros(z)
#                    ac_airy_vertical_z = np.zeros(z)
#                    for i in z1:
#                        vel_airy_horizontal_z[i] = wave1.airy_vel_horizontal(
#                            t, g, k, H, w, -i, d, c, x)
#                        vel_airy_vertical_z[i] = wave1.airy_vel_vertical(
#                            t, g, k, H, w, -i, d, c, x)
#                        ac_airy_horizontal_z[i] = wave1.airy_ac_horizontal(
#                            t, g, k, H, w, -i, d, c, x)
#                        ac_airy_vertical_z[i] = wave1.airy_ac_vertical(
#                            t, g, k, H, w, -i, d, c, x)
#                    plt.clf()
#                    plt.title('Teoria de Airy')
#                    if vel_horizontal == True:
#                        plt.plot(z1, vel_airy_horizontal_z, 'b', label='Velocidade Horizontal')
#                    else:
#                        pass
#                    if vel_vertical == True:
#                        plt.plot(z1, vel_airy_vertical_z, 'g', label='Velocidade Vertical')
#                    else:
#                        pass
#                    if ac_horizontal == True:
#                        plt.plot(z1, ac_airy_horizontal_z, 'r', label='Aceleração Horizontal')
#                    else:
#                        pass
#                    if ac_vertical == True:
#                        plt.plot(z1, ac_airy_vertical_z, 'k', label='Aceleração Vertical')
#                    else:
#                        pass
#                    plt.legend()
#                    plt.show()
#            elif airy == False and stokes == True:
#                # Calculo percentual das velocidades e acelerações
#                # Nomear variaveis de acordo com cada função criada, após isso criar as variáveis percentuais
#                wave2 = Stokes()
#                uthL0 = wave2.stokes_vel_horizontal(
#                    t, g, k, H, T, w, 0, d, c, x)
#                uthL2 = wave2.stokes_vel_horizontal(
#                    t, g, k, H, T, w, -L/2, d, c, x)
#                vthL0 = wave2.stokes_vel_vertical(t, g, k, H, T, w, 0, d, c, x)
#                vthL2 = wave2.stokes_vel_vertical(
#                    t, g, k, H, T, w, -L/2, d, c, x)
#                AtuL0 = wave2.stokes_ac_vertical(
#                    t, g, k, H, T, w, 0, d, c, L, x)
#                AtuL2 = wave2.stokes_ac_vertical(
#                    t, g, k, H, T, w, -L/2, d, c, L, x)
#                AthL0 = wave2.stokes_ac_horizontal(
#                    t, g, k, H, T, w, 0, d, c, L, x)
#                AthL2 = wave2.stokes_ac_horizontal(
#                    t, g, k, H, T, w, -L/2, d, c, L, x)
#                PsVh = 100*(uthL2/uthL0)
#                PsVv = 100*(vthL2/vthL0)
#                PsAv = 100*(AtuL2/AtuL0)
#                PsAh = 100*(AthL2/AthL0)
#                print(
#                    f'Variáveis percentuais: \nVelocidade Horizontal: {PsVh} \n Velocidade Vertical: {PsVv} \n Aceleração Horizontal: {PsAh} \n Aceleração Vertical: {PsAv} ')
#                # Plotando o gráficos
#                if choice_tempo == True and choice_profundidade == False:
#                    # Plotando ao longo do tempo
#                    t1 = np.arange(0, 100, 1)
#                    vel_stokes_horizontal_t = np.zeros(100)
#                    vel_stokes_vertical_t = np.zeros(100)
#                    ac_stokes_horizontal_t = np.zeros(100)
#                    ac_stokes_vertical_t = np.zeros(100)
#                    for i in t1:
#                        vel_stokes_horizontal_t[i] = wave2.stokes_vel_horizontal(
#                            i, g, k, H, T, w, 0, d, c, x)
#                        vel_stokes_vertical_t[i] = wave2.stokes_vel_vertical(
#                            i, g, k, H, T, w, 0, d, c, x)
#                        ac_stokes_horizontal_t[i] = wave2.stokes_ac_horizontal(
#                            i, g, k, H, T, w, 0, d, c, L, x)
#                        ac_stokes_vertical_t[i] = wave2.stokes_ac_vertical(
#                            i, g, k, H, T, w, 0, d, c, L, x)
#                    plt.clf()
#                    plt.title('Teria de Stokes')
#                    if vel_horizontal == True:
#                        plt.plot(t1, vel_stokes_horizontal_t, 'b', label='Velocidade Horizontal')
#                    else:
#                        pass
#                    if vel_vertical == True:
#                        plt.plot(t1, vel_stokes_vertical_t, 'g', label='Velocidade Vertical')
#                    else:
#                        pass
#                    if ac_horizontal == True:
#                        plt.plot(t1, ac_stokes_horizontal_t, 'r', label='Aceleração Horizontal')
#                    else:
#                        pass
#                    if ac_vertical == True:
#                        plt.plot(t1, ac_stokes_vertical_t, 'k', label='Aceleração Vertical')
#                    else:
#                        pass
#                    plt.legend()
#                    plt.show()
#                else:
#                    # Plotando ao longo da profundidade
#                    z = int(d)
#                    z1 = np.arange(0, z, 1)
#                    vel_stokes_horizontal_z = np.zeros(z)
#                    vel_stokes_vertical_z = np.zeros(z)
#                    ac_stokes_horizontal_z = np.zeros(z)
#                    ac_stokes_vertical_z = np.zeros(z)
#                    for i in z1:
#                        vel_stokes_horizontal_z[i] = wave2.stokes_vel_horizontal(
#                            t, g, k, H, T, w, -i, d, c, x)
#                        vel_stokes_vertical_z[i] = wave2.stokes_vel_vertical(
#                            t, g, k, H, T, w, -i, d, c, x)   
#                        ac_stokes_horizontal_z[i] = wave2.stokes_ac_horizontal(
#                            t, g, k, H, T, w, -i, d, c, L, x)
#                        ac_stokes_vertical_z[i] = wave2.stokes_ac_vertical(
#                            t, g, k, H, T, w, -i, d, c, L, x)
#                    plt.clf()
#                    plt.title('Teria de Stokes')
#                    if vel_horizontal == True:
#                        plt.plot(z1, vel_stokes_horizontal_z, 'b', label='Velocidade Horizontal')
#                    else:
#                        pass
#                    if vel_vertical == True:
#                        plt.plot(z1, vel_stokes_vertical_z, 'g', label='Velocidade Vertical')
#                    else:
#                        pass
#                    if ac_horizontal == True:
#                        plt.plot(z1, ac_stokes_horizontal_z, 'r', label='Aceleração Horizontal')
#                    else:
#                        pass
#                    if ac_vertical == True:
#                        plt.plot(z1, ac_stokes_vertical_z, 'k', label='Aceleração Vertical')
#                    else:
#                        pass
#                    plt.legend()
#                    plt.show()
tela = Tela()
tela.iniciar()