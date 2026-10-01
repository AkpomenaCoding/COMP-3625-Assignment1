from translator import UniversalTranslator
from matplotlib import pyplot as plt
import numpy as np

# create the UniversalTranslator object, with 2 knobs
translator = UniversalTranslator(n_dim=2)
sample_settings = np.random.rand(18, 2) # this line needs to go and be replaced by the algorithm
setting_scores = []

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

"""
    function name: plot_decode_rate
    params: settings, decode_rate
    description: plots the graph of settings against their decode rates 
    Adapted from Eric's code from the assignment google doc
"""

# given settings: a Nx2 array of N setting combinations
# and decode_rate: a length-N array of decode rates corresponding to those settings

def plot_decode_rate(settings, decode_rate):
    # generate a scatter plot
    plt.scatter(x=settings[:, 0],
            y=settings[:, 1],
            c=decode_rate,
            vmin=0, vmax=1
            )

# add colorbar and gridlines
    cbar = plt.colorbar(label="decode rate")
    plt.grid()

# add labels
    plt.xlabel('knob 0 setting')
    plt.ylabel('knob 1 setting')
    plt.title('decode rates for settings tried')

# display
    plt.show()

for s in sample_settings:
    translated_string = translator.translate(s)
    rate = decode_rate(translated_string)
    setting_scores.append(rate)
    print(f"The decode rate for this setting {s} is: {rate:.3f}") 
    
# print total number of settings evaluated
print(f'# settings tried: {translator.n_settings_tried()}')

plot_decode_rate(sample_settings, setting_scores)