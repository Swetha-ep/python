x = 0 
while x < 5:
    x += 1
    if x ==3:
        continue
    print(x)



#executes only if the loop runs completely without break
for i in range(1,4):
    print(i)
else:
    print("Loop finished!")