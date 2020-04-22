this_year = 2020
age = input("What is your birthday DD/MM/YYYY: ")
year = age.split("/")[-1]
age = this_year - int(year)
candle = int(str(age)[-1])

cake = f"""
	___{"i"*candle}___
      |:H:a:p:p:y:|
    __|___________|__
   |^^^^^^^^^^^^^^^^^|
   |:B:i:r:t:h:d:a:y:|
   |                 |
   ~~~~~~~~~~~~~~~~~~~
"""

print(cake)
