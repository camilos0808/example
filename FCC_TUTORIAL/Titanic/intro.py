from __future__ import absolute_import,division,print_function,unicode_literals
import tensorflow as tf
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import os

df_eval = pd.read_csv(os.path.join(os.getcwd(),'eval.csv'))
df_train = pd.read_csv(os.path.join(os.getcwd(),'train.csv'))



