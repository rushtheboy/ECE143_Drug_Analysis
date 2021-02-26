import pandas as pd
import numpy as np

def condition_filter(condition):
    if type(condition) != str: return True
    if 'comment' in condition: return True
    if condition == 'Other': return True
    return False

def drug_filter(drug):
    return False

