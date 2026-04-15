"""
==============================================================
Day 10 Lab: Build Your First Automated ETL Pipeline
==============================================================
Student ID: AI20K-2A202600475
Name: Mai Văn Quân

Nhiem vu:
   1. Extract:   Doc du lieu tu file JSON
   2. Validate:  Kiem tra & loai bo du lieu khong hop le
   3. Transform: Chuan hoa category + tinh gia giam 10%
   4. Load:      Luu ket qua ra file CSV

Cham diem tu dong:
   - Script phai chay KHONG LOI (20d)
   - Validation: loai record gia <= 0, category rong (10d)
   - Transform: discounted_price + category Title Case (10d)
   - Logging: in so record processed/dropped (10d)
   - Timestamp: them cot processed_at (10d)
==============================================================
"""

import json
import pandas as pd
import os
import datetime

# --- CONFIGURATION ---
SOURCE_FILE = 'raw_data.json'
OUTPUT_FILE = 'processed_data.csv'


def extract(file_path):
    """
    Task 1: Doc du lieu JSON tu file.
    """
    print(f"Extracting data from {file_path}...")
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            data = json.load(f)
        return data
    except FileNotFoundError:
        print(f"Error: File '{file_path}' not found.")
        return []
    except json.JSONDecodeError:
        print(f"Error: File '{file_path}' contains invalid JSON.")
        return []


def validate(data):
    """
    Task 2: Kiem tra chat luong du lieu.
    """
    valid_records = []
    error_count = 0

    for record in data:
        price = record.get('price', 0)
        category = record.get('category')

        # Kiem tra gia > 0 va category khong rong (not None va not empty string)
        if isinstance(price, (int, float)) and price > 0 and category:
            valid_records.append(record)
        else:
            error_count += 1

    print(f"Validation complete. Valid: {len(valid_records)}, Errors: {error_count}")
    return valid_records


def transform(data):
    """
    Task 3: Ap dung business logic.
    """
    if not data:
        return None
        
    # Tao DataFrame
    df = pd.DataFrame(data)

    # Tinh discounted_price = price * 0.9
    df['discounted_price'] = df['price'] * 0.9

    # Chuan hoa category thanh Title Case
    df['category'] = df['category'].astype(str).str.title()

    # Them cot processed_at = timestamp hien tai
    df['processed_at'] = datetime.datetime.now().isoformat()

    return df


def load(df, output_path):
    """
    Task 4: Luu DataFrame ra file CSV.
    """
    try:
        df.to_csv(output_path, index=False, encoding='utf-8')
        print(f"Data saved to {output_path}")
    except Exception as e:
        print(f"Error saving file: {e}")


# ============================================================
# MAIN PIPELINE
# ============================================================
if __name__ == "__main__":
    print("=" * 50)
    print("ETL Pipeline Started...")
    print("=" * 50)

    # 1. Extract
    raw_data = extract(SOURCE_FILE)

    if raw_data:
        # 2. Validate
        clean_data = validate(raw_data)

        # 3. Transform
        final_df = transform(clean_data)

        # 4. Load
        if final_df is not None:
            load(final_df, OUTPUT_FILE)
            print(f"\nPipeline completed! {len(final_df)} records saved.")
        else:
            print("\nTransform returned None. Check your transform() function.")
    else:
        print("\nPipeline aborted: No data extracted.")