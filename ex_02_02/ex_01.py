# sh = input('Enter your Hours: ')
# sr = input('Enter your rate: ')
# try:
#     fh = float(sh)
#     fr = float(sr)
# except:
#     print('Error, make sure to enter a number!')
#     quit()
# if fh > 40 :
#     reg = fr * fh
#     otp = (fh -40.0) * ( fr * 0.5)
#     xp = reg + otp
# else:
#     xp = fh *fr
# print("pay:", xp)
arg = input('enter your string => ')

def thing(arg) :
    print(arg)
    print('the bigest char in the string is: ')
    big = max(arg)
    tiny = min(arg)
    print(big)
    print('an the smallest is: ')
    print(tiny)

thing(arg)