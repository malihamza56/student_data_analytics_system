
"""
Crude Module : Adding,Deleting,updating columns 
"""

import pandas as pd
class Crude :
    def __init__(self, dataframe):
        self.dataframe = dataframe

    def crude_menu(self):
        print("Please Choose from menu :")
        print("1.Add new column/columns : ")
        print("2.Delete column/columns : ")
        print("3.Update  column/columns : ")

    def add_column(self, lst : list[list]):
        choice = int(input("1 for adding one column, 2 for adding multiple columns : "))

        if choice == 1 : 
            column = input("Enter the name of column : ")
            self.dataframe[column] = [i for i in lst[0]]

        elif choice == 2 :
            columns = input("Enter the names of colums (comma separated)")
            lst_of_columns = columns.split(",")
            for col,val in zip(lst_of_columns, lst) :
                self.dataframe[col] = [i for i in val]

    def delete_columns(self):
        choice = int(input("1 for deleting one column, 2 for deleting multiple columns : "))

        if choice == 1 : 
            column = input("Enter the name of column : ")
            self.dataframe.drop(column, axis=1, inplace = True)

        elif choice == 2 :
            columns = input("Enter the names of colums (comma separated) : ")
            lst_of_colums = columns.split(",")
            self.dataframe.drop(lst_of_colums, axis = 1, inplace = True)

        else :
            print("Inavlid choice selected.")           

    
    def update_column(self, lst : list[list]):
        choice = int(input("1 for updating one column, 2 for updating multiple columns : "))

        if choice == 1 : 
            column = input("Enter the name of column : ")
            new_column_name = input("Enter the new column name if you want to cahnge it otherwise skip : ")
            self.dataframe[column] = [i for i in lst[0]]
            if new_column_name :
                self.dataframe.rename(columns = {column : new_column_name}, inplace = True)


        elif choice == 2 :
            columns = input("Enter the names of colums (comma separated)")
            new_column_name = input("Enter the new columns name (comma separated)if you want to cahnge it otherwise skip : ")

            lst_of_columns = columns.split(",")
            index = 0
            for col,val in zip(lst_of_columns, lst) :
                self.dataframe[col] = [i for i in val]
                if new_column_name :
                    self.dataframe.rename(columns = {col : new_column_name.split(",")[index]}, inplace = True)
                    index += 1         



# Testing
# 1. DataFrame banao 5 columns 10 rows ke sath
data = {
    'student_id': [101, 102, 103, 104, 105, 106, 107, 108, 109, 110],
    'name': ['Ali', 'Ahmed', 'Sara', 'Ayesha', 'Hamza', 'Fatima', 'Usman', 'Zainab', 'Bilal', 'Noor'],
    'city': ['Lahore', 'Karachi', 'Lahore', 'Multan', 'Karachi', 'Lahore', 'Islamabad', 'Multan', 'Lahore', 'Karachi'],
    'marks': [85, 90, 78, 88, 92, 76, 80, 89, 84, 91],
    'year': [2023, 2023, 2024, 2024, 2023, 2024, 2023, 2024, 2023, 2024]
}

df = pd.DataFrame(data)
# print(df)

a = Crude(df)

multi_columns = [
    # ['A', 'A+', 'B', 'A', 'A+', 'C', 'B+', 'A', 'B', 'A+']
]
multi_columns = [
    ['A', 'A+', 'B', 'A', 'A+', 'C', 'B+', 'A', 'B', 'A+'],
    ['Pass', 'Pass', 'Pass', 'Pass', 'Pass', 'Fail', 'Pass', 'Pass', 'Pass', 'Pass']
]
# a.add_column(multi_columns)
# a.delete_columns()
a.update_column(multi_columns)

print(df)



