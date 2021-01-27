import numpy as np


# Base coefficients
BASE = {
    'peak': np.array([-8.76]),
    'off_peak': np.array([-1.5064]),
    '(3 hours) 2PM to 5PM': np.array([0.2482]),
    '(4 hours) 2PM to 6PM': np.array([0.3314]),
    '(6 hours) 2PM to 8PM': np.array([0]),
    '(3 hours) 3PM to 6PM': np.array([0.2726]),
    '(3 hours) 4PM to 7PM': np.array([0.1905]),
    '(2 hours) 5PM to 7PM': np.array([0.2247])
}

# Summer and winter coefficients
SEASONS = {
    'Summer': np.array([-0.2002]),
    'Summer and Winter': np.array([0])
}

# group block index to name
BLOCK_GROUP_INDEX_TO_NAME = {
    1: 'AE - Top Tier',
    2: 'AE - Professional Pride',
    3: 'AE - Boomburbs',
    4: 'AE - Savvy Suburbanites',
    5: 'AE - Exurbanites',
    6: 'UA - Urban Chic',
    7: 'UA - Pleasantville',
    8: 'UA - Pacific Heights',
    9: 'UA - Enterprising Professionals',
    10: 'UI - Laptops and Lattes',
    11: 'UI - Metro REnters',
    12: 'UI - Trendsetters',
    13: 'FL - Soccer Moms',
    14: 'FL - Home Improvement',
    15: 'FL - Middleburg',
    16: 'GX - Comfortable Empty Nesters',
    17: 'GX - In Style',
    18: 'GX - Parks and Rec',
    19: 'GX - Rustbelt Traditions',
    20: 'GX - Midlife Constants',
    21: 'CCL - Green Acres',
    22: 'CCL - Salt of the Earth',
    23: 'CCL - The Great Outdoors',
    24: 'CCL - Prairie Living',
    25: 'CCL - Rural Resort Dwellers',
    26: 'CCL - Heartland Communities',
    27: 'EE - Up and Coming Families',
    28: 'EE - Urban Villages',
    29: 'EE - American Dreamers',
    30: 'EE - Barrios Urbanos',
    31: 'EE - Valley Growers',
    32: 'EE - Southwestern Families',
    33: 'MG - City Lights',
    34: 'MG - Emerald City',
    35: 'MG - Bright Young Professionals',
    36: 'MG - Downtown Melting Pot',
    37: 'MG - Front Porches',
    38: 'MG - Old and Newcomers',
    39: 'MG - Hardscrabble Road',
    40: 'SS - Silver & Gold',
    41: 'SS - Golden Years',
    42: 'SS - The Elders',
    43: 'SS - Senior Escapes',
    44: 'SS - Retirement Communities',
    45: 'SS - Social Security Set',
    46: 'RO - Southern Satellites',
    47: 'RO - Rooted Rural',
    48: 'RO - Diners & Miners',
    49: 'RO - Down the Road',
    50: 'RO - Rural Bypasses',
    51: 'MS - City Strivers',
    52: 'MS - Young and Restless',
    53: 'MS - Metro Fusion',
    54: 'MS - Set to Impress',
    55: 'MS - City Commons',
    56: 'HT - Family Foundations',
    57: 'HT - Traditional Living',
    58: 'HT - Small Town Simplicity',
    59: 'HT - Modest Income Homes',
    60: 'NW - International Marketplace',
    61: 'NW - Las Casas',
    62: 'NW - NeWst Residents',
    63: 'NW - Fresh Ambitions',
    64: 'NW - High Rise Renters',
    65: 'SP - Military Proximity',
    66: 'SP - College Towns',
    67: 'SP - Dorms to Diplomas'
}
