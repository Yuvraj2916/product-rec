def product():
    import pickle
    f=open('product.dat','wb')
    for i in range(3):
        pno=int(input("Enter product number:"))
        pname=input("Enter product name:")
        cnm=input("Enter company name:")
        price=int(input("Enter product price:"))
        rec=[pno,pname,cnm,price]
        pickle.dump(rec,f)
        print(rec)
    f.close()
product()                                                                                                                                                       

import pickle
def showr():
    f=open('product.dat','rb')
    try:
        while True:
            rec=pickle.load(f)
            if rec[3]>1000:
                print(rec)
    except:
        f.close()

showr()

