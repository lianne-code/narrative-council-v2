# The Narrative Council
### A scrutiny engine for the document nobody scrutinizes.

---

The brief is the only document in your marketing process that nobody scrutinizes as much as the final product.  
It's also the only one where scrutiny would actually matter.

Instead, a room of well-paid executives will spend forty minutes debating a sentence most readers will skim. The irony is that nobody spent forty minutes on the brief that produced it.

The Narrative Council moves the scrutiny upstream. Run it on the brief — or whatever you have that functions as one — before writers touch it, before stakeholders see it, before the Safety Tax starts accumulating.

**The Safety Tax** is the organizational cost paid when a narrative is optimized for internal comfort rather than external truth. It begins at the brief, or the absence of one. By the time it reaches execution, the damage is done and it reads as a creative problem.

**This does not replace your internal review process.** Your stakeholder rounds, your legal review, your creative approvals — those still happen. The Narrative Council runs before them, so by the time those reviews start, the Safety Tax has already been reduced and the claim worth defending is already on the page.

---

## Start here

**No setup. No code. Works in Claude today.**

1. Open [Claude](https://claude.ai)
2. Click the **paperclip icon** (bottom left of the chat input on desktop, or the **+** icon on mobile) and upload `SKILL.md`
3. Paste your brief — or your deck outline, positioning doc, messaging framework, or campaign concept — and type `/council this`

Seven advisors review it in point form. A Chairman synthesizes. You decide.

**Don't have a brief?** That is the most common starting point. The council was built for it. Paste whatever you have — a deck, a one-pager, a Slack message that became a campaign, a creative brief someone emailed you. If it contains a claim you are about to execute on, the council can review it. The scrutiny engine works on whatever you feed it.

---

## Why this exists

The growing list of people reviewing final executions keeps getting longer. The brief that produced those executions keeps getting less scrutiny. These two facts are related.

Marketing teams run campaigns that underperform and attribute the miss to creative execution. The creative team built exactly what the brief asked for (or what the project evolved into). The brief asked for the wrong thing, and nobody caught it because nobody was looking.

The Narrative Council is the review that should have happened at the beginning of the project — before the Safety Tax accumulated, before the claim got softened in stakeholder rounds, before the revision cycles started fixing execution problems that were actually brief problems.

If you already run thorough creative reviews, this makes them faster. The hard conversations happen at the brief stage, where they cost an hour. Not in the fourth revision round, where they cost a campaign.

---

## What this is

The Narrative Council is a scrutiny engine — a structured adversarial review system for marketing briefs and narratives, built on [The Narrative Office](https://www.thenarrativeoffice.com)'s Safety Tax framework. Seven advisors. Equal votes. No veto power. One Chairman who synthesizes after reading everything.

Three tools, one sequence:

| Tool | What it does | When to use it |
|---|---|---|
| **SKILL.md** | Seven-advisor council reviews any brief, deck, or narrative | Anytime — no setup, no code |
| **Brief Builder** | Locks your core claim through five interrogation questions before writers touch it | Before a campaign, launch, or narrative goes external |
| **Content Drafter** | Turns a locked brief into a first draft | After the brief is committed |

The SKILL.md catches what already exists. The Brief Builder prevents the problem from starting. The Content Drafter closes the loop so the brief produces something.

---

## The council commands

| Command | What it does |
|---|---|
| `/council this` | Full seven-advisor review with Chairman synthesis |
| `/pressure-test this` | Chairman only — fastest path to the core tension |
| `/war room this` | Engineer, Competitor, and Legal only — adversarial focus |
| `/legal scan` | Legal lens only — isolated risk review before external submission |
| `/data check` | Analyst lens only — claim integrity review |

---

## The Seven Advisors

These seven lenses were chosen because they represent the perspectives most likely to be absent from the room when the brief is written — and most present in the room when the execution is reviewed. Each casts an equal vote. The Chairman reads all seven reports in full before synthesizing, including the observations that appear minor.

| Advisor | Lens | What they catch |
|---|---|---|
| The Engineer | Downside | What breaks, what's overpromised |
| The Audience | Fresh Eyes | Assumed context, insider language |
| The CMO | Reframe | Strategic coherence, genuine point of view, approval survivability |
| The Sales Lead | Action | Objection exposure, conversation utility |
| The Analyst | Data | Claim credibility, number integrity |
| The Competitor | Counter | Positioning gaps, easy counters you've handed them |
| Legal | Risk | What's actually at risk vs. what's just sharp — plus a standing data sensitivity flag on every review |

**On data sensitivity:** uploading brief content to an AI tool may implicate your organization's data policies. Legal flags this on every review. Confirm what can be shared externally before running confidential briefs through this system.

**This tool does not constitute professional strategic or legal advice.** The council's output is a structured perspective, not a professional recommendation. Use it to sharpen your thinking, not to replace it.

---

## Running the Brief Builder and Content Drafter

```bash
# Clone the repo
git clone https://github.com/your-username/narrative-council.git
cd narrative-council

# Install dependencies
pip install anthropic

# Set your API key
export ANTHROPIC_API_KEY=your_key_here

# Run the brief builder
python brief-builder/builder.py

# Run the content drafter (after saving a brief)
python content-drafter/drafter.py
```

**Requirements:** Python 3.8+, Anthropic API key ([console.anthropic.com](https://console.anthropic.com))

---

## What this is not

This is not a template filler. It is not a checklist. It is not a replacement for the internal reviews your organization already runs.

It is a scrutiny engine for the document that was never meant to survive scrutiny — run early enough that the findings cost you an hour, not a quarter.

---

## Built by

[The Narrative Office](https://www.thenarrativeoffice.com) — Narrative Counsel for B2B Enterprise and Series A.  
Lianne Stewart — former Meta executive. Clients include Amazon Ads, Pinterest, Dolby, and Shopify.

The Safety Tax framework is developed and maintained by The Narrative Office. Attribution appreciated when forking or building on this work.

[Substack](https://thesafetytax.substack.com) · [LinkedIn](https://linkedin.com/in/liannestewart)

---

## License

MIT. Use it. Fork it. Run it on whatever you have before your next campaign review.  
If it finds something, that finding was already there.
