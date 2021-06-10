#!/usr/bin/python3.8

# Description: Program that connects dots from a list of coordinate points
# Author: Ricardo Augusto Teixeira Barbosa

import argparse
import matplotlib.pyplot as plt
import numpy as np
import os
import sys
from matplotlib.backend_bases import MouseButton

show_dots = False
data = []

def plot_graph(show_dots):
    global data
    plt.close()
    plt.figure(figsize=(20,20)) # must set figsize before plotting it
    x, y = data.T

    if (show_dots):
        plt.plot(*data.T, marker=".", linewidth=3, markersize=30, markerfacecolor='red', color='blue')
    else:
        plt.plot(*data.T, linewidth=3)
    
    plt.gca().invert_yaxis()
    plt.axis('equal')
    plt.connect('button_press_event', on_click)
    plt.show()

def on_click(event):
    global show_dots
    if event.button is MouseButton.LEFT:
        show_dots = not show_dots # toggle
        plot_graph(show_dots)

def parse_args():

    parser = argparse.ArgumentParser(description = "Connect dots from  'X Y' coordinate list", \
    epilog = "Usage: python connect_dots.py --input <filename>")
    parser.add_argument("--input", required=True, metavar="<input_file>",
        type=str, help="file with coordinate list")
    args = parser.parse_args()

    if not os.path.exists(args.input):
        raise Exception ("Error: input file does not exist")

    return args

def main():
    global data
    args = parse_args()
    
    try:
        data = np.loadtxt(args.input)
    except:
        print("Unexpected error while file with coordinates")
    
    plot_graph(show_dots)

if __name__ == "__main__":
    sys.exit(main())
