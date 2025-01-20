# Titanic Data Analysis and Cleaning Project

Welcome to the Titanic Data Analysis and Cleaning Project repository! This project involves cleaning and preparing the Titanic dataset for analysis and modeling. The notebook explores techniques for handling missing data, transforming features, and saving processed data for future use.

---

## Table of Contents
1. [Project Overview](#project-overview)
2. [Dataset Description](#dataset-description)
3. [Data Cleaning Steps](#data-cleaning-steps)
4. [Feature Engineering](#feature-engineering)
5. [Output and Saved Data](#output-and-saved-data)
6. [Repository Structure](#repository-structure)
7. [How to Run the Project](#how-to-run-the-project)

---

## Project Overview
The Titanic dataset provides information about passengers aboard the RMS Titanic, including demographics, ticket information, and survival status. This project focuses on preparing the data for machine learning tasks by:

- Handling missing values.
- Dropping irrelevant or redundant columns.
- Transforming and cleaning features.
- Saving the cleaned dataset for further analysis.

---

## Dataset Description
The dataset used in this project contains the following columns:

- **PassengerId**: Unique identifier for each passenger.
- **Survived**: Target variable (1 = survived, 0 = did not survive).
- **Pclass**: Passenger class (1 = First, 2 = Second, 3 = Third).
- **Name**: Name of the passenger.
- **Sex**: Gender of the passenger.
- **Age**: Age of the passenger.
- **SibSp**: Number of siblings/spouses aboard.
- **Parch**: Number of parents/children aboard.
- **Ticket**: Ticket number.
- **Fare**: Fare paid for the ticket.
- **Cabin**: Cabin number.
- **Embarked**: Port of embarkation (C = Cherbourg, Q = Queenstown, S = Southampton).

---

## Data Cleaning Steps
### Handling Missing Values
1. **Age**:
   - Filled missing values with the mean age.
2. **Embarked**:
   - Imputed missing values with the most frequent category ('Q').

### Dropping Columns
- Removed columns that were deemed unnecessary for analysis or modeling:
  - `Name`, `Fare`, `PassengerId`, `Ticket`, `Cabin`, and `Embarked`.

### Data Type Adjustments
- Converted the `Age` column from float to integer after filling missing values.

---

## Feature Engineering
- Created a copy of the dataset (`df`) for further processing.
- Cleaned and prepared data for analysis by removing irrelevant features and ensuring consistency across columns.

---

## Output and Saved Data
The cleaned dataset is saved for future use. This includes:
- Removing unnecessary columns.
- Imputing missing values.
- Ensuring all columns are in appropriate formats for analysis.

---

## Repository Structure
```
├── data
│   ├── titanic-passengers.csv
├── notebooks
│   ├── Data_Analytic.ipynb
├── processed_data
│   ├── cleaned_data.csv
├── README.md
```

### File Descriptions
- **data/**: Raw Titanic dataset.
- **notebooks/**: Jupyter notebook for data cleaning and processing.
- **processed_data/**: Directory for cleaned and processed datasets.
- **README.md**: Documentation for the project.

---

## How to Run the Project
### Prerequisites
- Python 3.8+
- Required libraries: pandas, numpy

### Steps
1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/titanic-data-cleaning.git
   cd titanic-data-cleaning
   ```
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Open the Jupyter notebook:
   ```bash
   jupyter notebook notebooks/Data_Analytic.ipynb
   ```
4. Run the notebook cells to clean and process the data.

---

## Conclusion
This project highlights essential steps for cleaning and preparing data for machine learning. The cleaned dataset is now ready for exploratory analysis and modeling. For any questions or contributions, feel free to open an issue or contact me directly.

---

**Author**: Kingsley Sunday
**GitHub Repository**: [Titanic Data Cleaning Project](https://github.com/princekingsleysunday/Titanic_Passenger)


