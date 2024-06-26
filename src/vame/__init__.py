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

from .analysis import community
from .analysis import community_videos
from .analysis import generative_model
from .analysis import gif
from .analysis import motif_videos
from .analysis import pose_segmentation
from .analysis import visualization
from .initialize_project import init_new_project
from .model import create_trainset
from .model import evaluate_model
from .model import train_model
from .util import auxiliary
from .util.align_egocentrical import egocentric_alignment
from .util.auxiliary import update_config
from .util.csv_to_npy import csv_to_numpy

sys.dont_write_bytecode = True
