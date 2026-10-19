
"""
Loader Module: Load Datasets 
"""

import pandas as pd
from src.config import *


#Loading Datasets
studentDf = pd.read_csv(STUDENT_DATASET_PATH)
coursesDf = pd.read_csv(COURSES_DATASET_PATH)
attendanceDf = pd.read_csv(ATTENDANCE_DATASET_PATH)
feesDf = pd.read_csv(FEES_DATASET_PATH)
marksDf = pd.read_csv(MARKS_DATASET_PATH)
activitiesDf = pd.read_csv(COURSES_DATASET_PATH)


#DataFrames Dictionary
dataFrames = {
    1:studentDf,
    2:marksDf,
    3:feesDf,
    4:coursesDf,
    5:attendanceDf,
    6:activitiesDf
}