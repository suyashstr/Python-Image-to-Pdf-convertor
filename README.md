# Python-Image-to-Pdf-convertor

Let's Write Some Code We can work with some pre-defined libraries.

First, you need to import the relevant 2 packages/modules/libraries named os (which comes in Python’s standard utility modules) and img2pdf. Install this package from cmd.

    pip install img2pdf
If you want to work with some pre-defined libraries/modules, then it is necessary to mention them earlier as the interpreter would find them before working on those specific libraries. As for the other library, img2pdf, remember that we will use this library to convert our image files to PDF files. For importing the img2pdf library, we use the same import command, import img2pdf.

     with open("ImageContainingBook.pdf", "wb") as file:
This will create a PDF file named ImageContainingBook.pdf and integrate all of the image files there. And please check that you have also included the file extension (in this case, you are working with a PDF file so the file extension must be .pdf). As we will write in that file and work on the binary files, we have used the formatting as the wb. The wb indicates that the file is opened for writing in binary mode. "Then I need to specify what I want to do with the file. I want to write in that file and I want the conversion functionality of the img2pdf library. Also, I need to include the file directory where it will get all the images.

Therefore the last line of our script would be:

    file.write(img2pdf.convert([i for i in os.listdir("C:\\Users\\suyash sunil mane\\OneDrive\\Desktop\\Scriptproject.py")if i.endswith(".jpg")]))
Let me explain the code now.

os.listdir("C:\Users\fahim\Desktop\ImageToPdf") This line uses the os module to list all the files in the directory specified by the given path. In this case, it is the directory "C:\Users\fahim\Desktop\ImageToPdf".

([i for i in os.listdir("C:\Users\suyash sunil mane\OneDrive\Desktop\Scriptproject.py")if i.endswith(".jpg")])) This list comprehension filters the files obtained from the directory listing. It iterates through each file name in the directory and only includes those that end with the extension ".jpg". This step ensures that only JPEG images will be considered for the conversion to PDF.

img2pdf.convert(...) The img2pdf library provides the convert function, which takes a list of image file paths and converts them into a single PDF file. The code passed inside the parentheses is generating the list of image file paths (JPEG images ending with ".jpg") using the list comprehension.

file.write(...): It seems that a file is a file object that was opened in write mode. The write method is being used to write the PDF content to the file.

To use this code successfully, you need to make sure of the following:

That the img2pdf library is installed in your Python environment. Replace the directory path "C:\Users\fahim\Desktop\ImageToPdf" with the path to the directory containing the JPEG images you want to convert to PDF. That you have appropriate write permissions for the specified directory and file. It's important to note that the code converts all the JPEG images in the specified directory into a single PDF file. If there are other file types or non-image files in that directory, they will be ignored during the conversion.

In a nutshell, the entire Python script is:

    import os
    import img2pdf
    with open("ImageContainingBook.pdf", "wb") as file:
     file.write(img2pdf.convert([i for i in os.listdir("C:\\Users\\suyash sunil mane\\OneDrive\\Desktop\\Scriptproject.py")if i.endswith(".jpg")]))
Again, let me explain all of the detail lines:-

1)Make sure to include an extra backspace in the file directory.

2)First, we import the necessary modules: os to interact with the file system and img2pdf for image-to-PDF conversion.

3)These are the images that will be included in the PDF. The img2pdf.convert(...) function takes the list of image files and converts them into a single PDF file, storing the PDF content in the pdf_data variable.

4)Finally, we write the pdf_data content to the "output.pdf" file, effectively creating the PDF with the converted images.

5)imp: Before running the code, ensure that the img2pdf library is installed in your Python environment.
