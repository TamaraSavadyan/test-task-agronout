# Phone Number Extractor

A Python utility for extracting and normalizing phone numbers from text files. The tool processes text content and converts all found phone numbers into a standardized format.

## Features

- Extracts phone numbers from text files
- Supports various phone number formats
- Converts all numbers to a standardized format: +7(YYY)XXX-XX-XX
- Preserves the order of first appearance
- Removes duplicate numbers
- Supports both console output and file output

## Requirements

- Python 3.11 or higher
- Dependencies listed in requirements.txt:
  - loguru
  - click
  - six

## Installation

1. Clone the repository
2. Create and activate a virtual environment (recommended):
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```
3. Install dependencies:
```bash
pip install -r requirements.txt
```

## Usage

Basic usage:
```bash
python phone_extractor.py input_file.txt
```

Save output to a file:
```bash
python phone_extractor.py input_file.txt -o output.txt
```

### Input Format

The tool accepts text files containing phone numbers in various formats, such as:
- +7 912-345-67-89
- 8 (495) 123 45 67
- +7(903) 456 78 90
- 8-900-111-22-33
- +7 (999) 888.77.66

### Output Format

All phone numbers are converted to the standardized format:
```
+7(YYY)XXX-XX-XX
```


## Example

Input file (sample_input.txt):
```
Связаться с нами можно по телефону +7 912-345-67-89 или 8 (495) 123 45 67.
Также работает WhatsApp: +7(903) 456 78 90.
```

Output:
```
+7(912)345-67-89
+7(495)123-45-67
+7(903)456-78-90
```

## Error Handling

The tool includes basic error handling:
- Logs errors if the input file cannot be read
- Provides informative error messages
- Continues processing even if some numbers are invalid
