import csv
import os
import xml.etree.ElementTree as ET

# Define the CSV file path
csv_file = './output.csv'

# Define the output folder paths for each language
output_folders = {
    'as': './generated/values-as',
    'bn': './generated/values-bn',
    'en': './generated/values',
    'gu': './generated/values-gu',
    'hi': './generated/values-hi',
    'kn': './generated/values-kn',
    'ml': './generated/values-ml',
    'mr': './generated/values-mr',
    'or': './generated/values-or',
    'pa': './generated/values-pa',
    'ta': './generated/values-ta',
    'te': './generated/values-te',
}

# Read the CSV file
with open(csv_file, 'r') as file:
    reader = csv.DictReader(file)
    headers = reader.fieldnames

    # Iterate over each row in the CSV file
    for row in reader:
        # Get the name and values from the row
        name = row['name']

        # Iterate over each language and its corresponding value
        for lang in headers[1:]:
            value = row[lang]

            # Create the XML file path
            output_folder = output_folders[lang]
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
            ET.indent(tree, " ")
            tree.write(xml_file, encoding='utf-8', xml_declaration=True)

print("XML files generated successfully!")