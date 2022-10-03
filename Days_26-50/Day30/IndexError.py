fruits = ["Apple", "Pear", "Orange"]

def make_pie(index):
    try:
      fruit = fruits[index]
    except IndexError:
      print("Fruit mixed pie")
    else:
      print(fruit + " pie")

#make_pie(2) is ok but not 4 as this is out of range
num = int(input("Enter the number for the type of pie you want: "))
make_pie(num)

