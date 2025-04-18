import re
from typing import List, Set, Optional
from loguru import logger
import click


class PhoneExtractor:
    def __init__(self):
        self.pattern = re.compile(r'''
            (?:\+7|8)              
            [\s\-\(\)]*           
            (\d{3})               
            [\s\-\(\)]*           
            (\d{3})               
            [\s\-\(\)]*           
            (\d{2})               
            [\s\-\(\)]*           
            (\d{2})               
        ''', re.VERBOSE)

    def normalize_phone(self, match: re.Match) -> str:
        """Convert matched phone number to standard format."""
        return f"+7({match.group(1)}){match.group(2)}-{match.group(3)}-{match.group(4)}"

    def extract_phones_from_file(self, file_path: str) -> List[str]:
        """Extract and normalize phone numbers from a file."""
        try:
            with open(file_path, 'r', encoding='utf-8') as file:
                content = file.read()
            
            matches = self.pattern.finditer(content)
            phones = [self.normalize_phone(match) for match in matches]
            
            seen: Set[str] = set()
            unique_phones = []
            for phone in phones:
                if phone not in seen:
                    seen.add(phone)
                    unique_phones.append(phone)
            
            return unique_phones
        except Exception as e:
            logger.error(f"Error processing file {file_path}: {str(e)}")
            return []


@click.command()
@click.argument('input_file', type=click.Path(exists=True))
@click.option('--output', '-o', type=click.Path(), help='Output file path')
def main(input_file: str, output: Optional[str] = None):
    """Extract phone numbers from a text file and output them in a standardized format."""
    extractor = PhoneExtractor()
    phones = extractor.extract_phones_from_file(input_file)
    
    if output:
        with open(output, 'w', encoding='utf-8') as f:
            for phone in phones:
                f.write(f"{phone}\n")
        logger.info(f"Found {len(phones)} unique phone numbers. Results written to {output}")
    else:
        for phone in phones:
            print(phone)
        logger.info(f"Found {len(phones)} unique phone numbers.")


if __name__ == '__main__':
    main()
