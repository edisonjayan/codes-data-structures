def bubbleSort(inArray):
	swapped = True
	listLen = len(inArray)
	while swapped:
		swapped = False
		for i in range(listLen-1):
			if inArray[i] > inArray[i+1]:
				temp = inArray[i]
				inArray[i] = inArray[i+1]
				inArray[i+1] = temp
				swapped = True
				
def sort(algo, inArray):
	if algo == "bs":
		bubbleSort(inArray);

def main():
	print("hello World")
	ll = [5,1,4,2,8]
	print(ll)
	#bubbleSort(ll)
	sort("bs",ll)
	print(ll)

if __name__ == "__main__":
	main()
