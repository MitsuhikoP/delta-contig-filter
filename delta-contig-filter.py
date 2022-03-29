#!/usr/bin/env python3
# copyright (c) 2022 Mitsuhiko Sato. All Rights Reserved.
# Mitsuhiko Sato ( E-mail: mitsuhikoevolution@gmail.com )
#coding:UTF-8
def main():
    from argparse import ArgumentParser
    parser=ArgumentParser(description="",usage="python3 delta-contig-filter -i input.delta -o output.delta [-r chr1,chr2|-q chr1,chr2]", epilog="")
    parser.add_argument("-i",required=True, type=str,metavar="str",help="input delta file")
    parser.add_argument("-o",required=True, type=str,metavar="str",help="output delta file")

    group = parser.add_mutually_exclusive_group()
    group.add_argument("-r", type=str, help="reference contig names, sepalated by comma (chr1,chr2,chr3,...). Exclusive args with q")
    group.add_argument("-q", type=str, help="query contig names, sepalated by comma (chr1,chr2,chr3,...). Exclusive args with r")

    args = parser.parse_args()

    rlist=[]
    if args.r:
        rlist=args.r.split(",")
    qlist=[]
    if args.q:
        qlist=args.q.split(",")
    
    fhr=open(args.i,"r")
    out=fhr.readline()
    out+=fhr.readline()

    MATCH=0
    for line in fhr:
        line=line.rstrip()
        if line[0] == ">":
            MATCH=0
            lines=line[1:].split()
            if lines[0] in rlist:
                MATCH=1
            elif lines[1] in qlist:
                MATCH=1
        if MATCH == 1:
                out+=line+"\n"
                
    fhr.close()
    fhw=open(args.o,"w")
    fhw.write(out)
    fhw.close()

            
        

if __name__ == '__main__': main()
