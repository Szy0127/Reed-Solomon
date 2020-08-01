from QR import addlist,mullist,divlist
from QR import add,mul,pow,div
from QR import coef

def correctData(coef):
    def f(x): 
        ans = 0
        for i in range(len(coef)):
            ans = add(ans,mul(coef[i],pow(x,len(coef)-i-1)))
        return ans
    

    m =[]
    for i in range(4):#4个解
        m.append(f(pow(2,i)))
    for e1 in range(4,8):
        for e2 in range(e1+1,8):
            if mul(add(m[1],mul(m[0],pow(2,e2))),add(pow(4,e1),pow(4,e2))) \
               == mul(add(m[2],mul(m[0],pow(4,e2))),add(pow(2,e1),pow(2,e2)))\
               and mul(add(m[1],mul(m[0],pow(2,e2))),add(pow(3,e1),pow(3,e2)))\
               == mul(add(m[3],mul(m[0],pow(3,e2))),add(pow(2,e1),pow(2,e2))):
                print('错误位置：',e1,e2)
                y1 = div(add(m[1],mul(m[0],pow(2,e2))),add(pow(2,e1),pow(2,e2)))
                y2 = add(m[0],y1)
                print('错误大小：',y1,y2)
                corrected = coef.copy()
                corrected[7-e1] = add(coef[7-e1],y1)
                corrected[7-e2] = add(coef[7-e2],y2)
                print('修正后的数据：',*corrected)
    return corrected


coef[0] = 2
coef[2] = 6

corrected = correctData(coef)
