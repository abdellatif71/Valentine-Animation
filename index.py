#!/usr/bin/env/ python3

import random
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import matplotlib.patheffects as path_effects  # Explicit import of path_effects
import matplotlib  # Import matplotlib to use its functionality

# Set the backend to TkAgg to avoid the non-interactive warning
matplotlib.use('TkAgg')

class Valentine:
    def __init__(self):
        self.seed = 69
        self.message_hash = 0x53454e44204e5544553
        self.fig, self.ax = plt.subplots()

    def generate_pattern(self):
        num_dots = 143
        x = np.zeros(num_dots)
        y = np.zeros(num_dots)
        colors = []
        for j in range(num_dots):
            self.seed = (1103515245 * self.seed + 12345) % 2**31
            x[j] = self.seed / 2**31 * 10
            self.seed = (1103515245 * self.seed + 12345) % 2**31
            y[j] = self.seed / 2**31 * 10
            colors.append(f"#{random.randint(0, 0xFFFFFF):06x}")
        return x, y, colors

    def display_message(self):
        message = ""
        message_hash = self.message_hash
        for i in range(10):
            char_code = message_hash & 0xFF
            message = chr(char_code) + message
            message_hash >>= 8
        return message

    def animate(self, i):
        self.ax.clear()
        self.ax.set_xlim(0, 10)
        self.ax.set_ylim(0, 10)
        if i < 100:
            x, y, colors = self.generate_pattern()
            for j in range(len(x)):
                self.ax.plot(x[j], y[j], 'o', markersize=4, color=colors[j])
        else:
            message = self.display_message()
            alpha = 1 - (i - 100) / 100  # Fading effect
            self.ax.text(5, 5, message, fontsize=48, ha='center', va='center', color='white', alpha=alpha, 
                         path_effects=[path_effects.withStroke(linewidth=2, foreground='yellow')])

    def run(self):
        ani = animation.FuncAnimation(self.fig, self.animate, frames=200, interval=50)
        plt.show()

this_instance = Valentine()
this_instance.run()
