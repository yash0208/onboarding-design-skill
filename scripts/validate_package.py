#!/usr/bin/env python3
"""Offline package sanity checks, not a behavioral or security certification."""

import re
import sys
from pathlib import Path
from urllib.parse import unquote, urlsplit


def validate(root):
    root = Path(root).resolve()
    skill = root / "skills/onboarding-design"
    required = [
        "README.md", "LICENSE", "skills/onboarding-design/SKILL.md",
        "skills/onboarding-design/agents/openai.yaml", "tests/scenarios.md",
        "tests/rubric.md", "tests/VALIDATION.md",
    ]
    errors = [f"Missing: {name}" for name in required if not (root / name).is_file()]
    if errors:
        return errors
    entry = (skill / "SKILL.md").read_text(encoding="utf-8")
    if not entry.startswith("---\n") or "\n---\n" not in entry[4:]:
        errors.append("Missing or malformed skill frontmatter")
    else:
        front = entry.split("---", 2)[1]
        if not re.search(r"^name: onboarding-design$", front, re.M):
            errors.append("Skill name must match its directory")
        if not re.search(r"^description: .{20,1024}$", front, re.M):
            errors.append("Missing or invalid single-line skill description")
    metadata = (skill / "agents/openai.yaml").read_text(encoding="utf-8")
    for key in ("display_name", "short_description", "default_prompt"):
        match = re.search(rf'^  {key}: "([^"\n]+)"$', metadata, re.M)
        if not match:
            errors.append(f"Missing quoted UI field: {key}")
        elif key == "short_description" and not 25 <= len(match[1]) <= 64:
            errors.append("UI short description must be 25–64 characters")
        elif key == "default_prompt" and "$onboarding-design" not in match[1]:
            errors.append("Default prompt must name the skill")

    # Check only intended package areas; local research/run logs are excluded.
    paths = [root / "README.md", root / "LICENSE"]
    for directory in ("skills", "tests", "scripts"):
        paths.extend(p for p in (root / directory).rglob("*")
                     if p.is_file() and "__pycache__" not in p.parts)
    secret_patterns = [r"gh[pousr]_[A-Za-z0-9]{30,}", r"github_pat_[A-Za-z0-9_]{30,}",
                       r"-----BEGIN (?:RSA |EC |OPENSSH )?PRIVATE KEY-----"]
    for path in paths:
        if path.suffix not in (".md", ".yaml", ".py") and path.name != "LICENSE":
            errors.append(f"Unexpected package file type: {path.relative_to(root)}")
            continue
        text = path.read_text(encoding="utf-8")
        if path.suffix in (".md", ".yaml"):
            if re.search(r"/(?:Users|home)/[^/\s]+/|[A-Z]:\\Users\\", text):
                errors.append(f"Private absolute path: {path.relative_to(root)}")
            if re.search(r"\b(?:TODO|FIXME)\b", text):
                errors.append(f"Unfinished marker: {path.relative_to(root)}")
        if any(re.search(pattern, text) for pattern in secret_patterns):
            errors.append(f"Possible credential: {path.relative_to(root)}")
        if path.suffix != ".md":
            continue
        for target in re.findall(r"\[[^\]]*\]\(([^\s)]+)\)", text):
            parsed = urlsplit(target)
            if parsed.scheme or not parsed.path:
                continue
            resolved = (path.parent / unquote(parsed.path)).resolve()
            if root not in resolved.parents and resolved != root:
                errors.append(f"Link escapes package: {target}")
            elif not resolved.exists():
                errors.append(f"Broken relative link in {path.relative_to(root)}: {target}")
    return errors


if __name__ == "__main__":
    package_root = Path(sys.argv[1]) if len(sys.argv) > 1 else Path(__file__).resolve().parents[1]
    problems = validate(package_root)
    for problem in problems:
        print(problem)
    if problems:
        sys.exit(1)
    print("PASS: package files, metadata, relative file links, and bounded privacy-pattern checks")
    print("Not checked: remote URLs/anchors, runtime installation, usability, or conversion outcomes")
