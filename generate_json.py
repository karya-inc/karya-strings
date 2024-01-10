import csv
import json
from collections import defaultdict

# Define the CSV file path
csv_file = "./source.csv"
json_output_file = "./desktop_res.json"


# Read the CSV file
with open(csv_file, "r") as file:
    reader = csv.DictReader(file)
    headers = reader.fieldnames

    if headers is None:
        raise TypeError("headers cannot be None")

    resources = defaultdict(dict)

    # Iterate over each row in the CSV file
    for row in reader:
        # Get the name and values from the row
        name = row["name"]

        # if ame is blank, skip this row
        if name == "":
            continue

        # Iterate over each language and its corresponding value
        for lang in headers[1:]:
            value = row[lang]
            if value == "":
                continue

            if "translation" not in resources[lang]:
                resources[lang]["translation"] = {}

            formatted_value = value

            splitpoints = ["s", "d"]
            for splitchar in splitpoints:
                split = formatted_value.split(f"%{splitchar}")
                updated_value = split[0]
                for i in range(1, len(split)):
                    fmt = f"{{{{ {splitchar}{i} }}}}"
                    updated_value = updated_value + fmt + split[i]
                formatted_value = updated_value

            resources[lang]["translation"][name] = formatted_value

    resources_json = json.dumps(resources, ensure_ascii=False, indent=2)

    with open(json_output_file, "w+") as output_file:
        output_file.write(resources_json)
        print("JSON Resources for desktop application written successfully")
