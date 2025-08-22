import csv

def csv_to_dicts(csv_path):
    data = []
    with open(csv_path, mode='r', newline='', encoding='utf-8-sig') as csv_file:
        reader = csv.DictReader(csv_file)
        for row in reader:
            cleaned_row = {}
            for key, value in row.items():
                value = value.strip()
                if value == "":
                    continue
                cleaned_row[key] = value
            data.append(cleaned_row)
    return data