# JSON Sync Tool

This tool is designed to sync keys between two JSON files, maintaining the structure of the original JSON file while incorporating modifications from a second file. It ensures that any keys present in the original JSON file are also included in the output, while taking values from the modified JSON file where available.

## Features

- Load and process JSON files.
- Synchronize keys between an original and a modified JSON file.
- Rearrange the keys of a modified JSON file while preserving the order of keys from the original JSON file.
- If the modified JSON file does not exist, copy the original JSON file as-is.
- Write the resulting JSON to a specified output file.
- Handle file reading and writing errors gracefully.
- Supports reading and writing in UTF-8 encoding, accommodating non-ASCII characters such as Japanese.

## Installation

1. Clone this repository or download the script.
2. Ensure you have Python 3 installed.

## Dependencies

This script uses standard Python libraries and does not require any external dependencies. However, it is recommended to use Python 3.6 or later.

## Usage

The script can be executed from the command line using the following command:

```bash
python json_sync_tool.py <originalFilePath> <modifiedFilePath> <outputFilePath>
```

### Parameters

- `<originalFilePath>`: The path to the original JSON file. This file will provide the base structure and default values.
- `<modifiedFilePath>`: The path to the modified JSON file. This file will provide the updated values for existing keys in the original JSON.
- `<outputFilePath>`: The path where the synchronized output JSON will be saved.

### Example

```bash
python json_sync_tool.py data/original.json data/modified.json output/synced.json
```

This command will synchronize the JSON keys from `original.json` with `modified.json` and save the result to `synced.json`.

### Error Handling

- If the modified JSON file is not found or cannot be loaded, the script will copy the original JSON to the output file path.
- If there is an error writing to the output file, an error message will be printed.

## Functionality Overview

### load\_json(file\_path: str) -> Dict[str, Any]

Loads and returns a JSON object from a specified file path. If an error occurs, it returns an empty dictionary.

### write\_json(json\_data: Dict[str, Any], file\_path: str) -> None

Writes the given JSON object to a specified file path. If an error occurs, it prints an error message.

### sync\_keys(original: Dict[str, Any], modified: Dict[str, Any]) -> Dict[str, Any]

Creates a synchronized JSON object that retains keys from the original JSON, with values being replaced by those from the modified JSON if they exist.

### process\_json\_files(original\_file\_path: str, modified\_file\_path: str, output\_file\_path: str) -> None

Loads, synchronizes, and writes the JSON files, based on the paths provided as arguments.

## License

This tool is released under the [MIT License](/LICENSE).

## Contributing

Feel free to submit issues or pull requests if you have suggestions for improvements or new features.

## Contact

For any questions or suggestions, please contact [dev@tukuyo.net](mailto\:dev@tukuyo.net).
