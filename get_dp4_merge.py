## Description : This script generate single merge file for common variants from two input vcfs (DP4 values extracted)
## This script output used for input for SNP Index calculations.

fr1 = open(input("Name of first DP4 values vcf/indel file :"), "r")
fr2 = open(input("Name of second DP4 values vcf/indel file:"), "r")

fn = open("dp4_value_merge_file.txt",'w')

dpdict_1 = {}
line = fr1.readline()
while(line):
  line = line.rstrip("\n")
  linearr = line.split("\t")
  dictkey = "\t".join([linearr[0],linearr[1]])
  dictval = "\t".join([linearr[2],linearr[3],linearr[4],linearr[5]])
  dpdict_1[dictkey] = dictval
  line = fr1.readline()
fr1.close()

dpdict_2 = {}
line = fr2.readline()
while(line):
  line = line.rstrip("\n")
  linearr = line.split("\t")
  #print(linearr[2])
  dictkey = "\t".join([linearr[0],linearr[1]])
  dictval = "\t".join([linearr[2],linearr[3],linearr[4],linearr[5]])
  dpdict_2[dictkey] = dictval
  line = fr2.readline()
fr2.close()

for key in dpdict_1:
  if key in dpdict_2.keys():
    print(key, dpdict_1[key], dpdict_1[key], sep="\t", file=fn)

fn.close()
