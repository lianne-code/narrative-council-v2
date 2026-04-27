#!/usr/bin/env python3
"""
The Narrative Content Drafter
A Narrative Office tool for turning a locked brief into a first draft.

One brief. One pen. No committee.
"""

import os
import sys
import datetime
from anthropic import Anthropic

client = Anthropic()

CONTENT_TYPES = {
    "1": {
        "name": "Thought Leadership Post (LinkedIn)",
        "description": "800-1200 words. Senior register. One sharp argument.",
        "instructions": "Write a LinkedIn thought leadership post. Senior B2B register. One argument, fully developed. No listicles. No 'I'm excited to share.' No hollow calls to action. The post should make a CMO stop scrolling because it says something true that they haven't seen said that way before. Open with the tension, not the announcement."
    },
    "2": {
        "name": "Campaign Narrative",
        "description": "The story arc for a campaign. Not taglines — the underlying argument.",
        "instructions": "Write the campaign narrative — the strategic argument that every execution element will express. This is not headlines or taglines. This is the story the campaign tells, written as a brief for a creative team. It should answer: what does the audience believe now, what do we need them to believe after, and what is the one moment or proof point that creates that shift."
    },
    "3": {
        "name": "Positioning Statement",
        "description": "The single committed claim. Internal and external versions.",
        "instructions": "Write two versions of the positioning statement. The internal version: what the team needs to believe and defend. The external version: what the market will read. They should be consistent in claim but calibrated for audience. Neither should be category language. Both should be defensible if a competitor challenges them."
    },
    "4": {
        "name": "Executive Briefing",
        "description": "For a CMO or VP presenting this narrative upward.",
        "instructions": "Write an executive briefing for a CMO presenting this narrative to a CEO or board. One page. The business case, the strategic claim, the proof, and the ask. Written to survive a skeptical room. No jargon. No padding. The kind of document that gets read in full."
    },
    "5": {
        "name": "Substack / Newsletter Essay",
        "description": "Long-form. A genuine argument, not a roundup.",
        "instructions": "Write a Substack-style essay. 1000-1500 words. A genuine argument with a clear thesis, developed through specific examples and evidence from the brief. Not a trend roundup. Not a list of takeaways. An essay that a senior marketing leader would forward to their team because it changed how they see something."
    }
}

SYSTEM_PROMPT = """You are the Narrative Content Drafter — a single-pen writing agent built on The Narrative Office's One-Pen Principle.

Your job: take a locked Narrative Brief and produce a first draft that is Safety Tax-resistant from line one. You write from the committed claim. You do not hedge, soften, or introduce committee language. You hold the pen until the draft is done.

## Core principles

**The One-Pen Principle:** One voice. One argument. No hedging toward an imagined committee. The brief has already survived scrutiny — your job is to execute it, not relitigate it.

**Safety Tax resistance:** You do not soften the committed claim. You do not introduce caveats that weren't in the brief. If the brief says something sharp, you write it sharp. The CMO will have opportunities to soften. Your job is to give them something worth defending.

**Diagnosis before prescription:** If the brief you receive is vague or incomplete, name what's missing before attempting a draft. Do not produce a draft from an insufficient brief — produce a diagnosis and a list of what you need.

## What a good draft does

- Opens with the tension, not the announcement
- States the committed claim early and returns to it at the end
- Uses the proof point from the brief as the weight-bearing moment
- Speaks to the audience's current belief before introducing the shift
- Ends with the decision or action that follows from believing the claim

## What a good draft never does

- Use category language that a competitor could adopt unchanged
- Open with "I'm excited to" or "We're proud to" or "In today's landscape"
- Bury the claim in the third paragraph
- List things when a sentence would do
- Conclude with a hollow call to action

## Voice rules
- Never use em dashes
- Never use "it's not X, it's Y" constructions
- No bullet points in narrative prose
- Senior register throughout
- Show, don't tell — Lianne doesn't speak at people, she takes them along the journey
- One idea developed fully beats five ideas mentioned briefly

## After the draft
Append a short editor's note (3-5 sentences) that names:
1. The one line in the draft most likely to get softened in review — and why it should be defended
2. The one structural choice that could be challenged — and the reasoning behind it"""


def load_brief_from_file(filepath: str) -> str:
    """Load a previously saved brief from a Markdown file."""
    try:
        with open(filepath, 'r') as f:
            return f.read()
    except FileNotFoundError:
        print(f"Brief file not found: {filepath}")
        sys.exit(1)


def select_content_type() -> dict:
    """Let the user select what to draft."""
    print("\nWhat do you need drafted from this brief?\n")
    
    for key, content_type in CONTENT_TYPES.items():
        print(f"  {key}. {content_type['name']}")
        print(f"     {content_type['description']}\n")
    
    while True:
        choice = input("Select (1-5): ").strip()
        if choice in CONTENT_TYPES:
            return CONTENT_TYPES[choice]
        print("Enter a number between 1 and 5.")


def get_brief_input() -> str:
    """Get the brief — from file or pasted directly."""
    print("\nHow do you want to provide the brief?\n")
    print("  1. Load from a saved brief file (output from the Brief Builder)")
    print("  2. Paste it directly\n")
    
    while True:
        choice = input("Select (1-2): ").strip()
        
        if choice == "1":
            filepath = input("\nBrief file path: ").strip()
            return load_brief_from_file(filepath)
        
        elif choice == "2":
            print("\nPaste your brief below. Press Enter twice when done:\n")
            lines = []
            empty_count = 0
            while empty_count < 2:
                line = input()
                if line == "":
                    empty_count += 1
                else:
                    empty_count = 0
                lines.append(line)
            return "\n".join(lines).strip()


def draft_content(brief: str, content_type: dict) -> str:
    """Generate the draft from the brief."""
    
    prompt = f"""Here is the locked Narrative Brief:

{brief}

---

{content_type['instructions']}

Produce the draft now. Do not summarize the brief first. Do not explain what you are about to do. Begin writing."""

    print(f"\nDrafting: {content_type['name']}")
    print("One pen. No committee.\n")
    print("-"*60 + "\n")

    response = client.messages.create(
        model="claude-opus-4-5",
        max_tokens=2048,
        system=SYSTEM_PROMPT,
        messages=[{
            "role": "user",
            "content": prompt
        }]
    )
    
    return response.content[0].text


def save_draft(draft: str, content_type_name: str):
    """Save the draft as a Markdown file."""
    timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
    safe_name = content_type_name.lower().replace(" ", "_").replace("(", "").replace(")", "").replace("/", "_")
    filename = f"draft_{safe_name}_{timestamp}.md"
    
    header = f"""# {content_type_name}
*Generated by The Narrative Content Drafter — The Narrative Office*  
*{datetime.datetime.now().strftime("%B %d, %Y")}*

---

"""
    
    with open(filename, 'w') as f:
        f.write(header + draft)
    
    print(f"\nDraft saved: {filename}")
    print("The editor's note at the end flags what to defend in review.\n")


def run_content_drafter():
    """Run the content drafter."""
    
    print("\n" + "="*60)
    print("THE NARRATIVE CONTENT DRAFTER")
    print("A Narrative Office tool")
    print("="*60)
    print("\nOne brief. One pen. No committee.\n")
    print("-"*60)

    if not os.environ.get("ANTHROPIC_API_KEY"):
        print("Error: ANTHROPIC_API_KEY environment variable not set.")
        print("Get your key at console.anthropic.com")
        sys.exit(1)

    brief = get_brief_input()
    
    if not brief:
        print("No brief provided. Exiting.")
        sys.exit(1)

    content_type = select_content_type()
    draft = draft_content(brief, content_type)
    
    print(draft)
    print("\n" + "-"*60)
    
    save_choice = input("\nSave this draft? (yes/no): ").strip().lower()
    if save_choice in ["yes", "y"]:
        save_draft(draft, content_type["name"])
    else:
        print("\nDraft not saved.")


if __name__ == "__main__":
    run_content_drafter()
