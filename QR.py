addlist = []
addlist.append([0,1,2,3,4,5,6,7])
addlist.append([1,0,3,2,5,4,7,6])
addlist.append([2,3,0,1,6,7,4,5])
addlist.append([3,2,1,0,7,6,5,4])
addlist.append([4,5,6,7,0,1,2,3])
addlist.append([5,4,7,6,1,0,3,2])
addlist.append([6,7,4,5,2,3,0,1])
addlist.append([7,6,5,4,3,2,1,0])

mullist = []
mullist.append([0,0,0,0,0,0,0,0])
mullist.append([0,1,2,3,4,5,6,7])
mullist.append([0,2,4,6,3,1,7,5])
mullist.append([0,3,6,5,7,4,1,2])
mullist.append([0,4,3,7,6,2,5,1])
mullist.append([0,5,1,4,2,7,3,6])
mullist.append([0,6,7,1,5,3,2,4])
mullist.append([0,7,5,2,1,6,4,3])

divlist = []
divlist.append([0, 0, 0, 0, 0, 0, 0, 0])
divlist.append([-1, 1, 5, 6, 7, 2, 3, 4])
divlist.append([-1, 2, 1, 7, 5, 4, 6, 3])
divlist.append([-1, 3, 4, 1, 2, 6, 5, 7])
divlist.append([-1, 4, 2, 5, 1, 3, 7, 6])
divlist.append([-1, 5, 7, 3, 6, 1, 4, 2])
divlist.append([-1, 6, 3, 2, 4, 7, 1, 5])
divlist.append([-1, 7, 6, 4, 3, 5, 2, 1])

def add(a,b):
    return addlist[a][b]

def mul(a,b):
    return mullist[a][b]

def pow(a,b): #a^b b = 0,1,2,3,4,5,6,7
    if b == 0 :
        return 1
    ans = 1
    for i in range(b):
        ans = mul(ans,a)
    return ans

def div(a,b):
    if b == 0:
        raise Exception('除数为0')
    else:
        return divlist[a][b]

data = [1,2,3,4]
def findCode(data):
    def listSub(list1,list2):
        listans = [0 for i in list1]
        for i in range(len(list1)):
            listans[i] = add(list1[i],list2[i])
        return listans
    
    def listMul(list1,num):
        listans = [0 for i in list1]
        for i in range(len(list1)):
            listans[i] = mul(list1[i],num)
        return listans
    
    m = [*data,0,0,0,0]
    g = [1,4,7,7,5]
    m = listSub(m,listMul([*g,0,0,0],m[0]))
    m = listSub(m,listMul([0,*g,0,0],m[1]))
    m = listSub(m,listMul([0,0,*g,0],m[2]))
    m = listSub(m,listMul([0,0,0,*g],m[3]))
    return m[-4:]


data = [3,4,5,6]
code = findCode(data)
coef = [*data,*code]

if __name__ == '__main__':
    print('数据：',data,'纠错码：',code)
