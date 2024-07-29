# import math

def USB(usb2_0, usb3_0):
#    usb2_0 = 2
#    usb3_0 = 3.5
    profit = (usb3_0)/(usb2_0)

    print('profit'+' '+'reaches:', profit)


#def inp():
#    usb2_0 = input('usb2.0: ')
#    usb3_0 = input('usb3.0: ')
    
#    return usb2_0, usb3_0


#def init():
#    usb2_0, usb3_0 = inp()
#    print(USB(profit))


if __name__ == '__main__':
    usb2_0 = float(input('usb2_0: ')) 
    usb3_0 = float(input('usb3_0: '))
    USB(usb2_0, usb3_0)
#    print(USB(profit))
    