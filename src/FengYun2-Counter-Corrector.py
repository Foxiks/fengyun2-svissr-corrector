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

counter=create_counter()
size=os.path.getsize(inputfile)
total=int(size/44356)
n=1
op=total/100
last=total-int(op*11)
first=int(op*3)
t=first+2501
i=0
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
        x = hexdata1[i:i+88712]
        i += 88712
        syncwordfile = x[:14]
        if (n<first):
            vcducounter="0000"
            syncword="00000000000000"
        if (n>=first<=t):
            count1=counter()
            vcducounter=hex(count1).split('x')[-1].upper().zfill(4)
            syncword = "00000033FFFF00"  
        if (n>t):
            vcducounter ="0000"
            syncword="000000CC000000"
        if (n>=last):
            vcducounter="0000"
            syncword="000000CC000000"
        block1=x[14:134]
        block2=x[138:88712]
        with open(outfile, 'ab') as ff:
            ff.write(binascii.unhexlify(syncword+block1+vcducounter+block2))
        proz=n/op
        print("Total lines: " + str(total) + " | Line: " + str(n) + " | Frame Sync: 0x" + syncwordfile.upper() + " | New Frame Sync: 0x" + syncword.upper() + " | Progress: " + str("%.0f" % proz) + "%", end='\r')
        n+=1
        sizeout = os.path.getsize(outfile)
        if(sizeout>=size):
            print("")
            print("Done!", end='\r')
            break