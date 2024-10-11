import json
import sys
from typing import Any, Dict

def load_json(file_path: str) -> Dict[str, Any]:
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            return json.load(file)
    except Exception as e:
        print(f"Error reading file at path: {file_path}. Error: {e}")
        return {}

def write_json(json_data: Dict[str, Any], file_path: str) -> None:
    try:
        with open(file_path, 'w', encoding='utf-8') as file:
            json.dump(json_data, file, indent=4, ensure_ascii=False)
    except Exception as e:
        print(f"Error writing JSON to file: {e}")

def sync_keys(original: Dict[str, Any], modified: Dict[str, Any]) -> Dict[str, Any]:
    sync_json = {}

    for key in original.keys():
        if key in modified:
            sync_json[key] = modified[key]
        else:
            sync_json[key] = original[key]
    
    return sync_json

def process_json_files(original_file_path: str, modified_file_path: str, output_file_path: str) -> None:
    original_json = load_json(original_file_path)
    
    modified_json = load_json(modified_file_path)
    if not modified_json:
        print("Modified JSON file not found. Copying the original JSON.")
        write_json(original_json, output_file_path)
        return
    
    sync_json = sync_keys(original_json, modified_json)
    write_json(sync_json, output_file_path)
    print(f"Processed JSON file has been saved to: {output_file_path}")

if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Usage: python json_sorter.py <originalFilePath> <modifiedFilePath> <outputFilePath>")
    else:
        original_file_path = sys.argv[1]
        modified_file_path = sys.argv[2]
        output_file_path = sys.argv[3]
        
        process_json_files(original_file_path, modified_file_path, output_file_path)