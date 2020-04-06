
Input = [] 
n = int(input("Enter number of elements : ")) 
for i in range(0, n): 
    ele = int(input()) 
    Input.append(ele)
if(Input[0]<0):
    prev =1
else:
    prev=-1
for elem in Input: 
	if elem =0: 		
		sign = -1
	else: 
		sign = elem / abs(elem) 

	if sign == -prev: 		
		ans = ans + 1
		prev = sign  
print(sign)

SAMPLE INPUT-1
5
1 -2 3 4 -5
SAMPLE OUTPUT:1
3
SAMPLE INPUT-2
7
1 0 2 -3 -4 5 6 

SAMPLE OUTPUT:2
2
