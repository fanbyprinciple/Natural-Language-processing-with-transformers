from pdf2image import convert_from_path
import os
 
pdf_path = "inp.pdf"

# Store Pdf with convert_from_path function
images = convert_from_path(pdf_path)

dirname = pdf_path.split('.')[0]
os.system(f"mkdir {dirname}")

for i in range(len(images)):
      # Save pages as images in the pdf
    images[i].save('./' + dirname + '/' + str(i) +'.png', 'PNG')

print(f"Saved into {dirname}.")