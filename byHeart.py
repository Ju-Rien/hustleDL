#! /usr/bin/env python3

import sys

def main():
    wgt = 0.0
    alpha = 0.1
    eps = 1e-8

    x = 2
    y = 0.8

    err = 1
    for iteration in range(50):
        pred = wgt * x
        delta = pred - y
        err = delta ** 2
        step = 2 * delta * x # Derivative of the error function
        wgt = wgt - alpha * step

        print("Error: " + str(err) + " Pred: " + str(pred))

        if err < eps:
            break

if __name__ == "__main__":
    main()
