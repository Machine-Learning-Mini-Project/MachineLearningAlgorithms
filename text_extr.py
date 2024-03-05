from pypdf import PdfReader


reader = PdfReader("/home/mohak/Downloads/Copy of AI_Experiment03.pdf")

page = reader.pages[6]
print(page.extract_text())


page = reader.pages[4]
count = 0

for image_file_object in page.images:
    with open(str(count) + image_file_object.name, "wb") as fp:
        fp.write(image_file_object.data)
        count += 1
