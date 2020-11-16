import PySimpleGUI as sg
import math
from math import pi, cos, sqrt, sin, cosh, sinh
import numpy as np
import random
import matplotlib.pyplot as plt

# Criar janelas e layouts


class Tela:
    def janela_inicio():
        layout = [
            [sg.Text('Qual o tipo de estudo que deseja fazer?')],
            [sg.Radio('Ondas Regulares', 'tipo', key='regular', default=True), sg.Radio(
                'Ondas Irregulares', 'tipo', key='irregular')],
            [sg.Button('Continuar')],
        ]
        return sg.Window('Wave Kinematics', layout=layout, finalize=True)

    def janela_regular():
        layout = [
            [sg.Text('Insira o valor da altura da onda:'),
             sg.Input(size=(15, 0), key='altura')],
            [sg.Text('Insira o valor do período da onda:'),
                sg.Input(size=(15, 0), key='periodo')],
            [sg.Text('Insira o valor da profundidade da água:'),
                sg.Input(size=(15, 0), key='profundidade')],
            [sg.Text('Insira o valor da posição de onda:'),
                sg.Input(size=(15, 0), key='posicao')],
            [sg.Text('Insira o valor de tempo:'),
                sg.Input(size=(15, 0), key='tempo')],
            [sg.Text('Qual teoria de onda será usada?')],
            [sg.Radio('Airy', 'teoria', key='airy', default='True'),
                sg.Radio('Stokes', 'teoria', key='stokes')],
            [sg.Text('Deseja analisar as propriedades ao longo:')],
            [sg.Radio('do Tempo', 'tipo', key='choice_tempo', default='True'), sg.Radio(
                'da Profundidade', 'tipo', key='choice_profundidade')],
            [sg.Text('Assinale quais propriedades serão analisadas')],
            [sg.Checkbox('Velocidade Horizontal', key='vel_horizontal'), sg.Checkbox(
                'Velocidade Vertical', key='vel_vertical')],
            [sg.Checkbox('Aceleração Horizontal', key='ac_horizontal'), sg.Checkbox(
                'Aceleração Vertical', key='ac_vertical')],
            [sg.Button('Voltar'), sg.Button('Processar Dados')],
            [sg.Text('Resultados:')],
            # [sg.Output()]
        ]
        # janela
        return sg.Window('Wave Kinematics - Ondas Regulares', layout=layout, finalize=True)

    def janela_irregular():
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
            [sg.Button('Voltar'), sg.Button('Processar Dados')],
        ]
        return sg.Window('Wave Kinematics - Ondas Irregulares', layout=layout, finalize=True)

    # Criar janelas iniciais
    janela1, janela2, janela3 = janela_inicio(), None, None

    # Criar Loop de eventos
    while True:
        window, event, values = sg.read_all_windows()
        # Próxima Janela
        if window == janela1 and event == 'Continuar':
            if values['regular'] == True:
                janela2 = janela_regular()
                janela1.hide()
            elif values['irregular'] == True:
                janela3 = janela_irregular()
                janela1.hide()
            else:
                pass
        elif window == janela2 and event == 'Voltar':
            janela2.hide()
            janela1.un_hide()
        elif window == janela2 and event == 'Processar Dados':
            #def iniciar_regular(self):
                # Extrair dados da tela
                button, values = janela2.Read()
                H = float(values['altura'])
                T = float(values['periodo'])
                d = float(values['profundidade'])
                x = float(values['posicao'])
                t = float(values['tempo'])
                airy = values['airy']
                stokes = values['stokes']
                vel_horizontal = values['vel_horizontal']
                vel_vertical = values['vel_vertical']
                ac_horizontal = values['ac_horizontal']
                ac_vertical = values['ac_vertical']
                choice_tempo = values['choice_tempo']
                choice_profundidade = values['choice_profundidade']

                # Variaveis complementares
                g = 9.81
                W = ((4*(pi**2)*d)/(g*(T**2)))
                f = (1 + (0.666*W + 0.445*W**2 - 0.105*W**3 + 0.272*W**4))
                L = ((T*sqrt(g*d)*sqrt(f/(1+W*f))))
                k = (2*pi/L)
                w = (2*pi/T)
                c = (w/k)

                class Airy:
                    # Criar todos os cálculos necessários para o estudo de velocidade e aceleração
                    def vel_horizontal(self, t, g, k, H, w, z, d, c, x):
                        return (((g*k*H)/(2*w))*(cosh(k*(z+d))/cosh(k*d))*cos(k*(x-c*t)))

                    def vel_vertical(self, t, g, k, H, w, z, d, c, x):
                        return (((g*k*H)/(2*w))*(sinh(k*(z+d))/cosh(k*d))*sin(k*(x-c*t)))

                    def ac_horizontal(self, t, g, k, H, w, z, d, c, x):
                        return (((g*k*H)/(2))*(cosh(k*(z+d))/cosh(k*d))*sin(k*(x-c*t)))

                    def ac_vertical(self, t, g, k, H, w, z, d, c, x):
                        return -(((g*k*H)/(2))*(sinh(k*(z+d))/cosh(k*d))*cos(k*(x-c*t)))

                class Stokes:
                    # Criar todos os cálculos necessários para o estudo de velocidade e aceleração
                    def vel_horizontal_ordem1(self, t, g, k, H, T, w, z, d, c, x):
                        return ((((pi*H)/(T))*(cosh(k*(z+d))/sinh(k*d))*cos(k*(x-c*t))))

                    def vel_horizontal_ordem2(self, t, g, k, H, T, w, z, d, c, x):
                        return ((3/4*c)*(((pi*H)/T)**2)*((cosh(2*k*(z+d)))/((sinh(k*d))**4))*(cos(2*(k*(x-c*t)))))

                    def vel_horizontal(self, t, g, k, H, T, w, z, d, c, x):
                        u1hl = self.vel_horizontal_ordem1(t, g, k, H, T, w, z, d, c, x)
                        u2hl = self.vel_horizontal_ordem2(t, g, k, H, T, w, z, d, c, x)
                        return u1hl + u2hl

                    def vel_vertical_ordem1(self, t, g, k, H, T, w, z, d, c, x):
                        return (((pi*H)/(T))*(sinh(k*(z+d))/sinh(k*d))*sin(k*(x-c*t)))

                    def vel_vertical_ordem2(self, t, g, k, H, T, w, z, d, c, x):
                        return ((3/(4*c))*((pi*H/T)**2)*((sinh(2*k*(z+d))/(sinh(k*d)**4)))*(sin(2*k*(x - c*t))))

                    def vel_vertical(self, t, g, k, H, T, w, z, d, c, x):
                        v1hL = self.vel_vertical_ordem1(t, g, k, H, T, w, z, d, c, x)
                        v2hL = self.vel_vertical_ordem2(t, g, k, H, T, w, z, d, c, x)
                        return v1hL + v2hL

                    def ac_vertical_ordem1(self, t, g, k, H, T, w, z, d, c, L, x):
                        return (((2*(pi**2)*H)/(T**2))*((cosh(k*(z+d)))/(sinh(k*d)))*(sin(k*(x-c*t))))

                    def ac_vertical_ordem2(self, t, g, k, H, T, w, z, d, c, L, x):
                        return ((3*pi/(2*L))*(((pi*H)/(T))**2)*((cosh(2*k*(z+d))/((sinh(k*d))**4)))*(sin(2*(x - c*t))))

                    def ac_vertical(self, t, g, k, H, T, w, z, d, c, L, x):
                        A1uL = self.ac_vertical_ordem1(t, g, k, H, T, w, z, d, c, L, x)
                        A2uL = self.ac_vertical_ordem2(t, g, k, H, T, w, z, d, c, L, x)
                        return A1uL + A2uL

                    def ac_horizontal_ordem1(self, t, g, k, H, T, w, z, d, c, L, x):
                        return (-(((2*(pi**2)*H)/(T**2))*(sinh(k*(z+d))/sinh(k*d))*(cos(x-c*t))))

                    def ac_horizontal_ordem2(self, t, g, k, H, T, w, z, d, c, L, x):
                        return (-((3*pi/(2*L))*(((pi*H)/(T))**2)*((sinh(2*k*(z+d))/((sinh(k*d))**4)))*(cos(2*(x - c*t)))))

                    def ac_horizontal(self, t, g, k, H, T, w, z, d, c, L, x):
                        A1hL = self.ac_horizontal_ordem1(t, g, k, H, T, w, z, d, c, L, x)
                        A2hL = self.ac_horizontal_ordem2(t, g, k, H, T, w, z, d, c, L, x)
                        return A1hL + A2hL

                if airy == True and stokes == False:
                    # Calculo percentual das velocidades e acelerações
                    # Nomear variaveis de acordo com cada função criada, após isso criar as variáveis percentuais
                    wave1 = Airy()
                    uhL0 = wave1.vel_horizontal(
                        t, g, k, H, w, 0.0, d, c, x)
                    uhL2 = wave1.vel_horizontal(
                        t, g, k, H, w, -L/2, d, c, x)
                    uvL0 = wave1.vel_vertical(t, g, k, H, w, 0.0, d, c, x)
                    uvL2 = wave1.vel_vertical(t, g, k, H, w, -L/2, d, c, x)
                    AvL0 = wave1.ac_vertical(t, g, k, H, w, 0.0, d, c, x)
                    AvL2 = wave1.ac_vertical(t, g, k, H, w, -L/2, d, c, x)
                    AhL0 = wave1.ac_horizontal(t, g, k, H, w, 0.0, d, c, x)
                    AhL2 = wave1.ac_horizontal(
                        t, g, k, H, w, -L/2, d, c, x)

                    PVh = 100*(uhL2/uhL0)
                    PVv = 100*(uvL2/uvL0)
                    PAv = 100*(AvL2/AvL0)
                    PAh = 100*(AhL2/AhL0)
                    print(
                        f'Variáveis percentuais: \nVelocidade Horizontal: {PVh} \nVelocidade Vertical: {PVv} \nAceleração Horizontal: {PAh} \nAceleração Vertical: {PAv}')

                    # Criação de gráficos

                    if choice_tempo == True and choice_profundidade == False:
                        # Plotando ao longo do tempo

                        t1 = np.arange(0, 100, 1)
                        vel_horizontal_t = np.zeros(100)
                        vel_vertical_t = np.zeros(100)
                        ac_horizontal_t = np.zeros(100)
                        ac_vertical_t = np.zeros(100)
                        for i in t1:
                            vel_horizontal_t[i] = wave1.vel_horizontal(
                                i, g, k, H, w, 0, d, c, x)
                            vel_vertical_t[i] = wave1.vel_vertical(
                                i, g, k, H, w, 0, d, c, x)
                            ac_horizontal_t[i] = wave1.ac_horizontal(
                                i, g, k, H, w, 0, d, c, x)
                            ac_vertical_t[i] = wave1.ac_vertical(
                                i, g, k, H, w, 0, d, c, x)
                        plt.clf()
                        plt.title('Teoria de Airy')
                        if vel_horizontal == True:
                            plt.plot(t1, vel_horizontal_t, 'b',
                                     label='Velocidade Horizontal')
                        else:
                            pass
                        if vel_vertical == True:
                            plt.plot(t1, vel_vertical_t, 'g',
                                     label='Velocidade Vertical')
                        else:
                            pass
                        if ac_horizontal == True:
                            plt.plot(t1, ac_horizontal_t, 'r',
                                     label='Aceleração Horizontal')
                        else:
                            pass
                        if ac_vertical == True:
                            plt.plot(t1, ac_vertical_t, 'k',
                                     label='Aceleração Vertical')
                        else:
                            pass
                        plt.legend()
                        plt.grid()
                        plt.show()

                    else:
                        # Plotando ao longo da profundidade
                        z = int(d)
                        z1 = np.arange(0, z, 1)
                        vel_horizontal_z = np.zeros(z)
                        vel_vertical_z = np.zeros(z)
                        ac_horizontal_z = np.zeros(z)
                        ac_vertical_z = np.zeros(z)
                        for i in z1:
                            vel_horizontal_z[i] = wave1.vel_horizontal(
                                t, g, k, H, w, -i, d, c, x)
                            vel_vertical_z[i] = wave1.vel_vertical(
                                t, g, k, H, w, -i, d, c, x)
                            ac_horizontal_z[i] = wave1.ac_horizontal(
                                t, g, k, H, w, -i, d, c, x)
                            ac_vertical_z[i] = wave1.ac_vertical(
                                t, g, k, H, w, -i, d, c, x)
                        plt.clf()
                        plt.title('Teoria de Airy')
                        if vel_horizontal == True:
                            plt.plot(z1, vel_horizontal_z, 'b',
                                     label='Velocidade Horizontal')
                        else:
                            pass
                        if vel_vertical == True:
                            plt.plot(z1, vel_vertical_z, 'g',
                                     label='Velocidade Vertical')
                        else:
                            pass
                        if ac_horizontal == True:
                            plt.plot(z1, ac_horizontal_z, 'r',
                                     label='Aceleração Horizontal')
                        else:
                            pass
                        if ac_vertical == True:
                            plt.plot(z1, ac_vertical_z, 'k',
                                     label='Aceleração Vertical')
                        else:
                            pass
                        plt.legend()
                        plt.grid()
                        plt.show()

                elif airy == False and stokes == True:
                    # Calculo percentual das velocidades e acelerações
                    # Nomear variaveis de acordo com cada função criada, após isso criar as variáveis percentuais
                    wave2 = Stokes()
                    uthL0 = wave2.vel_horizontal(
                        t, g, k, H, T, w, 0, d, c, x)
                    uthL2 = wave2.vel_horizontal(
                        t, g, k, H, T, w, -L/2, d, c, x)
                    vthL0 = wave2.vel_vertical(
                        t, g, k, H, T, w, 0, d, c, x)
                    vthL2 = wave2.vel_vertical(
                        t, g, k, H, T, w, -L/2, d, c, x)
                    AtuL0 = wave2.ac_vertical(
                        t, g, k, H, T, w, 0, d, c, L, x)
                    AtuL2 = wave2.ac_vertical(
                        t, g, k, H, T, w, -L/2, d, c, L, x)
                    AthL0 = wave2.ac_horizontal(
                        t, g, k, H, T, w, 0, d, c, L, x)
                    AthL2 = wave2.ac_horizontal(
                        t, g, k, H, T, w, -L/2, d, c, L, x)
                    PsVh = 100*(uthL2/uthL0)
                    PsVv = 100*(vthL2/vthL0)
                    PsAv = 100*(AtuL2/AtuL0)
                    PsAh = 100*(AthL2/AthL0)
                    print(
                        f'Variáveis percentuais: \nVelocidade Horizontal: {PsVh} \n Velocidade Vertical: {PsVv} \n Aceleração Horizontal: {PsAh} \n Aceleração Vertical: {PsAv} ')

                    # Plotando o gráficos
                    if choice_tempo == True and choice_profundidade == False:
                        # Plotando ao longo do tempo
                        t1 = np.arange(0, 100, 1)
                        vel_horizontal_t = np.zeros(100)
                        vel_vertical_t = np.zeros(100)
                        ac_horizontal_t = np.zeros(100)
                        ac_vertical_t = np.zeros(100)
                        for i in t1:
                            vel_horizontal_t[i] = wave2.vel_horizontal(
                                i, g, k, H, T, w, 0, d, c, x)
                            vel_vertical_t[i] = wave2.vel_vertical(
                                i, g, k, H, T, w, 0, d, c, x)
                            ac_horizontal_t[i] = wave2.ac_horizontal(
                                i, g, k, H, T, w, 0, d, c, L, x)
                            ac_vertical_t[i] = wave2.ac_vertical(
                                i, g, k, H, T, w, 0, d, c, L, x)
                        plt.clf()
                        plt.title('Teria de Stokes')
                        if vel_horizontal == True:
                            plt.plot(t1, vel_horizontal_t, 'b',
                                     label='Velocidade Horizontal')
                        else:
                            pass
                        if vel_vertical == True:
                            plt.plot(t1, vel_vertical_t, 'g',
                                     label='Velocidade Vertical')
                        else:
                            pass
                        if ac_horizontal == True:
                            plt.plot(t1, ac_horizontal_t, 'r',
                                     label='Aceleração Horizontal')
                        else:
                            pass
                        if ac_vertical == True:
                            plt.plot(t1, ac_vertical_t, 'k',
                                     label='Aceleração Vertical')
                        else:
                            pass
                        plt.legend()
                        plt.grid()
                        plt.show()

                    else:
                        # Plotando ao longo da profundidade
                        z = int(d)
                        z1 = np.arange(0, z, 1)
                        vel_horizontal_z = np.zeros(z)
                        vel_vertical_z = np.zeros(z)
                        ac_horizontal_z = np.zeros(z)
                        ac_vertical_z = np.zeros(z)
                        for i in z1:
                            vel_horizontal_z[i] = wave2.vel_horizontal(
                                t, g, k, H, T, w, -i, d, c, x)
                            vel_vertical_z[i] = wave2.vel_vertical(
                                t, g, k, H, T, w, -i, d, c, x)
                            ac_horizontal_z[i] = wave2.ac_horizontal(
                                t, g, k, H, T, w, -i, d, c, L, x)
                            ac_vertical_z[i] = wave2.ac_vertical(
                                t, g, k, H, T, w, -i, d, c, L, x)
                        plt.clf()
                        plt.title('Teria de Stokes')
                        if vel_horizontal == True:
                            plt.plot(z1, vel_horizontal_z, 'b',
                                     label='Velocidade Horizontal')
                        else:
                            pass
                        if vel_vertical == True:
                            plt.plot(z1, vel_vertical_z, 'g',
                                     label='Velocidade Vertical')
                        else:
                            pass
                        if ac_horizontal == True:
                            plt.plot(z1, ac_horizontal_z, 'r',
                                     label='Aceleração Horizontal')
                        else:
                            pass
                        if ac_vertical == True:
                            plt.plot(z1, ac_vertical_z, 'k',
                                     label='Aceleração Vertical')
                        else:
                            pass
                        plt.legend()
                        plt.grid()
                        plt.show()

        elif window == janela3 and event == 'Voltar':
            janela3.hide()
            janela1.un_hide()
        elif window == janela3 and event == 'Processar Dados':
            #def iniciar_irregular(self):
                button, values = janela3.Read()
                H = float(values['altura'])
                Tp = float(values['periodo_pico'])
                d = float(values['profundidade'])
                choice_pm = values['pierson_moskowitz']
                choice_jonswap = values['jonswap']
                espectro = values['espectro']
                elevacao = values['elevacao']
                vel_horizontal = values['vel_horizontal']
                vel_vertical = values['vel_vertical']
                ac_horizontal = values['ac_horizontal']
                ac_vertical = values['ac_vertical']
                wp = (2*pi)/(Tp)
                wf = 5*wp
                y = 6.4*Tp**(-0.491)
                g = 9.81
                W = ((4*(pi**2)*d)/(g*(Tp**2)))
                f = (1 + (0.666*W + 0.445*W**2 - 0.105*W**3 + 0.272*W**4))
                L = ((Tp*sqrt(g*d)*sqrt(f/(1+W*f))))
                k = (2*pi/L)
                x = 4
                z = 0
                e = math.e
                pf = random.random()
                fi = (pf*2*pi)

                # Discretização do espectro de mar
                class PM:             
                    # Utilização das versões modificadas para facilitação de implementação
                    def espectro(self, H, wp, w):
                        return ((5/16)*(H**2)*((wp**4)/(w**5))*((math.e)**(-1.25*((w/wp)**(-4)))))

                    def amplitude(self, H, wp, w, dw):
                        #S = PM().espectro(H, wp, w)
                        S = self.espectro(H, wp, w)
                        return sqrt(2*S*dw)

                    def elevacao(self, H, w, t, k, x, fi, A):
                        # A = PM().amplitude(H, wp, w, dw)
                        return (A*(sin(w*t-k*x + fi)))

                    def vel_horizontal(self, H, w, k, z, t, x, fi, A):
                        # A = PM().amplitude(H, wp, w, dw)
                        return (A*w*((math.e)**(k*z))*(sin(w*t-k*x+fi)))

                    def vel_vertical(self, H, w, k, z, t, x, fi, A):
                        # A = PM().amplitude(H, wp, w, dw)
                        return (A*w*((math.e)**(k*z))*(cos(w*t-k*x+fi)))

                    def ac_horizontal(self, H, w, k, z, t, x, fi, A):
                        # A = PM().amplitude(H, wp, w, dw)
                        return (A*(w**2)*((math.e)**(k*z))*(cos(w*t-k*x+fi)))

                    def ac_vertical(self, H, w, k, z, t, x, fi, A):
                        # A = PM().amplitude(H, wp, w, dw)
                        return ((-1)*A*(w**2)*((math.e)**(k*z))*(sin(w*t-k*x+fi)))

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
                        # A = Jonswap().amplitude(H, wp, w, dw, y)
                        return (A*(sin(w*t-k*x + fi)))

                    def vel_horizontal(self, H, w, k, z, t, x, fi, A):
                        # A = Jonswap().amplitude(H, wp, w, dw, y)
                        return (A*w*((math.e)**(k*z))*(sin(w*t-k*x+fi)))

                    def vel_vertical(self, H, w, k, z, t, x, fi, A):
                        # A = Jonswap().amplitude(H, wp, w, dw, y)
                        return (A*w*((math.e)**(k*z))
                                * (cos(w*t-k*x+fi)))

                    def ac_horizontal(self, H, w, k, z, t, x, fi, A):
                        # A = Jonswap().amplitude(H, wp, w, dw, y)
                        return (A*(w**2)*((math.e)**(k*z))
                                * (cos(w*t-k*x+fi)))

                    def ac_vertical(self, H, w, k, z, t, x, fi, A):
                        # A = Jonswap().amplitude(H, wp, w, dw)
                        return ((-1)*A*(w**2)*((math.e)**(k*z))*(sin(w*t-k*x+fi)))

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
                        fi[j] = (random.random()*(2*pi))
                        amplitude_pm[j] = pierson_moskowitz.amplitude(
                            H, wp, i, 0.01)
                        W = ((4*(pi**2)*d)/(g*((1/i)**2)))
                        f = (1 + (0.666*W + 0.445*W **
                                  2 - 0.105*W**3 + 0.272*W**4))
                        L = ((Tp*sqrt(g*d)*sqrt(f/(1+W*f))))
                        k[j] = (2*pi/L)
                        j = j+1

                    # elevação, velocidades e acelerações
                    t1 = np.arange(0, 400, 1)
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
                    # espectro de energia
                    plt.clf()
                    plt.title('Pierson-Moskowitz')
                    if espectro == True:
                        plt.plot(dw, pm, 'brown', label='Espectro de Onda')
                    else:
                        pass
                    if elevacao == True:
                        plt.plot(t1, pm_elevacao, 'gray',
                                 label='Elevação de Superfíce')
                    else:
                        pass
                    if vel_horizontal == True:
                        plt.plot(t1, pm_vel_horizontal, 'b',
                                 label='Velocidade Horizontal')
                    else:
                        pass
                    if vel_vertical == True:
                        plt.plot(t1, pm_vel_vertical, 'g',
                                 label='Velocidade Vertical')
                    else:
                        pass
                    if ac_horizontal == True:
                        plt.plot(t1, pm_ac_horizontal, 'r',
                                 label='Aceleração Horizontal')
                    else:
                        pass
                    if ac_vertical == True:
                        plt.plot(t1, pm_ac_vertical, 'k',
                                 label='Aceleração Vertical')
                    else:
                        pass
                    plt.legend()
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
                        fi[j] = (random.random()*(2*pi))
                        amplitude_j[j] = jonswap.amplitude(
                            H, wp, i, 0.01, y)
                        W = ((4*(pi**2)*d)/(g*((1/i)**2)))
                        f = (1 + (0.666*W + 0.445*W **
                                  2 - 0.105*W**3 + 0.272*W**4))
                        L = ((Tp*sqrt(g*d)*sqrt(f/(1+W*f))))
                        k[j] = (2*pi/L)
                        j = j+1
                    # elevação, velocidades e acelerações
                    t1 = np.arange(0, 400, 1)
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
                            jonswap_ac_vertical[j] += jonswap.ac_vertical(
                                H, i, k[nwave], z, l, x, fi[nwave], amplitude_j[nwave])
                            nwave = nwave + 1
                        j = j+1
                    # plotagem dos gráficos
                    # espectro de energia
                    plt.clf()
                    plt.title('Jonswap')

                    if espectro == True:
                        plt.plot(dw, pm, 'brown', label='Espectro de Onda')
                    else:
                        pass

                    # elevacao, velocidades e acelerações
                    if elevacao == True:
                        plt.plot(t1, jonswap_elevacao, 'gray',
                                 label='Elevação de Superfíce')
                    else:
                        pass
                    if vel_horizontal == True:
                        plt.plot(t1, jonswap_vel_horizontal, 'b',
                                 label='Velocidade Horizontal')
                    else:
                        pass
                    if vel_vertical == True:
                        plt.plot(t1, jonswap_vel_vertical, 'g',
                                 label='Velocidade Vertical')
                    else:
                        pass
                    if ac_horizontal == True:
                        plt.plot(t1, jonswap_ac_horizontal, 'r',
                                 label='Aceleração Horizontal')
                    else:
                        pass
                    if ac_vertical == True:
                        plt.plot(t1, jonswap_ac_vertical, 'k',
                                 label='Aceleração Vertical')
                    else:
                        pass
                    plt.legend()
                    plt.grid()
                    plt.show()


tela = Tela()
