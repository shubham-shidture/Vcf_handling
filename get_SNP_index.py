## Descriptiion : This script is for creating SNP index, It requires input of 2 vcf files from which SNP index, and ED values are calculated.


import os
import sys

## Variant splittng into SNP and Indels from first VCF file
def split_vcf_1(vcf_1,picard_tool):
	snp_vcf_1 = vcf_1.split('.')[0] + "_snp.vcf"
	indel_vcf_1 = vcf_1.split('.')[0] + "_indel.vcf"
	cmd = ["java -jar", picard_tool, "SplitVcfs", "-I", vcf_1, "-SNP_OUTPUT", snp_vcf_1, "-INDEL_OUTPUT", indel_vcf_1, "-STRICT false"]
	cmd = " ".join(cmd)
	os.popen(cmd)

## Variant splittng into SNP and Indels from Second VCF file
def split_vcf_2(vcf_2,picard_tool):
	snp_vcf_2 = vcf_2.split('.')[0] + "_snp.vcf"
	indel_vcf_2 = vcf_2.split('.')[0] + "_indel.vcf"
	cmd = ["java -jar", picard_tool, "SplitVcfs", "-I", vcf_2, "-SNP_OUTPUT", snp_vcf_2, "-INDEL_OUTPUT", indel_vcf_2, "-STRICT false"]
	cmd = " ".join(cmd)
	os.popen(cmd)

# Selecting specific columns from vcf_1 files for DP4 value
def get_cols_vcf_1 (snp_vcf_1,indel_vcf_1):
	cols_snp_vcf_1 = snp_vcf_1.split('.')[0] + ".txt"
	cols_indel_vcf_1 = indel_vcf_1.split('.')[0] + ".txt"
	#dp4_snp_vcf_1 = cols_snp_vcf_1.split('.') + ".txt"
	cmd_1 = ["cut", "-f1,2,8", snp_vcf_1, ">",cols_snp_vcf_1]
	cmd_2 = ["cut", "-f1,2,8", indel_vcf_1, ">",cols_indel_vcf_1]
	cmd_1 = " ".join(cmd_1)
	cmd_2 = " ".join(cmd_2)
	os.popen(cmd_1)
	os.popen(cmd_2)

# Selecting specific columns from vcf_2 files for DP4 value
def get_cols_vcf_2 (snp_vcf_2,indel_vcf_2):
	cols_snp_vcf_2 = snp_vcf_2.split('.')[0] + ".txt"
	cols_indel_vcf_2 = indel_vcf_2.split('.')[0] + ".txt"
	cmd_1 = ["cut", "-f1,2,8", snp_vcf_2, ">",cols_snp_vcf_2]
	cmd_2 = ["cut", "-f1,2,8", indel_vcf_2, ">",cols_indel_vcf_2]
	cmd_1 = " ".join(cmd_1)
	cmd_2 = " ".join(cmd_2)
	os.popen(cmd_1)
	os.popen(cmd_2)

def main( arguments ):

	vcf_1= arguments[ arguments.index( '-vcf_1' )+1 ]
	vcf_2= arguments[ arguments.index( '-vcf_2' )+1 ]
	picard_tool = arguments[ arguments.index( '-picard_tool' )+1 ]
	snp_index_script = arguments[ arguments.index( '-snp_index_script' )+1 ]
	snp_vcf_1 = arguments[arguments.index('-snp_vcf_1') + 1]
	indel_vcf_1 = arguments[arguments.index('-indel_vcf_1') + 1]
	snp_vcf_2 = arguments[arguments.index('-snp_vcf_2') + 1]
	indel_vcf_2 = arguments[arguments.index('-indel_vcf_2') + 1]
	


	
