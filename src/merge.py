"""
Merging Module : Used for DataMerging
"""

import time
import pandas as pd


class DataCombining:

    def __init__(self, dataSet):
        self.dataSet = dataSet

        if dataSet is not None and len(dataSet) != 0:
            ...
        else:
            raise ValueError("DataSet Not Loaded for Combining!")

    # Combining Methods
    def merge_data(self, secondDataSet):
        merge_types = {
            1: "inner",
            2: "left",
            3: "right",
            4: "outer"
        }
        try:
            print("\nChoose Merge Type:")
            print("1: Inner Merge.")
            print("2: Left Merge.")
            print("3: Right Merge.")
            print("4: Outer Merge.")
            choice = int(input("\nEnter Choice B/W (1-4): "))
        
            if choice not in merge_types:
                print("Invalid Choice! Choose B/W (1-4).")
                return
            print("Avaialable columns in DataSet 1")
            for i,column in enumerate(self.dataSet.columns.to_list()):
                print(f"{i+1}: {column}")
                
            print("Available columns in DataSet 2")
            for i,col in enumerate(secondDataSet.columns.to_list()):
                print(f"{i+1}:{col}")
                
            column = input("Enter the common column name for merging: ").strip()
            if column not in self.dataSet.columns:
                print(f"Column '{column}' not found in first DataSet.")
                return
            if column not in secondDataSet.columns:
                print(f"Column '{column}' not found in second DataSet.")
                return
            merged_df = pd.merge(
                self.dataSet,
                secondDataSet,
                on=column,
                how=merge_types[choice],
                suffixes=("_left", "_right")
            )

            return merged_df

        except ValueError:
            print("Invalid Input! Enter a valid integer.")
        except Exception as e:
            print(f"Failed to Merge DataSets | Error: {e}")

    def join_data(self, secondDataSet):
        join_types = {
            1: "left",
            2: "right",
            3: "inner",
            4: "outer"
        }
        try:
            print("Avaialable columns in DataSet 1")
            for i,column in enumerate(self.dataSet.columns.to_list()):
                print(f"{i+1}: {column}")
                
            print("Available columns in DataSet 2")
            for i,col in enumerate(secondDataSet.columns.to_list()):
                print(f"{i+1}:{col}")
            column = input(
                "Enter the common column name for joining: "
            ).strip()

            if column not in self.dataSet.columns:
                print(f"Column '{column}' not found in first DataSet.")
                return
            if column not in secondDataSet.columns:
                print(f"Column '{column}' not found in second DataSet.")
                return
            print("\nChoose Join Type:")
            print("1: Left Join.")
            print("2: Right Join.")
            print("3: Inner Join.")
            print("4: Outer Join.")
            choice = int(input("\nEnter Choice B/W (1-4): "))
            if choice not in join_types:
                print("Invalid Choice! Choose B/W (1-4).")
                return
            first_df = self.dataSet.set_index(column)
            second_df = secondDataSet.set_index(column)
            joined_df = first_df.join(
                second_df,
                how=join_types[choice],
                lsuffix="_left",
                rsuffix="_right"
            )
            joined_df.reset_index(inplace=True)
            return joined_df
        except ValueError:
            print("Invalid Input! Enter a valid integer.")
        except Exception as e:
            print(f"Failed to Join DataSets | Error: {e}")

    def concatenate_data(self, secondDataSet):
        try:
            print("\nChoose Concatenation Direction:")
            print("1: Concatenate Rows (Vertical).")
            print("2: Concatenate Columns (Horizontal).")

            choice = int(input("\nEnter Choice B/W (1-2): "))

            if choice == 1:
                combined_df = pd.concat(
                    [self.dataSet, secondDataSet],
                    axis=0,
                    ignore_index=True
                )
            elif choice == 2:
                combined_df = pd.concat(
                    [self.dataSet, secondDataSet],
                    axis=1
                )
            else:
                print("Invalid Choice! Choose B/W (1-2).")
                return
            return combined_df
        except ValueError:
            print("Invalid Input! Enter a valid integer.")
        except Exception as e:
            print(f"Failed to Concatenate DataSets | Error: {e}")


def chose_dataSet_menu_for_combining(dataFrames):

    print()

    while True:
        print()
        print("=" * 19)
        print("Available DataSets")
        print("=" * 19)

        print("\nChoose the First DataSet:")
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
            print("Invalid Input! Enter a valid integer.")
            continue

        try:
            if choice == 1:
                stu_df = dataFrames.get(1)
                stu_merge = DataCombining(dataSet=stu_df)
                combining_menu(stu_merge,choice)
            elif choice == 2:
                marks_df = dataFrames.get(2)
                marks_merge = DataCombining(dataSet=marks_df)
                combining_menu(marks_merge,choice)
            elif choice == 3:
                fee_df = dataFrames.get(3)
                fee_merge = DataCombining(dataSet=fee_df)
                combining_menu(fee_merge,choice)
            elif choice == 4:
                courses_df = dataFrames.get(4)
                course_merge = DataCombining(dataSet=courses_df)
                combining_menu(course_merge,choice)
            elif choice == 5:
                attendance_df = dataFrames.get(5)
                attendance_merge = DataCombining(dataSet=attendance_df)
                combining_menu(attendance_merge,choice)
            elif choice == 6:
                activities_df = dataFrames.get(6)
                activities_merge = DataCombining(dataSet=activities_df)
                combining_menu(activities_merge,choice)
            elif choice == 0:
                print("Navigating to Main Menu...\nWait for 2 sec...\n")
                time.sleep(2)
                break
            else:
                print("Invalid Choice ! Choice must B/W (0-6).")
        except ValueError as e:
            print(f"Error: {e}")

def combining_menu(combining_obj,first_choice):

    while True:
        print()
        print("=" * 25)
        print("DataSet Combining Menu")
        print("=" * 25)

        print("\nChoose Operation from below:")
        print("1: Merge DataSets.")
        print("2: Join DataSets.")
        print("3: Concatenate DataSets.")
        print("0: Back To DataSet Selection Menu.")

        try:
            choice = int(input("Enter Choice from Above Menu: "))
        except ValueError:
            print("Invalid Input! Enter a valid integer.")
            continue
        
        dataFrames = {
                1:"studentDf",
                2:"marksDf",
                3:"feesDf",
                4:"coursesDf",
                5:"attendanceDf",
                6:"activitiesDf"
                }
        if choice == 1:
            print("\nChose Second DataSet for Merging.")
            for key,val in dataFrames.items():
                print(f"{key}:{val}")
            
            try:
                choose = int(input("Choose 2nd DataSet: "))
            except ValueError:
                print("Invalid Input! Enter a valid integer.")
                continue
            if first_choice != choose:
                print(f"Fist DataSet: {dataFrames.get(first_choice)}")
                print(f"Second DataSet: {dataFrames.get(choose)}")
                second_dataset = dataFrames.get(choose)
                if second_dataset is None:
                    print("Invalid DataSet Choice!")
                    continue
                result = combining_obj.merge_data(second_dataset)
                if result is not None:
                    print(result)
            else:
                print("Dataset cannot be same choose a different DataSet.")
        elif choice == 2:
            print("\nChoose Dataset for Joining.")
            for key,val in dataFrames.items():
                print(f"{key}:{val}")
                        
            try:
                choose = int(input("Choose 2nd DataSet: "))
            except ValueError:
                print("Invalid Input! Enter a valid integer.")
                continue
            if first_choice != choose:
                print(f"Fist DataSet: {dataFrames.get(first_choice)}")
                print(f"Second DataSet: {dataFrames.get(choose)}")
                second_dataset = dataFrames.get(choose)
                if second_dataset is None:
                    print("Invalid DataSet Choice!")
                    continue
                result = combining_obj.join_data(second_dataset)
                if result is not None:
                    print(result)
            else:
                print("DataSet Cannot be same choose a different DataSet.")
        elif choice == 3:
            print("\nChoose Dataset for Concatenation.")
            for key,val in dataFrames.items():
                print(f"{key}:{val}")
                        
            try:
                choose = int(input("Choose 2nd DataSet: "))
            except ValueError:
                print("Invalid Input! Enter a valid integer.")
                continue
            if first_choice != choose:
                print(f"Fist DataSet: {dataFrames.get(first_choice)}")
                print(f"Second DataSet: {dataFrames.get(choose)}")
                second_dataset = dataFrames.get(choose)
                if second_dataset is None:
                    print("Invalid DataSet Choice!")
                    continue
                result = combining_obj.concatenate_data(second_dataset)
                if result is not None:
                    print(result)
            else:
                print("DataSet Cannot be same choose a different DataSet.")
        elif choice == 0:
            break
        else:
            print("Invalid Choice! Choose B/W (0-3).")