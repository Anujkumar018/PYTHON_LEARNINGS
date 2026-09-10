#type function in python is used to identify the datatype of a variable

a="hello python"
print(type(a))

b=12
print(type(b))

c="32"                  #when we assign 32 will double couts it assign the value as string datatype
print(type(c))          #we can  correct it by 'typecasting'

#Type casting

y=int("23")
print(type(y))


z=float(23)
print(type(z))

#taking user input by using typecasting

x=float(input("ENTER  ANY NO:"))   
print(type(z),z)                         #<class 'float'> 23.0


m=str(input("ENTER ANY NO:"))
print(type(m),m)                         #<class 'str'> 21

#"NOTE AN DEFAULT INPUT() FUNCTION STORES THE VALUE AS STRING "

h=input("ENTER ANYTHING:")
print(type(h),h)                         #ENTER ANYTHING:11 <class 'str'> 11


