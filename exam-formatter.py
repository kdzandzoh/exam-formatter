import PyPDF2
import os


while True:
	fileName = input("Enter the name of your pdf file you would like to separate: \n>")
	if fileName == 'q':
		print('Bye')
		exit()
	try:
		# open original file
		originalPdfFile = open(fileName, 'rb')
		originalPdfReader = PyPDF2.PdfFileReader(originalPdfFile)
		break
	except FileNotFoundError:
		print('\nUnable to find the file, try again\n')

# remove extension '.pdf'
fileName = fileName.split('.pdf')[0]

# make new directory for files
os.mkdir(fileName)

for pageNumber in range(originalPdfReader.numPages):
	# create PdfWriter
	pdfWriter = PyPDF2.PdfFileWriter()

	# get the page number pageNumber
	page = originalPdfReader.getPage(pageNumber)

	# make a new file called page_pageNumber
	newFile = open(f'./{fileName}/{fileName}_{pageNumber}.pdf', 'wb')

	# add page to pdfWriter
	pdfWriter.addPage(page)

	# add page to newFile
	pdfWriter.write(newFile)

	# close the file
	newFile.close()

# end program
originalPdfFile.close()
