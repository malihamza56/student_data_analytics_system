"""
Data Exporter Module: Export final cleaned DataFrames into one Excel workbook.
Each DataFrame is saved on a separate worksheet.
"""

import os
import pandas as pd
from src.config import FINAL_DATA_DIR


def export_final_data(dataFrames):
    try:
        filename = input("Enter Excel file name (e.g: students_final_data.xlsx): ").strip()
        if not filename:
            print("File Name Cannot Be Empty!")
            return
        if not filename.lower().endswith(".xlsx"):
            filename += ".xlsx"
        file_path = os.path.join(FINAL_DATA_DIR,filename)
        sheet_names = {
            1: "Students",
            2: "Marks",
            3: "Fees",
            4: "Courses",
            5: "Attendance",
            6: "Activities"
        }
        # Collect available DataFrames before opening the Excel writer
        available_data = {}

        for key, sheet_name in sheet_names.items():
            dataSet = dataFrames.get(key)

            if isinstance(dataSet, pd.DataFrame):
                available_data[sheet_name] = dataSet

        if not available_data:
            print("No DataSets Available to Export!")
            return

        # Save all available DataFrames in one Excel file
        with pd.ExcelWriter(file_path, engine="openpyxl") as writer:
            for sheet_name, dataSet in available_data.items():
                dataSet.to_excel(
                    writer,
                    sheet_name=sheet_name,
                    index=False
                )

        print("\nAll Available DataSets Exported Successfully!")
        print(f"Excel File Saved At: {file_path}")
        print(f"Number of Sheets Exported: {len(available_data)}")

    except Exception as e:
        print(f"Failed to Export DataSets | Error: {e}")
