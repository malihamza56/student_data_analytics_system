"""
Data Refining Module: Refine or clean data on the basis of missing values and also handles them.
"""

import time
import os
import pandas as pd
from src.config import CLEANED_DATA_DIR

class DataRefining:

    def __init__(self, dataSet):
        self.dataSet = dataSet

        if len(dataSet) != 0:
            ...
        else:
            raise ValueError("DataSet Not loaded for Cleaning !")

    # Refining Methods

    def show_null(self):
        try:
            return self.dataSet.isnull().sum()
        except Exception as e:
            print(f"Failed to Count Null Values | Error {e}")

    def drop_null_row(self):
        try:
            null_rows = self.dataSet.isnull().any(axis=1).sum()
            self.dataSet.dropna(inplace=True, axis=0)
            print(f"Successfully Removed {null_rows} Rows Containing Null Values.")
            return self.dataSet
        except Exception as e:
            print(f"Failed to Drop Null Row | Error {e}")

    def fill_null(self):
        try:
            print("\nChoose Method to Fill Null Values:")
            print("1: Fill With a Specific Value.")
            print("2: Fill Numeric Columns With Mean.")
            print("3: Fill Numeric Columns With Median.")
            print("4: Fill All Columns With Mode.")

            choice = int(input("\nEnter Choice B/W (1-4): "))

            if choice == 1:
                value = input("Enter Value to Fill Null Values: ")
                
                value = float(value)
                if value.is_integer():
                    value = int(value)
            
                self.dataSet.fillna(value=value, inplace=True)
                print("Null Values Filled Successfully.")
            elif choice == 2:
                numeric_columns = self.dataSet.select_dtypes(
                    include="number"
                ).columns
                if len(numeric_columns) == 0:
                    print("No Numeric Columns Found in DataSet.")
                    return self.dataSet
                
                for column in numeric_columns:
                    mean_value = self.dataSet[column].mean()
                    if pd.notna(mean_value):
                        self.dataSet[column] = self.dataSet[
                            column
                        ].fillna(mean_value)
                        
                print("Null Values Filled With Mean Successfully.")
            elif choice == 3:
                numeric_columns = self.dataSet.select_dtypes(
                    include="number"
                ).columns
                if len(numeric_columns) == 0:
                    print("No Numeric Columns Found in DataSet.")
                    return self.dataSet
                for column in numeric_columns:
                    median_value = self.dataSet[column].median()
                    if pd.notna(median_value):
                        self.dataSet[column] = self.dataSet[column].fillna(median_value)
                print("Null Values Filled With Median Successfully.")
            elif choice == 4:
                for column in self.dataSet.columns:
                    mode_values = self.dataSet[column].mode(dropna=True)
                    if not mode_values.empty:
                        self.dataSet[column] = self.dataSet[column].fillna(mode_values.iloc[0])
                print("Null Values Filled With Mode Successfully.")
            else:
                print("Invalid Choice! Choose B/W (1-4).")
            return self.dataSet
        except Exception as e:
            print(f"Failed to Fill Null Values | Error {e}")
            
    def show_duplicate(self):
        try:
            return self.dataSet.duplicated().sum()

        except Exception as e:
            print(f"Failed to Count Duplicate | Error {e}")

    def remove_duplicate(self):
        try:
            duplicate_count = self.dataSet.duplicated().sum()
            self.dataSet.drop_duplicates(inplace=True)
            print(
                f"Successfully Removed {duplicate_count} Duplicate Rows."
            )
            return self.dataSet
        except Exception as e:
            print(f"Failed to Remove Duplicates | Error {e}")

    def clean_id(self):
        try:
            column = input("Enter ID Column Name: ").strip()
            n = int(input("Enter How Many IDs You Want To Clean: "))
            correction = {}
            
            for i in range(n):
                incorrect = input("Enter InCorrect ID Value: ")
                correct = input("Enter Correct ID Value: ")
                correction[incorrect]=correct
                
            if column not in self.dataSet.columns:
                print("ID Column Not Found!")
                return

            self.dataSet[column] = (
                self.dataSet[column]
                .astype("string")
                .str.strip()
                .str.upper()
            )

            self.dataSet[column] = self.dataSet[column].replace(correction)

            self.dataSet[column] = self.dataSet[column].replace("", pd.NA)

            print("ID Column Cleaned Successfully!")
            return self.dataSet

        except Exception as e:
            print(f"Failed to Clean ID Column | Error: {e}")

    def save_cleaned_dataset(
        self,
        dir_path
        ):
        try:
            print("\nChoose Export Format:")
            print("1: CSV File.")
            print("2: Excel File.")

            choice = int(input("\nEnter Choice B/W (1-2): "))
            if choice == 1:
                filename = input(
                    "Enter CSV File Name (e.g. cleaned_dataset.csv): "
                ).strip()
                if not filename:
                    raise ValueError("File Name Cannot Be Empty.")
                if not filename.lower().endswith(".csv"):
                    filename += ".csv"
                
                filePath = os.path.join(dir_path,filename)
                self.dataSet.to_csv(filePath,index=False)
                print(f"Cleaned DataSet Saved Successfully: {filename}")
            elif choice == 2:
                filename = input("Enter Excel File Name (e.g. cleaned_data.xlsx): ").strip()
                if not filename:
                    raise ValueError("File Name Cannot Be Empty.")
                if not filename.lower().endswith(".xlsx"):
                    filename += ".xlsx"
                filePath = os.path.join(dir_path,filename)
                self.dataSet.to_excel(filename, index=False)
                print(f"Cleaned DataSet Saved Successfully: {filename}")
            else:
                print("Invalid Choice! Choose B/W (1-2).")
                
        except Exception as e:
            print(f"Failed to Save / Export Cleaned Dataset | Error {e}")

def chose_dataSet_menu_for_refining(dataFrames):

    print()

    while True:
        print()
        print("=" * 19)
        print("Available DataSets")
        print("=" * 19)

        print("\nChoose DataSet option from Below:")
        print("1: Students DataSet.")
        print("2: Marks DataSet.")
        print("3: Fees DataSet.")
        print("4: Courses DataSet.")
        print("5: Attendance DataSet.")
        print("6: Activities DataSet.")
        print("0: Back To Main Menu.")

        try:
            choice = int(input("\nEnter Choice B/W (0-6): "))
        except ValueError:
            print("Invalid Input! Enter an Integer.")
            continue

        if choice == 1:
            stu_df = dataFrames.get(1)
            try:
                stu_ref = DataRefining(dataSet=stu_df)
                refining_menu(stu_ref)
            except (ValueError, TypeError) as e:
                print(f"Failed to Load Students DataSet | Error {e}")
        elif choice == 2:
            marks_df = dataFrames.get(2)
            try:
                marks_ref = DataRefining(dataSet=marks_df)
                refining_menu(marks_ref)
            except (ValueError, TypeError) as e:
                print(f"Failed to Load Marks DataSet | Error {e}")
        elif choice == 3:
            fee_df = dataFrames.get(3)
            try:
                fee_ref = DataRefining(dataSet=fee_df)
                refining_menu(fee_ref)
            except (ValueError, TypeError) as e:
                print(f"Failed to Load Fees DataSet | Error {e}")
        elif choice == 4:
            courses_df = dataFrames.get(4)
            try:
                course_ref = DataRefining(dataSet=courses_df)
                refining_menu(course_ref)
            except (ValueError, TypeError) as e:
                print(f"Failed to Load Courses DataSet | Error {e}")
        elif choice == 5:
            attendance_df = dataFrames.get(5)
            try:
                attendance_ref = DataRefining(dataSet=attendance_df)
                refining_menu(attendance_ref)
            except (ValueError, TypeError) as e:
                print(f"Failed to Load Attendance DataSet | Error {e}")
        elif choice == 6:
            activities_df = dataFrames.get(6)
            try:
                activities_ref = DataRefining(dataSet=activities_df)
                refining_menu(activities_ref)
            except (ValueError, TypeError) as e:
                print(f"Failed to Load Activities DataSet | Error {e}")
        elif choice == 0:
            print("Navigating to Main Menu...\nWait for 2 sec...\n")
            time.sleep(2)
            break
        else:
            print("Invalid Choice! Choice must B/W (0-6).")


def refining_menu(refining_obj):

    print()

    while True:
        print()
        print("=" * 24)
        print("DataSet Refining Menu")
        print("=" * 24)

        print("\nChoose Operation from below:")
        print("1: Show Null Values.")
        print("2: Remove Null Value Rows.")
        print("3: Fill Null Values.")
        print("4: Show Duplicates.")
        print("5: Remove Duplicates.")
        print("6: Clean IDs")
        print("7: Save / Export Cleaned Dataset.")
        print("0: Back To DataSet Selection Menu.")

        try:
            choice = int(input("\nEnter your choice from above (0-6): "))
        except ValueError:
            print("Invalid Input! Enter an Integer.")
            continue
        if choice == 1:
            print("\nNumber of Null Values in Each Column:")
            null_values = refining_obj.show_null()

            if null_values is not None:
                print(null_values)
                print(f"\nTotal Null Values: {null_values.sum()}")
        elif choice == 2:
            refining_obj.drop_null_row()
        elif choice == 3:
            refining_obj.fill_null()

        elif choice == 4:
            duplicates = refining_obj.show_duplicate()
            if duplicates is not None:
                print(f"\nNumber of Duplicate Rows: {duplicates}")
        elif choice == 5:
            refining_obj.remove_duplicate()
        elif choice == 7:
            refining_obj.save_cleaned_dataset(dir_path=CLEANED_DATA_DIR)
        elif choice == 6:
            refining_obj.clean_id()
        elif choice == 0:
            print(
                "\nNavigating to DataSet Selection Menu...\n"
                "Wait for 2 Sec..."
            )
            time.sleep(2)
            break
        else:
            print("Invalid Choice! Choose B/W (0-7).")