"""
Analysis Module: Performs Data Analysis on the base of Data Aggregiaton & Sorting
"""

import time
class DataAnalysis:
    def __init__(self,dataSet):
        self.dataSet = dataSet
        
        if len(self.dataSet) != 0:
            ...
        else:
            raise ValueError("DataSet not Found/Loaded for Aggregiation")
        
    #Methods
    def show_columns(self):
        try:
            for i,clm in enumerate(self.dataSet.columns.to_list()):
                print(f"{i+1}: {clm}")
            print()
        except Exception as e:
            print(f"Failed to Show Columns Name {e}")
            
    def aggregiation(self):
        
        self.show_columns()
        clms_lst = []
        agg = ['mean','min','max','std','sum','count']
        clm_no = int(input("Enter Numbers of Columns: "))
        
        for _ in range(clm_no):
            clm_name = input("Enter Column Name with only integer values from above: ").capitalize().strip()
            
            clms_lst.append(clm_name)
            
        if clms_lst and len(clms_lst) == 1:
            print(self.dataSet[clms_lst].agg(agg))
        elif clms_lst and len(clms_lst) > 1:
            print(self.dataSet[clms_lst].agg(agg))
        else:
            print("No Columns Found for aggregiation")
    
    def groupby(self):
        
        agg = {
            1:'mean',
            2:'max',
            3:'count',
            4:'min',
            5:'std',
            6:'median'
        }
        
        try:
            group_columns = list(
                map(
                    str,input(
                        "Enter Columns for GroupBy (use ',' for sep.): "
                    ).split(",")
                )
            )
            
            op_clm = input("Enter Column for operation/Calculation: ")
            
            for key,val in agg.items():
                print(f"{key}: {val}")
            print()
            
            choose = int(input("Chose Function (1-5): "))
            
            if choose == 1:
                print(self.dataSet.groupby(group_columns)[op_clm].mean())
            elif choose == 2:
                print(self.dataSet.groupby(group_columns)[op_clm].max())
            elif choose == 3:
                print(self.dataSet.groupby(group_columns)[op_clm].count())
            elif choose == 4:
                print(self.dataSet.groupby(group_columns)[op_clm].min())
            elif choose == 5:
                print(self.dataSet.groupby(group_columns)[op_clm].std())
            elif choose == 6:
                print(self.dataSet.groupby(group_columns)[op_clm].median())
            else:
                print("Operation Choice Not valid! ")
            
        except Exception as e:
            print(f"Failed to perform GroupBy Aggregiation ! {e}")
        
            
    def sort(self):
        self.show_columns()
        
        try:
            columns = list(
                map(
                    str,input(
                            "Enter Columns for Sorting (use ',' for sep.): "
                    ).split(",")
                )
            )
            
            self.dataSet.sort_values(
                by=columns,
                inplace= True
            )
            print(self.dataSet)
            
        except Exception as e:
            print(f"Failed to Sort Values | Error {e}")
        

#MENU Functions

def chose_dataSet_menu_for_analysis(dataFrames):
    
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
            stu_analysis = DataAnalysis(dataSet=stu_df)
            analysis_menu(stu_analysis)
        elif choice == 2:
            marks_df = dataFrames.get(2)
            marks_analysis = DataAnalysis(dataSet=marks_df)
            analysis_menu(marks_analysis)
        elif choice == 3:
            fee_df = dataFrames.get(3)
            fee_analysis = DataAnalysis(dataSet=fee_df)
            analysis_menu(fee_analysis)
        elif choice == 4:
            courses_df = dataFrames.get(4)
            course_analysis = DataAnalysis(dataSet=courses_df)
            analysis_menu(course_analysis)
        elif choice == 5:
            attendance_df = dataFrames.get(5)
            attendance_analysis = DataAnalysis(dataSet=attendance_df)
            analysis_menu(attendance_analysis)
        elif choice == 6:
            activities_df = dataFrames.get(6)
            activities_analysis = DataAnalysis(dataSet=activities_df)
            analysis_menu(activities_analysis)
        elif choice == 0:
            print("Navigating to Main Menu...\nWait for 2 sec...\n")
            time.sleep(2)
            break
        else:
            print("Invalid Choice ! Choice must B/W (0-5).")

def analysis_menu(analysis_object):
    
    print()
    while True:
        print()
        print("="*24)
        print("DataSet Analysis Menu")
        print("="*24)

        print("\nChose Operation from below:")
        print("1: Apply Aggregiation.")
        print("2: Apply groubBy Aggrigiation.")
        print("3: Sort Values.")
        print("0: Back To dataSet Menu.")
        
        choice = int(input("\nEnter Choice B/W (0-3): "))
        
        if choice == 1:
           analysis_object.aggregiation()
        elif choice == 2:
            analysis_object.groupby()
        elif choice == 3:
            analysis_object.sort()
        elif choice == 0:
            print()
            print("\nNavigating to DataSet Selection Menu...\nWait for 2 Sec...")
            time.sleep(2)
            break
        else:
            print("\nInvalid Choice! Chose B/W (0-6)")
            
            