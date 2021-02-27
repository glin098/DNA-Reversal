DNA = input('Enter a DNA sequence: ')
Pattern = input('Enter a pattern: ') #Marker

index = DNA.find(Pattern)   #finds the marker in the DNA sequence
pLength = len(Pattern)  #length of pattern
Prefix = DNA[0: index]    #before the pattern
PReverse = Pattern[ : :-1]  #reverse of the pattern
prLength = len(PReverse)    #length of reverse pattern/PReverse
index2 = DNA.find(PReverse, index + pLength) #find the reverse of the pattern in original strand starting from index
#index = 4
#index2 = 13
Middle = DNA[index + pLength: index2] # middle of the two indexes; index + marker length to index2
MReverse = Middle[ : :-1] #reverse of middle
Suffix = DNA[index2 + prLength: ] #after the middle and reverse patterns,index+marker length 
Result = Prefix + Pattern + MReverse + PReverse + Suffix

print('Prefix: ', Prefix)
print('Marker: ', Pattern)
print('Middle: ', Middle) 
print('Reversed Middle: ', MReverse)
print('Reversed Marker: ', PReverse)
print('Suffix: ', Suffix)
print('Result: ', Result)


























