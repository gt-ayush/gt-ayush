from datetime import datetime
from pathlib import Path

README_PATH = Path(__file__).resolve().parents[1] / "README.md"
START_MARKER = "<!-- THOUGHT_FOR_THE_DAY_START -->"
END_MARKER = "<!-- THOUGHT_FOR_THE_DAY_END -->"

THOUGHTS = {
    "Monday": "Start the week with clarity and one meaningful step.",
    "Tuesday": "Small consistent actions build extraordinary momentum.",
    "Wednesday": "Progress is often just showing up again with intention.",
    "Thursday": "A calm mind makes better decisions than a hurried one.",
    "Friday": "Finish the week by shipping what matters and leaving room to breathe.",
    "Saturday": "Use your energy to create, explore, and restore yourself.",
    "Sunday": "Rest is not laziness; it is preparation for the next beginning.",
}


def build_block(day_name: str) -> str:
    return f"**{day_name}**\n> {THOUGHTS[day_name]}\n"


def update_readme(readme_path: Path) -> None:
    content = readme_path.read_text(encoding="utf-8")
    day_name = datetime.now().strftime("%A")
    new_block = build_block(day_name)

    if START_MARKER in content and END_MARKER in content:
        before, _, after = content.partition(START_MARKER)
        _, _, rest = after.partition(END_MARKER)
        updated = before + START_MARKER + "\n" + new_block + END_MARKER + rest
    else:
        updated = content.rstrip() + "\n\n" + START_MARKER + "\n" + new_block + END_MARKER + "\n"

    readme_path.write_text(updated, encoding="utf-8")
    print(f"Updated README with {day_name}'s thought.")


if __name__ == "__main__":
    update_readme(README_PATH)
