from random import choice, randint, random
from random import choice
import translator

"""
    function name: decorate rate 
    params: translated_string
    description: takes the string that has been translated and returns the percentage of that string are words
                words are seen the success in the string.
"""

def decode_rate(translated_string):
    tokens = translated_string.split()
    words = [t for t in tokens if not t.isdigit()]

    rate = len(words)/len(tokens)
    
    return rate

# decode rate: words translated / total words in the message
# hill-climbing for the maximum decode rate and minimizing finding optimal settings 
# this will be done through starting each knob at a random value, 
# and then iteratively adjusting each knob to find the best setting for that knob, 
# while keeping the other knobs fixed. This will be repeated until no further improvements can be made.


# This function is just for 2 knobs, will make a new one that is for the general case of n knobs, and will be able to handle any number of knobs. bin = binary
def decode_hill_climb_bin(translator: translator.UniversalTranslator, num_knobs: int, num_steps: int) -> tuple[list, float]:
    # need to add random functionality sfter a few runs to search in different locations
    best_settings = [round(random(), 1) for setting in range(num_knobs)]
    best_trans_string = translator.translate(best_settings)
    best_dec_rate = decode_rate(best_trans_string)

    for step in range(num_steps):
        curr_settings = best_settings.copy()
        knob = randint(0, num_knobs - 1)
        curr_settings[knob] += choice([-0.01, 0.01])
        curr_settings[knob] = round(curr_settings[knob], 2)
        curr_settings[knob] = max(0.0, min(1.0, curr_settings[knob]))
        
        curr_trans_string = translator.translate(curr_settings)
        curr_dec_rate = decode_rate(curr_trans_string)

        if curr_dec_rate > best_dec_rate:
            best_settings = curr_settings
            best_dec_rate = curr_dec_rate
        print(f'Step {step + 1}: Current settings: {curr_settings}, decode rate: {curr_dec_rate:.0%}')
    
    return best_settings, best_dec_rate


# Generalized version for the hill climbing algorithm that can handle any number of knobs.
def decode_hill_climb(translator: translator.UniversalTranslator, num_knobs: int, num_steps: int) -> tuple[list, float]:
    # Initialize the best settings with random values for each knob
    best_settings = [round(random(), 1) for setting in range(num_knobs)]
    best_trans_string = translator.translate(best_settings)
    best_dec_rate = decode_rate(best_trans_string)

    for step in range(num_steps):
        curr_settings = best_settings.copy()
        knob = randint(0, num_knobs - 1)
        curr_settings[knob] += choice([-0.01, 0.01])
        curr_settings[knob] = round(curr_settings[knob], 2)
        curr_settings[knob] = max(0.0, min(1.0, curr_settings[knob]))
        
        curr_trans_string = translator.translate(curr_settings)
        curr_dec_rate = decode_rate(curr_trans_string)

        if curr_dec_rate > best_dec_rate:
            best_settings = curr_settings
            best_dec_rate = curr_dec_rate
        print(f'Step {step + 1}: Current settings: {curr_settings}, decode rate: {curr_dec_rate:.0%}')
    
    return best_settings, best_dec_rate    

