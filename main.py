# with open('energy.pdf', 'r') as file:
#     file1 =file.read()
#     print(file1)


# importing required modules
import PyPDF2
with open('energy.pdf','rb') as file:
    pdf_reader=PyPDF2.PdfReader(file)
    # print(f"Number of pages: {len(pdf_reader.pages)}\n")
    first_page=pdf_reader.pages[0]
    # print("Text on first page:\n")
    text1=first_page.extract_text()
    # print(text1)
    # print(len(text1))
    # print(type(text1))



