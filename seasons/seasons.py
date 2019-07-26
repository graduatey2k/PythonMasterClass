month = input("enter month")
day = input("enter day")

spring = ['March', 'April', 'May', 'June']
summer = ['June', 'July','August', 'September']
autumn = ['September', 'October', 'November', 'December']
winter = ['December', 'January', 'February','March']

March_spring_day = ["20", "21", "22", "23", "24", "25", "26", "27", "28", "29", "30"]
April_day = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12", "13", "14", "15", "16", "17", "18", "19", "20", "21", "22", "23", "24", "25", "26", "27", "28", "29", "30"]
May_day = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31]
June_day = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]

JuneSummer_day = [21, 22, 23, 24, 25, 26, 27, 28, 29, 30]
July_day = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12", "13", "14", "15", "16", "17", "18", "19", "20", "21", "22", "23", "24", "25", "26", "27", "28", "29", "30", "31"]
August_day = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12", "13", "14", "15", "16", "17", "18", "19", "20", "21", "22", "23", "24", "25", "26", "27", "28", "29", "30", "31"]
September_day = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12", "13", "14", "15", "16", "17", "18", "19", "20"]

SeptemberAutumn_day = ["21", "22", "23", "24", "25", "26", "27", "28", "29", "30"]
October_day = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12", "13", "14", "15", "16", "17", "18", "19", "20", "21", "22", "23", "24", "25", "26", "27", "28", "29", "30", "31"]
November_day = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12", "13", "14", "15", "16", "17", "18", "19", "20", "21", "22", "23", "24", "25", "26", "27", "28", "29", "30"]
December_day = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12", "13", "14", "15", "16", "17", "18", "19", "20"]

December_winter_day = [ "21", "22", "23", "24", "25", "26", "27", "28", "29", "30","31"]
January_day = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12", "13", "14", "15", "16", "17", "18", "19", "20", "21", "22", "23", "24", "25", "26", "27", "28", "29", "30", "31"]
February_day = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12", "13", "14", "15", "16", "17", "18", "19", "20", "21", "22", "23", "24", "25", "26", "27", "28", "29"]
March_day = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12", "13", "14", "15", "16", "17", "18", "19"]

if  ((month in spring) and (day in March_spring_day) or \
        (month in spring) and (day in April_day) or \
        (month in spring) and (day in May_day) or \
        (month in spring) and (day in June_day)):
    print("Spring")
elif(month in summer and day in JuneSummer_day) or \
        (month in summer and day in July_day) or \
        (month in summer and day in August_day) or \
        (month in summer and day in September_day):
    print("Summer")
elif(month in autumn and day in SeptemberAutumn_day) or \
        (month in autumn and day in October_day) or \
        (month in autumn and day in November_day) or \
        (month in autumn and day in December_day):
    print("Autumn")
elif(month in winter and day in December_winter_day) or \
        (month in winter and day in January_day) or \
        (month in winter and day in February_day) or \
        (month in winter and day in March_day):
    print("Winter")
else:
    print("Invalid")