# pattern_builder.py – Build pattern text from template
from core.templates import shark_pattern_template
from core.terms import CROCHET_TERMS

def build_shark_pattern():
    template = shark_pattern_template()
    output = []

    output.append(f"# 🧶 {template['title']}\n")
    output.append(f"**Size**: {template['size']}")
    output.append(f"**Difficulty**: {template['difficulty']}\n")

    output.append("## 🧵 Materials:")
    for item in template['materials']['yarn']:
        output.append(f"- {item}")
    output.append(f"- Crochet Hook: {template['materials']['hook']}")
    output.append(f"- Eyes: {template['materials']['eyes']}")
    output.append(f"- Stuffing: {template['materials']['stuffing']}")
    for notion in template['materials']['notions']:
        output.append(f"- {notion}")
    output.append("")

    output.append("## ✨ Features:")
    for feature in template['features']:
        output.append(f"- {feature}")
    output.append("")

    output.append("## 🪡 Body:")
    for line in template['body_instructions']:
        output.append(f"{line}")
    output.append("")

    output.append("## 🦈 Fins:")
    for part, steps in template['fins'].items():
        output.append(f"### {part.capitalize()} Fin:")
        for step in steps:
            output.append(f"- {step}")
        output.append("")
    
    output.append("## 🧷 Assembly:")
    for step in template['assembly']:
        output.append(f"- {step}")
    output.append("")

    output.append("## 📘 Abbreviation Key:")
    for abbr, desc in CROCHET_TERMS.items():
        output.append(f"- **{abbr}**: {desc}")

    return "\n".join(output)
