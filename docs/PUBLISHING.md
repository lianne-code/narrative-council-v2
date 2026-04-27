# How to publish the Narrative Council to GitHub

Step by step. No assumed knowledge.

---

## What you need first

- A GitHub account. If you don't have one: github.com → Sign up. Free.
- The `narrative-council.zip` file downloaded to your computer.

---

## Step 1 — Unzip the files

On your Mac, double-click `narrative-council.zip`.  
A folder called `narrative-council` will appear in the same location.  
Leave it there for now.

---

## Step 2 — Create a new repository on GitHub

1. Go to [github.com](https://github.com) and sign in
2. Click the **+** icon in the top right corner
3. Select **New repository**
4. Fill in:
   - **Repository name:** `narrative-council`
   - **Description:** `A scrutiny engine for the document nobody scrutinizes. Brief review council built on The Narrative Office's Safety Tax framework.`
   - **Visibility:** Select **Public** (so others can find and fork it)
   - Leave everything else unchecked
5. Click **Create repository**

You will land on an empty repository page. Leave it open.

---

## Step 3 — Install GitHub Desktop (easiest upload method)

If you're comfortable with Terminal, skip to the Terminal method below.

1. Go to [desktop.github.com](https://desktop.github.com)
2. Download and install GitHub Desktop
3. Open it and sign in with your GitHub account

---

## Step 4 — Upload your files using GitHub Desktop

1. In GitHub Desktop, click **File → Add Local Repository**
2. Click **Choose** and navigate to your `narrative-council` folder
3. GitHub Desktop will say it's not a git repository — click **create a repository here**
4. Fill in:
   - Name: `narrative-council`
   - Keep everything else as default
5. Click **Create Repository**
6. In the top bar, click **Publish repository**
7. Make sure **Keep this code private** is **unchecked**
8. Click **Publish Repository**

Your repo is now live at `github.com/your-username/narrative-council`

---

## Alternative: Terminal method (faster if you're comfortable with it)

Open Terminal (Applications → Utilities → Terminal) and run these commands one at a time:

```bash
# Navigate to the folder (adjust path if yours is different)
cd ~/Downloads/narrative-council

# Initialize git
git init

# Add all files
git add .

# First commit
git commit -m "Initial release — Narrative Council v1.0"

# Connect to your GitHub repo (replace YOUR-USERNAME with your GitHub username)
git remote add origin https://github.com/YOUR-USERNAME/narrative-council.git

# Push
git branch -M main
git push -u origin main
```

---

## Step 5 — Add a topic tag so people can find it

1. Go to your repo on github.com
2. Click the gear icon next to **About** (top right of the repo)
3. Under **Topics**, add:
   - `marketing`
   - `ai`
   - `claude`
   - `narrative`
   - `brief`
   - `anthropic`
4. Click **Save changes**

---

## Step 6 — Confirm everything looks right

Your repo should show:

```
narrative-council/
├── SKILL.md
├── README.md
├── requirements.txt
├── .gitignore
├── brief-builder/
│   ├── builder.py
│   └── README.md
├── content-drafter/
│   ├── drafter.py
│   └── README.md
└── docs/
    └── sample-brief.md
```

The README will render automatically on the repo homepage — that's your public-facing page.

---

## Step 7 — Share it

Your repo URL is:  
`https://github.com/YOUR-USERNAME/narrative-council`

This is what you share on LinkedIn, Substack, and anywhere else.

A clean share line:

> The brief is the only document in your marketing process that nobody scrutinizes. I built a council to fix that. Eight advisors. One chairman. Drop it into Claude and run /council this on your next brief. github.com/YOUR-USERNAME/narrative-council

---

## If anything breaks

The most common issue is the API key. When someone runs the Brief Builder or Content Drafter, they need their own Anthropic API key set as an environment variable:

```bash
export ANTHROPIC_API_KEY=their_key_here
```

They get a key at [console.anthropic.com](https://console.anthropic.com). Free tier available.

The SKILL.md requires no API key — it runs directly in Claude with no setup.
