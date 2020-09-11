import numpy as np
import numpy.linalg as linalg


class Mankiw:
    r"""
    \bar{Y_{t}}: Natural Level output
    \pi_{t}^{*}: Central bank target for inflation
    \alpha: The responsiveness of the demand for goods and services to the real interest rate
    \rho: The natural rate of interest
    \Phi: The responsiveness of inflation to output in the Phillips curve
    \theta_{\pi}: The responsiveness of the nominal interest rate minus the inflation in the monetary-policy rule
    \theta_{Y}: The responsiveness of the nominal interest rate output output in the monetary-policy rule
    \pi_{t-1}: predetermined lagged inflation rate
    """
    _eps: int

    def __init__(self, Yt_bar=100, pi_t_star=2., alpha=1., rho=2., phi=.25, theta_pi=.5, theta_y=.5, eps=0, v=0):
        self._Yt_bar, self._pi_t_star, self._alpha, \
        self._rho, self._phi, self._theta_pi, \
        self._theta_y = Yt_bar, pi_t_star, alpha, rho, phi, theta_pi, theta_y
        self._eps, self._v = eps, v
        self._lag_pi = pi_t_star

    # Each time we change phi, we update A
    @property
    def A(self):
        phi, theta_y, theta_pi, alpha = self._phi, self._theta_y, self._theta_pi, self._alpha
        ############### [Yt, rt, pi_t, Et, it]
        AA = np.array ([[1, alpha, 0, 0, 0],
                        [0, 1, 0, 1, -1],
                        [-phi, 0, 1, 0, 0],
                        [0, 0, -1, 1, 0],
                        [-theta_y, 0, -(1 + theta_pi), 0, 1]
                        ])
        return AA

    # Calculate Constant Vector b
    @property
    def b(self):
        rho, pi_t_star, phi, theta_y, theta_pi = self._rho, self._pi_t_star, self._phi, self._theta_y, self._theta_pi
        Yt_bar = self._Yt_bar
        alpha = self._alpha
        eps, v = self._eps, self._v
        lag_pi = self._lag_pi
        b = np.array ([[Yt_bar + alpha * rho + eps],
                       [0],
                       [lag_pi - phi * Yt_bar + v],
                       [0],
                       [rho - theta_pi * pi_t_star - theta_y * Yt_bar]
                       ])
        return b

    def update(self):
        pi_t_star: float
        pi_t_star, phi, eps, v, alpha, theta_pi, theta_y = self._pi_t_star, self._phi, self._eps, \
                                                           self._v, self._alpha, self._theta_pi, self._theta_y
        lag_pi = self._lag_pi

        # self._lag_pi = (lag_pi + (phi * alpha * theta_pi / (1 + alpha * theta_y)) * pi_t_star - eps / (
        #         1 + alpha * theta_y) + v) / (1 + phi * alpha * theta_pi / (1 + alpha * theta_y))
        self._lag_pi = (lag_pi+phi*alpha*theta_pi*pi_t_star/(1+alpha*theta_y)+phi*eps/(1+alpha*theta_y)+v)/(
                1+phi*alpha*theta_pi/(1+alpha*theta_y))

    def cal_steady(self):
        return linalg.solve (self.A, self.b)

    def simulate_path(self, t):
        epsilon = np.zeros (t)
        epsilon[3:8] = self._eps
        v = np.zeros (t)
        v[3] = self._v
        y, r, pi, e_pi, i = [], [], [], [], []
        paths = [epsilon, v, y, r, pi, e_pi, i]


        for i in range (t):
            self._eps = epsilon[i]
            self._v = v[i]
            s = self.cal_steady ()
            for j in range (2, len (paths)):
                paths[j].append (s[j - 2][0])

            self.update ()

        return paths
