import PySimpleGUI as sg
import math
from math import pi, cos, sqrt, sin, cosh, sinh
import numpy as np
from numpy import ndim
import matplotlib.pyplot as plt


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
            [sg.Button('Processar dados')],
            # [sg.Output()]
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
            g = 9.81
            W = ((4*(pi**2)*d)/(g*(T**2)))
            f = (1 + (0.666*W + 0.445*W - 0.105*W + 0.272*W))
            L = ((T*sqrt(g*d)*sqrt(f/(1+W*f))))
            k = (2*pi/L)
            w = (2*pi/T)
            c = (w/k)
            lbd = L

            class Airy:
                # Criar todos os cálculos necessários para o estudo de velocidade e aceleração
                # Velocidade horizontal e vertical

                def airy_vel_horizontal(self, t, g, k, H, w, z, d, c, x):
                    return (((g*k*H)/(2*w))*(cosh(k*(z+d))/cosh(k*d))*cos(k*(x-c*t)))

                def airy_vel_vertical(self, t, g, k, H, w, z, d, c, x):
                    return (((g*k*H)/(2*w))*(sinh(k*(z+d))/cosh(k*d))*sin(k*(x-c*t)))

                # Aceleração horzontal e vertical
                def airy_ac_horizontal(self, t, g, k, H, w, z, d, c, x):
                    return (((g*k*H)/(2))*(cosh(k*(z+d))/cosh(k*d))*sin(k*(x-c*t)))

                def airy_ac_vertical(self, t, g, k, H, w, z, d, c, x):
                    return -(((g*k*H)/(2))*(sinh(k*(z+d))/cosh(k*d))*cos(k*(x-c*t)))

            class Stokes:
                # Criar todos os cálculos necessários para o estudo de velocidade e aceleração
                # Velocidade horizontal e vertical
                def stokes_vel_horizontal_ordem1(self, t, g, k, H, T, w, z, d, c, x):
                    return ((((pi*H)/(T))*(cosh(k*(z+d))/sinh(k*d))*cos(k*(x-c*t))))

                def stokes_vel_horizontal_ordem2(self, t, g, k, H, T, w, z, d, c, x):
                    return ((3/4*c)*(((pi*H)/T)**2)*((cosh(2*k*(z+d))) /
                                                     ((sinh(k*d))**4))*(cos(2*(k*(x-c*t)))))

                def stokes_vel_horizontal(self, t, g, k, H, T, w, z, d, c, x):
                    u1hl = Stokes().stokes_vel_horizontal_ordem1(t, g, k, H, T, w, z, d, c, x)
                    u2hl = Stokes().stokes_vel_horizontal_ordem2(t, g, k, H, T, w, z, d, c, x)
                    return u1hl + u2hl

                def stokes_vel_vertical_ordem1(self, t, g, k, H, T, w, z, d, c, x):
                    return (((pi*H)/(T))*(sinh(k*(z+d))/sin(k*d))*sin(k*(x-c*t)))

                def stokes_vel_vertical_ordem2(self, t, g, k, H, T, w, z, d, c, x):
                    return ((3/(4*c))*((pi*H/T)**2)*((sinh(2*k*(z+d))/(sinh(k*d)**4)*sin(2*k*(x - c*t)))))

                def stokes_vel_vertical(self, t, g, k, H, T, w, z, d, c, x):
                    v1hL = Stokes().stokes_vel_vertical_ordem1(t, g, k, H, T, w, z, d, c, x)
                    v2hL = Stokes().stokes_vel_vertical_ordem2(t, g, k, H, T, w, z, d, c, x)
                    return v1hL + v2hL

                # Acelerações Horizontais e verticais
                def stokes_ac_vertical_ordem1(self, t, g, k, H, T, w, z, d, c, lbd, x):
                    return (((2*(pi**2)*H)/(T**2))*((cosh(k*(z+d)))/(sinh(k*d)))*(sin(k*(x-c*t))))				
                def stokes_ac_vertical_ordem2(self, t, g, k, H, T, w, z, d, c, lbd, x):
                    return ((3*pi/(2*lbd))*(((pi*H)/(T))**2)*((cosh(2*k*(z+d))/((sinh(k*d))**4)))*(sin(2*(x - c*t))))				
                def stokes_ac_vertical(self, t, g, k, H, T, w, z, d, c, lbd, x):
                    A1uL = Stokes().stokes_ac_vertical_ordem1(t, g, k, H, T, w, z, d, c, lbd, x)
                    A2uL = Stokes().stokes_ac_vertical_ordem2(t, g, k, H, T, w, z, d, c, lbd, x)
                    return A1uL + A2uL

                def stokes_ac_horizontal_ordem1(self, t, g, k, H, T, w, z, d, c, lbd, x):
                    return (-(((2*(pi**2)*H)/(T**2))*(sinh(k*(z+d))/sinh(k*d))*(cos(x-c*t))))
                def stokes_ac_horizontal_ordem2(self, t, g, k, H, T, w, z, d, c, lbd, x):
                    return (-((3*pi/(2*lbd))*(((pi*H)/(T))**2)*((sinh(2*k*(z+d))/((sinh(k*d))**4)))*(cos(2*(x - c*t)))))
                def stokes_ac_horizontal(self, t, g, k, H, T, w, z, d, c, lbd, x):
                    A1hL = Stokes().stokes_ac_horizontal_ordem1(t, g, k, H, T, w, z, d, c, lbd, x)
                    A2hL = Stokes().stokes_ac_horizontal_ordem2(t, g, k, H, T, w, z, d, c, lbd, x)
                    return A1hL + A2hL



            if airy == True and stokes == False:
                # Calculo percentual das velocidades e acelerações
                # Nomear variaveis de acordo com cada função criada, após isso criar as variáveis percentuais
                wave1 = Airy()
                uhL0 = wave1.airy_vel_horizontal(t, g, k, H, w, 0.0, d, c, x)
                uhL2 = wave1.airy_vel_horizontal(t, g, k, H, w, -L/2, d, c, x)
                uvL0 = wave1.airy_vel_vertical(t, g, k, H, w, 0.0, d, c, x)
                uvL2 = wave1.airy_vel_vertical(t, g, k, H, w, -L/2, d, c, x)
                AvL0 = wave1.airy_ac_vertical(t, g, k, H, w, 0.0, d, c, x)
                AvL2 = wave1.airy_ac_vertical(t, g, k, H, w, -L/2, d, c, x)
                AhL0 = wave1.airy_ac_horizontal(t, g, k, H, w, 0.0, d, c, x)
                AhL2 = wave1.airy_ac_horizontal(t, g, k, H, w, -L/2, d, c, x)

                PVh = 100*(uhL2/uhL0)
                PVv = 100*(uvL2/uvL0)
                PAv = 100*(AvL2/AvL0)
                PAh = 100*(AhL2/AhL0)
                # Criação de gráficos
                #t1 = np.linspace(0, 1, 10)
                #plt.plot(uhL0(self, t1, g, k, H, w, 0, d, c), t1)
                # plt.show()
                
                # Criação de gráficos
                t2 = np.arange(0, 100, 1)
                vel_teste = np.zeros(100)
                for i in t2:
                    vel_teste[i] = wave1.airy_vel_horizontal(i, g, k, H, w, 0, d, c, x)
                plt.plot(t2, vel_teste)
                plt.show()
				

            else:
                # Calculo percentual das velocidades e acelerações
                # Nomear variaveis de acordo com cada função criada, após isso criar as variáveis percentuais
                wave2 = Stokes()
                uthL0 = wave2.stokes_vel_horizontal(t, g, k, H, T, w, 0, d, c, x)
                uthL2 = wave2.stokes_vel_horizontal(t, g, k, H, T, w, -L/2, d, c, x)
                vthL0 = wave2.stokes_vel_vertical(t, g, k, H, T, w, 0, d, c, x)
                vthL2 = wave2.stokes_vel_vertical(t, g, k, H, T, w, -L/2, d, c, x)
                AtuL0 = wave2.stokes_ac_vertical(t, g, k, H, T, w, 0, d, c, lbd, x)
                AtuL2 = wave2.stokes_ac_vertical(t, g, k, H, T, w, -L/2, d, c, lbd, x)
                AthL0 = wave2.stokes_ac_horizontal(t, g, k, H, T, w, 0, d, c, lbd, x)
                AthL2 = wave2.stokes_ac_horizontal(t, g, k, H, T, w, -L/2, d, c, lbd, x)

                PsVh = 100*(uthL2/uthL0)
                PsVv = 100*(vthL2/vthL0)
                PsAv = 100*(AtuL2/AtuL0)
                PsAh = 100*(AthL2/AthL0)

                #Plotando o gráfico da velocidade horizontal
                t2 = np.arange(0, 100, 1)
                vel_teste = np.zeros(100)
                for i in t2:
                    vel_teste[i] = wave2.stokes_vel_horizontal(i, g, k, H, T, w, 0, d, c, x)
                plt.plot(t2, vel_teste)
                plt.show()
				


tela = Tela()
tela.iniciar()
