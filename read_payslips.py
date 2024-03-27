import pandas as pd
import tabula
import numpy as np
from pypdf import PdfReader
import os

pdf_folder = "PartTime_Payslips/"

list_of_tables = np.array(["Date", "Description", "Hours", "Rate", "Amount", "YTD", "Type"])

for file in os.listdir(pdf_folder):
    date = 'tmp'
    file_path = pdf_folder + file

    pdftext = PdfReader(file_path).pages[0].extract_text()
    date = pdftext.split("Payment Date: ", 2)[1].strip().split(" ")[0].split("\n")[0]

    table = tabula.read_pdf(file_path, pages='all', silent=True)[0]
    table.insert(0, "Date", date, True)

    list_of_tables = np.vstack((list_of_tables, table.iloc[0]))


print(list_of_tables)

df = pd.DataFrame(list_of_tables)
df.to_csv('output.csv', index=False)
