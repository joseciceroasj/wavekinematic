import math
from math import pi, sin, sqrt, cos
import random
import numpy as np
import pandas as pd


class Jonswap:
    def __init__(self, profundidade, altura, periodo, qtdondas, x, z):
        self.d = profundidade
        self.H = altura
        self.Tp = periodo
        self.nOndas = qtdondas
        self.x = x
        self.z = z
        self.g = 9.81
        self.wp = (2*pi/self.Tp)
        self.wi = 0.01
        self.wf = 5*self.wp
        self.dw = (self.wf - self.wi)/self.nOndas
        self.w = np.arange(self.wi, self.wf, self.dw)
        self.y = 6.4*self.Tp**(-0.491)
        self.e = math.e
        self.k = np.zeros(self.w.size)
        self.fi = np.zeros(self.w.size)
        self.A = np.zeros(self.w.size)
        self.T = np.zeros(self.w.size)
        self.T = 2*pi/self.w
        self.L = np.zeros(self.w.size)
        self.jp = np.zeros(self.w.size)
        j = 0
        for i in self.w:
            self.jp[j] = self.espectro(i)
            self.fi[j] = (random.random()*(2*pi))
            self.A[j] = self.amplitude(i, 0.01)
            W = ((4*(pi**2)*self.d)/(self.g*((1/i)**2)))
            f = (1 + (0.666*W + 0.445*W ** 2 - 0.105*W**3 + 0.272*W**4))
            self.L[j] = ((self.T[j]*sqrt(self.g*self.d)*sqrt(f/(1+W*f))))
            self.k[j] = (2*pi/self.L[j])
            j = j+1

        # Guardando dados no excel
        espectro_valores = {'Frequência': self.w, 'Energia': self.jp}
        excel_espectro = pd.DataFrame(espectro_valores)
        excel_espectro.to_excel('espectro_jp.xlsx')

    def espectro(self, w):
        # definição do fator de forma (sig) para o espectro de jonswap
        if w <= self.wp:
            sig = 0.07
        else:
            sig = 0.09
        return ((5/16)*(self.H**2)*(self.Tp)*((self.wp**4)/(w**5))*((self.e)**(-1.25*((w/self.wp)**(-4))))*(1-0.287*(math.log(self.y)))*(self.y**((self.e)**(-((w-self.wp)**2)/(2*(sig**2)*(self.wp**2))))))

    def amplitude(self, w, dw):
        S = self.espectro(w)
        return sqrt(2*S*dw)

    def elevacao(self, w, t, A, nwave):
        return (A*(sin(w*t-self.k[nwave]*self.x + self.fi[nwave])))

    def vel_horizontal(self, w, t, A, nwave):
        return (A*w*((self.e)**(self.k[nwave]*self.z))*(sin(w*t-self.k[nwave]*self.x + self.fi[nwave])))

    def vel_vertical(self, w, t, A, nwave):
        return (A*w*((self.e)**(self.k[nwave]*self.z))*(cos(w*t-self.k[nwave]*self.x+self.fi[nwave])))

    def ac_horizontal(self, w, t, A, nwave):
        return (A*(w**2)*((self.e)**(self.k[nwave]*self.z))*(cos(w*t-self.k[nwave]*self.x+self.fi[nwave])))

    def ac_vertical(self, w, t, A, nwave):
        return ((-1)*A*(w**2)*((self.e)**(self.k[nwave]*self.z))*(sin(w*t-self.k[nwave]*self.x+self.fi[nwave])))
