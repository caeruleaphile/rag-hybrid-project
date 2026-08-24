import re


def normalize_text(text: str) -> str:

    text = text.replace("\r\n", "\n").replace("\r", "\n")

    lines = []
    for line in text.splitlines():
        cleaned_line = re.sub(r"[ \t]+", " ", line).strip()
        lines.append(cleaned_line)

    normalized = "\n".join(lines)

    normalized = re.sub(r"\n{3,}", "\n\n", normalized)

    return normalized.strip()
