
from pathlib import Path
import re


readme = Path("README.md")
levels_folder = Path("levels")
backup = Path("README_backup.md")

if not readme.exists():
    print("README.md not found.")
    exit()

text = readme.read_text(encoding="utf-8")

pattern = re.compile(
    r'(?:<a name="level-\d+-\d+"></a>\s*)?'
    r'<details>\s*'
    r'<summary><b>Level (\d+) -> Level (\d+)</b></summary>'
    r'(.*?)</details>',
    re.DOTALL
)

levels = list(pattern.finditer(text))

if len(levels) != 33:
    print("Could not find all 33 levels.")
    print("Found:", len(levels))
    exit()

if levels_folder.exists() and any(levels_folder.iterdir()):
    print("The levels folder is not empty.")
    exit()

# Check if a backup already exists
if backup.exists():
    print("Backup file already exists.")
    exit()

backup.write_text(text, encoding="utf-8")

# Create the levels folder
levels_folder.mkdir(exist_ok=True)

# Split each level into a separate file
for level in levels:
    start = int(level.group(1))
    end = int(level.group(2))
    content = level.group(3).strip()

    file_name = f"level-{start:02}-{end:02}.md"
    file_path = levels_folder / file_name

    page = f"# Level {start} -> Level {end}\n\n{content}\n"

    file_path.write_text(page, encoding="utf-8")

    print("Created:", file_name)

intro = text[:levels[0].start()].strip()

if "## Quick Navigation" in intro:
    intro = intro.split("## Quick Navigation")[0].strip()

navigation = "## Quick Navigation\n\n"
navigation += "Click a level below to view its write-up.\n\n"

groups = [
    ("Levels 0–10", 0, 10),
    ("Levels 10–20", 10, 20),
    ("Levels 20–33", 20, 33)
]

for title, first, last in groups:
    navigation += f"### {title}\n\n"

    for i in range(first, last):
        file_name = f"level-{i:02}-{i+1:02}.md"
        navigation += f"- [Level {i} → {i+1}]({levels_folder / file_name})\n"

    navigation += "\n"

# Update the main README
new_readme = intro + "\n\n" + navigation
readme.write_text(new_readme, encoding="utf-8")

print("\nAll 33 levels have been separated successfully!")
print("Check the README.md and levels folder.")
