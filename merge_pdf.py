from PyPDF2 import PdfMerger

def unisci_pdf(pdf1, pdf2, output):
    merger = PdfMerger()
    
    merger.append(pdf1)
    merger.append(pdf2)
    
    with open(output, "wb") as file_output:
        merger.write(file_output)
    
    merger.close()

if __name__ == "__main__":
    unisci_pdf("da_stampare.pdf", "CEO.pdf", "da_stampare_merged.pdf")
