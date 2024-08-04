import pandas as pd
import random

# Генерация данных
lst = ['robot'] * 10
lst += ['human'] * 10
random.shuffle(lst)
data = pd.DataFrame({'whoAmI': lst})

# Получение уникальных значений из столбца
unique_values = data['whoAmI'].unique()

# Создание новых столбцов для каждой уникальной категории
for value in unique_values:
    data[value] = (data['whoAmI'] == value).astype(int)
    
# Удаление исходного столбца
data = data.drop(columns=['whoAmI'])

print(data.head())