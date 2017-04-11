import sys
import os

listcome = ['.c','.py']
outcome ={}
def main():

    init()

    work()

    Mprint()

def Mprint():
    for ty in listcome:
        print('%s:%d  %sBlank:%d  %sCount:%d All:%d'
              %(ty,outcome[ty],ty,outcome[ty+'blank'],ty,outcome[ty+'count'],outcome[ty+'count'] + outcome[ty+'blank']))

def work():
    if len(sys.argv) != 2:
        print('wrong argv')
        print(len(sys.argv))
        print(sys.argv)
        return False


    filepath = sys.argv[1]

    for rt,dirnames,filenames in os.walk(filepath):
        for filename in filenames:
            suffix = os.path.splitext(filename)[1]
            if suffix in outcome:
                outcome[suffix] = outcome[suffix] + 1
                #print(outcome[suffix])
                #print(os.path.join(rt,filename))
                with open(os.path.join(rt,filename)) as f:
                    #print(filename)
                    for line in f:
                        if line == '\n':
                            outcome[suffix + 'blank'] = outcome[suffix + 'blank'] + 1
                        else:
                            outcome[suffix + 'count'] = outcome[suffix + 'count'] + 1

def init():
    for ty in listcome:
        outcome[ty] = 0;
        outcome[ty + 'blank'] = 0;
        outcome[ty + 'count'] = 0;

if __name__ == '__main__':
    main()

