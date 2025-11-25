# Publications Metadata Guidelines

This document explains how to use and maintain the Trail of Bits publications metadata system.

## Overview

The publications repository now includes **structured metadata** for all 816+ publications, enabling:
- Multi-dimensional search and filtering
- Programmatic querying via JSON
- Topic-based discovery across publication types
- Technology stack filtering

**Key Features:**
- ✅ 816 publications with metadata
- ✅ JSON schema validation
- ✅ Search and query tools
- ✅ Aligned with blog taxonomy

---

## Directory Structure

```
publications/
├── README.md                    # Primary human interface
├── metadata/                    # Structured metadata
│   ├── schema.json             # JSON Schema definition
│   ├── publications.json       # Master index
│   ├── papers/                 # Academic paper metadata
│   ├── presentations/          # Presentation metadata
│   ├── reviews/                # Security review metadata
│   ├── podcasts/               # Podcast metadata
│   ├── workshops/              # Workshop metadata
│   ├── guides/                 # Guide metadata
│   └── comments/               # Public comment metadata
├── scripts/                     # Tools
│   ├── search.py               # Search/query tool
│   └── validate.py             # Validation script
└── [papers/, presentations/, reviews/, etc.]  # Actual files
```

---

## Metadata Schema

Each publication has a JSON metadata file with the following structure:

```json
{
  "id": "unique-publication-id",
  "title": "Publication Title",
  "type": "academic-paper|white-paper|presentation|security-review|...",
  "publicationDate": "2024-01-15",
  "authors": ["Author Name"],
  "url": "path/to/file.pdf",

  "categories": {
    "publicationType": "academic-paper",
    "domain": ["blockchain", "cryptography"],
    "subdomain": ["smart-contracts", "zero-knowledge-proofs"]
  },

  "tags": {
    "topics": ["fuzzing", "formal-verification"],
    "technologies": ["solidity", "rust"],
    "tools": ["echidna", "slither"],
    "platforms": ["ethereum"],
    "concepts": ["reentrancy", "memory-safety"]
  },

  "metadata": {
    "venue": "USENIX Security 2024",
    "client": "Offchain Labs",
    "reviewType": "security-assessment",
    "announcementUrl": "https://..."
  }
}
```

---

## Adding a New Publication

### Step 1: Add to README.md

Add your publication to the appropriate section in `README.md` following existing format:

```markdown
| [Publication Title](path/to/file.pdf) | Author(s) | Date |
```

### Step 2: Create Metadata File

Create a JSON file in the appropriate metadata subdirectory:

**Filename:** `metadata/{type}/{slug}-{hash}.json`

Where:
- `{type}` = papers, presentations, reviews, etc.
- `{slug}` = URL-friendly title
- `{hash}` = 8-character unique ID

**Example:** `metadata/papers/echidna-fuzzing-smart-contracts-a1b2c3d4.json`

### Step 3: Fill in Metadata

```json
{
  "id": "echidna-fuzzing-smart-contracts-a1b2c3d4",
  "title": "Echidna: Effective, Usable, and Fast Fuzzing for Smart Contracts",
  "type": "academic-paper",
  "publicationDate": "2020",
  "authors": ["Gustavo Grieco", "Will Song", "Artem Cygan"],
  "url": "papers/echidna_issta2020.pdf",

  "categories": {
    "publicationType": "academic-paper",
    "domain": ["fuzzing", "blockchain"],
    "subdomain": ["smart-contracts", "property-testing"]
  },

  "tags": {
    "topics": ["fuzzing", "smart-contracts", "property-testing"],
    "technologies": ["solidity"],
    "tools": ["echidna"],
    "platforms": ["ethereum"],
    "concepts": ["invariant-testing"]
  },

  "metadata": {
    "venue": "ISSTA 2020",
    "venueType": "conference",
    "peerReviewed": true
  }
}
```

### Step 4: Validate

Run validation to ensure your metadata is correct:

```bash
cd publications
python3 scripts/validate.py
```

---

## Publication Types

| Type | Description | Metadata Directory |
|------|-------------|-------------------|
| `academic-paper` | Peer-reviewed research | `metadata/papers/` |
| `white-paper` | Technical reports | `metadata/papers/` |
| `guide` | Educational handbooks | `metadata/guides/` |
| `presentation` | Conference talks | `metadata/presentations/` |
| `podcast` | Interview appearances | `metadata/podcasts/` |
| `webinar` | Live technical sessions | `metadata/presentations/` |
| `public-comment` | Regulatory submissions | `metadata/comments/` |
| `security-review` | Client assessments | `metadata/reviews/` |
| `disclosure` | Vulnerability disclosures | `metadata/papers/` |
| `workshop` | Training materials | `metadata/workshops/` |
| `dataset` | Data collections | `metadata/datasets/` |
| `service-overview` | Service descriptions | `metadata/guides/` |

---

## Taxonomy Dimensions

### Categories

**Domains** (Primary technical area):
- `blockchain` - Smart contracts, DeFi, Web3
- `cryptography` - Cryptographic protocols
- `ai-ml` - AI/ML security
- `fuzzing` - Fuzzing and testing
- `static-analysis` - Static code analysis
- `dynamic-analysis` - Runtime analysis
- `program-analysis` - Program analysis
- `reversing` - Reverse engineering
- `compilers` - Compiler security
- `kernel` - OS and kernel security
- `platform-security` - Platform-specific
- `mobile-security` - Mobile platforms
- `cloud-native` - Containers, Kubernetes
- `supply-chain` - Supply chain security
- `application-security` - Application security
- `infrastructure` - Infrastructure security
- `engineering` - Engineering practices
- `education` - Educational content

**Subdomains** (More specific areas):
- `smart-contracts`, `defi`, `wallets`, `bridges`
- `zero-knowledge-proofs`, `threshold-cryptography`, `post-quantum`
- `property-testing`, `differential-fuzzing`, `symbolic-execution`

### Tags

**Topics:** High-level security topics
- `fuzzing`, `formal-verification`, `threat-modeling`, `vulnerability-research`

**Technologies:** Programming languages/frameworks
- `solidity`, `rust`, `go`, `python`, `c-cpp`, `llvm`, `mlir`, `webassembly`

**Tools:** Specific security tools
- `echidna`, `slither`, `manticore`, `semgrep`, `codeql`, `binary-ninja`, `buttercup`

**Platforms:** Blockchain platforms, OS
- `ethereum`, `solana`, `arbitrum`, `avalanche`, `algorand`, `cosmos`, `starknet`
- `linux`, `macos`, `windows`, `kubernetes`

**Concepts:** Security concepts
- `reentrancy`, `memory-corruption`, `access-control`, `timing-attacks`, `integer-overflow`

---

## Using the Search Tool

### Basic Usage

```bash
cd publications
python3 scripts/search.py [options]
```

### Examples

**Show statistics:**
```bash
python3 scripts/search.py --stats
```

**List all domains:**
```bash
python3 scripts/search.py --list domains
```

**Find all fuzzing publications:**
```bash
python3 scripts/search.py --domain fuzzing
```

**Find Rust security work:**
```bash
python3 scripts/search.py --technology rust
```

**Find all Echidna publications:**
```bash
python3 scripts/search.py --tool echidna
```

**Find blockchain security reviews:**
```bash
python3 scripts/search.py --type security-review --domain blockchain
```

**Complex query:**
```bash
python3 scripts/search.py --domain blockchain --technology solidity --topic fuzzing
```

**Get JSON output:**
```bash
python3 scripts/search.py --domain cryptography --format json
```

**Count results:**
```bash
python3 scripts/search.py --domain ai-ml --format count
```

### Search Options

| Option | Description | Example |
|--------|-------------|---------|
| `--type` | Filter by publication type | `--type academic-paper` |
| `--domain` | Filter by domain | `--domain blockchain` |
| `--technology` | Filter by technology | `--technology rust` |
| `--topic` | Filter by topic | `--topic fuzzing` |
| `--tool` | Filter by tool | `--tool slither` |
| `--platform` | Filter by platform | `--platform ethereum` |
| `--client` | Filter by client (reviews) | `--client "Offchain Labs"` |
| `--year` | Filter by year | `--year 2024` |
| `--text` | Search in title | `--text "smart contract"` |
| `--format` | Output format | `--format json` (table/json/count) |
| `--list` | List all values | `--list domains` |
| `--stats` | Show statistics | `--stats` |

---

## Review-Specific Metadata

For security reviews, add additional fields:

```json
{
  "type": "security-review",
  "metadata": {
    "client": "Offchain Labs",
    "product": "Nitro",
    "blockchain": "Ethereum",
    "reviewType": "security-assessment",
    "technologyStack": ["Go", "Solidity", "WebAssembly"],
    "announcementUrl": "https://...",
  }
}
```

**Review Types:**
- `security-assessment` - Full security audit
- `code-review` - Code review only
- `threat-model` - Threat modeling
- `letter-of-attestation` - LOA
- `fix-review` - Fix review
- `design-review` - Design review

---

## Best Practices

### Do's ✅

- **Use multiple domains** when publication spans multiple areas
- **Be generous with tags** - more tags = better discoverability
- **Use existing tags** when possible - check `--list` options
- **Tag technologies** mentioned in the publication
- **Tag tools** used or discussed
- **Include platforms** when relevant
- **Add announcement URLs** for reviews when available

### Don'ts ❌

- **Don't create new domains** - use existing taxonomy
- **Don't duplicate** - if already in categories, don't repeat in tags
- **Don't over-tag** - be relevant and accurate
- **Don't skip validation** - always validate before committing
- **Don't forget the README** - metadata supplements, doesn't replace README

---

## Maintenance

### Regenerating Metadata

If README structure changes significantly:

```bash
cd /path/to/trail-content-taxonomy
python3 generate_publications_metadata.py
```

### Validating All Metadata

```bash
cd publications
python3 scripts/validate.py
```

### Checking Statistics

```bash
python3 scripts/search.py --stats
```

---

## Integration with Blog Taxonomy

The publications metadata uses **the same taxonomy dimensions** as the blog:

- Same domain categories (blockchain, cryptography, fuzzing, etc.)
- Same tag structure (topics, technologies, tools, platforms, concepts)
- Aligned terminology and naming conventions

**Benefits:**
- Consistent user experience across blog and publications
- Cross-referencing possible
- Unified search in the future

---

## Questions?

For questions about:
- **Metadata structure:** See `metadata/schema.json`
- **Search capabilities:** Run `python3 scripts/search.py --help`
- **Validation:** Run `python3 scripts/validate.py`
- **Examples:** Browse `metadata/` subdirectories

---

## Quick Reference

```bash
# Add new publication
1. Add to README.md
2. Create metadata/{type}/{slug}-{hash}.json
3. Fill in required fields: id, title, type, publicationDate
4. Add categories and tags
5. Validate: python3 scripts/validate.py
6. Commit both README and metadata file

# Search publications
python3 scripts/search.py --domain blockchain --technology solidity

# List all options
python3 scripts/search.py --list domains
python3 scripts/search.py --list topics
python3 scripts/search.py --list technologies

# Show stats
python3 scripts/search.py --stats
```

---

**Remember:** The README remains the primary human interface. Metadata enhances discoverability and enables programmatic access without changing the existing workflow.
