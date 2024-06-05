# simple calculator solely built using python performs the foll0wing function:
# addition
# substraction
# divison
# powers of 3
# powers of 3
# square root 
# cube root

# firstly import module for maths essential for square root and cube root
import math
# need to print the output for the required functionality
print('1),addition')
print('2),substraction')
print('3),multiplication')
print('4),divison')
print('5)exponeation for power 2')
print('6)exponeation for power 3')
print('7),square root')
print('8),cuberoot')


# writing of variable
cal_fun = input()
# conditional statement apply for the logic of the calculator
if cal_fun == '1':
    # inputs of number essence of using float to allow us input decimal numbers
 num_ber1 = float(input('enter: first number:'))
 num_ber2 = float(input('enter: second number:'))
  # codes for addition
 out_put = num_ber1 + num_ber2
 print('final answer for addition:1'+ str(out_put))

elif cal_fun == '2':
 num_ber1 = float(input('enter: first number:'))
 num_ber2 = float(input('enter: second number:'))
 # codes for substraction
 out_put = num_ber1 - num_ber2
 print('final answer for substraction:'+ str(out_put) )

elif cal_fun == '3':
 num_ber1 = float(input('enter: first number:'))
 num_ber2 =float(input('enter: second number:'))
 # codes for multiplication
 out_put = num_ber1 * num_ber2
 print('final answer for multiplication:'+ str(out_put))

elif cal_fun == '4':
 num_ber1 = float(input('enter: first number:'))
 num_ber2 = float(input('enter: second number:'))
 # codes for division
 out_put = num_ber1 / num_ber2
 print('final answer for divison:'+ str(out_put) )

elif cal_fun == '5':
 num_ber1 = float(input('enter: number:'))
 # codes for powers of two
 out_put = num_ber1**2
 print ('final answer for powers of two:'+ str(out_put))

elif cal_fun == '6':
 num_ber1 = float(input('enter: number:'))
 # codes for powers of three
 out_put = num_ber1 **3
 print('final answers for powers of three' + str(out_put))

elif cal_fun == '7':
 num_ber1 = float(input('enter: number:'))
 # codes for square root
 out_put = math.sqrt(num_ber1)
 print('final answers for square root:' + str(out_put))

elif cal_fun == '8':
 num_ber1 = float(input('enter : number:'))
 # codes for cube root
 out_put = math.pow(num_ber1,1/3)
 print('final answers for cube root:'+ str(out_put))

else:
 print('invalid number')









