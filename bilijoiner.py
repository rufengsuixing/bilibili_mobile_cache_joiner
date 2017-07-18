#*~ utf-8~*#
import os
import glob
import json
import flv_join
import mp4_join
def hebing(name):
    li=glob.glob('[1234567890]*lv')
#    lit=[]
#    for a in li:
#        lit+=abspath(a)
    if not li:
        li=glob.glob('*mp4')
        assert li!=[] ,os.getcwd()
        mp4_join.concat_mp4s(li, name+'.mp4')
        return 'mp4'
    flv_join.concat_flvs(li,name+'.flv')   #conbian flv to name
    return 'flv'
def usage():
    print('bilibilitopc.py -i <download dir> -o <wantdir>')
    
def getname():
    with open('entry.json',encoding='utf-8') as oinfo:
        info=json.loads(oinfo.readlines()[0])
    return info['title']+info['ep']['index']
def main():
    import sys, getopt
    try:
        opts, args = getopt.getopt(sys.argv[1:], "ho:i:", ["help", "output=","input="])
    except getopt.GetoptError as err:
        usage()
        sys.exit(1)
    output = None
    input=None
    if len(opts)<2:
        usage()
        print(output)
        print(input)
        print(args)
        sys.exit(1)
        
    for o, a in opts:
        if o in ("-h", "--help"):
            usage()
            sys.exit()
        elif o in ("-o", "--output"):
            output = a
        elif o in ("-i", "--input"):
            input = a        
        else:
            usage()
            sys.exit(1)
    os.makedirs(output,exist_ok=True)
    os.chdir(input)
    for a in glob.glob('*'): 
        s_dir=os.path.join(input,a)
        
        os.chdir(s_dir)  #s_dir 
        for b in glob.glob('*'):
            os.chdir(os.path.join(s_dir,b)) #entry dir
            name=getname()
            
            os.chdir(glob.glob('*api*')[0])
            print(os.getcwd())
            hebing(os.path.join(output,name))
    print('完成')
if __name__=='__main__':
    main()