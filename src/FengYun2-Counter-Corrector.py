import binascii, os, argparse
parser = argparse.ArgumentParser()
parser.add_argument("-o", "--output", help="Output binary file name")
parser.add_argument("-i", "--input", help="Input binary file name")
inputfile = parser.parse_args().input
outfile = parser.parse_args().output
def create_counter():
    i = -1
    
    def func():
        nonlocal i
        i += 1
        if i == 16777216:
            i = 0
            return i
        else:
            return i
    
    return func
counter2 = create_counter()
size = os.path.getsize(inputfile)
total = int(size/44356)
n = 1
op = total/100
last = total - int(op*11)
line = 88712
backline = 0
syncword = "00000000000000"
if __name__ == "__main__":
    print("-----------------------------------------------------------------")
    print("                                                                 ")
    print("        FengYun-2 S-VISSR Counter + Sync Marker Corrector        ")
    print("                         by Egor UB1QBJ                          ")
    print("                                                                 ")
    print("-----------------------------------------------------------------")
    with open(inputfile, 'rb') as f1:
        hexdata1 = f1.read().hex()
    while True:
        x = hexdata1[backline:line]
        backline = line
        line += 88712
        syncwordfile = x[:14]
        if (n < 101):
            vcducounter = "0000"
            syncword = "00000000000000"
        if (n >= 101 <= 2601):
            count1 = counter2()
            hexdata = hex(count1).split('x')[-1]
            if len(hexdata) == 1:
                vcducounter = "000" + hexdata.upper()
            elif len(hexdata) == 2:
                vcducounter = "00" + hexdata.upper()
            elif len(hexdata) == 3:
                vcducounter = "0" + hexdata.upper()    
            else:
                vcducounter = hexdata.upper()
            syncword = "00000033FFFF00"  
        if (n > 2601):
            vcducounter = "0000"
            syncword = "000000CC000000"
        if (n >= last):
            vcducounter = "0000"
            syncword = "000000CC000000"
        block1 = x[14:134]
        block2 = x[138:88712]
        with open(outfile, 'ab') as ff:
            ff.write(binascii.unhexlify(syncword + block1 + vcducounter + block2))
        proz = n/op
        print("Total lines: " + str(total) + " | Line: " + str(n) + " | Frame Sync: 0x" + syncwordfile.upper() + " | New Frame Sync: 0x" + syncword.upper() + " | Progress: " + str("%.0f" % proz) + "%", end='\r')
        n += 1
        sizeout = os.path.getsize(outfile)
        if(sizeout >= size):
            print("")
            print("Done!", end='\r')
            break