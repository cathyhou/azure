import seaborn as sn
import pandas as pd
import matplotlib.pyplot as plt
from openpyxl import load_workbook

wb = load_workbook(filename = 'results.xlsx')
ws = wb['results']
array = [[0,0,0,0,0], [0,0,0,0,0], [0,0,0,0,0], [0,0,0,0,0], [0,0,0,0,0]]


def change(emo):
    emotions = ['HAPPY', 'NEUTRAL', 'SCARED', 'ANGRY', 'SAD']
    for i in range(5):
        if emo == emotions[i]:
            return i
    return 'error'


for row in range(128):
    r = str(row + 2)
    predicted = change(ws['B'+r].value)
    true = change(ws['E'+r].value)
    if predicted == 'error' or true == 'error':
        continue
    else:
        current = array[true][predicted]
        array[true][predicted] = current + 1


df_cm = pd.DataFrame(array, columns=["HAPPY","NEUTRAL","SCARED","ANGRY","SAD"], index=["HAPPY","NEUTRAL","SCARED","ANGRY","SAD"] )
plt.figure(figsize = (10,10))
sn.set(font_scale=1)
ax = sn.heatmap(df_cm, annot=True,annot_kws={"size": 10}, cbar=False, cmap='Blues')# font size
ax.xaxis.tick_top()
ax.xaxis.set_ticks_position('none')
ax.set_xlabel('Predicted \n', fontsize=16)
ax.xaxis.set_label_position('top')
plt.yticks(va='center')
plt.ylabel('True \n', fontsize=16)
#plt.show()

array2 = array

for row in range(5):
    s = 0
    for col in range(5):
        s = s + array2[row][col]
    for col in range(5):
        current = array2[row][col]
        array2[row][col] = round(current/s * 100.00, 1)

df_cm = pd.DataFrame(array2, columns=["HAPPY","NEUTRAL","SCARED","ANGRY","SAD"], index=["HAPPY","NEUTRAL","SCARED","ANGRY","SAD"] )
plt.figure(figsize = (10,10))
sn.set(font_scale=1)
ax = sn.heatmap(df_cm, annot=True,annot_kws={"size": 10}, cbar=False, cmap='Blues', fmt='g')# font size
ax.xaxis.tick_top()
ax.xaxis.set_ticks_position('none')
ax.set_xlabel('Predicted \n', fontsize=16)
ax.xaxis.set_label_position('top')
plt.yticks(va='center')
plt.ylabel('True \n', fontsize=16)
plt.show()
