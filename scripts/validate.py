#!/usr/bin/env python3
"""
Validate publications metadata against JSON schema.
"""

import json
import jsonschema
from pathlib import Path
from collections import defaultdict

METADATA_DIR = Path(__file__).parent.parent / "metadata"
SCHEMA_FILE = METADATA_DIR / "schema.json"

def load_schema():
    """Load JSON schema."""
    with open(SCHEMA_FILE, 'r') as f:
        return json.load(f)

def find_metadata_files():
    """Find all metadata JSON files."""
    files = []
    for subdir in METADATA_DIR.glob('*/'):
        if subdir.is_dir() and subdir.name not in ['__pycache__']:
            files.extend(subdir.glob('*.json'))
    return files

def validate_file(file_path, schema):
    """Validate a single metadata file."""
    try:
        with open(file_path, 'r') as f:
            data = json.load(f)

        # Validate against schema
        jsonschema.validate(instance=data, schema=schema)
        return True, None

    except jsonschema.ValidationError as e:
        return False, f"Schema validation error: {e.message}"
    except json.JSONDecodeError as e:
        return False, f"JSON parse error: {e}"
    except Exception as e:
        return False, f"Error: {e}"

def main():
    print("=" * 80)
    print("VALIDATING PUBLICATIONS METADATA")
    print("=" * 80)
    print()

    # Load schema
    print(f"Loading schema from {SCHEMA_FILE}...")
    schema = load_schema()
    print("✓ Schema loaded")
    print()

    # Find metadata files
    print("Finding metadata files...")
    files = find_metadata_files()
    print(f"✓ Found {len(files)} metadata files")
    print()

    # Validate each file
    print("Validating files...")
    errors = []
    stats = defaultdict(int)

    for i, file_path in enumerate(sorted(files), 1):
        valid, error = validate_file(file_path, schema)

        if valid:
            stats['valid'] += 1
        else:
            stats['invalid'] += 1
            errors.append((file_path.name, error))

        if i % 100 == 0:
            print(f"  Validated {i}/{len(files)}...")

    print(f"✓ Validation complete")
    print()

    # Print results
    print("=" * 80)
    print("VALIDATION RESULTS")
    print("=" * 80)
    print(f"Total files:    {len(files)}")
    print(f"Valid:          {stats['valid']}")
    print(f"Invalid:        {stats['invalid']}")
    print()

    if errors:
        print("Errors:")
        for filename, error in errors[:20]:
            print(f"  - {filename}: {error}")

        if len(errors) > 20:
            print(f"  ... and {len(errors) - 20} more errors")

        print()
        return 1

    print("✓ All metadata files are valid!")
    return 0

if __name__ == "__main__":
    import sys
    sys.exit(main())
