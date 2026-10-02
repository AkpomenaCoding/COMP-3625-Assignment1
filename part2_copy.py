import math
import time
from random import choice,randint, random
from translator import UniversalTranslator
from part1 import decode_rate

def cost(settings):
    return 1 - decode_rate(translator.translate(settings))

def simulated_annealing(f, start, n, T0, step): # f is a cost
    current_settings = start
    best_settings = current_settings

    for i in range(n) :
        T = T0 * (1 - i/n) # geometric approach to doing this
        if T <= 0:
            break

        next_settings = current_settings.copy()
        k = randint(0, len(next_settings) - 1) # my random successor
        next_settings[k] = round(max(0.0, min(1.0, next_settings[k] + choice([-step, step]))), 2)

        dE = f(next_settings) - f(current_settings)    # dE is delta E
        if dE < 0 or random() < math.exp(-dE/T):
            current_settings = next_settings
            if f(current_settings) < f(best_settings):
                best_settings = current_settings

    return best_settings

if __name__ == "__main__":

    # create the UniversalTranslator object, with 10 knobs
    translator = UniversalTranslator(n_dim=10)

    start = [round(random(), 2) for knob in range(10)]
    best = simulated_annealing(cost, start, n=500, T0=0.1, step=0.1)

    print(f'Final translation: {translator.translate(best)}')
    print(f'Decode rate: {1 - cost(best):.0%}')
    # print total number of settings evaluated
    print(f'# settings tried: {translator.n_settings_tried()}')