import csv
from docxtpl import DocxTemplate
from docx2pdf import convert  # Import the convert function from docx2pdf

# Configuration
template = DocxTemplate('certificate-template-sample.docx')
filename = 'data-sample.csv'
output = 'certifications'

# get all rows
getList = []

# Open and reading csv
with open(filename, 'r') as data:
    for line in csv.reader(data, delimiter=','):
        getList.append(line)

# Function to create files .docx
def create_certification():
    for names in getList[1:]:
        # Column's Name
        name = names[1]
        id = names[0]
        alias = names[2]  # Assign the third column value to 'alias'
        context = {
            'name': name,
            'id': id,
            'alias': alias  # Use 'alias' in the context
        }
        template.render(context)
        docx_filename = f"{output}/{id}.docx"
        template.save(docx_filename)
        
        # Convert the DOCX file to PDF
        convert(docx_filename)

# Run function
create_certification()
