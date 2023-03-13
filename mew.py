import time


class Tm():
    def Timr(*args):
        Total = 0
        print("\nTimer Function:")
        for func in args:
            fTime = time.time()
            func()
            sTime = time.time()
            print(f"{func.__name__} : {round(sTime - fTime, 4)}s")
            Total += sTime - fTime
        print("----------------------")
        print(f"total time : {round(Total, 4)}s")
    
    def wrapper(func):
        fTime = time.time()
        func()
        sTime = time.time()
        print(f"{func.__name__} : {sTime - fTime}")

