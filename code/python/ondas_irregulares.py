import PySimpleGUI as sg
import math
from math import pi, sin, sqrt, cos
# import random
import numpy as np
import matplotlib.pyplot as plt


class Tela:
    def __init__(self):
        layout = [
            [sg.Text('Insira o valor da altura significativa da onda:'),
             sg.Input(size=(15, 0), key='altura')],
            [sg.Text('Insira o valor do período de pico da onda:'),
             sg.Input(size=(15, 0), key='periodo_pico')],
            [sg.Text('Insira o valor da profundidade da água:'),
             sg.Input(size=(15, 0), key='profundidade')],
            [sg.Text('Qual tipo de espectro de onda será analisado:')],
            [sg.Radio('Pierson-Moskowitz', 'espectro', key='pierson_moskowitz', default=True),
             sg.Radio('Jonswap', 'espectro', key='jonswap')],
            [sg.Text('Assinale quais propriedades serão analisadas')],
            [sg.Checkbox('Espectro de Energia', key='espectro'), sg.Checkbox(
                'Elevacao de Superfície', key='elevacao')],
            [sg.Checkbox('Velocidade Horizontal', key='vel_horizontal'), sg.Checkbox(
                'Velocidade Vertical', key='vel_vertical')],
            [sg.Checkbox('Aceleração Horizontal', key='ac_horizontal'), sg.Checkbox(
                'Aceleração Vertical', key='ac_vertical')],
            [sg.Button('Processar dados')],
            # [sg.Output()]
        ]
        # janela
        self.janela = sg.Window('Ondas Irregulares').layout(layout)

    def iniciar(self):
        while True:
            # Extrair dados da tela
            self.button, self.values = self.janela.Read()
            H = float(self.values['altura'])
            Tp = float(self.values['periodo_pico'])
            d = float(self.values['profundidade'])
            choice_pm = self.values['pierson_moskowitz']
            choice_jonswap = self.values['jonswap']
            espectro = self.values['espectro']
            elevacao = self.values['elevacao']
            vel_horizontal = self.values['vel_horizontal']
            vel_vertical = self.values['vel_vertical']
            ac_horizontal = self.values['ac_horizontal']
            ac_vertical = self.values['ac_vertical']
            wp = (2*pi)/(Tp)
            wf = 5*wp
            y = 6.4*Tp**(-0.491)
            g = 9.81
            W = ((4*(pi**2)*d)/(g*(Tp**2)))
            f = (1 + (0.666*W + 0.445*W**2 - 0.105*W**3 + 0.272*W**4))
            L = ((Tp*sqrt(g*d)*sqrt(f/(1+W*f))))
            k = (2*pi/L)
            x = 0
            z = 0
            pf = np.random.random((1, 1))
            fi = (pf*2*pi)

            # Discretização do espectro de mar

            class PM:
                # Utilização das versões modificadas para facilitação de implementação
                def espectro(self, H, wp, w):
                    return ((5/16)*(H**2)*((wp**4)/(w**5))*((math.e)**(-1.25*((w/wp)**(-4)))))

                def amplitude(self, H, wp, w, dw):
                    S = PM().espectro(H, wp, w)
                    return sqrt(2*S*dw)

                def elevacao(self, H, w, t, k, x, fi, A):
                    # A = PM().amplitude(H, dw, wp)
                    return (A*(sin(w*t-k*x + fi)))

                def vel_horizontal(self, H, w, k, z, t, x, fi, A):
                    # A = PM().amplitude(H, dw, wp)
                    return (A*w*((math.e)**(k*z))*(sin(w*t-k*x+fi)))

                def vel_vertical(self, H, w, k, z, t, x, fi, A):
                    # A = PM().amplitude(H, dw, wp)
                    return (A*w*((math.e)**(k*z))*(cos(w*t-k*x+fi)))

                def ac_horizontal(self, H, w, k, z, t, x, fi, A):
                    # A = PM().amplitude(H, dw, wp)
                    return (A*(w**2)*((math.e)**(k*z))*(cos(w*t-k*x+fi)))

                def ac_vertical(self, H, w, k, z, t, x, fi, A):
                    # A = PM().amplitude(H, dw, wp)
                    return (-A*(w**2)*((math.e)**(k*z))*(sin(w*t-k*x+fi)))

            class Jonswap:
                def espectro(self, H, wp, w, y):
                    # definição do fator de forma (sig) para o espectro de jonswap
                    if w <= wp:
                        sig = 0.07
                    else:
                        sig = 0.09
                    return ((5/16)*(H**2)*((wp**4)/(w**5))*((math.e)**(-1.25*((w/wp)**(-4))))*(1-0.287*(math.log(y)))*(y**((math.e)**(-((w-wp)**2)/(2*(sig**2)*(wp**2))))))

                def amplitude(self, H, wp, w, dw, y):
                    S = Jonswap().espectro(H, wp, w, y)
                    return sqrt(2*S*dw)

                def elevacao(self, H, w, t, k, x, fi, A):
                    # A = Jonswap().amplitude(H, dw, wp, y)
                    return (A*(sin(w*t-k*x + fi)))

                def vel_horizontal(self, H, w, k, z, t, x, fi, A):
                    # A = Jonswap().amplitude(H, dw, wp, y)
                    return (A*w*((math.e)**(k*z))*(sin(w*t-k*x+fi)))

                def vel_vertical(self, H, w, k, z, t, x, fi, A):
                    # A = Jonswap().amplitude(H, dw, wp, y)
                    return (A*w*((math.e)**(k*z))
                            * (cos(w*t-k*x+fi)))

                def ac_horizontal(self, H, w, k, z, t, x, fi, A):
                    # A = Jonswap().amplitude(H, dw, wp, y)
                    return (A*(w**2)*((math.e)**(k*z))
                            * (cos(w*t-k*x+fi)))

                def ac_vertical(self, H, w, k, z, t, x, fi, A):
                    # A = Jonswap().amplitude(H, dw, wp, y)
                    return (-A*(w**2)*((math.e)**(k*z))
                            * (sin(w*t-k*x+fi)))

            if choice_pm == True and choice_jonswap == False:
                # Gráfico do Espectro de onda x frequencia
                pierson_moskowitz = PM()
                wf = 5*(wp)
                dw = np.arange(0.01, wf, 0.01)
                pm = np.zeros(dw.size)
                fi = np.zeros(dw.size)
                amplitude_pm = np.zeros(dw.size)
                k = np.zeros(dw.size)
                j = 0
                for i in dw:
                    pm[j] = pierson_moskowitz.espectro(H, wp, i)
                    fi[j] = (np.random.random((1, 1)))*(2*pi)
                    amplitude_pm[j] = pierson_moskowitz.amplitude(
                        H, wp, i, 0.01)
                    W = ((4*(pi**2)*d)/(g*((1/i)**2)))
                    f = (1 + (0.666*W + 0.445*W**2 - 0.105*W**3 + 0.272*W**4))
                    L = ((Tp*sqrt(g*d)*sqrt(f/(1+W*f))))
                    k[j] = (2*pi/L)
                    j = j+1
                    
                # elevação, velocidades e acelerações
                t1 = np.arange(0, 100, 1)
                pm_elevacao = np.zeros(t1.size)
                pm_vel_horizontal = np.zeros(t1.size)
                pm_vel_vertical = np.zeros(t1.size)
                pm_ac_horizontal = np.zeros(t1.size)
                pm_ac_vertical = np.zeros(t1.size)
                j = 0
                for l in t1:
                    nwave = 0
                    for i in dw:

                        pm_elevacao[j] += pierson_moskowitz.elevacao(
                            H, i, l, k[nwave], x, fi[nwave], amplitude_pm[nwave])
                        pm_vel_horizontal[j] += pierson_moskowitz.vel_horizontal(
                            H, i, k[nwave], z, l, x, fi[nwave], amplitude_pm[nwave])
                        pm_vel_vertical[j] += pierson_moskowitz.vel_vertical(
                            H, i, k[nwave], z, l, x, fi[nwave], amplitude_pm[nwave])
                        pm_ac_horizontal[j] += pierson_moskowitz.ac_horizontal(
                            H, i, k[nwave], z, l, x, fi[nwave], amplitude_pm[nwave])
                        pm_ac_vertical[j] += pierson_moskowitz.ac_vertical(
                            H, i, k[nwave], z, l, x, fi[nwave], amplitude_pm[nwave])
                        nwave = nwave + 1
                    j = j + 1
                # plotagem dos gráficos
                plt.clf()
                # espectro de energia
                if espectro == True:
                    plt.plot(dw, pm)
                else:
                    pass

                # elevacao, velocidades e acelerações
                if elevacao == True:
                    plt.plot(t1, pm_elevacao)
                else:
                    pass
                if vel_horizontal == True:
                    plt.plot(t1, pm_vel_horizontal)
                else:
                    pass
                if vel_vertical == True:
                    plt.plot(t1, pm_vel_vertical)
                else:
                    pass
                if ac_horizontal == True:
                    plt.plot(t1, pm_ac_horizontal)
                else:
                    pass
                if ac_vertical == True:
                    plt.plot(t1, pm_ac_vertical)
                else:
                    pass
                plt.grid()
                plt.show()

            else:
                # Gráfico do Espectro de onda x frequencia
                jonswap = Jonswap()
                wf = 5*(wp)
                dw = np.arange(0.01, wf, 0.01)
                jp = np.zeros(dw.size)
                fi = np.zeros(dw.size)
                amplitude_j = np.zeros(dw.size)
                k = np.zeros(dw.size)
                j = 0
                for i in dw:
                    jp[j] = jonswap.espectro(H, wp, i, y)
                    fi[j] = (np.random.random((1, 1)))*(2*pi)
                    amplitude_j[j] = jonswap.amplitude(H, wp, i, 0.01, y)
                    W = ((4*(pi**2)*d)/(g*((1/i)**2)))
                    f = (1 + (0.666*W + 0.445*W**2 - 0.105*W**3 + 0.272*W**4))
                    L = ((Tp*sqrt(g*d)*sqrt(f/(1+W*f))))
                    k[j] = (2*pi/L)
                    j = j+1

                t1 = np.arange(0, 100, 1)
                jonswap_elevacao = np.zeros(t1.size)
                jonswap_vel_horizontal = np.zeros(t1.size)
                jonswap_vel_vertical = np.zeros(t1.size)
                jonswap_ac_horizontal = np.zeros(t1.size)
                jonswap_ac_vertical = np.zeros(t1.size)
                j = 0
                for l in t1:
                    nwave = 0
                    for i in dw:
                        jonswap_elevacao[j] += jonswap.elevacao(
                            H, i, l, k[nwave], x, fi[nwave], amplitude_j[nwave])
                        jonswap_vel_horizontal[j] += jonswap.vel_horizontal(
                            H, i, k[nwave], z, l, x, fi[nwave], amplitude_j[nwave])
                        jonswap_vel_vertical[j] += jonswap.vel_vertical(
                            H, i, k[nwave], z, l, x, fi[nwave], amplitude_j[nwave])
                        jonswap_ac_horizontal[j] += jonswap.ac_horizontal(
                            H, i, k[nwave], z, l, x, fi[nwave], amplitude_j[nwave])
                        jonswap_ac_horizontal[j] += jonswap.ac_vertical(
                            H, i, k[nwave], z, l, x, fi[nwave], amplitude_j[nwave])
                        nwave = nwave + 1
                    j = j+1
                # plotagem dos gráficos
                plt.clf()
                # espectro de energia
                if espectro == True:
                    plt.plot(dw, pm)
                else:
                    pass

                # elevacao, velocidades e acelerações
                if elevacao == True:
                    plt.plot(t1, jonswap_elevacao)
                else:
                    pass
                if vel_horizontal == True:
                    plt.plot(t1, jonswap_vel_horizontal)
                else:
                    pass
                if vel_vertical == True:
                    plt.plot(t1, jonswap_vel_vertical)
                else:
                    pass
                if ac_horizontal == True:
                    plt.plot(t1, jonswap_ac_horizontal)
                else:
                    pass
                if ac_vertical == True:
                    plt.plot(t1, jonswap_ac_vertical)
                else:
                    pass
                plt.grid()
                plt.show()


tela = Tela()
tela.iniciar()
