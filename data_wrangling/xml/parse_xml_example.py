# More suitable when working with document oriented XML data
import xml.etree.ElementTree as ET

file_path = 'C:\Temp\PythonSamples\data_wrangling\\xml\\resources\exampleresearcharticle.xml'

tree = ET.parse(file_path)
root = tree.getroot()

# Example of using an Xpath expression
title = root.find('./fm/bibl/title')

title_text = ""
for p in title:
    title_text += p.text
print("\nTitle:\n", title_text)

print("\nAuthor email addresses:")
for a in root.findall('./fm/bibl/aug/au'):
    email = a.find('email')
    if email is not None:
        print(email.text)

print("\nChildren for root:")
for child in root:
    print(child.tag)