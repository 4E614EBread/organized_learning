import os
import csv
import pandas as pd

# Check if 'test_files' exists as a file
if os.path.exists('test_files') and not os.path.isdir('test_files'):
    print("Error: 'test_files' exists as a file, not a directory. Please rename or remove the file.")
else:
    # Create test folder if it doesn't exist
    try:
        os.makedirs('test_files', exist_ok=True)
        print("Directory 'test_files' created or already exists.")
    except Exception as e:
        print(f"Error creating directory: {e}")

    # Test URLs
    urls = [
        "https://example.com",
        "https://github.com",
        "https://docs.python.org"
    ]

    # Create CSV file
    csv_file_path = 'test_files/test_links.csv'
    try:
        if not os.path.exists(csv_file_path):
            with open(csv_file_path, mode='w', newline='') as file:
                writer = csv.writer(file)
                writer.writerow(urls)
            print(f"CSV file '{csv_file_path}' created.")
        else:
            print(f"CSV file '{csv_file_path}' already exists.")
    except Exception as e:
        print(f"Error creating CSV file: {e}")

    # Create TXT file
    txt_file_path = 'test_files/test_links.txt'
    try:
        if not os.path.exists(txt_file_path):
            with open(txt_file_path, mode='w') as file:
                for url in urls:
                    file.write(url + '\n')
            print(f"TXT file '{txt_file_path}' created.")
        else:
            print(f"TXT file '{txt_file_path}' already exists.")
    except Exception as e:
        print(f"Error creating TXT file: {e}")

    # Create Excel file
    excel_file_path = 'test_files/test_links.xlsx'
    try:
        if not os.path.exists(excel_file_path):
            df = pd.DataFrame({'link': urls})
            df.to_excel(excel_file_path, index=False)
            print(f"Excel file '{excel_file_path}' created.")
        else:
            print(f"Excel file '{excel_file_path}' already exists.")
    except Exception as e:
        print(f"Error creating Excel file: {e}")
