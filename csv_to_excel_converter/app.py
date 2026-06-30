import argparse
import sys
from logger import logger
from converter import convert_csv_to_excel

def main():
    parser = argparse.ArgumentParser(description="Professional CSV to Excel Converter Utility")
    parser.add_argument('-i', '--input', required=True, help="Path to the source CSV file.")
    parser.add_argument('-o', '--output', required=True, help="Target path for Excel output.")
    args = parser.parse_args()

    logger.info("Initializing conversion task...")
    success = convert_csv_to_excel(args.input, args.output)
    
    if success:
        logger.info("Task completed successfully.")
        sys.exit(0)
    else:
        logger.error("Task failed.")
        sys.exit(1)

if __name__ == "__main__":
    main()
