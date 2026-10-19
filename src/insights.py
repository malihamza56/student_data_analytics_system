"""
Insights Module: Generate meaningful, data-driven insights from a Pandas DataFrame.
"""

import pandas as pd


class DataInsights:
    def __init__(self, dataSet, dataSetName="DataSet"):
        if not isinstance(dataSet, pd.DataFrame):
            raise TypeError("A valid Pandas DataFrame is required.")
        if dataSet.empty:
            raise ValueError("DataSet is empty. No insights can be generated.")

        self.dataSet = dataSet
        self.dataSetName = dataSetName

    def show_overview(self):
        try:
            df = self.dataSet
            print("\n" + "=" * 45)
            print(f"DATASET OVERVIEW: {self.dataSetName}")
            print("=" * 45)
            print(f"Total Rows       : {df.shape[0]:,}")
            print(f"Total Columns    : {df.shape[1]:,}")
            print(f"Duplicate Rows   : {df.duplicated().sum():,}")
            print(f"Total Missing    : {df.isna().sum().sum():,}")
            print(f"Memory Usage     : {df.memory_usage(deep=True).sum() / 1024:.2f} KB")
            print("\nColumn Data Types:")
            print(df.dtypes.to_string())
        except Exception as e:
            print(f"Failed to Generate Overview | Error: {e}")

    def show_data_quality(self):
        try:
            df = self.dataSet
            total_cells = df.shape[0] * df.shape[1]
            missing_total = int(df.isna().sum().sum())

            print("\n" + "=" * 45)
            print("DATA QUALITY INSIGHTS")
            print("=" * 45)

            if total_cells:
                missing_percent = (missing_total / total_cells) * 100
                print(f"Missing cells: {missing_total:,}/{total_cells:,} ({missing_percent:.2f}%)")

            missing = df.isna().sum()
            missing = missing[missing > 0].sort_values(ascending=False)

            if missing.empty:
                print("Great: no missing values were found.")
            else:
                print("\nColumns with missing values:")
                for column, count in missing.items():
                    percent = (count / len(df)) * 100
                    print(f"- {column}: {count} missing ({percent:.2f}%)")

            duplicate_count = int(df.duplicated().sum())
            if duplicate_count:
                duplicate_percent = (duplicate_count / len(df)) * 100
                print(f"\nReview duplicate rows: {duplicate_count} ({duplicate_percent:.2f}% of rows).")
            else:
                print("\nNo fully duplicated rows were found.")

            constant_columns = [
                column for column in df.columns
                if df[column].nunique(dropna=False) <= 1
            ]

            if constant_columns:
                print("\nColumns with one repeated value (or all missing):")
                for column in constant_columns:
                    print(f"- {column}")
            else:
                print("\nNo constant columns were detected.")
        except Exception as e:
            print(f"Failed to Generate Data Quality Insights | Error: {e}")

    def show_numeric_insights(self):
        try:
            df = self.dataSet
            numeric_df = df.select_dtypes(include="number")

            print("\n" + "=" * 45)
            print("NUMERICAL INSIGHTS")
            print("=" * 45)

            if numeric_df.empty:
                print("No numeric columns found for statistical analysis.")
                return

            print("\nStatistical Summary:")
            print(numeric_df.describe().round(2).to_string())

            print("\nColumn Highlights:")
            for column in numeric_df.columns:
                series = numeric_df[column].dropna()
                if series.empty:
                    print(f"- {column}: no non-missing numeric values.")
                    continue

                print(
                    f"- {column}: mean={series.mean():.2f}, "
                    f"median={series.median():.2f}, "
                    f"min={series.min():.2f}, max={series.max():.2f}"
                )

                if series.nunique() == 1:
                    print(f"  Observation: '{column}' has only one distinct numeric value.")

            if len(numeric_df.columns) >= 2:
                corr = numeric_df.corr()
                pairs = []
                columns = list(corr.columns)

                for i in range(len(columns)):
                    for j in range(i + 1, len(columns)):
                        value = corr.iloc[i, j]
                        if pd.notna(value):
                            pairs.append((columns[i], columns[j], value))

                if pairs:
                    pairs.sort(key=lambda item: abs(item[2]), reverse=True)
                    col_a, col_b, value = pairs[0]
                    print(f"\nStrongest observed numeric correlation: {col_a} and {col_b} (r={value:.2f}).")
                    print("Correlation indicates association, not proof that one variable causes the other.")
        except Exception as e:
            print(f"Failed to Generate Numerical Insights | Error: {e}")

    def show_categorical_insights(self, top_n=5):
        try:
            df = self.dataSet
            categorical_df = df.select_dtypes(include=["object", "string", "category", "bool"])

            print("\n" + "=" * 45)
            print("CATEGORICAL INSIGHTS")
            print("=" * 45)

            if categorical_df.empty:
                print("No text or categorical columns found.")
                return

            for column in categorical_df.columns:
                print(f"\nColumn: {column}")
                print(f"Unique non-missing values: {df[column].nunique(dropna=True)}")
                counts = df[column].value_counts(dropna=True).head(top_n)

                if counts.empty:
                    print("No non-missing values to summarize.")
                else:
                    print(f"Top {min(top_n, len(counts))} values:")
                    for value, count in counts.items():
                        percent = (count / len(df)) * 100
                        print(f"- {value}: {count} rows ({percent:.2f}% of all rows)")
        except Exception as e:
            print(f"Failed to Generate Categorical Insights | Error: {e}")

    def generate_all_insights(self):
        self.show_overview()
        self.show_data_quality()
        self.show_numeric_insights()
        self.show_categorical_insights()


def insights_menu(dataFrames):
    dataset_names = {
        1: "Students",
        2: "Marks",
        3: "Fees",
        4: "Courses",
        5: "Attendance",
        6: "Activities"
    }

    while True:
        print("\n" + "=" * 28)
        print("DATA INSIGHTS MENU")
        print("=" * 28)

        for key, name in dataset_names.items():
            print(f"{key}: {name} DataSet")

        print("7: Generate Insights for All DataSets")
        print("0: Back to Main Menu")

        try:
            choice = int(input("\nEnter Choice (0-7): "))
        except ValueError:
            print("Invalid Input! Enter an integer.")
            continue

        if choice == 0:
            break
        elif choice in dataset_names:
            dataSet = dataFrames.get(choice)
            if not isinstance(dataSet, pd.DataFrame) or dataSet.empty:
                print("DataSet Not Found or Empty!")
                continue

            insights = DataInsights(dataSet, dataset_names[choice])
            insights.generate_all_insights()

        elif choice == 7:
            for key, name in dataset_names.items():
                dataSet = dataFrames.get(key)
                if not isinstance(dataSet, pd.DataFrame) or dataSet.empty:
                    print(f"\nSkipping {name}: DataSet not found or empty.")
                    continue

                insights = DataInsights(dataSet, name)
                insights.generate_all_insights()
        else:
            print("Invalid Choice! Choose B/W (0-7).")
