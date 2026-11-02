# Workshop: Web Design with GitHub Copilot — Render, Check, Repeat

**Duration:** 60 minutes · **Level:** beginner, after the main workshop ·
**Prerequisites:** you have done [VIBE_CODING_BASICS.md](VIBE_CODING_BASICS.md),
or at least have a `vibe-site` folder with `index.html`,
`business_brief.md` and `site_check.py`. You still don't write code
yourself. You learn to write prompts that make the AI **look at** its result
and **check** it before it says "done".

---

## Introduction

### Background

In the main workshop, you did the *Check* step of the loop yourself: open
the page, make the window narrow, run Lighthouse, read the console. A
chatbot cannot do any of this. It never sees your page.

**GitHub Copilot in agent mode** is different. It works inside VS Code, on
your files, and it can use **tools**: read and edit files, run commands in
the terminal, and, with one extra setup step, control a real browser. That
means the AI can take over part of the checking, **if your prompt tells it
how**:

```
  ┌────────────┐     ┌────────────┐     ┌──────────────────────┐     ┌────────────┐
  │  Describe  │ ──▶ │  Generate  │ ──▶ │ Render + verify (AI) │ ──▶ │   Review   │
  │   (you)    │     │    (AI)    │     │  fix, verify again   │     │   (you)    │
  └────────────┘     └────────────┘     └──────────────────────┘     └────────────┘
```

There are three ways to check a page, and today you use all three:

| Level | Who checks | How | Example |
|---|---|---|---|
| **1. You look** | You | A preview next to the code | "The button looks too small" |
| **2. The AI looks** | Copilot | Screenshots from a real browser | "At 360 px, the menu covers the headline" |
| **3. The AI measures** | Copilot | Commands that print a clear result | "Page width 412 px, window 360 px: FAIL" |

Level 3 is the most reliable. A screenshot needs to be interpreted, and the
AI can interpret it wrongly. A number is either above the limit or it isn't.

> **The most important rule of today.** An AI that says "I verified it" has
> not necessarily verified anything. Ask for **evidence**: the screenshot,
> the command and its output, the measured number. No evidence, no check.

### Before the Workshop

**1. GitHub Copilot.** In VS Code, click the Copilot icon in the status bar
at the bottom (or the *Accounts* icon at the bottom left) and sign in with
your GitHub account. The **Copilot Free** plan is enough, but it has a
monthly limit on chat requests (it was 50 when this was written). This
workshop needs about 15 to 25 of them, so don't use up your requests in the
days before. Students and teachers get Copilot Pro for free through
[GitHub Education](https://education.github.com).

**2. Node.js** (the *LTS* version) from [nodejs.org](https://nodejs.org).
Copilot needs it to start the browser tool in Task 2. Check it in the
terminal:

```bash
node --version       # Should print v20 or higher
npx --version        # Comes with Node.js
```

**3. Live Server** from the main workshop, and **Python 3** for
`site_check.py`.

**4. A copy of your page.** Copilot changes your files directly. Before you
start, copy `index.html` to `index-before-copilot.html`. If anything goes
wrong today, you can always go back.

### Agent Mode in Two Minutes

Open the Copilot **Chat** view (the chat icon in the title bar, or
`Ctrl + Alt + I` / `Cmd + Ctrl + I` on macOS). At the bottom of the chat
box there is a drop-down for the **mode**. Choose **Agent**. Next to it you
can pick the model. Any model offered on your plan works for today.

In agent mode, Copilot works in steps you can watch in the chat:

- **Edits** appear in the editor as a diff (red: removed, green: added).
  You click **Keep** or **Undo** for each file.
- **Terminal commands** and **browser actions** need your approval. A box
  appears with the exact command and an **Allow** button. Read it before
  you click. Never choose "always allow" for terminal commands.
- Every message you send costs one request, and long tasks can cost more.
  Write **one precise prompt** instead of five vague ones.

Menu names and buttons in Copilot change often. If something is not exactly
where described, look for the same word nearby.

---

## Task 1 — A Live Preview Next to the Code

**1.** Open your `vibe-site` folder in VS Code and open `index.html`. Click
**Go Live** in the blue status bar at the bottom. Your browser opens
`http://127.0.0.1:5500/index.html`.

**2.** Now open the same page **inside** VS Code: open the Command Palette
(`Ctrl + Shift + P` / `Cmd + Shift + P`), type `Simple Browser: Show`, press
Enter and paste the address. Drag the tab to the right half of the window,
so you see code, preview and chat at the same time.

**3.** In the Copilot chat (mode: **Agent**), send:

> *In index.html, make the "Same-day flat tyre repair" offer stand out more,
> for example as a highlighted box. Use the existing colour tokens from the
> :root block. Change nothing else.*

Look at the diff, then at the preview. Live Server reloads it each time a
file is saved. Click **Keep** if you like it, **Undo** if not.

**4.** Read Copilot's last message. Does it say anything about how the page
*looks* now? How could it know?

<details>
<summary>Solution</summary>

- With Live Server, the preview reloads by itself as soon as the file is
  saved. You no longer switch windows and press `F5`.
- Copilot usually ends with a confident summary such as "The offer is now
  highlighted with a box in the accent colour". It wrote that **without
  seeing the page**. It only knows what it wrote into the file. Whether the
  box is readable, too wide on a phone or clashes with the hero is still
  unknown to it. Right now, you are the only one who looked.
- That is level 1 from the table: useful, fast, but completely dependent on
  your eyes and your patience.

**Key points:**
- Code, preview and chat side by side is the basic setup for everything
  that follows.
- "Change nothing else" is still important. Agents like to tidy up things
  you didn't ask about.
- A summary from the AI is a description of its *intention*, not of the
  *result*.

</details>

---

## Task 2 — Give Copilot Eyes: a Browser It Can Control

**Playwright** is a free tool from Microsoft that controls a real browser:
open pages, change the window size, take screenshots, read the console,
click and type. The **Playwright MCP server** makes these abilities
available to Copilot as tools. *MCP* (Model Context Protocol) is the
standard way to plug extra tools into AI assistants.

**1.** In your `vibe-site` folder, create a folder `.vscode` (with the dot)
and in it a file `mcp.json` with this content:

```json
{
  "servers": {
    "playwright": {
      "command": "npx",
      "args": ["@playwright/mcp@latest"]
    }
  }
}
```

**2.** Save the file. Above `"playwright"`, VS Code shows a small **Start**
link. Click it. The first start downloads the tool and can take a minute.
When it says **Running**, the tools are available. In the chat, the
**tools icon** (next to the mode drop-down) now lists `playwright` with
tools such as `browser_navigate` and `browser_take_screenshot`.

**3.** Make sure Live Server is running (Task 1). Then send this prompt:

> *Use the Playwright browser tools. Do not change any files.*
> *1. Open http://127.0.0.1:5500/index.html.*
> *2. Set the window to 360 × 800 pixels and take a screenshot of the full
> page.*
> *3. Set the window to 1280 × 800 pixels and take another full-page
> screenshot.*
> *4. Describe the differences between the two, and list anything that
> looks broken, cut off or hard to read. Name the section for each finding.*

Approve the browser actions when asked. Compare its findings with what you
see in the preview.

<details>
<summary>Solution</summary>

- Copilot opens its own browser window (or works invisibly in the
  background), and the screenshots appear in the chat. Now the AI really
  has *seen* the page, at two widths, in a few seconds.
- The prompt has a fixed structure that you will reuse: **which tool**, a
  **numbered list of steps**, **what not to do** ("do not change any
  files") and **what the answer must contain**.
- Typical findings: a navigation that wraps into two or three lines on a
  phone, a hero that fills the whole first screen, a table with columns
  squeezed together, the highlighted box from Task 1 touching the screen
  edge.
- Compare critically. The AI can miss things in a screenshot, and it
  sometimes "sees" problems that are not there. If a finding surprises
  you, check it yourself in the preview.

If **Start** does not appear or the server stops with an error, check
`node --version` in the terminal. Most problems come from a missing or very
old Node.js. If `localhost` does not open, check that Live Server is
running: the status bar shows **Port: 5500**.

**Key points:**
- `.vscode/mcp.json` belongs to this project folder. In another project,
  you add it again or set it up once for all projects in your VS Code user
  settings.
- Screenshots are level 2: much better than nothing, but still an
  interpretation.
- Playwright only runs on your computer and only opens the addresses you
  (or the AI) give it. Still, read each action before you allow it.

</details>

---

## Task 3 — Prompts with Acceptance Criteria

So far you asked Copilot to *look*. Now you ask it to **change something,
check the result itself, and fix it if the check fails**. For that, the
prompt needs a part that the prompts in the main workshop didn't have:
**acceptance criteria**, i.e. checks that can only pass or fail.

Bad criterion: *"It should look good on phones."*
Good criterion: *"At 360 px width, the page is not wider than the window."*

A render-and-verify prompt has five parts:

| Part | Question it answers |
|---|---|
| **Change** | What exactly should be different? |
| **Limits** | What must stay as it is? |
| **Verify** | Which checks, at which widths, with which tools? |
| **Evidence** | What must the final answer show? |
| **Stop rule** | What happens if a check keeps failing? |

**1.** Send this prompt. It asks for a change with a well-known trap:

> **Change:** *Make the header with the navigation stay visible at the top
> while scrolling (sticky header).*
>
> **Limits:** *Only change index.html. Keep all texts and colours.*
>
> **Verify** *with the Playwright tools on http://127.0.0.1:5500/index.html,
> at 360 × 800 and at 1280 × 800:*
> *1. Scroll down: the header must stay visible at the top.*
> *2. Measure the header height. At 360 px it must be at most 25 % of the
> window height.*
> *3. Click every link in the navigation. After each click, the heading of
> the target section must be visible and not hidden under the header.
> Check this by comparing the top position of the heading with the bottom
> of the header, using JavaScript in the page.*
>
> **Evidence:** *End with a table: check, width, measured value, PASS or
> FAIL. Add one screenshot per width.*
>
> **Stop rule:** *If a check fails, fix it and run all checks again. After
> two failed fix attempts, stop and tell me what fails and why.*

**2.** Watch what happens in the chat. Did a check fail in the first round?
What did Copilot change to fix it?

**3.** Test it yourself in the preview: make the window narrow and click a
menu item. Does the table tell the truth?

<details>
<summary>Solution</summary>

- **The trap.** A sticky header lies *on top* of the page. When you click a
  link in the menu, the browser scrolls the section to the very top of the
  window, right **under** the header. The section's heading is hidden.
  This is one of the most common bugs on real websites, and you don't
  notice it by looking at the page. You only notice it by clicking.
- Criterion 3 catches it. A typical first round looks like this:

  | Check | Width | Measured | Result |
  |---|---|---|---|
  | Header stays visible | 360 | top = 0 after scrolling | PASS |
  | Header height ≤ 25 % | 360 | 118 px of 800 (15 %) | PASS |
  | Headings visible after click | 360 | "Prices": heading top 0, header bottom 118 | FAIL |

  The usual fix is one line of CSS, such as
  `section { scroll-margin-top: 8rem; }` or `scroll-padding-top` on `html`.
  It tells the browser to stop scrolling a little earlier. After the fix,
  the same checks run again and pass.
- If the header on a phone is too high (navigation in three lines), check 2
  fails and Copilot has to make the navigation more compact. Without a
  number, "a bit large" would have been accepted.
- **Step 3** matters. Sometimes the AI writes PASS for a check it did not
  really carry out, or measures the wrong element. A table with *measured
  values* makes this visible: "PASS" without a number is a warning sign.

**Key points:**
- Acceptance criteria turn "looks fine to me" into something that can be
  checked, by the AI and by you.
- "Use JavaScript in the page" lets the AI **measure** instead of looking:
  positions, sizes, widths. That is level 3.
- The stop rule protects your request budget and your file. Without it, an
  agent can try fix after fix and make the page worse each time.
- One change per prompt is still the rule. The checks are what makes the
  prompt longer, not the number of changes.

</details>

---

## Task 4 — Automatic Checks the Agent Runs Itself

Some checks are so useful that they should run after **every** change, not
just after a special one. In this task you collect them in one prompt.

| Check | Tool | Clear pass condition |
|---|---|---|
| No horizontal scrolling | Playwright + JavaScript | `document.documentElement.scrollWidth` ≤ `window.innerWidth` |
| No JavaScript errors | Playwright console | 0 messages of type *error* |
| Keyboard focus visible | Playwright, `Tab` key | A visible outline on each focused element |
| Structure, alt texts, contrast | `site_check.py` in the terminal | Output ends with *No problems found by this script* |

**1.** Make a deliberate mistake first, so you know the checks work. In
`index.html`, find the `<style>` block and add this line just before
`</style>`:

```css
h1 { white-space: nowrap; }
```

Save. The headline now refuses to wrap and is wider than a phone screen.

**2.** Send this prompt:

> *Run these checks on http://127.0.0.1:5500/index.html. Do not change any
> files yet.*
> *1. At 360, 768 and 1280 px width: compare
> document.documentElement.scrollWidth with window.innerWidth. PASS if the
> page is not wider than the window. If it fails, find the element that
> sticks out.*
> *2. Reload the page and read the browser console. PASS if there are no
> errors.*
> *3. At 1280 px, press Tab ten times. After each press, report which
> element has focus and whether it has a visible outline.*
> *4. Run `python3 site_check.py index.html` in the terminal
> (on Windows: `python site_check.py index.html`). PASS if the output ends
> with "No problems found by this script".*
> *Report a table: check, width, measured value or output, PASS/FAIL. Then
> propose fixes for every FAIL, but wait for my OK before you change
> anything.*

**3.** Read the table. If the overflow check found your line, answer
*"OK, fix the FAILs and run all checks again."* Look at the diff before you
click **Keep**.

<details>
<summary>Solution</summary>

- Check 1 should fail at 360 px, and usually at 768 px too, with something
  like *scrollWidth 512, innerWidth 360*. A good answer names the culprit
  (the `h1`) and the rule `white-space: nowrap`. You **planted** the bug,
  so you know the check is not just saying PASS to everything. Testing your
  checks with a known mistake is called **testing the tester**, and it is
  worth doing for every new check.
- Check 4 runs in the VS Code terminal. Copilot asks before running it,
  and the output appears in the chat. If Python is not found, the answer
  should say so instead of pretending the check passed.
- "Wait for my OK" splits the work in two: first the diagnosis, then the
  fix. That costs one more request, but you decide what gets changed, and
  you learn what the problems were.
- Check 3 is the weakest one: whether an outline is "visible" is again
  interpretation. If in doubt, press `Tab` yourself.

**Key points:**
- The best checks have a **pass condition you could explain to a
  colleague in one sentence**.
- Scripts like `site_check.py` give the same answer every time. The AI's
  judgment does not. Let scripts do what scripts can do.
- None of these checks says anything about whether the **content** is true.
  That's next.

</details>

---

## Task 5 — Checking the Facts Against the Brief

In Task 1 of the main workshop, the AI invented ratings, addresses and
customer numbers. Neither Lighthouse nor `site_check.py` could catch that.
Copilot can, because it can read `business_brief.md` **and** the page.

**1.** Make another deliberate mistake. In `index.html`, change the price of
the full service from `€ 89` to `€ 79` (however your page writes
the price), and add this sentence anywhere in
the page text: *"Rated 4.9 out of 5 by our customers."* Save.

**2.** Send:

> *Compare the visible text of http://127.0.0.1:5500/index.html with
> business_brief.md. Do not change any files.*
> *Make a table of every fact on the page: names, address, phone, email,
> opening hours, prices, promises, numbers. For each fact give: the text on
> the page, the matching line in business_brief.md, and one of MATCH,
> DIFFERENT or NOT IN BRIEF.*
> *Then list everything the brief says under "What we do NOT offer" and
> check that the page does not promise any of it.*

**3.** Did it find both of your mistakes? Did it find anything you didn't
plant?

**4.** Now ask Copilot to make this check **repeatable**:

> *Write a small Python script check_facts.py that reads index.html and
> checks that each of these appears in the page text exactly as written:
> the phone number, the email address, the address, and every price from
> the price table in business_brief.md. Print OK or MISSING for each, and
> a summary at the end. Use only the Python standard library. Then run it.*

<details>
<summary>Solution</summary>

- A good table shows `€ 79` as **DIFFERENT** (brief: `€ 89`) and the rating
  as **NOT IN BRIEF**. Often it also finds things the original AI added
  without anyone noticing: "expert mechanics", "fast turnaround", a "free
  estimate". Each of them is a promise Mara would have to keep.
- The *"What we do NOT offer"* check catches a typical slip: a page that
  says "We repair all e-bike problems" or shows a PayPal logo.
- **Step 4** shows the difference between the two kinds of check. The AI
  comparison understands meaning ("Tue–Fri" and "Tuesday – Friday" are the
  same) but can overlook something and gives slightly different results
  each time. The script only finds exact text, but it finds it reliably,
  every time, in a fraction of a second. Run `check_facts.py` once now: it
  should report `€ 89` as MISSING. Then fix the price and run it again.
- Read the script before you trust it. Ask *"Explain check_facts.py in five
  bullet points"* if you're unsure what it does. Check that it reads the
  prices from the brief, and does not just contain a copy of the prices
  that happen to be on the page.

**Key points:**
- The business brief is now not only the source for the prompt, but also
  the **reference for the check**.
- "NOT IN BRIEF" is the most valuable column. It finds invented content.
- Fix both planted mistakes before you continue, or go back to
  `index-before-copilot.html` and redo the changes you kept.

</details>

---

## Task 6 — Make It a Habit: Instructions and a /verify Command

Writing the checks into every prompt is tiring. VS Code lets you store
them once:

- **`.github/copilot-instructions.md`** is read by Copilot automatically
  in every chat in this folder. It is the place for rules that always
  apply.
- **Prompt files** in `.github/prompts/` become your own **slash
  commands**. A file `verify.prompt.md` can be started by typing `/verify`
  in the chat.

**1.** Create `.github/copilot-instructions.md`:

```markdown
# Rules for this project

- This is a one-page website for Kurbelwerk, a bike workshop. The only
  source of facts is business_brief.md. Never invent names, prices, numbers,
  reviews or promises.
- Everything stays in one file, index.html, with CSS in a <style> tag. No
  frameworks, no external files, no external fonts, no tracking.
- All colours are CSS custom properties in the :root block.
- Change only what was asked for. If something else looks wrong, mention it
  instead of fixing it.
- The page is served by Live Server at http://127.0.0.1:5500/index.html.
- Never say a change is "verified" or "works" without showing evidence: a
  screenshot, a measured value, or a command with its output.
```

**2.** Create `.github/prompts/verify.prompt.md`:

```markdown
---
description: Render index.html and run all automatic checks
---

Check http://127.0.0.1:5500/index.html with the Playwright browser tools
and the terminal. Do not change any files.

1. At 360 × 800 and 1280 × 800: take a full-page screenshot.
2. At 360, 768 and 1280 px: PASS if document.documentElement.scrollWidth
   is not larger than window.innerWidth. If it fails, name the element
   that sticks out.
3. Reload the page. PASS if the browser console has no errors.
4. Click every navigation link at 360 px. PASS if the target heading is
   visible and not covered by the header.
5. Run `python3 site_check.py index.html`. PASS if the output ends with
   "No problems found by this script".
6. Run `python3 check_facts.py`. PASS if nothing is MISSING.

Report a table: check, width, measured value or output, PASS/FAIL.
Then list proposed fixes for every FAIL. Do not apply them.
```

On Windows, write `python` instead of `python3` in both lines.

**3.** Open a **new chat** (the `+` icon in the chat view), choose **Agent**,
type `/verify` and press Enter.

**4.** Now use the setup for a real change. Write one prompt in the style of
Task 3 for a change Mara would like, for example *"Add a short section
'How a repair works' with three steps: book by phone or email, bring the
bike, pick it up. Use only facts from the brief."* End the prompt with
*"When you are done, follow the steps in .github/prompts/verify.prompt.md,
fix any FAIL, and check again. Stop after two failed fix attempts."*

<details>
<summary>Solution</summary>

- With the instructions file, Copilot follows the rules without you
  repeating them, but it is not a guarantee. Rules are instructions, not
  locks. Your diff review stays in place.
- `/verify` gives you the same full check every time, in one request. Use
  it after every change you kept, and once more before you upload the page.
- Step 4 combines everything: a precise change, limits from the
  instructions file, automatic checks, a fix loop with a stop rule, and
  evidence at the end. That is the workflow professionals use with AI
  agents, just on a smaller scale.
- For the "How a repair works" section, the facts check matters. A typical
  AI addition is *"We'll call you when your bike is ready"*. That sounds
  harmless, but it is not in the brief, and it is a promise.

**Key points:**
- Rules that always apply go into the **instructions file**. Checks you
  start on purpose go into a **prompt file**.
- Both are plain text files in your project. You can improve them over
  time, and they go with the project to every computer.
- Prompt file options change with VS Code versions. If `/verify` does not
  appear, check that the file is in `.github/prompts/` and ends with
  `.prompt.md`.

</details>

---

## The Render-and-Verify Checklist

Before you accept a change from an AI agent:

- [ ] The prompt had **acceptance criteria** that can only pass or fail.
- [ ] The answer contains **evidence**: screenshots, measured values,
      command output. No "I checked it" without proof.
- [ ] I **read the diff** before clicking Keep.
- [ ] I **tested at least one check myself** in the preview, or with a
      planted mistake.
- [ ] `/verify` passes, including the facts check against the brief.
- [ ] I still have a working copy from before the change.

---

## Where to Go Next

- **Real tests.** Playwright can also run tests as ordinary scripts, without
  an AI in between: `npm init playwright@latest` sets up a project. Ask
  Copilot to turn your `/verify` steps into a test file. Then the checks run
  identically every time, and they cost no requests.
- **Lighthouse from the terminal.** `npx lighthouse
  http://127.0.0.1:5500/index.html --view` runs the audit from Task 7 of
  the main workshop as a command, so an agent can run it too.
- **Checks on GitHub.** With *GitHub Actions*, scripts like `site_check.py`
  can run automatically each time you upload a change to your repository.
- **Other agents.** Cursor, Claude Code and other AI coding tools support
  MCP servers and instruction files in a similar way. The prompts from today
  work there with small changes.
