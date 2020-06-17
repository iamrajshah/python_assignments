from datetime import date
def findDayBetweenTwoDate(date1, date2):
    year, month, day = map(int, date1.split('/'))
    year2, month2, day2 = map(int, date2.split('/'))
    comutedDate1 = date(year, month, day)
    comutedDate2 = date(year2, month2, day2)
    print(comutedDate2 - comutedDate1)


date1 = input('Enter date in format yyyy/mm/dd:')
date2 = input('Enter date in format yyyy/mm/dd:')
findDayBetweenTwoDate(date1, date2)
