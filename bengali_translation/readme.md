# Steps for recognising bengali

### installation of conda

from conda official site.

https://www.anaconda.com/products/distribution/

### install hugging face transformers

`conda create --name myenv`

`conda activate myenv`

for tensorflow -
`conda create --name tensor_gpu tensorflow-gpu anaconda`

for pytorch -
`conda install pytorch torchvision torchaudio cudatoolkit=11.3 -c pytorch`

for hugging face - 
`conda install -c huggingface transformers`

### convert pdf into png
https://www.geeksforgeeks.org/convert-pdf-to-image-using-python/

1. `pip install pdf2image`

2. install poppler - https://github.com/oschwartz10612/poppler-windows/releases/ and add its bin file to path.

3. use `convert_pdf_to_png.py`

### install libraries for tesseract


from https://stackoverflow.com/questions/42831662/python-install-tesseract-for-windows-7
```
Step [1] To install tesseract kindly visit

https://github.com/UB-Mannheim/tesseract/wiki

https://www.softpedia.com/get/Programming/Other-Programming-Files/Tesseract-OCR.shtml

The latest installers can be downloaded from here: e.g., tesseract-ocr-setup-3.05.02-20180621.exe, tesseract-ocr-w32-setup-v4.0.0-beta.1.20180608.exe, tesseract-ocr-w64-setup-v4.0.0-beta.1.20180608.exe (64 bit)

Step [2] Download Microsoft Visual C++ Compiler for Python 2.7 from the link given below https://download.microsoft.com/download/7/9/6/796EF2E4-801B-4FC4-AB28-B59FBF6D907B/VCForPython27.msi

Step [3] Install pytesseract for binding for tesseract using pip

pip install pytesseract
Step [4] Furthermore you can install an image processing library in python, e.g., pillow:

pip install pillow
greetings!! you are done!! :)0
```

while installing tesseract remeber to add bangla model in drop down during installation.

2. Installing open cv

``pip install opencv-python`

Then running `ocr_pytesseract.py` will work.

The result of pages are stored in ocr/result.

### Using hugging face offline

https://huggingface.co/docs/transformers/installation#installing-from-source

some problem with the file.













