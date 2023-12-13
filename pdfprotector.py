import PyPDF2

input_pdf = "Experiment No 4^5^J6.pdf" 
output_pdf = "protected.pdf"  
password = "12345"  

def add_password(input_pdf, output_pdf, password):
    with open(input_pdf, 'rb') as file:
        pdf_reader = PyPDF2.PdfReader(file)
        pdf_writer = PyPDF2.PdfWriter()

        for page_num in range(len(pdf_reader.pages)):
            pdf_writer.add_page(pdf_reader.pages[page_num])

        pdf_writer.encrypt(password)

        with open(output_pdf, 'wb') as output_file:
            pdf_writer.write(output_file)

add_password(input_pdf, output_pdf, password)
print(f"PDF '{output_pdf}' created with password protection.")
