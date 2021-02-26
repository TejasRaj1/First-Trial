x=int(input("\t\t\t1= An\n\t\t\t2= Sn\n"))
print("\tTo find the value of a given thing\n\n\t\t\tENTER=0\n\n")
if x==1:
  a=int(input("Enter value of 1st term = "))
  n=int(input("Enter value of n = "))
  d=int(input("Enter difference = "))
  A=int(input("Enter value of nth term = "))
  if a==0:
    ans=-n*d+d+A
    print("\t\t\tValue of a","=",ans)
  if n==0:
    ans=(A-a+d)/d
    print("\t\t\tValue of n","=",ans)
  if d==0:
    ans=(A-a)/(n-1)
    print("\t\t\tValue of d","=",ans)
  if A==0:
    ans=a+n*d-d
    print("\t\t\tValue of An","=",ans)
if x==2:
  a=int(input("Enter value of 1st term = "))
  n=int(input("Enter value of n = "))
  d=int(input("Enter difference = "))
  s=int(input("Sum of the numbers = "))
  if s==0:
    ans=(2*a*n+n*n*d-d*n)/2
    print("\t\t\tValue of Sn","=",ans)
  if n==0:
    for i in range(1,99999999999999,0.0000000001):
     d=i*i-i
