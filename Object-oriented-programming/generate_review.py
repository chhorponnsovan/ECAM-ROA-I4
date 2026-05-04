from pathlib import Path
import re

BASE_DIR = Path(__file__).parent
MD_FILE = BASE_DIR / "Object-oriented-programming.md"
TXT_FILE = BASE_DIR / "java_quiz_review.txt"

QUIZ_PATTERN = re.compile(r"Quiz(\d+)Question(\d+)\.java$", re.IGNORECASE)


def extract_key(path: Path):
    match = QUIZ_PATTERN.search(path.name)
    if match:
        return int(match.group(1)), int(match.group(2)), path.name
    return 9999, 9999, path.name


def bold_trailing_comment(line: str) -> str:
    idx = line.find("//")
    if idx == -1:
        return line
    before = line[:idx]
    comment = line[idx:]
    if before.strip() == "":
        return line
    return f"{before}**{comment}**"


def format_java_file(path: Path) -> str:
    lines = path.read_text(encoding="utf-8").splitlines()
    formatted = []
    for line in lines:
        formatted.append(bold_trailing_comment(line))
    return "\n".join(formatted)


def build_review() -> str:
    java_files = sorted(
        [p for p in BASE_DIR.rglob("*.java") if p.is_file()],
        key=extract_key,
    )

    parts = ["## Java Quiz Review", "", "Generated automatically from the `.java` files in the 'QuizQuestion' folder.", "To regenerate this section, run `python generate_review.py`.", ""]

    if not java_files:
        parts.append("No Java quiz files found.")
        return "\n".join(parts)

    for path in java_files:
        match = QUIZ_PATTERN.search(path.name)
        if match:
            quiz, question = match.groups()
            title = f"### Quiz {quiz} - Question {question}"
        else:
            title = f"### {path.name}"

        parts.append(title)
        parts.append("")
        parts.append("```java")
        parts.append(format_java_file(path))
        parts.append("```")
        parts.append("")

    return "\n".join(parts)


def replace_section(md_text: str, replacement: str) -> str:
    start = "<!-- BEGIN JAVA QUIZ REVIEW -->"
    end = "<!-- END JAVA QUIZ REVIEW -->"
    if start in md_text and end in md_text:
        before, rest = md_text.split(start, 1)
        _, after = rest.split(end, 1)
        return before + start + "\n" + replacement + "\n" + end + after
    return md_text.strip() + "\n\n" + start + "\n" + replacement + "\n" + end + "\n"


def main():
    review = build_review()
    txt_content = review
    TXT_FILE.write_text(txt_content, encoding="utf-8")

    md_text = MD_FILE.read_text(encoding="utf-8")
    updated_md = replace_section(md_text, review)
    MD_FILE.write_text(updated_md, encoding="utf-8")
    print(f"Generated review for {len([p for p in BASE_DIR.rglob('*.java') if p.is_file()])} Java files.")
    print(f"Wrote {TXT_FILE.name} and updated {MD_FILE.name}.")


if __name__ == "__main__":
    main()
