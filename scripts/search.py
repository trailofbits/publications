#!/usr/bin/env python3
"""
Search and query Trail of Bits publications metadata.
"""

import json
import argparse
from pathlib import Path
from collections import defaultdict

METADATA_DIR = Path(__file__).parent.parent / "metadata"
INDEX_FILE = METADATA_DIR / "publications.json"

def load_index():
    """Load master publications index."""
    with open(INDEX_FILE, 'r') as f:
        return json.load(f)

def search_publications(index, **filters):
    """Search publications with various filters."""
    results = []

    for pub in index['publications']:
        # Check all filters
        match = True

        # Type filter
        if filters.get('type') and pub['type'] != filters['type']:
            match = False

        # Domain filter
        if filters.get('domain'):
            pub_domains = pub.get('categories', {}).get('domain', [])
            if filters['domain'] not in pub_domains:
                match = False

        # Technology filter
        if filters.get('technology'):
            pub_techs = pub.get('tags', {}).get('technologies', [])
            if filters['technology'] not in pub_techs:
                match = False

        # Topic filter
        if filters.get('topic'):
            pub_topics = pub.get('tags', {}).get('topics', [])
            if filters['topic'] not in pub_topics:
                match = False

        # Tool filter
        if filters.get('tool'):
            pub_tools = pub.get('tags', {}).get('tools', [])
            if filters['tool'] not in pub_tools:
                match = False

        # Platform filter
        if filters.get('platform'):
            pub_platforms = pub.get('tags', {}).get('platforms', [])
            if filters['platform'] not in pub_platforms:
                match = False

        # Client filter (for reviews)
        if filters.get('client'):
            pub_client = pub.get('metadata', {}).get('client', '')
            if filters['client'].lower() not in pub_client.lower():
                match = False

        # Year filter
        if filters.get('year'):
            pub_date = pub.get('publicationDate', '')
            if filters['year'] not in pub_date:
                match = False

        # Text search (title)
        if filters.get('text'):
            if filters['text'].lower() not in pub.get('title', '').lower():
                match = False

        if match:
            results.append(pub)

    return results

def print_results(results, format='table'):
    """Print search results."""
    if not results:
        print("No results found.")
        return

    print(f"\nFound {len(results)} publications:\n")

    if format == 'table':
        # Print as table
        for i, pub in enumerate(results, 1):
            print(f"{i}. {pub['title']}")
            print(f"   Type: {pub['type']}")
            print(f"   Date: {pub.get('publicationDate', 'unknown')}")

            domains = pub.get('categories', {}).get('domain', [])
            if domains:
                print(f"   Domains: {', '.join(domains)}")

            topics = pub.get('tags', {}).get('topics', [])
            if topics:
                print(f"   Topics: {', '.join(topics[:5])}")

            url = pub.get('url', '')
            if url:
                print(f"   URL: {url}")

            print()

    elif format == 'json':
        print(json.dumps(results, indent=2))

    elif format == 'count':
        print(f"Total: {len(results)}")

def list_values(index, field):
    """List all unique values for a field."""
    values = set()

    for pub in index['publications']:
        if field == 'domains':
            values.update(pub.get('categories', {}).get('domain', []))
        elif field == 'topics':
            values.update(pub.get('tags', {}).get('topics', []))
        elif field == 'technologies':
            values.update(pub.get('tags', {}).get('technologies', []))
        elif field == 'tools':
            values.update(pub.get('tags', {}).get('tools', []))
        elif field == 'platforms':
            values.update(pub.get('tags', {}).get('platforms', []))
        elif field == 'types':
            values.add(pub['type'])

    return sorted(values)

def stats(index):
    """Print statistics about the publications."""
    print("\nPublications Statistics")
    print("=" * 80)
    print(f"Total publications: {index['total']}\n")

    print("By Type:")
    for pub_type, count in sorted(index['by_type'].items(), key=lambda x: -x[1]):
        print(f"  {pub_type:30} {count:4}")

    print("\nBy Domain:")
    for domain, count in sorted(index['by_domain'].items(), key=lambda x: -x[1]):
        print(f"  {domain:30} {count:4}")

    print()

def main():
    parser = argparse.ArgumentParser(description='Search Trail of Bits publications')
    parser.add_argument('--type', help='Filter by publication type')
    parser.add_argument('--domain', help='Filter by domain')
    parser.add_argument('--technology', help='Filter by technology')
    parser.add_argument('--topic', help='Filter by topic')
    parser.add_argument('--tool', help='Filter by tool')
    parser.add_argument('--platform', help='Filter by platform')
    parser.add_argument('--client', help='Filter by client name')
    parser.add_argument('--year', help='Filter by year')
    parser.add_argument('--text', help='Search in title')
    parser.add_argument('--format', choices=['table', 'json', 'count'], default='table',
                        help='Output format')
    parser.add_argument('--list', choices=['domains', 'topics', 'technologies', 'tools', 'platforms', 'types'],
                        help='List all values for a field')
    parser.add_argument('--stats', action='store_true', help='Show statistics')

    args = parser.parse_args()

    # Load index
    index = load_index()

    # Show stats
    if args.stats:
        stats(index)
        return

    # List values
    if args.list:
        values = list_values(index, args.list)
        print(f"\nAll {args.list}:")
        for value in values:
            print(f"  - {value}")
        print(f"\nTotal: {len(values)}")
        return

    # Search
    filters = {
        'type': args.type,
        'domain': args.domain,
        'technology': args.technology,
        'topic': args.topic,
        'tool': args.tool,
        'platform': args.platform,
        'client': args.client,
        'year': args.year,
        'text': args.text,
    }

    # Remove None values
    filters = {k: v for k, v in filters.items() if v is not None}

    results = search_publications(index, **filters)
    print_results(results, format=args.format)

if __name__ == "__main__":
    main()
