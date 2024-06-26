#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Variational Animal Motion Embedding 0.1 Toolbox
© K. Luxem & P. Bauer, Department of Cellular Neuroscience
Leibniz Institute for Neurobiology, Magdeburg, Germany

https://github.com/LINCellularNeuroscience/VAME
Licensed under GNU General Public License v3.0
"""

import sys

from .create_training import create_trainset
from .dataloader import SEQUENCE_DATASET
from .evaluate import evaluate_model
from .rnn_vae import train_model

sys.dont_write_bytecode = True


