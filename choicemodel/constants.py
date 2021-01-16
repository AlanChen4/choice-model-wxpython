import numpy as np


# Base coefficients
BASE = {
    'peak': np.array([-8.76]),
    'off_peak': np.array([-1.5064]),
    'two_to_five': np.array([0.2482]),
    'two_to_six': np.array([0.3314]),
    'two_to_eight': np.array([0]),
    'three_to_six': np.array([0.2726]),
    'four_to_seven': np.array([0.1905]),
    'five_to_seven': np.array([0.2247])
}

# Summer and winter coefficients
SEASONS = {
    'summer': np.array([-0.2002]),
    'summer_and_winter': np.array([0])
}
