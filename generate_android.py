import csv
import os
import xml.etree.ElementTree as ET
import shutil

# Define the CSV file path
csv_file = './source.csv'

# Define the output folder paths for each language
output_folders = {
    'as': 'values-as',
    'bn': 'values-bn',
    'en': 'values',
    'gu': 'values-gu',
    'hi': 'values-hi',
    'kn': 'values-kn',
    'ml': 'values-ml',
    'mr': 'values-mr',
    'or': 'values-or',
    'pa': 'values-pa',
    'ta': 'values-ta',
    'te': 'values-te',
}

shutil.rmtree("./android_res", ignore_errors=True)

# Read the CSV file
with open(csv_file, 'r') as file:
    reader = csv.DictReader(file)
    headers = reader.fieldnames

    # Iterate over each row in the CSV file
    for row in reader:
        # Get the name and values from the row
        name = row['name']

        # if ame is blank, skip this row
        if name == '':
            continue

        # Iterate over each language and its corresponding value
        for lang in headers[1:]:
            value = row[lang]
            if value == '':
                continue

            # Create the XML file path
            output_folder = "./android_res/"+ output_folders[lang]
            os.makedirs(output_folder, exist_ok=True)
            xml_file = os.path.join(output_folder, 'strings.xml')

            # If the XML file already exists, parse it and append the new <string> element
            if os.path.exists(xml_file):
                tree = ET.parse(xml_file)
                root = tree.getroot()
            else:
                # If the XML file doesn't exist, create a new XML tree with root element 'resources'
                root = ET.Element('resources')

            # Create the 'string' element with the name attribute and text value
            string_elem = ET.SubElement(root, 'string')
            string_elem.set('name', name)
            string_elem.text = value

            # Write the XML tree to the file
            tree = ET.ElementTree(root)
            ET.indent(tree, "  ") # two space tab in 
            tree.write(xml_file, encoding='utf-8', xml_declaration=True)

print("XML files android_res successfully!")