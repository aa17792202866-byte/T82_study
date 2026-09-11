# for i in range(2):
#     for j in range(2):
#         print(i,j,end=" ")

# for i in range(1,10):
#     for j in range(i):
#         print(f"{j+1}*{i}={i*(j+1)}\t",end="")
#     print()
#
for i in range(1,10):
    for j in range(1,i+1):
        print(f"{j}*{i}={i*j}\t",end="")
    print()