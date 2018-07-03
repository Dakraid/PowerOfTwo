# import the necessary packages
import sys, getopt, magic, os, re

common_res = [1, 2, 4, 8, 16, 32, 64, 128, 256, 512, 1024, 2048, 4096]

def is_power(n):
    n = int(n)
    if n in common_res:
        return True
    elif n%2 != 0:
        return False
    else:
        return is_power(n/2.0)

def main(argv):
    path = ""

    try:
        opts, args = getopt.getopt(argv,"hp:",["path=",])
    except getopt.GetoptError:
        print('PowerOfTwo.py -p <absolute path>')
        sys.exit(2)
        
    for opt, arg in opts:
        if opt == '-h':
            print('PowerOfTwo.py -p <absolute path>')
            sys.exit()
        elif opt in ("-p", "--path"):
            path = arg
    
    if not path:
        try:
            path = os.path.dirname(os.path.realpath(__file__))
        except:
            print("No path defined")
            
    print("Start of scan, please wait.")
            
    file = open("results.txt","w") 

    for root, dirs, files in os.walk(path):
        for name in files:
            exclude = re.search('(Interface|interface|LOD|lod)', root)
            if not exclude:
                if name.endswith((".dds")):
                    im = magic.from_file(os.path.join(root, name))
                    proof = re.search('DDS', im)
                    if proof:
                        width, height = re.search('(\d+) x (\d+)', im).groups()
                        check1 = is_power(width)
                        check2 = is_power(height)
                        # print("Checking " + os.path.join(root, name))
                        if check1 == False or check2 == False:
                            file.write(os.path.join(root, name) + " is not Power of Two! " + width + " x " + height + "\n")
         
    file.write("End of scan, results above.")               
    file.close()

    print("End of scan, program can be closed.")
    
if __name__ == "__main__":
   main(sys.argv[1:])
