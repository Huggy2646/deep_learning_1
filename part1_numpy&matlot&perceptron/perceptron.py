import numpy as np
'''
 편향 X AND
'''
def AND(x1,x2):
    w1,w2,theta = 0.5,0.5,0.7
    tmp = x1*w1 + x2*w2
    if tmp<=theta:
        return 0
    elif tmp>theta:
        return 1

# print(AND(0,0))
# print(AND(1,0))
# print(AND(0,1))
# print(AND(1,1))
# print("")

'''
 편향 0, NAND
'''
def NAND(x1,x2):
    w1,w2,theta=-0.5,-0.5,-0.7
    tmp=x1*w1 + x2*w2
    if tmp<=theta:
        return 0
    else:
        return 1

'''
편향 0, OR
'''
def OR(x1,x2):
    w1,w2,theta=0.5,0.5,0.3
    tmp=x1*w1 + x2*w2
    if tmp<=theta:
        return 0
    else:
        return 1
# print(OR(0,0))
# print(OR(1,0))
# print(OR(0,1))
# print(OR(1,1))

'''
 편향 0, AND
'''
def AND_b(x1,x2):
    x=np.array([x1,x2])
    w=np.array([0.5,0.5])
    b=-0.7
    tmp=np.sum(x*w)+b
    if tmp<=0:
        return 0
    else:
        return 1

# print(AND_b(0,0))
# print(AND_b(1,0))
# print(AND_b(0,1))
# print(AND_b(1,1))
# print("")

'''
편향0,NAND
NAND는 AND의 매개변수의 부호만 반대로 하면 됨
'''
def NAND_b(x1,x2):
    x=np.array([x1,x2])
    w=np.array([-0.5,-0.5])
    b=0.7
    tmp=np.sum(x*w)+b
    if tmp<=0:
        return 0
    else:
        return 1

# print(NAND(0,0))
# print(NAND(1,0))
# print(NAND(0,1))
# print(NAND(1,1))
# print("")

'''
편향0,OR
'''

def OR_b(x1,x2):
    x=np.array([x1,x2])
    w=np.array([0.5,0.5])
    b=-0.3
    if np.sum(x*w)+b<=0:
        return 0
    else:
        return 1

# print(OR_b(0,0))
# print(OR_b(1,0))
# print(OR_b(0,1))
# print(OR_b(1,1))

'''
다층퍼셉트론(multi-layer perceptron)
XOR구현(NAND,OR,AND를 하나씩 조합하여 구현)
'''
def XOR(x1,x2):
    s1=NAND_b(x1,x2)
    s2=OR_b(x1,x2)
    y=AND(s1,s2)
    return y

print(XOR(0,0))
print(XOR(0,1))
print(XOR(1,0))
print(XOR(1,1))