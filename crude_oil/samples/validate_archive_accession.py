import csv
import json

# Открываем TSV-файл для чтения
with open('crude_oil_samples.tsv', 'r') as tsvfile:
    reader = csv.DictReader(tsvfile, delimiter='\t')
    # Преобразуем данные в список словарей, приводя значения полей к нужным типам данных
    rows = [
        {
            "project_name": row["project_name"],
            "publication_year": int(row["publication_year"]),
            "publication_doi": row["publication_doi"],
            "site_name": row["site_name"],
            "latitude": float(row["latitude"]) if row["latitude"] != "NA" else None,
            "longitude": float(row["longitude"]) if row["longitude"] != "NA" else None,
            "geo_loc_name": row["geo_loc_name"],
            "study_primary_focus": row["study_primary_focus"],
            "sequence_name": row["sequence_name"],
            "depth": float(row["depth"]) if row["depth"] != "NA" else None,
            "sample_name": row["sample_name"],
            "sample_age": int(row["sample_age"]) if row["sample_age"] != "NA" else None,
            "sample_age_doi": row["sample_age_doi"] if row["sample_age_doi"] != "NA" else None,
            "feature": row["feature"],
            "material": row["material"],
            "sampling_date": int(row["sampling_date"]) if row["sampling_date"] != "NA" else None,
            "archive": row["archive"],
            "archive_project": row["archive_project"],
            "archive_accession": row["archive_accession"]
        }
        for row in reader
    ]

# Открываем JSON-файл для записи
with open('crude_oil_samples.json', 'w') as jsonfile:
    # Записываем данные в формате JSON
    json.dump(rows, jsonfile, indent=4, ensure_ascii=False)
    
# Open and read the JSON file
with open('crude_oil_samples.json', 'r') as jsonfile:
    # Load the JSON data as a dictionary object
    data = json.loads(jsonfile.read())

# Create a set of all values in the "archive_accession" column
all_accessions = set()
for item in data:
    archive_accession = item['archive_accession']
    if archive_accession:
        accession_list = [value.strip() for value in archive_accession.split(',') if value.strip()]
        all_accessions.update(accession_list)

# Check if the number of unique values in the set is equal to the total number of values in the "archive_accession" column
if len(all_accessions) != sum(1 for item in data if item['archive_accession']):
    print('Error: Duplicate values found in "archive_accession"')
    exit(1)
else:
    print('All archive_accession are unique')