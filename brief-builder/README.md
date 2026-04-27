# Brief Builder

An agentic interrogation system that locks your core claim before writers touch it.

## What it does

The Brief Builder asks five questions. It rejects vague answers. It does not move forward until the claim is defensible. When all five inputs are sound, it produces a locked Narrative Brief with a named owner and a flagged dilution risk.

This is not a form. It is an interrogation.

## The five questions

1. What is this campaign trying to make someone believe? (Not do. Believe.)
2. Who specifically needs to believe it — and what are they currently believing instead?
3. What proof already exists that this claim is true?
4. Who is the single person accountable if this brief produces the wrong output?
5. What is the one thing about this brief that will get softened in review — and should it be?

## What it rejects

- Category language (your competitor could say the same thing)
- Aspirational proof points (projections, not facts)
- Demographic audiences (a role, not a person with a problem)
- Committee ownership (a team cannot own a brief)

## The output

A locked Narrative Brief in Markdown containing:

- The committed claim
- The named audience and belief shift required
- The existing proof point
- The flagged dilution risk
- The Narrative Commit Point
- A Chairman's note on the strategic tension this brief carries into execution

## Usage

```bash
export ANTHROPIC_API_KEY=your_key_here
python builder.py
```

Saved briefs can be passed directly to the Content Drafter.
