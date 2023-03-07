import pylab as lab
import scipy.interpolate as inp

x= [0, 0.3, 0.5, 0.8, 1,  2,  3 ]
y= [0, 0.1, 0.5, 1,   3, 10, 30]

x= "0 0.3 0.5 0.8 1  2  3".split()
y= "0 0.1 0.5 1   3 10 30".split()

x = list(map(float,x))
y = list(map(float,y))
lab.plot(x,y, 'ro', label='původní hodnoty')

funkce = inp.CubicSpline(x, y)
newX = lab.linspace(0 , 3, 99)
newY = funkce(newX)
lab.plot(newX, newY, '-' ,label='CubicSpline')


#lab.plot(newX, inp.PchipInterpolator(x, y)(newX), label='PhipInterpolator')
#lab.plot(newX, inp.Akima1DInterpolator(x, y)(newX), label='Akima1DInterpolator')

lab.plot(newX, inp.UnivariateSpline(x, y, s=0)(newX), ':', label='UnivariateSpline s=0')
lab.plot(newX, inp.UnivariateSpline(x, y, s=1)(newX), 'x', label='UnivariateSpline s=3')
lab.plot(newX, inp.UnivariateSpline(x, y, s=5)(newX), '+', label='UnivariateSpline s=5')


lab.legend()
lab.grid(1)
lab.show()