import datetime
import time

cday = datetime.date.today()
print(cday.strftime("%d %b %Y"))
d = int(input('Μέρα του χρόνου:  '))
m = int(input('Μήνας του χρόνου:  '))
y = int(input('Χρόνος:   '))
askeddate = datetime.date(y, m, d)
print(askeddate.strftime("%d %b %Y"))
diff = askeddate - cday
diff.days
print('Μέρες μεταξύ των 2 ημερομηνιών:')
print(diff.days)
diff2 = diff * 1440
print('Λεπτά μεταξύ των 2 ημερομηνιών:')
print(diff2.days)
diff3 = diff * 1440 * 60
print('Δευτερόλεπτα μεταξύ των 2 ημερομηνιών:')
print(diff3.days)
if (m==1 or m==3 or m==5 or m==7 or m==8 or m==10 or m==12):
    print (' Ο δοσμένος μήνας έχει 31 μέρες ')
elif (m==4 or m==6 or m==9 or m==11):
    print (' Ο δοσμένος μήνας έχει 30 μέρες ')
else:         
    if( y % 4 == 0 and y % 100 == 0 and y % 400 == 0 ):
        print ('Το' ,y,'είναι δίσεκτο,άρα ο Φεβρουάριος έχει 29 ημέρες')
    elif( y % 4 == 0 and y % 100 !=0):
        print ('Το' ,y, 'είναι δίσεκτο,άρα ο Φεβρουάριος έχει 29 ημέρες')
    else:
        print ('Το' ,y, 'δεν είναι δίσεκτο,άρα ο Φεβρουάριος έχει 28 ημέρες')
    
