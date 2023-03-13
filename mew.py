import time


class Tm():
    def Timr(*args, formatT='s'):
        Total = 0
        mul = 1
        formatTm = 's'
        
        if formatT == 'm':
            mul = 0.0166
            formatTm = 'm'
        elif formatT == 'ds':
            mul = 10
            formatTm = 'ds'
        elif formatT == 'cs':
            mul = 100
            formatTm = 'cs'
        elif formatT == 'ms':
            mul = 1000
            formatTm = 'ms'
        else:
            pass
        
        
        
        
        print("\nTimer Function:")
        for func in args:
            fTime = time.time()
            func()
            sTime = time.time()
            print(f"{func.__name__} : {round((sTime - fTime) * mul, 4)}{formatTm}")
            Total += sTime - fTime
        print("----------------------")
        print(f"total time : {round(Total*mul, 4)}{formatTm}")
    
    def wrapper(func):
        fTime = time.time()
        func()
        sTime = time.time()
        print(f"{func.__name__} : {sTime - fTime}")

