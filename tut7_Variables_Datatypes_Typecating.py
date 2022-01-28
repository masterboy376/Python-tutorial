var1 = "I am the crazy variable";
var2 = 5;
var3 = 5.004;
var4 = "concat";
var5 = "6";
var6 = "6";

print(type(var1));
print(type(var2+var3));
print(type(var4+var1));

#Typecasting : changing the datatype
print(str(var3)+str(var2));
print(int(var5)+int(var6));

#multiply
print(10* var1);
print(10* str(var2));

#user input
name = input();# this will store user input as a string -----> always
print("Your name is "+name);

# quiz
num1 = float(input());
num2 = float(input());
print("sum is "+(str(num1+num2)))