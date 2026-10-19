

"""
Config module: Store configurations of project
"""

import time
from pathlib import Path

ROOT_DIR = Path(__file__).resolve().parent.parent

#Directories Path
DATA_DIR = ROOT_DIR / "RawData"
OUTPUT_DIR = ROOT_DIR / "Processedoutput"
FILTERED_DATA_DIR = OUTPUT_DIR / "filteredData"
CLEANED_DATA_DIR = OUTPUT_DIR / "cleanedData"
FINAL_DATA_DIR = OUTPUT_DIR / "finalData"


#DataSets Files Path
STUDENT_DATASET_PATH = DATA_DIR / "students.csv"
COURSES_DATASET_PATH = DATA_DIR / "courses.csv"
FEES_DATASET_PATH = DATA_DIR / "fees.csv"
ATTENDANCE_DATASET_PATH = DATA_DIR /"attendance.csv"
MARKS_DATASET_PATH = DATA_DIR / "marks.csv"
ACTIVITIES_DATASET_PATH = DATA_DIR / "activities.csv"



def loader_animation():
    time.sleep(0.85)
    print(".",end="")
    time.sleep(0.85)
    print(".",end="")
    time.sleep(0.85)
    print(".",end="")