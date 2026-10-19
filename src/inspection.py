"""
Inspection Module: Inspect dataframes and implement inspection mehtods on all the dataframes
"""

import time

class DataInspection:
    
    def __init__(self,dataset):
        self.dataset = dataset
        
        if len(self.dataset) != 0:
            ...
        else:
            raise ValueError("DataSet Not Found!")
        
    def show_head(self,n):
        
        try:
            head = self.dataset.head(n)
            return head
        except Exception as e:
            print(f"Failed to show First {n} rows of dataset...|Error {e}")
        
    def show_tail(self,n):
        try:
            head = self.dataset.tail(n)
            return head
        except Exception as e:
            print(f"Failed to show Last {n} rows of dataset...|Error {e}")
        
    def view_rows_clmns_num(self):
        try:
            rows,column = self.dataset.shape
            return rows,column
        except Exception as e:
            print(f"Failed to Inspect Number of rows and columns...|Error {e}")
            
    def view_info(self):
        try:
            return self.dataset.info()
        except Exception as e:
            print(f"Failed to show Info...| Error {e}")      
            
    def view_columns(self):
        try:
            columns_list = self.dataset.columns.to_list()    
            return columns_list
        except Exception as e:
            print(f"Failed to inspect Columns...|Error {e}")
            
    def view_stats(self):
        try:
            return self.dataset.describe()
        except Exception as e:
            print(f"Failed to Describe Stats of Dataset...|Error {e}")
            
        
def chose_dataSet_menu_for_inspection(dataFrames):
    
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
            stu_df = dataFrames.get(1)
            stu_insp = DataInspection(dataset=stu_df)
            inspection_menu(stu_insp)
        elif choice == 2:
            marks_df = dataFrames.get(2)
            marks_insp = DataInspection(dataset=marks_df)
            inspection_menu(marks_insp)
        elif choice == 3:
            fee_df = dataFrames.get(3)
            fee_insp = DataInspection(dataset=fee_df)
            inspection_menu(fee_insp)
        elif choice == 4:
            courses_df = dataFrames.get(4)
            course_insp = DataInspection(dataset=courses_df)
            inspection_menu(course_insp)
        elif choice == 5:
            attendance_df = dataFrames.get(5)
            attendance_insp = DataInspection(dataset=attendance_df)
            inspection_menu(attendance_insp)
        elif choice == 6:
            activities_df = dataFrames.get(6)
            activities_insp = DataInspection(dataset=activities_df)
            inspection_menu(activities_insp)
        elif choice == 0:
            print("Navigating to Main Menu...\nWait for 2 sec...\n")
            time.sleep(2)
            break
        else:
            print("Invalid Choice ! Choice must B/W (0-5).")
                 
def inspection_menu(inspection_object):
    
    print()
    while True:
        print()
        print("="*24)
        print("DataSet Inspection Menu")
        print("="*24)

        print("\nChose Operation from below:")
        print("1: Show nth Rows from Top.")
        print("2: Show nth Rows from Bottom.")
        print("3: Show Number of Rows & Columns.")
        print("4: Show Complete Info of DataSet.")
        print("5: Show Columns Name.")
        print("6: Show Statistical Data.")
        print("0: Back To DataSet Selection Menu.")
        
        choice = int(input("\nEnter Choice B/W (0-6): "))
        
        if choice == 1:
            n = int(input("\nEnter Number of Rows You want to inspect From Top: "))
            print(f"\nTop {n}th Rows Data:")
            head = inspection_object.show_head(n)
            print("\n",head)
        elif choice == 2:
            n = int(input("\nEnter Number of Rows You want to inspect From Top: "))
            print(f"\nBottom {n}th Rows Data:")
            tail = inspection_object.show_tail(n)
            print("\n",tail)
        elif choice == 3:
            rows,col = inspection_object.view_rows_clmns_num()
            print()
            print("\nRows & Columns Number:")
            print(f"\nNo. of Rows: {rows}\nNo. of Columns: {col}")
            print()
        elif choice == 4:
            print()
            print("\nComplete Infromation of DataSet: ")
            info = inspection_object.view_info()
            print("\n",info)
            print()
        elif choice == 5:
            print()
            col_list = inspection_object.view_columns()
            print("\nColumns Names are:")
            for i,column in enumerate(col_list):
                print(f"{i+1}:{column}")
            print()
        elif choice == 6:
            print()
            stats = inspection_object.view_stats()
            print("\nDataSet Satistical Data is:")
            print("\n",stats)
            print()
        elif choice == 0:
            print()
            print("\nNavigating to DataSet Selection Menu...\nWait for 2 Sec...")
            time.sleep(2)
            break
        else:
            print("\nInvalid Choice! Chose B/W (0-6)")
            
            