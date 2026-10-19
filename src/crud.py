
"""
Crude Module : Adding,Deleting,updating columns 
"""
import time

class Crud :
    def __init__(self, dataframe):
        self.dataframe = dataframe

        if len(dataframe) != 0:
            ...
        else:
            raise ValueError("DataSet not Loaded/Found !")

    def add_columns(self, lst : list[list]):
        
        try:
            print("\nChose Option:")
            print("1: Add One Column.")
            print("2: Add Multiple Columns")
            
            choice = int(input("Enter Choice from Above Menu: "))
            
            if choice == 1 : 
                column = input("Enter the name of column : ")
                self.dataframe[column] = [i for i in lst[0]]

            elif choice == 2 :
                columns = input("Enter the names of colums (comma separated)")
                lst_of_columns = columns.split(",")
                for col,subList in zip(lst_of_columns, lst) :
                    self.dataframe[col] = [value for value in subList]
        except Exception as e:
            print(f"Failed to Add Column(s)|Error {e}")
            
    def delete_columns(self):
        try:
            print("\nChose Option:")
            print("1: Delete One Column.")
            print("2: Delete Multiple Columns")
            
            choice = int(input("Choose option from Above Menu: "))

            if choice == 1 : 
                column = input("Enter the name of column : ")
                self.dataframe.drop(column, axis=1, inplace = True)
            elif choice == 2 :
                columns = input("Enter the names of colums (comma separated) : ")
                lst_of_colums = columns.split(",")
                self.dataframe.drop(lst_of_colums, axis = 1, inplace = True)
            else :
                print("Inavlid choice ! Choose B/W (1-2).")           
        except Exception as e:
            print(f"Failed to Delete Column(s)| Error {e}")
        
    def update_columns(self, lst : list[list]):
        
        try:    
            print("\nChose Option:")
            print("1: Delete One Column.")
            print("2: Delete Multiple Columns")
                    
            choice = int(input("Choose option from Above Menu: "))

            if choice == 1 : 
                column = input("Enter the name of column to update : ")
                new_column_name = input("Enter the new column name (Press Enter to skip): ")
                self.dataframe[column] = [i for i in lst[0]]
                if new_column_name :
                    self.dataframe.rename(columns = {column : new_column_name}, inplace = True)
                    
            elif choice == 2 :
                columns = input("Enter the names of colums (comma separated): ")
                new_column_name = input("Enter the new columns name (comma separated)/Press Enter to skip : ")

                lst_of_columns = columns.split(",")
                index = 0
                for col,val in zip(lst_of_columns, lst) :
                    self.dataframe[col] = [i for i in val]
                    if new_column_name :
                        self.dataframe.rename(columns = {col : new_column_name.split(",")[index]}, inplace = True)
                        index += 1
        except Exception as e:
            print(f"Failed to Update Column(s)| Error {e}")


def chose_dataSet_menu_for_crud(dataFrames):
    
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
            stu_crud = Crud(dataset=stu_df)
            crud_menu(stu_crud)
        elif choice == 2:
            marks_df = dataFrames.get(2)
            marks_crud = Crud(dataset=marks_df)
            crud_menu(marks_crud)
        elif choice == 3:
            fee_df = dataFrames.get(3)
            fee_crud = Crud(dataset=fee_df)
            crud_menu(fee_crud)
        elif choice == 4:
            courses_df = dataFrames.get(4)
            course_crud = Crud(dataset=courses_df)
            crud_menu(course_crud)
        elif choice == 5:
            attendance_df = dataFrames.get(5)
            attendance_crud = Crud(dataset=attendance_df)
            crud_menu(attendance_crud)
        elif choice == 6:
            activities_df = dataFrames.get(6)
            activities_crud = Crud(dataset=activities_df)
            crud_menu(activities_crud)
        elif choice == 0:
            print("Navigating to Main Menu...\nWait for 2 sec...\n")
            time.sleep(2)
            break
        else:
            print("Invalid Choice ! Choice must B/W (0-5).")
                 
def crud_menu(crud_object):
    
    print()
    while True:
        print()
        print("="*24)
        print("DataSet Inspection Menu")
        print("="*24)

        print("\nChose Operation from below:")
        print("1: Add Column(s).")
        print("2: Delete Column(s).")
        print("3: Update Column(s).")
        print("0: Back To DataSet Menu.")
        
        choice = int(input("\nEnter Choice B/W (0-3): "))

        if choice == 1:
            crud_object.add_columns()
        elif choice == 2:
            crud_object.delete_columns()
        elif choice == 3:
            crud_object.update_columns()
        elif choice == 0:
            print()
            print("\nNavigating to DataSet Selection Menu...\nWait for 2 Sec...")
            time.sleep(2)
            break
        else:
            print("\nInvalid Choice! Chose B/W (0-6)")
            
            


# print("DataFrame rows:", len(df2))
# print("List length:", len(result))
# print("First nested list length:", len(result[0]))
# Crude Module: Adding, Deleting, and Updating DataFrame Columns
# """

# import time
# import pandas as pd


# class Crud:

#     def __init__(self, dataset):
#         self.dataset = dataset

#         if len(dataset) != 0:
#             ...
#         else:
#             raise ValueError("DataSet Not Loaded/Found! ")

#     def get_choice(self, message, valid_choices):
        
#         try:
#             choice = int(input(message))
#             if choice not in valid_choices:
#                 print("Invalid Choice! Select a valid option.")
#                 return None
#             return choice
#         except ValueError:
#             print("Invalid Input! Enter an integer.")
#             return None

#     def get_column_values(self, column_name):
        
#         values = input(
#             f"Enter values for '{column_name}' "
#             "(comma separated): "
#         ).split(",")

#         values = [value.strip() for value in values]

#         if len(values) != len(self.dataset):
#             raise ValueError(
#                 f"Expected {len(self.dataset)} values, "
#                 f"but received {len(values)}."
#             )

#         if any(value == "" for value in values):
#             raise ValueError("Column values cannot be empty.")

#         return values

#     # CRUD Methods

#     def add_column(self):
#         try:
#             choice = self.get_choice(
#                 "\n1: Add One Column\n"
#                 "2: Add Multiple Columns\n"
#                 "Enter Choice (1-2): ",
#                 {1, 2}
#             )

#             if choice is None:
#                 return

#             if choice == 1:
#                 column = input(
#                     "Enter the name of the new column: "
#                 ).strip()

#                 if not column:
#                     raise ValueError("Column name cannot be empty.")

#                 if column in self.dataset.columns:
#                     raise ValueError(
#                         f"Column '{column}' already exists."
#                     )

#                 values = self.get_column_values(column)
#                 self.dataset[column] = values

#                 print(f"Column '{column}' added successfully.")

#             elif choice == 2:
#                 columns = input(
#                     "Enter new column names (comma separated): "
#                 ).split(",")

#                 columns = [col.strip() for col in columns]

#                 if not columns or any(not col for col in columns):
#                     raise ValueError("Column names cannot be empty.")

#                 if len(columns) != len(set(columns)):
#                     raise ValueError(
#                         "Duplicate column names are not allowed."
#                     )

#                 existing = [
#                     col for col in columns
#                     if col in self.dataset.columns
#                 ]

#                 if existing:
#                     raise ValueError(
#                         f"These columns already exist: {existing}"
#                     )

#                 new_data = {}

#                 for column in columns:
#                     new_data[column] = self.get_column_values(column)

#                 for column, values in new_data.items():
#                     self.dataset[column] = values

#                 print("All columns added successfully.")

#         except Exception as e:
#             print(f"Failed to Add Column(s)...|Error: {e}")

#     def delete_columns(self):
#         try:
#             choice = self.get_choice(
#                 "\n1: Delete One Column\n"
#                 "2: Delete Multiple Columns\n"
#                 "Enter Choice (1-2): ",
#                 {1, 2}
#             )

#             if choice is None:
#                 return

#             if choice == 1:
#                 column = input(
#                     "Enter the column name to delete: "
#                 ).strip()

#                 if column not in self.dataset.columns:
#                     raise KeyError(
#                         f"Column '{column}' does not exist."
#                     )

#                 self.dataset.drop(columns=[column], inplace=True)

#                 print(f"Column '{column}' deleted successfully.")

#             elif choice == 2:
#                 columns = input(
#                     "Enter column names to delete "
#                     "(comma separated): "
#                 ).split(",")

#                 columns = [col.strip() for col in columns]

#                 if not columns or any(not col for col in columns):
#                     raise ValueError("Column names cannot be empty.")

#                 if len(columns) != len(set(columns)):
#                     raise ValueError(
#                         "Duplicate column names are not allowed."
#                     )

#                 missing = [
#                     col for col in columns
#                     if col not in self.dataset.columns
#                 ]

#                 if missing:
#                     raise KeyError(
#                         f"These columns do not exist: {missing}"
#                     )

#                 self.dataset.drop(columns=columns, inplace=True)

#                 print("All selected columns deleted successfully.")

#         except Exception as e:
#             print(f"Failed to Delete Column(s)...|Error: {e}")

#     def update_column(self):
#         try:
#             choice = self.get_choice(
#                 "\n1: Update One Column\n"
#                 "2: Update Multiple Columns\n"
#                 "Enter Choice (1-2): ",
#                 {1, 2}
#             )

#             if choice is None:
#                 return

#             if choice == 1:
#                 column = input(
#                     "Enter the existing column name: "
#                 ).strip()

#                 if column not in self.dataset.columns:
#                     raise KeyError(
#                         f"Column '{column}' does not exist."
#                     )

#                 values = self.get_column_values(column)

#                 new_name = input(
#                     "Enter a new column name "
#                     "(press Enter to keep the current name): "
#                 ).strip()

#                 if new_name and new_name != column:
#                     if new_name in self.dataset.columns:
#                         raise ValueError(
#                             f"Column '{new_name}' already exists."
#                         )

#                 # Validate first, then apply changes.
#                 self.dataset[column] = values

#                 if new_name and new_name != column:
#                     self.dataset.rename(
#                         columns={column: new_name},
#                         inplace=True
#                     )

#                 print(f"Column '{column}' updated successfully.")

#             elif choice == 2:
#                 columns = input(
#                     "Enter existing column names "
#                     "(comma separated): "
#                 ).split(",")

#                 columns = [col.strip() for col in columns]

#                 if not columns or any(not col for col in columns):
#                     raise ValueError("Column names cannot be empty.")

#                 if len(columns) != len(set(columns)):
#                     raise ValueError(
#                         "Duplicate column names are not allowed."
#                     )

#                 missing = [
#                     col for col in columns
#                     if col not in self.dataset.columns
#                 ]

#                 if missing:
#                     raise KeyError(
#                         f"These columns do not exist: {missing}"
#                     )

#                 new_data = {}

#                 for column in columns:
#                     new_data[column] = self.get_column_values(column)

#                 rename_input = input(
#                     "Enter new names for all selected columns "
#                     "in the same order, comma separated "
#                     "(press Enter to keep current names): "
#                 ).strip()

#                 rename_map = {}

#                 if rename_input:
#                     new_names = [
#                         name.strip()
#                         for name in rename_input.split(",")
#                     ]

#                     if len(new_names) != len(columns):
#                         raise ValueError(
#                             "The number of new names must match "
#                             "the number of selected columns."
#                         )

#                     if any(not name for name in new_names):
#                         raise ValueError(
#                             "New column names cannot be empty."
#                         )

#                     final_names = [
#                         rename_map.get(col, col)
#                         for col in columns
#                     ]

#                     if len(new_names) != len(set(new_names)):
#                         raise ValueError(
#                             "Duplicate new column names are not allowed."
#                         )

#                     # Unselected columns must not be overwritten.
#                     selected_set = set(columns)
#                     conflicts = [
#                         name for name in new_names
#                         if name in self.dataset.columns
#                         and name not in selected_set
#                     ]

#                     if conflicts:
#                         raise ValueError(
#                             f"These new names already exist: {conflicts}"
#                         )

#                     rename_map = dict(zip(columns, new_names))

#                 # Apply value updates only after validating all inputs.
#                 for column, values in new_data.items():
#                     self.dataset[column] = values

#                 if rename_map:
#                     self.dataset.rename(
#                         columns=rename_map,
#                         inplace=True
#                     )

#                 print("All selected columns updated successfully.")

#         except Exception as e:
#             print(f"Failed to Update Column(s)...|Error: {e}")


# def chose_dataSet_menu_for_crude(dataFrames):

#     print()

#     while True:
#         print()
#         print("=" * 19)
#         print("Available DataSets")
#         print("=" * 19)

#         print("\nChoose DataSet option from below:")
#         print("1: Students DataSet.")
#         print("2: Marks DataSet.")
#         print("3: Fees DataSet.")
#         print("4: Courses DataSet.")
#         print("5: Attendance DataSet.")
#         print("6: Activities DataSet.")
#         print("0: Back To Main Menu.")

        
#         choice = int(input("\nEnter Choice B/W (0-5): "))
                
#         if choice == 1:
#             stu_df = dataFrames.get(1)
#             stu_insp = Crud(dataset=stu_df)
#             crude_menu(stu_insp)
#         elif choice == 2:
#             marks_df = dataFrames.get(2)
#             marks_insp = Crud(dataset=marks_df)
#             crude_menu(marks_insp)
#         elif choice == 3:
#             fee_df = dataFrames.get(3)
#             fee_insp = Crud(dataset=fee_df)
#             crude_menu(fee_insp)
#         elif choice == 4:
#             courses_df = dataFrames.get(4)
#             course_insp = Crud(dataset=courses_df)
#             crude_menu(course_insp)
#         elif choice == 5:
#             attendance_df = dataFrames.get(5)
#             attendance_insp = Crud(dataset=attendance_df)
#             crude_menu(attendance_insp)
#         elif choice == 6:
#             activities_df = dataFrames.get(6)
#             activities_insp = Crud(dataset=activities_df)
#             crude_menu(activities_insp)
#         elif choice == 0:
#             print("Navigating to Main Menu...\nWait for 2 sec...\n")
#             time.sleep(2)
#             break
#         else:
#             print("Invalid Choice ! Choice must B/W (0-5).")
                         

# def crude_menu(crude_object):

#     print()

#     while True:
#         print()
#         print("=" * 24)
#         print("DataSet CRUD Menu")
#         print("=" * 24)

#         print("\nChoose Operation from below:")
#         print("1: Add Column(s).")
#         print("2: Delete Column(s).")
#         print("3: Update Column(s).")
#         print("0: Back To DataSet Selection Menu.")

#         try:
#             choice = int(input("\nEnter Choice B/W (0-3): "))
#         except ValueError:
#             print("Invalid Input! Enter an integer.")
#             continue

#         if choice == 1:
#             crude_object.add_column()
#             print("\nCurrent DataSet:")
#             print(crude_object.dataset)

#         elif choice == 2:
#             crude_object.delete_columns()
#             print("\nCurrent DataSet:")
#             print(crude_object.dataset)

#         elif choice == 3:
#             crude_object.update_column()
#             print("\nCurrent DataSet:")
#             print(crude_object.dataset)

#         elif choice == 0:
#             print("\nNavigating to DataSet Selection Menu...\n"
#                 "Wait for 2 sec...")
#             time.sleep(2)
#             break

#         else:
#             print("\nInvalid Choice! Choose B/W (0-3).")
