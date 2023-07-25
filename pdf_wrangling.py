from PyPDF2 import PdfReader, PdfWriter

architectural = list(range(0,25))
#structural = list(range(25, ))


with open(
    "filename.pdf", "rb") as f:
    reader = PdfReader(f)
    arch_writer = PdfWriter()
    str_writer = PdfWriter()   

    for page in range(len(reader.pages)):
        if page in architectural:
            arch_writer.add_page(reader.pages[page])
        # elif page in structural:
        #     str_writer.add_page(reader.pages[page])
    
    with open("Bldg 3 Architectural.pdf", "wb") as f2:
        arch_writer.write(f2)

    # with open("Structural.pdf", "wb") as f3:
    #     str_writer.write(f3)
