# This script will automate the name conversion between EnsemblID to external gene names.

library(biomaRt)

geneinput<- read.csv(file = "ensemblgenelist.csv"
mart.hs <- useMart(biomart = "ENSEMBL_MART_ENSEMBL", dataset = "hsapiens_gene_ensembl")
geneid <- getBM(attributes=c("ensembl_gene_id", "external_gene_name"), filter="ensembl_gene_id", values = geneinput, mart=mart.hs)

print(geneid)
