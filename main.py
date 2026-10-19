"""
Main Module: Main Module Controls Whole Workflow
""" 
from src.inspection import chose_dataSet_menu_for_inspection
from src.cleaner import chose_dataSet_menu_for_refining
from src.analytics import chose_dataSet_menu_for_analysis
from src.crud import chose_dataSet_menu_for_crud
from src.filter import chose_dataSet_menu_for_filteration
from src.merge import chose_dataSet_menu_for_combining
from src.exporter import export_final_data
from src.config import loader_animation
from src.insights import insights_menu
from src.loader import dataFrames


class App:
    
    def launch(self):
        
        print("="*41)
        print("Welcome To A Student Data Analytic System")
        print("="*41)
        print("\nLoading DataSets",end="")
        loader_animation()
        print("\nDataSets Loaded Successfully\n")
        
        while True:
            print("-"*20)
            print("Main Menu of System.")
            print("-"*20)
            print("\nSelect Your Operation from Main Menu.")
            print("1: Data Inspection.")
            print("2: Data Filtering.")
            print("3: Data Refining.")
            print("4: CRUD Operations (Create|Read|Update|Delete).")
            print("5: Data Analysis.")
            print("6: Data Merging/Joining.")
            print("7: Show Insights.")
            print("8: Export / Save Excel.")
            print("0: Close Application.")
            
            choice = int(input("\nEnter Choice from Above Menu (0-8): "))
            
            if choice == 1:
                chose_dataSet_menu_for_inspection(dataFrames=dataFrames)
            elif choice == 2:
                chose_dataSet_menu_for_filteration(dataFrames=dataFrames)
            elif choice == 3:
                chose_dataSet_menu_for_refining(dataFrames=dataFrames)
            elif choice == 4:
                chose_dataSet_menu_for_crud(dataFrames=dataFrames)
            elif choice == 5:
                chose_dataSet_menu_for_analysis(dataFrames=dataFrames)
            elif choice == 6:
                chose_dataSet_menu_for_combining(dataFrames=dataFrames)
            elif choice == 7:
                insights_menu(dataFrames=dataFrames)
            elif choice == 8:
                export_final_data(dataFrames=dataFrames)
            elif choice == 0:
                print("Closing Application",end="")
                loader_animation()
                print("\nApplication Closed")
                break
            else:
                print("Invalid Choice ! Chose B/W (0-8) ")
                

if __name__ == "__main__":
    app = App()
    app.launch()