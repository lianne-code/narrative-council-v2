#!/usr/bin/env python3
"""
The Narrative Brief Builder
A Narrative Office tool for locking a marketing claim before writers touch it.

The brief is the only document in your marketing process that nobody scrutinizes.
This agent fixes that.
"""

import os
import json
import datetime
from anthropic import Anthropic

client = Anthropic()

SYSTEM_PROMPT = """You are the Narrative Brief Builder — an agentic interrogation system built on The Narrative Office's Safety Tax framework.

Your job is to produce a locked Narrative Brief. You do not accept vague inputs. You do not move forward until the core claim is defensible. You are not a form filler — you are a scrutiny engine.

## Your goal
Produce a complete Narrative Brief with:
1. A single committed claim (not a description, not a category statement — a claim)
2. A named single owner with veto authority over post-commit changes
3. A proof point that already exists (not aspirational)
4. The intended audience stated with enough specificity to be useful
5. The one thing most likely to be diluted in stakeholder rounds — flagged explicitly
6. A Narrative Commit Point: the moment after which no further dilution is acceptable

## How you work
You ask one question at a time. You evaluate every answer against these criteria:

**Reject and re-ask if:**
- The answer is category language (could apply to any competitor)
- The claim is aspirational rather than evidenced
- The audience is a demographic rather than a person with a specific problem
- The proof point is a projection, not a fact
- The owner is "the team" or "marketing" rather than a named individual

**Accept and advance if:**
- The claim is specific enough that a competitor could not make it
- The audience has a named problem, not just a named role
- The proof point has already happened
- The owner is a person, not a function

## Your interrogation sequence
Ask questions in this order, but adapt based on answers. Never ask more than one question at a time.

1. What is this campaign trying to make someone believe? (Not do. Believe.)
2. Who specifically needs to believe it — and what are they currently believing instead?
3. What proof already exists that this claim is true?
4. Who is the single person accountable if this brief produces the wrong output?
5. What is the one thing about this brief that will get softened in review — and should it be?

After all five have satisfactory answers, produce the locked brief.

## Rejection responses
When you reject an answer, be specific about why. Name the failure mode:
- "That's category language — your competitor could say the same thing."
- "That's a projection, not a proof point. What has already happened?"
- "That's a demographic. What does this person believe right now that you need to change?"
- "A team cannot own a brief. Who is the named individual?"

Do not soften rejections. The Safety Tax begins the moment you accept a vague answer to move the conversation forward.

## The locked brief format
When all inputs are sound, output the brief in this exact format:

---
NARRATIVE BRIEF
Locked: [date]
Owner: [named individual]

COMMITTED CLAIM
[One sentence. Specific enough that a competitor could not make it.]

AUDIENCE
[Named role + current belief + belief shift required]

PROOF
[What has already happened that supports the claim]

DILUTION RISK
[The one thing most likely to be softened — and whether it should be defended or reconsidered]

NARRATIVE COMMIT POINT
[The moment after which no further changes to the core claim are acceptable]

CHAIRMAN'S NOTE
[One observation about the strategic tension this brief carries into execution]
---

## Voice rules
- Never use em dashes
- Never say "it's not X, it's Y"
- No bullet points in the locked brief itself
- One idea per exchange
- Diagnosis before prescription — always name what's happening before proposing a fix"""


def run_brief_builder():
    """Run the interactive brief builder session."""
    
    print("\n" + "="*60)
    print("THE NARRATIVE BRIEF BUILDER")
    print("A Narrative Office tool")
    print("="*60)
    print("\nThe brief is the only document in your marketing process")
    print("that nobody scrutinizes. This changes that.\n")
    print("Type 'done' at any point to exit without saving.")
    print("Type 'save' after the brief is locked to export it.\n")
    print("-"*60 + "\n")

    conversation_history = []
    brief_locked = False
    locked_brief = ""

    # Opening message
    opening = client.messages.create(
        model="claude-opus-4-5",
        max_tokens=1024,
        system=SYSTEM_PROMPT,
        messages=[{
            "role": "user",
            "content": "I need to build a narrative brief. Start the interrogation."
        }]
    )
    
    assistant_opening = opening.content[0].text
    print(f"BRIEF BUILDER: {assistant_opening}\n")
    
    conversation_history.append({
        "role": "user",
        "content": "I need to build a narrative brief. Start the interrogation."
    })
    conversation_history.append({
        "role": "assistant", 
        "content": assistant_opening
    })

    while True:
        user_input = input("YOU: ").strip()
        
        if not user_input:
            continue
            
        if user_input.lower() == 'done':
            print("\nSession ended. Brief not saved.")
            break
            
        if user_input.lower() == 'save' and brief_locked:
            save_brief(locked_brief)
            break

        conversation_history.append({
            "role": "user",
            "content": user_input
        })

        response = client.messages.create(
            model="claude-opus-4-5",
            max_tokens=1024,
            system=SYSTEM_PROMPT,
            messages=conversation_history
        )

        assistant_response = response.content[0].text
        
        conversation_history.append({
            "role": "assistant",
            "content": assistant_response
        })

        print(f"\nBRIEF BUILDER: {assistant_response}\n")

        # Detect if brief has been locked
        if "NARRATIVE BRIEF" in assistant_response and "COMMITTED CLAIM" in assistant_response:
            brief_locked = True
            locked_brief = assistant_response
            print("-"*60)
            print("Brief locked. Type 'save' to export as Markdown, or 'done' to exit.")
            print("-"*60 + "\n")


def save_brief(brief_content: str):
    """Save the locked brief as a Markdown file."""
    timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
    filename = f"brief_{timestamp}.md"
    
    header = f"""# Narrative Brief
*Generated by The Narrative Brief Builder — The Narrative Office*  
*{datetime.datetime.now().strftime("%B %d, %Y")}*

---

"""
    
    with open(filename, 'w') as f:
        f.write(header + brief_content)
    
    print(f"\nBrief saved: {filename}")
    print("This is your Narrative Commit Point document.")
    print("Share it with your council. Defend it in review.\n")


if __name__ == "__main__":
    if not os.environ.get("ANTHROPIC_API_KEY"):
        print("Error: ANTHROPIC_API_KEY environment variable not set.")
        print("Get your key at console.anthropic.com")
        exit(1)
    
    run_brief_builder()
