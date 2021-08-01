import pandas as pd

df = pd.read_csv('https://raw.githubusercontent.com/Captmoonshot/sentiment_analysis/master/movie_data.csv')

choices = pd.Series(['Male', 'Female'])

gender = choices.sample(n=50000, replace=True)

df['gender'] = gender.values
print(df['gender'])