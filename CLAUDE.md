# Guide for Claude when working with this repository

## Repository Guidelines

### Creating PRs
- Always create changes on a new branch (not master)
- Make a PR for changes rather than committing directly to master

### Date Formatting
- Use 3-letter abbreviations for all month names to save space in the layout:
  - Jan, Feb, Mar, Apr, May, Jun, Jul, Aug, Sep, Oct, Nov, Dec
  - Do NOT use: January, February, March, April, June, July, August, September, October, November, December
  - Do NOT use 4-letter abbreviations like Sept

### Section Organization
- Sections should appear in this order:
  1. Academic Papers
  2. White Papers
  3. Guides and Handbooks
  4. Conference Presentations
  5. Datasets
  6. Podcasts
  7. Public Comments
  8. Security Reviews
  9. Disclosures
  10. Workshops
  11. Service Overviews
- Within each section, entries should be sorted by date (newest first)
- When checking sort order, be aware that some sections may have subsections that are sorted independently

### Security Reviews Table Guidelines

#### Product Column Formatting
- Product column should contain ONLY the product/project name
  - Do NOT include document types like "Letter of Attestation", "Design Review", "Code Review", "Security Review", "Threat Model"
  - Just use the clean product name (e.g., "Discord DAVE", not "Discord DAVE Protocol Code Review")
- Keep product names concise to help rows fit on single lines:
  - Remove company suffixes like "Labs" when redundant (e.g., "Offchain Labs X" → "Offchain X")
  - Shorten verbose descriptions (e.g., "Custom Fee ERC-20 Bridge Upgrade and EIP-7702 Fixes" → "Custom Fee Bridge & EIP-7702")
  - Remove redundant words like "Protocol", "Smart Contracts", "Library" when context is clear
  - For multi-organization projects, consider using just the main product name (e.g., "SafeTensors Library" instead of "EleutherAI, Hugging Face, & Stability AI SafeTensors Library")

#### Document Icons and Formatting
- Use specific icons for different document types:
  - 📄 = Security Assessment report
  - ✅ = Fix review report  
  - 🔖 = Letter of Attestation
  - 📛 = Threat Model report
  - 📰 = Whitepaper
- When multiple related documents exist (e.g., security review + letter of attestation):
  - Keep them in the same row
  - Use separate icons with no space between: [📄✅](review.pdf)[🔖](loa.pdf)
  - This saves characters compared to [📄✅](review.pdf) [📄](loa.pdf)
  - Do NOT create separate rows for each document type

#### Announcement Links
- Add announcement links when available:
  - Search for official announcements that mention Trail of Bits
  - Use organization name only as link text (e.g., [Axiom], [Discord], [Scroll])
  - Do NOT use long announcement titles (e.g., avoid "Meet DAVE: Discord's New End-to-End Encryption")
  - This keeps the table clean and helps rows fit on single lines
- For URLs: only the displayed text matters for line length, not the actual URL length

### General Formatting Guidelines
- Priority: Keep security review table rows fitting on single lines
- Use double spaces in empty cells: `|  |` should be `| |`
- Fix decimal formatting: `.2` should be `0.2`
- Ensure proper spacing: `| 4|` should be `| 4 |`
- When in doubt, favor brevity over verbosity while maintaining clarity

### Editing Guidelines
- NEVER modify URLs or file paths when making formatting changes
- Preserve the exact order of entries when only changing date formats
- When moving sections, update both the section content AND the table of contents
- Double-check that the total number of table rows remains the same after edits
- Remove duplicate entries - combine multiple audits for the same product when appropriate