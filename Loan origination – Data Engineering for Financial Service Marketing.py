import matplotlib.pyplot as plt
import pandas as pd
loan = pd.read_csv("loan default.csv")
loan_new = loan
yes = 'Y'

while yes == 'Y':
    variable = input('Enter Variable: ')
    comparison = input('Enter comparison >,<,= : ')
    value = input('Enter value of cutoff: ')
    
    if value.isalpha():
        value = value
    else:
        value = int(value)
    
    if comparison == '>':
        loan_new = loan_new[(loan_new[variable] > value)] 
    elif comparison == '<':
        loan_new = loan_new[(loan_new[variable] < value)]
    else:
        loan_new = loan_new[(loan_new[variable] == value)]
    
    yes = input('Do you want to slice by another variable (Y for yes?) ')


print(loan_new.head(10))    
    
loan_new.hist(column="Credit_score",bins=10, color = 'blue')
plt.title('Credit Scores for segmented data')
plt.xlabel('Credit_scores')
plt.ylabel('Number of Occurances')

loan_new.to_csv('loan_segmented.csv')




