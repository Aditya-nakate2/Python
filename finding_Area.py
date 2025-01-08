print("Select the shape which you want to find Area")
print("1.Square\n2.Circle\n3.Rectangle")
print("4.Trangle")
num=int(input("Enter the shape no. :"))

if num== 1:
   a=float(input("Enter the side of the Square :"))
   Area=a*a
   print("The Area of square:",Area)
   
elif num==2:
   a=float(input("Enter the radius of the circle:"))
   Area= 3.14 *a*a
   print("The area of the circle is : ",Area)

elif num ==3:
   b= float(input("Enter the length of Rectangle :"))
   a= float(input("Enter the bridht of Rectangle :"))
   Area=a*b
   print("The Area of Rectangle:",Area)
     
elif num ==4:
   b= float(input("Enter the length of trangle :"))
   a= float(input("Enter the Base of trangle :"))
   Area=0.5*a*b
   print("The Area of trangle:",Area)

else:
   print("Enter the correct sape number")






     

