# Problem Linl : http://opc.iarcs.org.in/index.php/problems/VOTERS
 
def main():
	(a, b ,c) = map(int, raw_input().split(" "))
	t = a + b + c
	finalList = {}
	voterId = 0
	while t > 0:
	    voterId = int(raw_input())
	    if voterId in finalList:
	        finalList[voterId] +=1
	    else:
	        finalList[voterId] = 1;
	    
	    t -= 1
	    

	keys = finalList.keys()
	keys.sort()
	li = []
	for i in keys:
	    if finalList[i] > 1:
	        li.append(i)
	print len(li)
	for i in li:
	    print i

if __name__ == "__main__":
	main()