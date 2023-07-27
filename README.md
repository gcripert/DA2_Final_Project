# Customer Trends in Fashion Retail: A Data Analysis Project

### Overview

This is my final project for Code Louisville's Data Analysis track, ending summer 2023. I will be delving into some data sets from the clothing retail company H&M. The sets contain two years of data including customer transaction history, customer demographics, and articles purchased. My objective is to clean and combine the data into a more easily readable database format, then identify and interpret trends in customer purchases over time. As one of the largest international clothing retailers, I am particularly interested in examining how well H&M's target age demographic aligns with actual purchases. Furthermore, I would like to determine the average spending for each given age group.  A visualization of these results can be viewed on my Tableau Pubilc [profile](https://public.tableau.com/views/FashionData/Dashboard1?:language=en-US&publish=yes&:display_count=n&:origin=viz_share_link).


### Data Download

Data was downloaded in csv format from https://www.kaggle.com/competitions/h-and-m-personalized-fashion-recommendations/data, then extracted to the folder titled 'Data' in this repository. In order to access this data, it is necessary to have an active Kaggle account from which you must accept the rules of the competition as set forth by H&M. **NOTE:** the competition is no longer active and the rules state that the data is acceptable for use in educational purposes, which is my intent. 

Fork and clone this repository to your local machine and initialize a virtual environment by following the steps below. **NOTE** the file titled 'transactions_train.csv' is roughly 3.5 GB and as such may take longer to load.


### Setting Up The Virtual Environment

Python 3.11 is needed to run this program

For Windows users: 
  - if using GitBash, make sure you are in the correct folder, then enter the following commands:
    ```
      py -m venv venv
      source venv/Scripts/activate
      pip install -r requirements.txt
    ```
  - if using Command Prompt:
    ```
      py -m venv venv
      venv\Scripts\activate
      pip install -r requirements.txt
    ```
   
For Mac OS users:
  - using GitBash, make sure you are in the correct folder, then enter the following commands:
    ```
      py -m venv venv
      source venv/bin/activate
      pip install -r requirements.txt
    ```
   
Run Fashion_Analysis.py:
```
py Fashion_Analysis.py

```
   

### Project Conclusions

H&M markets itself primarily to a teenage and young adult audience, which is well reflected in the customer age distribution visualization. One might reasonably attribute this to the brand's relatively low average price point per article and rapid turnover of inventory, in keeping with ever-changing fashion trends. It is interesting that there is a distinct increase in the 45-54 year age group as well. I would hypothesize that this is because adults in this age range are more likely to have teen/young adult children themselves for whom they are buying H&M products. Additionally, there is a slight upward trend in average price per transaction according to age group. This is not too surprising, given that teens are much less likely to have significant disposable income than adults who have already spent years in the workforce.
    



## Code Louisville Project Requirements

### Feature 1: Loading Data

I set up a SQLite database to read in the CSV files downloaded from Kaggle into a new, empty table

### Feature 2: Cleaning and Operating on the Data

I determined data types for each colums as not all rows had values for each colums and eliminated rows lacking necessary information such as 'customer age' and 'price'. I then joined the CSVs into the SQLite table based on like column headers

### Feature 3: Data Visualization

I created a dashboard using Tablea Public to display key findings. Customer age distribution is displayed in a pie chart, with each segment representing a roughly 10-year span. **NOTE** The lowest age range is only 9 years, as customer age data begins at 16 years old. Total expenditures per age group and average transaction price per age group are both displayed in bar chart format. 

### Feature 4: Best Practices/Project Enhancement

I utilized a virtual environment for the creation of this code and have included a requirements.txt file containing all necessary packages as well as instructions for installation 

### Feature 5: Annotation and Interpretation

I have thoroughly annotated my code with concise but useful statements that explain my actions and intentions. Additionally, following the instructions for how to run my program, I have included my personal throughts and conclusions drawn from the data I analyzed. 

