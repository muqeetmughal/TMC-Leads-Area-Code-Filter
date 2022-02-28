import pandas as pd
import math
import numpy
import time
import os
import datetime

# filepath = input("Enter Filepath: ")

ROOT_DIR = os.path.dirname(os.path.abspath(__file__))

print(ROOT_DIR)
timestr = time.strftime("%Y%m%d-%H%M%S")
try:
    os.mkdir(os.path.join(ROOT_DIR, "output"))
except:
    pass

filepath = r"input\\TMC Fresh 236K 02242022.csv"
filename = filepath.split(r"\\")[-1].split(".")[-2]
print(filename)
try:
    os.mkdir(os.path.join(ROOT_DIR, "output", filename))
except:
    pass
data = pd.read_csv(filepath, dtype=object, low_memory=False)
# print(data)


flatten_data = data.to_numpy().flatten()
print("Here", flatten_data)
flatten_data = numpy.array(
    [x for x in flatten_data.astype(object) if x is not numpy.nan])
print("Here", flatten_data)

flatten_dataframe = pd.DataFrame(flatten_data, columns=['phone_number'])
# print(flatten_dataframe)


# true_or_false = flatten_dataframe['phone_number'].astype(str).str[:3].str.contains('202|204|206|209|213|216|219|220|226|231|234|236|248|249|250|253|260|262|269|274|279|283|289|306|308|310|313|314|317|323|326|330|339|340|341|343|351|360|365|367|368|369|380|402|403|408|413|414|415|416|417|418|419|424|425|431|437|438|440|442|450|463|474|506|508|509|510|513|514|517|519|530|531|534|548|557|559|562|564|567|573|574|579|581|582|586|587|604|608|613|614|616|617|619|626|627|628|636|639|647|650|657|660|661|669|671|672|679|684|705|707|714|715|734|740|742|747|752|760|764|765|771|774|778|780|781|782|787|805|807|810|812|816|818|819|820|825|831|840|857|858|867|873|902|905|906|907|909|916|920|925|930|935|937|939|947|949|951|975|978|989')
# # print(flatten_dataframe)
# print(true_or_false)


result = flatten_dataframe[~(flatten_dataframe['phone_number'].astype(str).str[:3].str.contains('202|204|206|209|213|216|219|220|226|231|234|236|248|249|250|253|260|262|269|274|279|283|289|306|308|310|313|314|317|323|326|330|339|340|341|343|351|360|365|367|368|369|380|402|403|408|413|414|415|416|417|418|419|424|425|431|437|438|440|442|450|463|474|506|508|509|510|513|514|517|519|530|531|534|548|557|559|562|564|567|573|574|579|581|582|586|587|604|608|613|614|616|617|619|626|627|628|636|639|647|650|657|660|661|669|671|672|679|684|705|707|714|715|734|740|742|747|752|760|764|765|771|774|778|780|781|782|787|805|807|810|812|816|818|819|820|825|831|840|857|858|867|873|902|905|906|907|909|916|920|925|930|935|937|939|947|949|951|975|978|989'))]
# output_array = result.to_numpy().flatten()

# print("Output Array is:", output_array)


def values_for_reshape_unsorted(array):

    array_length = len(array)

    row = 1000000

    col = array_length//row

    if array_length > (row*col):
        col = col+1

    print(row, col)

    return row, col


def values_for_reshape_sorted(array):

    array_length = len(array)
    print("Lenght of array is", array_length)

    nearest_perfect_square_of_array_length = round(math.sqrt(array_length))**2

    print("Nearest PS is :", nearest_perfect_square_of_array_length)

    if array_length >= nearest_perfect_square_of_array_length:

        nearest_perfect_square_of_array_length = (
            round(math.sqrt(array_length))+1)**2

    print("Nearest PS 2 is :", nearest_perfect_square_of_array_length)

    col = 5
    row = nearest_perfect_square_of_array_length//col

    if row > 1000000:
        col = col + 1
        row = 1000000

    print(row, col)

    return row, col



np_array = result.to_numpy().flatten()
#-------checks to implement on np_array--

np_array = numpy.array([str(el)[-10:] for el in np_array.astype(object) if len(str(el)) >= 10])

if len(np_array) > 1000000:
    row, col = values_for_reshape_sorted(np_array)
else:
    row, col = values_for_reshape_unsorted(np_array)


total_length = row * col

current_length = len(np_array)

length_of_nan = total_length-current_length


final_1d_array = numpy.array_split(np_array, col)

# print(total_length, current_length, length_of_nan)
# print(numpy.array(final_1d_array,dtype=object))
out_array = numpy.array(final_1d_array, dtype=object)
# print(len(final_1d_array))

i = 1
for array in final_1d_array:

    df = pd.DataFrame(array)
    df['Date'] = datetime.date.today()
    df.set_axis(["Phone","Date"],axis=1,inplace=True)


    df.to_csv(f"output/{filename}/file_{i}.csv", index=False)

    i = i + 1
