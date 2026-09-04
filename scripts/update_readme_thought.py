import random
from datetime import datetime
from pathlib import Path

README_PATH = Path(__file__).resolve().parents[1] / "README.md"
START_MARKER = "<!-- THOUGHT_FOR_THE_DAY_START -->"
END_MARKER = "<!-- THOUGHT_FOR_THE_DAY_END -->"

THOUGHTS = {
    "Monday": [
        "Start the week with clarity and one meaningful step.",
        "New Monday, new week, new goals.",
        "Set the tone for the week today with focus and purpose."
    ],
    "Tuesday": [
        "Small consistent actions build extraordinary momentum.",
        "Tuesday is the day to push through the resistance.",
        "Keep the momentum going, one task at a time."
    ],
    "Wednesday": [
        "Progress is often just showing up again with intention.",
        "Halfway there. Keep your eyes on the prize.",
        "Hump day is just a reminder of how far you've come this week."
    ],
    "Thursday": [
        "A calm mind makes better decisions than a hurried one.",
        "Thursday: The weekend is in sight, finish strong.",
        "Use today to wrap up the loose ends before the week closes."
    ],
    "Friday": [
        "Finish the week by shipping what matters and leaving room to breathe.",
        "Friday is for reflecting on wins and preparing for rest.",
        "Push through the final hours; you've earned the upcoming break."
    ],
    "Saturday": [
        "Use your energy to create, explore, and restore yourself.",
        "Saturdays are for adventures and unwinding.",
        "Disconnect to reconnect. Enjoy the weekend."
    ],
    "Sunday": [
        "Rest is not laziness; it is preparation for the next beginning.",
        "A Sunday well spent brings a week of content.",
        "Take a deep breath and reset for the days ahead."
    ],
    "Any": [
        "Code is poetry written for machines.",
        "Stay curious and keep learning.",
        "Don't forget to hydrate and stretch!",
        "The best time to plant a tree was 20 years ago. The second best time is now.",
        "Simplicity is the soul of efficiency.",
        "A bug is just an undocumented feature waiting to be fixed.",
        "Take a step back. Sometimes the solution is obvious from a distance."
    ]
}


def build_block(day_name: str) -> str:
    pool = THOUGHTS.get(day_name, []) + THOUGHTS.get("Any", [])
    selected_thought = random.choice(pool)
    return f"**{day_name}**\n> {selected_thought}\n"


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
