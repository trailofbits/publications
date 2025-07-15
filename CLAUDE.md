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
- Product column should contain ONLY the product/project name
  - Do NOT include document types like "Letter of Attestation", "Design Review", "Code Review"
  - Just use the clean product name (e.g., "Discord DAVE", not "Discord DAVE Protocol Code Review")
- When multiple related documents exist (e.g., security review + letter of attestation):
  - Combine them into a single row
  - List all PDFs in the same row's link column
- Add announcement links when available:
  - Search for official announcements that mention Trail of Bits
  - Include these in the announcement column with descriptive link text

### Editing Guidelines
- NEVER modify URLs or file paths when making formatting changes
- Preserve the exact order of entries when only changing date formats
- When moving sections, update both the section content AND the table of contents
- Double-check that the total number of table rows remains the same after edits