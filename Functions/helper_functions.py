from math import log, floor
import pyodbc as db

con = db.connect('DRIVER={SQL Server};'
                 'SERVER=137.116.139.217;'
                 'DATABASE=ARCHIVESKF;'
                 'UID=rptuser;'
                 'PWD=Rpt@1729')


def hazar(number):
    k = 1000.0
    final_number = number / 1000
    return '%.1f %s ' % (final_number, 'K')


# ----------convert the number into thousand and give comma -------
def joker(number):
    number = number / 1000
    number = int(number)
    number = format(number, ',')
    number = number + 'K'
    return number


# --------------give comma in a number and add k-------------------
def for_bar(number):
    number = round(number, 1)
    number = format(number, ',')
    number = number + 'K'
    return number


def get_value(value):
    if (len(value) > 6):
        return str(value[0:len(value) - 6] + "," + value[len(value) - 6:len(value) - 3] + ","
                   + value[len(value) - 3:len(value)])
    elif (len(value) > 3):
        return str(value[0:len(value) - 3] + "," + value[len(value) - 3:len(value)])
    elif (len(value) > 0):
        return value
    else:
        return "-"


def human_format(number):
    units = ['', 'K', 'M', 'B', 'T', 'P']
    k = 1000.0
    magnitude = int(floor(log(number, k)))
    return '%.1f %s ' % (number / k ** magnitude, units[magnitude])
