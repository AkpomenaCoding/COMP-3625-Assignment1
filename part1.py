from random import choice, randint, random

from translator import UniversalTranslator

# This does not take int account split words and punctuation marks
def decode_rate(translated_string):
    words = translated_string.split()
    translated_words = 0

    for word in words:
        if not word.isnumeric():
            translated_words += 1

    return translated_words / len(words)


# create the UniversalTranslator object, with 2 knobs
translator = UniversalTranslator(n_dim=2)

# demo of how to use the UniversalTranslator object. You can delete these lines
# need to initialize best to something rabdomely

#best_settings = [0, 0]
#sample_settings = [0.9, 0.3]

#translated_string = translator.translate(sample_settings)
#print(translated_string)


# decode rate: words translated / total words in the message


# hill-climbing for the maximum decode rate and minimizing finding optimal settings 
# this will be done through starting each knob at a random value, 
# and then iteratively adjusting each knob to find the best setting for that knob, 
# while keeping the other knobs fixed. This will be repeated until no further improvements can be made.

def decode_hill_climb(translator: UniversalTranslator, num_knobs: int, num_steps: int) -> tuple[list, float]:
    
    best_settings = [round(random(), 1) for setting in range(num_knobs)]
    best_trans_string = translator.translate(best_settings)
    best_dec_rate = decode_rate(best_trans_string)

    for step in range(num_steps):
        curr_settings = best_settings.copy()
        knob = randint(0, num_knobs - 1)
        curr_settings[knob] += choice([-0.1, 0.1])
        curr_settings[knob] = round(curr_settings[knob], 1)
        curr_settings[knob] = max(0.0, min(1.0, curr_settings[knob]))
        
        curr_trans_string = translator.translate(curr_settings)
        curr_dec_rate = decode_rate(curr_trans_string)

        if curr_dec_rate > best_dec_rate:
            best_settings = curr_settings
            best_dec_rate = curr_dec_rate
        print(f'Step {step + 1}: Current settings: {curr_settings}, decode rate: {curr_dec_rate:.0%}')
    
    return best_settings, best_dec_rate

# create the UniversalTranslator object, with 2 knobs
translator = UniversalTranslator(n_dim=2)

result = decode_hill_climb(translator, num_knobs=2, num_steps=2000)

# print the reults
print(f'Final translation: {translator.translate(result[0])}')
print(f'Final result: {result[0]}, decode rate: {result[1]:.0%}')

# print total number of settings evaluated
print(f'# settings tried: {translator.n_settings_tried()}')