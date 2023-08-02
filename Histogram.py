import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# Завантажуємо csv файл у DataFrame, пропустивши перший рядок
df = pd.read_csv('frequency.csv', header=None, skiprows=1, names=['word', 'count'])

# Відсікаємо слова, що містять менше 4 букв
df = df[df['word'].apply(lambda x: len(x) >= 5)]

# Сортуємо DataFrame у порядку спадання числа повторень
df = df.sort_values(by='count', ascending=False)

# Відбираємо топ 20 найбільш уживаних слів
top_20_words = df.head(20)

# Побудуємо гістограму з різними кольорами стовбців
colors = plt.cm.Paired(np.linspace(0, 1, len(top_20_words)))
plt.barh(top_20_words['word'], top_20_words['count'], color=colors)
plt.xlabel('Кількість повторень')
plt.ylabel('Слова')
plt.title('20 найбільш уживаних слів')

# Додамо аннотації зі значеннями над кожним стовбцем
for i, v in enumerate(top_20_words['count']):
    plt.text(v + 0.5, i, str(v), color='black')

# Встановимо явні значення осі X для правильного порядку
plt.xticks(np.arange(0, max(top_20_words['count']) + 10, 10))

plt.gca().invert_yaxis()  # Інвертуємо ось Y для зручності читання
plt.tight_layout()
plt.show()
