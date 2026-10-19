"""
Data Filtering Module: Fileterd all the datasets with the help of pandas 
"""
import time,os
from src.config import FILTERED_DATA_DIR
class DataFilteration:
    def __init__(self,dataSet):
        self.dataSet = dataSet
        if len(dataSet) != 0:
            ...
        else:
            raise ValueError("DataSet Not Loaded / Found !")
        
        
    #Filteration Methods
    def show_columns(self):
        print("\nAvailable Columns:")
        try:
            for i,column in enumerate(self.dataSet.columns.to_list()):
                print(f"{i}: {column}")
            print()
        except Exception as e:
            print(f"Failed to Show Columns.. |Error {e}")
            
    def select_column(self):
        print("Select Column from available columns.")
        self.show_columns()
        try:
            column_name = input("Enter Column Name same as Given Above: ")
            return column_name
        except Exception as e:
            print(f"Failed to select Column...|Error {e}")
            
    def single_conditional_filteration(self):
        clmn_name = self.select_column()
       
        try:
            op = str(input("Enter Conditional Operator from (<,>,==,!=,<=,>=): ")).strip()
            value = str(input("Enter Value for filter: "))
            
            filtered_df = self.dataSet.query(clmn_name+op+value)
            return filtered_df
        
        except Exception as e:
            print(f"Failed to perform Single Filteration...|Error {e}")
            
        
    def multi_conditional_filteration(self):
        
        clmn_name = self.select_column()
        try:
            op1 = input("Enter First Conditonal Operator from (<,>,==,!=,<=,>=): ").strip()
            value1 = input("Enter value 1 for Filter: ")
            
            bool_op = input("Enter Boolean Operator Symbol AND,OR,NOT -->(&,|,~): ")
            clmn_name2 = input("Enter Second Column Name from Above: ")
            op2 = input("Enter Second Conditional Operator from (<,>,==,!=,<=,>=): ")
            value2 = input("Enter Value 2 for filteration: ")
            
            conditon1 = clmn_name + op1 + value1 + bool_op
            conditon2 = clmn_name2 + op2 + value2
             
            filtered_df = self.dataSet.query(
                conditon1 + conditon2
            )
            
            return filtered_df
        
        except Exception as e:
            print(
                f"MultiFilteration Failed | Error {e}"
            )
        
    def export_filtered_data(self,filtered_dir,filtered_data):
        try:
            print("\nChoose Export Format.")
            print("1: CSV File.")
            print("2: Excel File.")
            
            choose = int(input("Choose Format from Above: "))
            
            if choose == 1:
                filename = input("Enter File Name (e.g filtered_data.csv): ").strip()
                if not filename:
                    raise ValueError("FileName can not be Empty!")
                if not filename.lower().endswith(".csv"):
                    filename+=".csv"
                filePath = os.path.join(filtered_dir,filename)
                self.dataSet.to_csv(filePath,index=False)
            elif choose == 2:
                filename = input("Enter File Name (e.g filtered_data.xlsx): ").strip()
                if not filename:
                    raise ValueError("FileName can not be Empty!")
                if not filename.lower().endswith(".xlsx"):
                    filename+=".xlsx"
                filePath = os.path.join(filtered_dir,filename)
                filtered_data.to_csv(filePath,index=False)

        except Exception as e:
            print(f"Failed to Export / Save Filtered Dataset |Error {e}")
            
def chose_dataSet_menu_for_filteration(dataFrames):
    
    print()
    while True:
        print()
        print("="*19)
        print("Available DataSets")
        print("="*19)
        
        print("\nChose DataSet option from Below:")
        print("1: Students DataSet.")
        print("2: Marks DataSet.")
        print("3: Fees DataSet.")
        print("4: Courses DataSet.")
        print("5: Attendance DataSet.")
        print("6: Activities DataSet.")
        print("0: Back To Main Menu.")
        
        choice = int(input("\nEnter Choice B/W (0-5): "))
        
        if choice == 1:
            stu_df = dataFrames.get(choice)
            stu_filt = DataFilteration(dataSet=stu_df)
            filteration_menu(stu_filt)
        elif choice == 2:
            marks_df = dataFrames.get(2)
            marks_filt = DataFilteration(dataSet=marks_df)
            filteration_menu(marks_filt)
        elif choice == 3:
            fee_df = dataFrames.get(3)
            fee_filt = DataFilteration(dataSet=fee_df)
            filteration_menu(fee_filt)
        elif choice == 4:
            courses_df = dataFrames.get(4)
            course_filt = DataFilteration(dataSet=courses_df)
            filteration_menu(course_filt)
        elif choice == 5:
            attendance_df = dataFrames.get(5)
            attendance_filt = DataFilteration(dataSet=attendance_df)
            filteration_menu(attendance_filt)
        elif choice == 6:
            activities_df = dataFrames.get(6)
            activities_filt = DataFilteration(dataSet=activities_df)
            filteration_menu(activities_filt)
        elif choice == 0:
            print("Navigating to Main Menu...\nWait for 2 sec...\n")
            time.sleep(2)
            break
        else:
            print("Invalid Choice ! Choice must B/W (0-5).")
            
            
def filteration_menu(filteration_obj):
    
    print()
    while True:
        print()
        print("="*24)
        print("DataSet Filteration Menu.")
        print("="*24)

        print("\nChose Operation from below:")
        print("1: Single Conditon Filteration.")
        print("2: MultiConditonal Filteration.")
        print("3: Save / Export Data.")
        print("0: Back To DataSet Menu.")
        
        choice = int(input("\nEnter Choice B/W (0-2): "))
        
        if choice == 1:
            
            filtered_data = filteration_obj.single_conditional_filteration()
            print("\nFiltered Data is: ")
            print(filtered_data)
            print()
            
        elif choice == 2:
            filtered_data = filteration_obj.multi_conditional_filteration()
            print("\nFiltered Data is: ")
            print(filtered_data)
            print()
        elif choice == 3:
            filteration_obj.export_filtered_data(filtered_data=filtered_data,filtered_dir=FILTERED_DATA_DIR)
            print("Filtered Data Export Successfull !")
            
        elif choice == 0:
            print("Navigating Back to DataSet Menu...")
            time.sleep(2)
            break
        else:
            print("Invalid Choice ! Choose B/W (0-2)")
