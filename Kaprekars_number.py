#Kaprekars Constant= 6174
#give me any 4 digit long number with the only condition
#being that all 4 numbers cannot be the same
#example: 2222 will not work, but 2223 will
#how can you always get back to the number 6174?

def backwards(num):#reverses the integers in a number
	h=0
	while num != 0:
		r = num%10
		h = h*10+r
		num = num//10
	return h 
	
def LargeSmall(num):
	#orders the integers in a number from biggest to smallest 
	l_num=[]
	q_num=''
	for number in num:
		#l_num.insert(0,number)
		l_num.append(number)
	while len(l_num) < 4:
		l_num.append('0')
	l_num.sort(key=int, reverse = True)
	for number in l_num:
		q_num += number
	return int(q_num)
	
	
def KaprekarsNumber(num):
	#finds Kaprekars number from a given 4 digit number
	x= num
	counter= 0
	while x != 6174:
		x= LargeSmall(str(x))
		print(x)
		z=0
		y=backwards(x)
		z= x-y
		if z > 0:
			x = z
		if z<0:
			x = -z
		counter +=1
	print(num +" took "+str(counter)+ " iterations to finish")
		 
	return x , counter
#LargeSmall(2111)
KaprekarsNumber(input())
