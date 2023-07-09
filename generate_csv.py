import csv
import xml.etree.ElementTree as ET


# Define the language codes and corresponding file paths
languages = {
    'as': './src/values-as/strings.xml',
    'bn': './src/values-bn/strings.xml',
    'en': './src/values/strings.xml',
    'gu': './src/values-gu/strings.xml',
    'hi': './src/values-hi/strings.xml',
    'kn': './src/values-kn/strings.xml',
    'ml': './src/values-ml/strings.xml',
    'mr': './src/values-mr/strings.xml',
    'or': './src/values-or/strings.xml',
    'pa': './src/values-pa/strings.xml',
    'ta': './src/values-ta/strings.xml',
    'te': './src/values-te/strings.xml',
}

# Create a dictionary to store the data
data = {}

# Iterate over each language and parse the corresponding XML file
for lang, filepath in languages.items():
    print(filepath)
    tree = ET.parse(filepath)
    root = tree.getroot()

    # Iterate over each <string> element and extract the name and value
    for string_elem in root.findall('string'):
        name = string_elem.get('name')
        value = string_elem.text

        # If the name already exists in the dictionary, update the value for the current language
        if name in data:
            data[name][lang] = value
        else:
            # If the name doesn't exist, create a new entry in the dictionary with the value for the current language
            data[name] = {lang: value}

# Define the CSV file path
csv_file = './output.csv'

# Write the data to the CSV file
with open(csv_file, 'w', newline='') as file:
    writer = csv.writer(file)
    
    # Write the headers to the CSV file
    writer.writerow(["name",*(languages.keys())])
    
    # Write each row of data to the CSV file
    for name, values in data.items():
        # Create a list of values for the row, using None if a language doesn't have a value for a given name
        row = [values.get(lang) for lang in languages.keys()]
        
        # Write the row to the CSV file
        writer.writerow([name] + row)

print(f"CSV file created: {csv_file}")
