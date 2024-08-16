import pandas as pd
import numpy as np  

<<<<<<< HEAD
# with open('test_data.csv', 'r') as csvfile:
#     # creating a csv reader object
#     csvreader = csv.reader(csvfile)
# print(csvreader)
=======
dt_test = pd.read_csv(fr'test_ds\all_purs\raw_data_0a14f818-b0de-11ec-b89c-e82aea2c97f4.csv')
#print(dt_test)
>>>>>>> 7170625fef7f5942d6c95fbce0112226bc5806c9

for i in ["THUMB_MCP", "THUMB_IP", 
            "INDEX_FINGER_PIP", "INDEX_FINGER_DIP",
            "MIDDLE_FINGER_PIP", "MIDDLE_FINGER_DIP",
            "RING_FINGER_PIP", "RING_FINGER_DIP",
            "PINKY_PIP", "PINKY_DIP",]:
    for j in ["x", "y", "z"]:
        dt_test = dt_test.drop(f"{i}.{j}", axis=1)

<<<<<<< HEAD
dt_test = pd.read_csv(r'raw_data_0a14f818-b0de-11ec-b89c-e82aea2c97f4.csv')
print(dt_test)

for i in ["THUMB_MCP", "THUMB_IP", 
          "INDEX_FINGER_PIP", "INDEX_FINGER_DIP",
          "MIDDLE_FINGER_PIP", "MIDDLE_FINGER_DIP",
          "RING_FINGER_PIP", "RING_FINGER_DIP",
          "PINKY_PIP", "PINKY_DIP",]:
    for j in ["x", "y", "z"]:
        dt_test = dt_test.drop(f"{i}.{j}", axis=1)

index_del = []

start = dt_test.copy()

=======
index_del = []

start = dt_test.copy()

>>>>>>> 7170625fef7f5942d6c95fbce0112226bc5806c9
ind_delit = 5
rasnos = 80
test_izm = 2
for ind in range(1, dt_test.shape[0]):
    # 2 вариант
    chk_izm = 1
    #if (ind == test_izm): print(ind)
    for ind_col in range(len(dt_test.columns)):
        #if (ind == test_izm): print(dt_test.columns[ind_col], dt_test.iloc[ind-1, ind_col], dt_test.iloc[ind, ind_col], round(abs(dt_test.iloc[ind, ind_col] - dt_test.iloc[ind-1, ind_col]) * pow(10, ind_delit+1)), rasnos)
        if dt_test.iloc[ind, ind_col] != 0 and dt_test.iloc[ind-1, ind_col] != 0 and round(abs(dt_test.iloc[ind, ind_col] - dt_test.iloc[ind-1, ind_col]) * pow(10, ind_delit+1)) <= rasnos: 
            chk_izm = 0
            break
    #if (ind == test_izm): print()
    
    if (chk_izm == 1): index_del.append(ind-1)

<<<<<<< HEAD
print(index_del)
dt_test = dt_test.drop(index_del, axis=0)

print(len(start))
start.iloc[:20]

print(len(dt_test))
dt_test.iloc[:20]
=======
print("index")
print(index_del)
dt_test = dt_test.drop(index_del, axis=0)

print("start")
print(len(start))
#print(start.iloc[:20])

print("itog")
print(len(dt_test))
#print(dt_test.iloc[:20])
print()



# for name_f in pd.read_csv(r'test_ds\MLtest.csv')["имя файла данных"]:
#     dt_test = pd.read_csv(fr'test_ds\all_purs\{name_f}')
#     #print(dt_test)

#     for i in ["THUMB_MCP", "THUMB_IP", 
#               "INDEX_FINGER_PIP", "INDEX_FINGER_DIP",
#               "MIDDLE_FINGER_PIP", "MIDDLE_FINGER_DIP",
#               "RING_FINGER_PIP", "RING_FINGER_DIP",
#               "PINKY_PIP", "PINKY_DIP",]:
#         for j in ["x", "y", "z"]:
#             dt_test = dt_test.drop(f"{i}.{j}", axis=1)

#     index_del = []

#     start = dt_test.copy()

#     ind_delit = 5
#     rasnos = 80
#     test_izm = 2
#     for ind in range(1, dt_test.shape[0]):
#         # 2 вариант
#         chk_izm = 1
#         #if (ind == test_izm): print(ind)
#         for ind_col in range(len(dt_test.columns)):
#             #if (ind == test_izm): print(dt_test.columns[ind_col], dt_test.iloc[ind-1, ind_col], dt_test.iloc[ind, ind_col], round(abs(dt_test.iloc[ind, ind_col] - dt_test.iloc[ind-1, ind_col]) * pow(10, ind_delit+1)), rasnos)
#             if dt_test.iloc[ind, ind_col] != 0 and dt_test.iloc[ind-1, ind_col] != 0 and round(abs(dt_test.iloc[ind, ind_col] - dt_test.iloc[ind-1, ind_col]) * pow(10, ind_delit+1)) <= rasnos: 
#                 chk_izm = 0
#                 break
#         #if (ind == test_izm): print()
        
#         if (chk_izm == 1): index_del.append(ind-1)

#     print("index")
#     print(index_del)
#     dt_test = dt_test.drop(index_del, axis=0)

#     print("start")
#     print(len(start))
#     #print(start.iloc[:20])

#     print("itog")
#     print(len(dt_test))
#     #print(dt_test.iloc[:20])
#     print()
print("\n\nDONE")
>>>>>>> 7170625fef7f5942d6c95fbce0112226bc5806c9
