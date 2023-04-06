import pandas as pd
import numpy as np

from scipy.stats import norm
from scipy.stats import chi2

chat_id = 38897891 # Ваш chat ID, не меняйте название переменной

def solution(p: float, x: np.array) -> tuple:
    
    n = len(x)
    alpha = 1 - p
    
    z1 = chi2.ppf(alpha/2,df=2*n)
    z2 = chi2.ppf(1-alpha/2,df=2*n)
    
    right = np.sqrt(sum(x**2)/(z1*47))
    left = np.sqrt(sum(x**2)/(z2*47))
    
    return left, right
