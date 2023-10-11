# Certificate Generation Script

## Overview

This script is designed to generate certificates from a CSV file using a DOCX template and then convert them to PDF files. It can be used for various purposes, such as creating certificates for participants in an event.

## Prerequisites

Before using this script, you need to have the following installed:

- Python 3.x
- [docxtpl](https://pypi.org/project/docxtpl/) - A library for working with DOCX templates.
- [docx2pdf](https://pypi.org/project/docx2pdf/) - A library for converting DOCX files to PDF.

You can install the required libraries using pip:


```bash
pip install docxtpl docx2pdf

```
# Usage

- Create a DOCX template: Start by creating a DOCX template for your certificates. Ensure that you have placeholders in the template that match the column names in your CSV file. The template should be named certificate-template-sample.docx and placed in the same directory as this script.

- Prepare your data: Organize your data in a CSV file named data-sample.csv in the same directory. The CSV file should contain the data you want to populate in the certificates.

```
