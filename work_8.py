#if9
# A=float(input("A="))
# B=float(input("B="))
# if A<B:
#     print(A, B)
# else:
#     print("Nozima ruchkani chaynidi")
# #if10
# A=int(input("A="))
# B=int(input("B="))
# if A>B:
#     print(A+B, B+A)
# elif A<B:
#     print(A+B, B+A)
# else:
#     print(0, 0)
#if11
# A=int(input())
# B=int(input())
# a=0
# if(A>B):
#     print(a+A)
# elif(A<B):
#     print(a+B)
# else:
#     print(0, 0)
#if12
# a=int(input("a="))
# b=int(input("b="))
# c=int(input("c="))
# if (a>b and a>c and b>c) or (a<b and b>c and a>c) or (a==b and a>c and b>c):
#     print(c)
# elif(a>b and a>c and b<c) or (b<c and a<c and a<b) or (a==c and c>b and a>b):
#     print(b)
# elif(a<b and a<c and b<c) or (b>c and a<c and a<b) or (b==c and a<b and a<c):
#     print(a)
# else:
#     print(a, b, c)
#if13
# a,b,c=map(int,input().split())
# if a>b>c or c>b>a:
#     print(b)
# elif b>a>c or c>a>b:
#     print(a)
# elif a>c>b or b>c>a:
#     print(c)
# else:
#     print("harakata barakat")
#if 14
# a,b,c=map(int,input().split())
# if a>b>c or b>a>c:
#     print((c, a) or (c, b))
# elif c>b>a or b>c>a:
#     print((a, c) or (a, b))
# elif a>c>b or c>a>b:
#     print((b, a) or (b, c))
# else:
#     print("yoqimtoysiz")
#if 15
# a,b,c=map(int,input().split())
# if a>b>c or b>a>c:
#     print(a+b)
# elif c>b>a or b>c>a:
#     print(b+c)
# elif a>c>b or c>a>b:
#     print(a+c)
# else:
#     print("siz g'olibsiz")
#if 16
# A,B,C=map(float, input().split())
# if A<B<C:
#     print(A*2,B*2,C*2)
# else:
#     print(A*(-1),B*(-1),C*(-1))
