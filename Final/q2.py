import numpy
def f(x):
    return x**2 + 3*x + 4

def make_derivative(func,dx):
    top_term = func(dx) - func
    return top_term/dx
    

def main():


    fprime = make_derivative(f,0.0001)
    for i in range(6):
        x = 0.5 * i
        print("%6.2f %6.2f %6.2f" % (x, f(x), fprime(x)))

if __name__ == '__main__':
    main()