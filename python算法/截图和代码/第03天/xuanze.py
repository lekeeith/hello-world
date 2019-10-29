import time
def xuanze(li):
    n = len(li)
    for i in range(n-1):
        cur = i
        for j in range(i+1,n):
            if li[j]<li[cur]:
                cur = j
        li[cur], li[i] = li[i], li[cur]
                







if __name__ == "__main__":
    li = [12,13,42,62,85,74,43,39,91,24,67]
    print(li)
    start_time = time.time()
    xuanze(li)
    end_time = time.time()
    print("times:%d" % (end_time-start_time))
    print(li)  