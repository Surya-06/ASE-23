from pathlib import Path
import re

def coerce(s):
    s = float(s) if bool(re.search(r'\d', s)) else s
    return s

def get_csv_rows(filepath: str) -> []:
        filepath = Path(filepath);
        print("Exists criteria : ", filepath.exists())
        print("suffix : ", filepath.suffix)

        if not filepath.exists() or filepath.suffix != '.csv':
            print("File path does not exist OR File not csv, given path: ", filepath.absolute())
            return

        rows = []
        with open(filepath.absolute(), 'r', encoding='utf-8') as file:
            for row_no, line in enumerate(file):
                row = list(map(coerce, line.strip().split(',')))
                rows.append(row)

        print("Found {} rows in the file", len(rows))

        return rows
