# Student Data Analytics

A menu-based Python program that loads university student data, cleans it, combines it into one master dataset, and analyses academic performance, attendance and fee status using **Pandas**. Results can be viewed through the menu and exported to Excel/CSV.

> University of Sargodha – Project Report

---

## Table of Contents

1. [Problem Statement](#problem-statement)
2. [Objectives](#objectives)
3. [Features](#features)
4. [Tech Stack](#tech-stack)
5. [Project Structure](#project-structure)
6. [Module Description](#module-description)
7. [Datasets](#datasets)
8. [Workflow](#workflow)
9. [Installation and Usage](#installation-and-usage)
10. [Menu Options](#menu-options)
11. [Future Improvements](#future-improvements)
12. [Author](#author)

---

## Problem Statement

Universities keep large amounts of student data (profiles, marks, attendance, fees) in separate files, often with missing values, duplicate entries and inconsistent spellings. Answering simple questions such as *which students are performing poorly* or *which department has the best results* becomes slow and error-prone when done manually, and at-risk students are often noticed too late.

## Objectives

- Import student datasets (students, courses, marks, attendance, fees, activities) from CSV files.
- Clean the data: handle missing values, duplicates, wrong data types and invalid entries.
- Combine the datasets into one master dataset using merge/join operations.
- Analyse performance, attendance and fees using selection, filtering, sorting, aggregation and grouping.
- Identify top performers and students at academic risk.
- Present results through a simple menu and export reports to Excel/CSV.

## Features

- Data loading and inspection (shape, types, missing values, duplicates)
- Automatic data cleaning
- Merging of multiple datasets on `Student_ID`
- Filtering and searching of student records
- Academic, attendance and fee analysis
- Categorical insights (department and gender distribution, duplicates, missing values)
- CRUD operations on student records
- Export of cleaned, filtered and final data to Excel/CSV
- Menu-driven command-line interface

## Tech Stack

| Item | Details |
|---|---|
| Language | Python 3.x |
| Library | Pandas |
| Excel support | openpyxl |
| Interface | Command line (menu-driven) |
| Programming style | Modular programming |

## Project Structure

```
universty_data_analytics/
│
├── data/                      # Raw input datasets
│   ├── activities.csv
│   ├── attendance.csv
│   ├── courses.csv
│   ├── fees.csv
│   ├── marks.csv
│   └── students.csv
│
├── docs/                      # Project documentation / report
│
├── ProcessedOutput/           # Generated output files
│   ├── cleanedData/           # Cleaned datasets
│   ├── filteredData/          # Filtered results
│   ├── finalData/             # Final merged data
│   └── university_summary.xlsx  # Excel report
│
├── src/                       # Source code (modules)
│   ├── analytics.py
│   ├── cleaner.py
│   ├── config.py
│   ├── crud.py
│   ├── exporter.py
│   ├── filter.py
│   ├── insights.py
│   ├── inspection.py
│   ├── loader.py
│   └── merge.py
│
├── main.py                    # Entry point (menu)
├── test.py                    # Testing script
├── .gitignore
└── README.md
```

## Module Description

| File | Purpose |
|---|---|
| `main.py` | Entry point of the program. Displays the menu and calls the required modules. |
| `src/config.py` | Stores file paths, folder names and common settings. |
| `src/loader.py` | Loads the CSV files from the `data/` folder into Pandas DataFrames. |
| `src/inspection.py` | Inspects the data: shape, data types, missing values, duplicates, summary statistics. |
| `src/cleaner.py` | Cleans the data: missing values, duplicates, data types, text formatting and invalid values. |
| `src/merge.py` | Merges the cleaned datasets into one master DataFrame using `Student_ID`. |
| `src/filter.py` | Selects and filters records, such as by department or by student. |
| `src/analytics.py` | Performs analysis: sorting, grouping, aggregation, ranking and risk detection. |
| `src/insights.py` | Generates categorical insights such as top values, percentages and unique counts. |
| `src/crud.py` | Create, read, update and delete operations on student records. |
| `src/exporter.py` | Exports cleaned, filtered and final results to Excel/CSV in `ProcessedOutput/`. |

## Datasets

| Dataset | Description |
|---|---|
| `students.csv` | Basic profile of each student (ID, name, department, gender, etc.) |
| `courses.csv` | Courses offered by each department |
| `marks.csv` | Marks obtained by students in each course |
| `attendance.csv` | Attendance record of students |
| `fees.csv` | Fee amount, paid amount and fee status |
| `activities.csv` | Extra-curricular activities of students |

All datasets are linked through the common key column **`Student_ID`**.

## Workflow

```
Load Data  →  Inspect  →  Clean  →  Merge  →  Filter / Analyse  →  Insights  →  Export
```

1. **Load**: read the CSV files from `data/`.
2. **Inspect**: check structure, missing values and duplicates.
3. **Clean**: fix data-quality problems and save the cleaned data.
4. **Merge**: combine all datasets into one master dataset.
5. **Analyse**: filter, sort, group and aggregate the master dataset.
6. **Export**: save results in `ProcessedOutput/`.

## Installation and Usage

**1. Clone the repository**

```bash
git clone <your-repository-link>
cd universty_data_analytics
```

**2. Install the requirements**

```bash
pip install pandas openpyxl
```

**3. Run the program**

```bash
python main.py
```

Choose an option from the menu by typing its number.

## Menu Options

> Update this table to match your actual menu.

| Option | Menu Item | Operation |
|---|---|---|
| 1 | Search Student | Selection / filtering by Student ID |
| 2 | Top Students | Sorting by percentage |
| 3 | Department Analysis | Grouping and aggregation |
| 4 | Attendance Analysis | Filtering and grouping |
| 5 | Fee Analysis | Filtering and aggregation |
| 6 | At-Risk Students | Condition-based filtering |
| 7 | Export Report | Save results to Excel/CSV |
| 8 | Exit | Close the program |

## Future Improvements

- Charts and visualisations (Matplotlib / Seaborn)
- Graphical user interface (Tkinter or a web dashboard)
- Prediction of student performance using machine learning
- Database support (MySQL / SQLite) instead of CSV files

## Author

- **Name:** [Your Name]
- **Roll No:** [Your Roll No]
- **Class:** [Your Class]
- **University:** University of Sargodha