
import Selffunction as SelF

tes = "點@jeremy@無糖奶茶@60"
tes2 ="點@jess@無糖紅茶@30"

a = SelF.checkevent(tes)
b = SelF.checkevent(tes2)

co =[]
co.append(a[1:4])
print (co)
co.append(b[1:4])
print(co)