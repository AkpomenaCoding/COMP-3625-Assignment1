import time
from translator import UniversalTranslator
import numpy as np
from part1 import decode_hill_climb

# use time function to calculate how long it takes to run the code
start_time = time.time()
end_time = start_time + 60


# create the UniversalTranslator object, with 10 knobs
translator = UniversalTranslator(n_dim=10)


    # demo of how to use the UniversalTranslator object. You can delete these lines
result = decode_hill_climb(translator, num_knobs=10, num_steps=500, improvement_judge=100)

    # print the reults
print(f'Final translation: {translator.translate(result[0])}')
print(f'Final result: {result[0]}, decode rate: {result[1]:.0%}')
    
# create the UniversalTranslator object, with 10 knobs
# translator = UniversalTranslator(n_dim=10)



# print total number of settings evaluated
print(f'# settings tried: {translator.n_settings_tried()}')