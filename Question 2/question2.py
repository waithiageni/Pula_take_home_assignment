def validate_ipv4(ipv4):
    R = ipv4.split(".")
    if len (R) < 4 or len(R) > 4:
        return "Not a valid IP length"
    else:
        while len (R) == 4:
            e = int(R[0])
            f = int(R[1])
            g = int(R[2])
            h = int(R[3])

            if e <= 0 or e == 127:
                return "Not a valid IP address"
            elif h ==0:
                return "The host id should not be 0 or less than 0"
            elif e > 255:
                return "it should not be greater than 255 or less than 0"
            elif f >  255 or  f < 0:
                return "it should not be greater than 255 or less than 0"
            elif g > 255 or g < 0:
                return "it should not be greater than 255 or less than 0"
            elif h > 255 or h <0:
                return "it should not be greater than 255 or less than 0"
            else:
                return "Successful it is a valid IP address", ipv4
i = input("Enter IP address :")
print validate_ipv4(i)              


