# coding:utf-8
import time
def maopao(li):
    n = len(li)
    
    # time.sleep(1)
    for i in range(len(li)-1):
        for j in range(0,len(li)-1-i):
            if li[j] > li[j+1]:
                li[j], li[j+1] = li[j+1], li[j]
    
    






if __name__ == "__main__":
    li = [12,13,42,62,85,74,43,39,91,24,67]
    print(li)
    start_time = time.time()
    maopao(li)
    end_time = time.time()
    print("times:%d" % (end_time-start_time))
    print(li)