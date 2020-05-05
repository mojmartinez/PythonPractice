# for i in range(1, 21):
#     if i == 4 or i == 13:
#         print(f"{i} is Unlucky!")
#     elif i%2 == 0:
#         print(f"{i} is Even")
#     else:
#         print (f"{i} is Odd")


for i in range(1, 21):
    if i == 4 or i == 13:
        state = "Unlucky"
    elif i%2 == 0:
        state = "Even"
    else:
        state = "Odd"
    print (f"{i} is {state}")