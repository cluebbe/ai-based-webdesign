# Workshop: AI-Based Webdesign with Vibe Coding

**Duration:** 90 minutes · **Level:** beginner ·
**Prerequisites:** none. You should be able to install programs and use a
web browser. You will not write code from scratch: an AI writes it, and you
learn to steer it, read it and check it. The Python part at the end is
optional.

---

## Introduction

### Background

A web page is made of plain text files. A browser downloads them from a
**server** and turns them into what you see. Three languages share the work:

| Language | Job | Comparison |
|---|---|---|
| **HTML** | Structure and content: headings, text, images, links | The rooms and walls of a house |
| **CSS** | Appearance: colours, fonts, spacing, layout | Paint, furniture, lighting |
| **JavaScript** | Behaviour: menus that open, things that react to clicks | Light switches and doorbells |

**Vibe coding** means building software by describing what you want in
plain language and letting an AI write the code. The term was made popular
by AI researcher Andrej Karpathy in early 2025. It works because large
language models (LLMs) have seen huge amounts of public web code, and web
pages follow well-known patterns.

The work happens in a loop, and you will go through it many times today:

```
  ┌────────────┐     ┌────────────┐     ┌────────────┐     ┌────────────┐
  │  Describe  │ ──▶ │  Generate  │ ──▶ │   Check    │ ──▶ │   Refine   │
  │   (you)    │     │    (AI)    │     │   (you)    │     │   (you)    │
  └────────────┘     └────────────┘     └────────────┘     └─────┬──────┘
        ▲                                                        │
        └────────────────────────────────────────────────────────┘
```

The AI is fast, but it has no taste, does not know your customers, and does
not check its own work. **You stay the designer and the reviewer.** The AI
is a very fast assistant that sometimes makes things up.

There are three kinds of AI tools for web pages. Today you only need the
first one:

| Kind | Examples | What you get | Today |
|---|---|---|---|
| **AI chatbot** | ChatGPT, Claude, Gemini, Microsoft Copilot | Code in a chat, you save it yourself | ✓ All tasks |
| **AI site builder** | Bolt.new, v0, Lovable | Code plus live preview in the browser | *Where to Go Next* |
| **AI code editor** | Cursor, VS Code with GitHub Copilot | AI inside the editor, working on your files | Optional Task 10 |

Chatbots are the most transparent: you see every line, and you decide what
goes into your files. What you learn with them carries over to every other
tool.

### Before the Workshop

Please do these steps **at home, before the workshop**. All accounts are
free and need no credit card.

**1. An AI chatbot account.** Sign up for one of
[ChatGPT](https://chatgpt.com), [Claude](https://claude.ai),
[Gemini](https://gemini.google.com) or
[Microsoft Copilot](https://copilot.microsoft.com). Free plans have daily
limits. If you hit one during the workshop, switch to a second chatbot.

**2. Google Chrome or Microsoft Edge.** Both contain the developer tools and
the *Lighthouse* audit used in Tasks 3, 6 and 7.

**3. A text editor for code.** Word processors such as Word or TextEdit add
hidden formatting and break HTML files. Install the free
[Visual Studio Code](https://code.visualstudio.com). The instructions
assume it.

**4. A GitHub account** at [github.com](https://github.com), for publishing
your page in Task 8. Your username becomes part of your web address
(`username.github.io`), so pick something you would show a future client or
employer, such as your name.

**5. Create your project folder.** All files from this workshop go into one
folder called `vibe-site` in your home folder. Open a terminal (macOS:
`Cmd + Space`, type `Terminal`; Windows: Windows key, type `PowerShell`) and
type:

```bash
cd ~                 # Go to your home folder
mkdir vibe-site      # Create the project folder
cd vibe-site         # Go into it
code .               # Open the folder in Visual Studio Code
```

If `code .` is not found, open VS Code yourself and choose *File → Open
Folder…* → `vibe-site`.

> **What not to paste into a chatbot.** Everything you type is sent to the
> provider's servers. Do not paste customer data, passwords, API keys or
> anything confidential. Today we only use an invented business.

### Creating a File in Your Project Folder

Several tasks ask you to create a file. It always works the same way:

1. In VS Code, click the *New File* icon next to `VIBE-SITE` in the file
   list on the left (or *File → New File…*).
2. Type the **exact** file name given in the task, e.g. `index.html`.
3. Paste the content and save with `Cmd + S` (macOS) or `Ctrl + S`
   (Windows/Linux).

To **look at** an HTML file, find it in your file manager (Finder or
Explorer) and double-click it, or drag it into a browser window. After every
change: save in VS Code, then press `F5` (macOS: `Cmd + R`) in the browser.

---

## Task 1 — From One Sentence to a Web Page

**1.** Create a file named `hello.html` with this content, save it and open
it in your browser:

```html
<!DOCTYPE html>
<html lang="en">
  <head>
    <title>My first page</title>
  </head>
  <body>
    <h1>It works!</h1>
    <p>This page is a text file on my own computer.</p>
  </body>
</html>
```

**2.** Now let the AI do it. Open your chatbot and send this deliberately
short prompt:

> *Make a website for a bike repair shop. Give me one HTML file.*

Create a file `first-try.html`, paste the code from the answer, save it and
open it in the browser.

**3.** The result probably looks surprisingly good. Look closer:

1. What does the page contain that you never told the AI? Make a list of
   every fact: name, address, numbers, ratings, opening hours.
2. Make the browser window as narrow as a phone. Can you still reach every
   part of the navigation?
3. Where do the photos come from? Search the code (`Cmd + F` / `Ctrl + F`
   in VS Code) for `https://`.
4. Could you put this page online for a real shop?

<details>
<summary>Solution</summary>

Today's chatbots usually deliver a polished page that works at first
glance: clean layout, matching colours, working photos. That is exactly what
makes the problems easy to miss.

**1. Invented content.** The AI fills every gap with something plausible. In
one test run, the page contained a shop name, an address in Portland, a
phone number, an email address on a domain that may well belong to someone
else, opening hours, "12k+ bikes serviced", a "4.9/5 average rating" and
"certified mechanics". None of it is true. This is the same effect as a
**hallucination**: the model produces text that *sounds* right, with no
idea whether it *is* right. Numbers and ratings are the most dangerous
inventions because they look like facts.

**2. Hidden weaknesses.** Typical findings when you look more closely:
- Below a certain width the navigation simply disappears, with no menu
  button to replace it.
- White text on a bright orange or amber button: looks fine, but the
  contrast is often too low to read comfortably (Task 4).
- Icons made of emoji, or `<label>` used for things that are not form
  fields: small things that confuse screen readers (Task 7).

**3. Photos from someone else's server.** The images are usually loaded
directly from a stock photo site such as Unsplash. They show *some* bike
shop, not this one, and every visit to your page also sends the visitor's
IP address to that server (Task 8). Sometimes the address is invented and
the image does not load at all.

**4. Not without checking every line.** Invented ratings and customer
numbers are not just embarrassing: in Germany and the EU, fake reviews and
misleading claims are an unfair commercial practice and can be expensive.
Invented prices or opening hours annoy customers.

**Key points:**
- `hello.html` *is* a web page. Everything the AI produces is the same kind
  of file, just longer.
- "Looks professional" and "is correct" are two different things. The AI is
  very good at the first and has no way of knowing the second.
- A short prompt gives the AI freedom, and it fills that freedom with
  guesses. The next task shows how to take that freedom away.
- Your result looks different from your neighbour's, even with the same
  prompt. Chatbots answer with a little randomness.

</details>

---

## Task 2 — A Prompt That Works: Your Reusable Template

**Your first customer.** Mara Lenz runs **Kurbelwerk**, a small bicycle
repair workshop in the (invented) town of Musterstadt. She would like a
simple website and has sent you a short *business brief*: everything about
her shop that should be on the page, such as services, prices, opening hours
and contact details. From now on, every task works on this website.

This time you do not leave the AI any room for guessing. A good web design prompt answers the questions a human designer would ask in
a first meeting:

| Part | Question it answers |
|---|---|
| **Role** | Who should the AI act as? |
| **Goal** | What is being built, for whom? |
| **Audience** | Who visits, and what do they want to find quickly? |
| **Main action** | What is the *one* thing a visitor should do? |
| **Content** | Which facts are allowed, and what happens with missing ones? |
| **Sections** | Which parts, in which order? |
| **Look and feel** | Which mood, which colours? |
| **Technical rules** | Which file format, which limits? |
| **Output** | What exactly should the answer contain? |

**1.** Create a file `business_brief.md` with the content below. This is
Mara's brief: the only source of facts for her website.

<details>
<summary>business_brief.md: content to copy</summary>

````markdown
# Business Brief — Kurbelwerk Bike Workshop

*Fictional business, invented for this workshop. Any resemblance to a real
shop is coincidental.*

## Who we are

- Small bicycle repair workshop in Musterstadt, open since 2019.
- Run by Mara Lenz, a trained bicycle mechanic, together with one apprentice.
- We repair, we refurbish used bikes, and we explain what we did.

## Contact

- Address: Mühlgasse 7, 12345 Musterstadt
- Phone: 01234 567890
- Email: hallo@kurbelwerk.example
- No online booking. Repairs are booked by phone or email.

## Opening hours

| Day | Hours |
|---|---|
| Tuesday – Friday | 09:00 – 18:00 |
| Saturday | 10:00 – 14:00 |
| Sunday, Monday | closed |

## Services and prices (incl. VAT)

| Service | Price |
|---|---|
| Safety check (brakes, tyres, lights, chain) | € 39 |
| Full service (cleaning, adjusting, all bearings checked) | € 89 |
| Flat tyre repair | € 15 plus the new tube |
| Brake adjustment | € 19 |
| E-bike check (no motor or battery repairs) | € 59 |

## What makes us different

- **Same-day flat tyre repair** if you bring the bike before 11:00.
- **Free loan bike** while yours is with us. We have two, so ask when you book.
- **Refurbished city bikes** from € 249, with a 6-month warranty.

## What we do NOT offer

- We do not sell new bikes.
- We do not repair e-bike motors or batteries. Those go back to the
  manufacturer, and we help you arrange it.
- We accept cash and girocard, but not PayPal or credit cards.

## Audience and tone

- Commuters, students and families, many of them without a car.
- Friendly, plain language, a little nerdy about bikes. No jargon without an
  explanation.

## Not available yet

- No photos of the workshop yet.
- No customer reviews yet.
````

</details>

**2.** Create a file `prompt_template.md` with the template below.

<details>
<summary>prompt_template.md: content to copy</summary>

````markdown
# Web Page Prompt Template

Copy everything below the line into your AI chatbot, fill in the parts in
[square brackets], and paste the business brief at the very end.

---

**Role:** You are an experienced web designer who writes clean, accessible
HTML and CSS.

**Goal:** Build a one-page website for [business name], a [what kind of
business] in [town].

**Audience:** [who visits the page and what they want to find quickly]

**Main action:** The most important thing a visitor should do is
[one action, e.g. for a bakery: order a birthday cake].

**Content:** Use ONLY the facts from the business brief below. Do not invent
names, prices, opening hours, reviews, awards or photos. If something is
missing, write a visible placeholder like `[TODO: photo of the workshop]`.

**Sections, in this order:**
1. Header with the business name and a navigation menu
2. Hero: one headline, one sentence, one button for the main action
3. [the sections your visitors need, one per line, in the order they
   look for them]
4. Footer with a link to the legal notice (Impressum)

**Look and feel:** [three adjectives, e.g. for a bakery: warm, traditional, cosy].
Colours: [your colours, or "suggest a palette with good contrast"].

**Technical rules:**
- One single file `index.html` with the CSS in a `<style>` tag and any
  JavaScript in a `<script>` tag.
- No frameworks, no external files, no external fonts, no tracking. Use a
  system font stack.
- Semantic HTML (`header`, `nav`, `main`, `section`, `footer`), exactly one
  `h1`, and `lang="en"` on the `html` tag.
- Mobile first: it must look good at 360 px wide and scale up to desktop.
- Accessible: colour contrast of at least 4.5:1, visible keyboard focus,
  meaningful `alt` text.
- Put all colours in CSS custom properties in a `:root` block.

**Output:** Reply with the complete file in one code block and nothing else.

**Business brief:**

[paste the business brief here]
````

</details>

**3.** Turn the template into a prompt for Mara's website. The template is
a fill-in-the-blanks text:

1. Copy everything in `prompt_template.md` **below** the line `---`. The
   lines above it are only instructions for you.
2. Replace every part in `[square brackets]` with information about
   Kurbelwerk. You find it in the business brief. For the sections, decide
   yourself: what does someone visiting a bike workshop's website want to
   find, and in which order? Only plan sections the brief has content for.
3. Replace the last line, `[paste the business brief here]`, with the
   **whole** content of `business_brief.md`.
4. Leave `[TODO: photo of the workshop]` in the *Content* rule as it is.
   It is not a gap for you, but an example that shows the AI how to mark
   missing content.
5. Start a **new chat** in your chatbot, paste the complete text, and send
   it as one message. A new chat matters: otherwise the chatbot still sees
   your one-sentence prompt from Task 1 and mixes the two.
6. The answer should be one code block. Copy it (most chatbots show a
   *Copy* button on the block), create a file `index.html` in `vibe-site`,
   paste the code, save, and open the file in the browser.

**4.** Compare with `first-try.html` from Task 1:

1. Which line of the template stopped the AI from inventing reviews?
2. Why "one single file" and "no external files"?
3. Did the AI follow *every* rule? Check the reviews, the prices and the
   `lang` attribute.

<details>
<summary>Solution</summary>

**Check your filled-in prompt first.** There is no single right wording,
but these decisions should match the brief:
- **Audience:** not just "everyone", but who visits and *what they look
  for*. Commuters with a broken bike want prices, hours and a phone number,
  not a company history.
- **Main action:** the brief says there is *no online booking*. A main
  action like "book online" would make the AI build a booking form that
  cannot work.
- **Sections:** the brief has content for services and prices, what makes
  the workshop different, and opening hours with contact details. Visitors
  with a broken bike usually look for prices first and contact last, or the
  other way round if they are in a hurry. Both orders can be argued. A
  "Reviews", "Our team" or "Shop" section cannot: the brief has nothing for
  them, so the AI would have to invent the content.
- **Look and feel:** adjectives that fit the tone described in the brief.
  "Luxurious" or "edgy" would not.

If one of these did not fit, change it in your prompt and try again in a new
chat. Comparing the two results is the fastest way to see how much each line
matters.

1. The **Content** rule: *"Use ONLY the facts from the business brief …
   If something is missing, write a visible placeholder."* The brief even
   says that there are no reviews and no photos yet. A visible `[TODO]` is
   much better than an invisible invention: you cannot miss it before going
   live.
2. One file is easy to copy between the chat, your editor and GitHub. No
   external files means nothing can fail to load, and no external fonts or
   scripts means no data about your visitors goes to other companies (see
   Task 8).
3. Usually *almost* every rule. Typical slips: one price rounded or changed,
   an extra "Our team" section, a contact form despite "no online booking".
   **Always compare the facts on the page with the brief.** If something is
   wrong, tell the AI exactly what: *"The full service costs € 89, not € 79.
   Change only that."*

**Key points:**
- The template is reusable: for the next customer, only the brackets and the
  brief change.
- Separating **content** (the brief) from **instructions** (the template)
  makes both easier to check.
- Starting a new chat for a new page avoids old instructions leaking in. The
  chatbot sees the whole conversation every time.
- The reference solution [site/index.html](site/index.html) shows what a
  good result can look like. Yours will look different, and that is fine.

</details>

---

## Task 3 — Reading the Code the AI Wrote

You do not need to *write* HTML, but you need to *find your way around* it:
to change a phone number yourself, to tell the AI where a problem is, and to
notice when something does not belong.

**1.** Open `index.html` in VS Code and find:

1. The text shown in the browser tab.
2. The main headline of the page.
3. The navigation menu.
4. The place where the main colours are defined.
5. The JavaScript, if there is any. What does it do?

**2.** Change the phone number in the page to `01234 999999` **yourself**,
without the AI. Save and reload the browser.

**3.** In the browser, right-click the main button and choose
**Inspect**. The **developer tools** (DevTools) open. In the *Styles* panel
on the right, find its `background` colour, click the small colour square,
and pick another colour. Then reload the page. What happens to your change?

<details>
<summary>Solution</summary>

| What | Where in the file |
|---|---|
| Browser tab text | `<title>…</title>` inside `<head>` |
| Main headline | `<h1>…</h1>`. There should be exactly one |
| Navigation | `<nav>` with a list (`<ul>`, `<li>`) of links (`<a href="#…">`) |
| Main colours | In `<style>`, at the top: `:root { --color-primary: #1f6f5c; … }` |
| JavaScript | In `<script>` at the end. Usually: the mobile menu button opens and closes the menu |

The most common **semantic** elements, which describe what a part *is*:

| Element | Meaning |
|---|---|
| `<header>` / `<footer>` | Top and bottom area of the page |
| `<nav>` | Main navigation |
| `<main>` | The main content, once per page |
| `<section>` | A thematic block, usually with its own heading |
| `<h1>` … `<h6>` | Headings, from most to least important |
| `<a href="…">` | A link. `href="#contact"` jumps to the element with `id="contact"` |
| `<button>` | Something that *does* something on this page |

**2.** Search with `Cmd + F` / `Ctrl + F` in VS Code. The number often
appears twice: as visible text and in a link like `href="tel:+491234567890"`.
Change both, otherwise tapping it on a phone still calls the old number.

**3.** Changes in DevTools apply immediately, but only in your browser, and
they **disappear on reload**. DevTools are for *trying out*. Once you like a
colour, change it in the file or tell the AI the exact value.

**Key points:**
- Small text changes are faster, cheaper and safer to do yourself. The AI
  might "helpfully" change other things at the same time.
- `#1f6f5c` is a colour written as a **hex code**: red, green and blue, each
  from `00` to `ff`.
- Colours stored as **custom properties** (`--color-primary`) are used
  throughout the CSS with `var(--color-primary)`. Change them in one place,
  and the whole page changes.

</details>

---

## Task 4 — Design Basics: Hierarchy, Type and Colour

AI-generated pages often look "fine but generic". A few rules make the
difference, and knowing them lets you give precise instructions instead of
"make it nicer".

**Visual hierarchy.** The eye should know where to look first, second, third.
You control this with **size, weight, colour, space and position**. Each
screen should have one clear main action, so give it the strongest colour,
and nothing else.

**Typography.**
- One font family is enough, two at most (one for headings, one for text).
- Body text at least **16 px**, line height about **1.5**.
- Lines of about **45 – 75 characters**. Longer lines are tiring to read.
- A *system font stack* uses the fonts already on the visitor's device: fast,
  and nothing is downloaded from another company.

**Colour.**
- A small palette: a background, a text colour, one **primary** colour for
  actions, maybe one **accent**. A common split is 60 % background, 30 %
  secondary areas, 10 % accent.
- **Contrast** between text and background is measured as a ratio from 1:1
  (none) to 21:1 (black on white). The accessibility guideline WCAG requires
  at least **4.5:1** for normal text and **3:1** for large text, icons and
  the borders of buttons and input fields.

**Your task:**

**1.** Check these four colour pairs with the free
[WebAIM Contrast Checker](https://webaim.org/resources/contrastchecker/).
Which ones can be used for normal text?

| Text | Background |
|---|---|
| `#ffffff` (white) | `#f2a541` (amber) |
| `#1c2321` (near black) | `#f2a541` (amber) |
| `#9aa5a1` (light grey) | `#ffffff` (white) |
| `#ffffff` (white) | `#1f6f5c` (dark green) |

**2.** Give your page a palette of **design tokens**, named colours that
are used everywhere. Send this to the chatbot, in the same chat as your page:

> *Replace the colours in the `:root` block with exactly these tokens and use
> them everywhere in the CSS. Do not change anything else.*
>
> ```css
> :root {
>   --color-bg: #fbfaf7;         /* page background, warm off-white */
>   --color-surface: #ffffff;    /* cards and the header */
>   --color-text: #1c2321;       /* main text */
>   --color-muted: #5b6662;      /* secondary text */
>   --color-primary: #1f6f5c;    /* buttons and links */
>   --color-on-primary: #ffffff; /* text on primary */
>   --color-accent: #f2a541;     /* highlights, never with white text */
> }
> ```

Save the new version over `index.html`, reload, and look at it next to the
old version. You can also pick your own colours, but check their contrast
first.

<details>
<summary>Solution</summary>

| Pair | Ratio | Normal text? |
|---|---|---|
| White on amber | 2.05:1 | **No**, not even for large text |
| Near black on amber | 7.80:1 | Yes |
| Light grey on white | 2.54:1 | **No**, a classic AI favourite for "subtle" text |
| White on dark green | 6.02:1 | Yes |

So amber works as a button colour, but only with **dark** text. That is why
the token list says *"never with white text"*.

You can also see contrast inside the browser: in DevTools, click a colour
square in the *Styles* panel. The colour picker shows the **contrast ratio**
with a ✓ or ✗.

**Key points:**
- Naming tokens by their **job** (`--color-primary`) rather than their look
  (`--green`) means you can change the brand colour later without the names
  becoming wrong.
- *"Do not change anything else"* matters. Without it, the AI often
  rewrites half of the page while it is at it.
- A set of tokens for colours, fonts and spacing is the beginning of a
  **design system**. Paste the same tokens into every future prompt, and all
  pages of a project look like they belong together.
- Good prompts use design words: *"increase the space between sections"*,
  *"make the headline larger and the subline lighter"*, *"only one primary
  button per section"*.

</details>

---

## Task 5 — Small Steps and Good Bug Reports

**Part A: one change at a time.** Ask for these three changes, **each in its
own message**, and check the page after each one:

1. *"Add a short line under the hero headline: 'Flat tyre before 11:00?
   Ride home the same day.' Change nothing else."*
2. *"Show the opening hours as a table."*
3. *"Make the navigation stick to the top of the screen when scrolling."*

Before each step, keep a copy of the working version: copy `index.html` to
`index-v1.html`, `index-v2.html`, and so on.

**Part B: a bug hunt.** Create a file `bug.html` with this content and open
it in the browser. Click the question. Nothing happens.

```html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>FAQ — bug hunt</title>
  <style>
    body { font-family: system-ui, sans-serif; max-width: 40rem; margin: 2rem auto; padding: 0 1rem; }
    button { font: inherit; padding: 0.6rem 1rem; }
  </style>
</head>
<body>
  <h1>Frequently asked questions</h1>

  <button id="faq-button" type="button">Do I need to book a flat tyre repair?</button>
  <p id="faq-answer" hidden>No. Bring your bike before 11:00 and it is ready the same day.</p>

  <script>
    const button = document.getElementById("faq-button");
    const answer = document.getElementById("faq-anwser");

    button.addEventListener("click", () => {
      answer.hidden = !answer.hidden;
    });
  </script>
</body>
</html>
```

1. Open DevTools (`F12`, or `Cmd + Option + I` on macOS) and click the
   **Console** tab. Click the question again. What appears?
2. Write a bug report for the chatbot using this structure, then send it:

   > **What I did:** …
   > **What I expected:** …
   > **What happened instead:** …
   > **Error message in the console:** …
   > **The code:** (paste `bug.html`)

<details>
<summary>Solution</summary>

**Part A.** Small, separate requests are easier for the AI to get right and
easier for you to check. If step 3 breaks something, you only need to undo
step 3. Asking for ten changes at once usually gives you nine and a half,
and you have to search for what went missing.

If the AI breaks a working page and two follow-up messages don't fix it, go
back to your last copy instead of piling fixes on top of each other.

**Part B.**
1. The console shows: *Uncaught TypeError: Cannot read properties of null
   (reading 'hidden')*, with a link to the line. In plain words: the script
   looked for an element, found nothing (`null`), and then tried to use it.
2. The cause is a typo: `faq-anwser` in the script, `faq-answer` in the
   HTML. A good bug report lets the AI find it immediately, and it also lets
   *you* find it: the error points to the line with `answer.hidden`, and the
   only place `answer` is set is one line with a typo.

**Key points:**
- "It doesn't work" is the worst prompt there is. Expected versus actual
  behaviour plus the exact error message is the best.
- The **Console** is the first place to look whenever something on a page
  does not react. Red lines are errors.
- Ask the AI to *explain* the fix in one sentence. You learn something, and
  you notice when its explanation does not make sense.

</details>

---

## Task 6 — Mobile First and Responsive Design

More than half of all web visits come from phones. **Responsive** design
means one page that adapts to every screen width. **Mobile first** means
designing for the small screen first, then adding layout for larger
screens, because squeezing a desktop design onto a phone rarely works.

What makes a page responsive:

| Building block | Purpose |
|---|---|
| `<meta name="viewport" content="width=device-width, initial-scale=1">` | Tells phones not to show a shrunken desktop page |
| Flexible layout (CSS `flex`, `grid`) | Columns that wrap or stack instead of overflowing |
| Relative units (`rem`, `%`, `ch`) | Sizes that grow with text size and screen |
| `img { max-width: 100%; }` | Images never wider than the screen |
| **Media queries**, e.g. `@media (min-width: 48rem) { … }` | Extra rules from a certain width upwards (a **breakpoint**) |

**Your task:**

**1.** Open `index.html` in Chrome or Edge, open DevTools and click the
**device toolbar** icon (phone and tablet symbol), or press
`Cmd + Shift + M` / `Ctrl + Shift + M`. Set the width to **360**, then
**768**, then **1280** pixels.

**2.** At each width, check:

1. Can you scroll **sideways**? (You should not be able to.)
2. Is all text readable without zooming?
3. Does the navigation work? On a phone, try the menu button.
4. Are buttons and links big enough to tap with a thumb?

**3.** If you scroll sideways at 360 px, find the culprit: paste this into
the **Console** and press Enter. It lists all elements wider than the
screen:

```js
[...document.querySelectorAll("body *")].filter(el => el.getBoundingClientRect().right > document.documentElement.clientWidth + 1)
```

**4.** Describe one problem to the chatbot *precisely*, and let it fix it.

<details>
<summary>Solution</summary>

Typical problems at 360 px and how to describe them:

| What you see | Precise prompt |
|---|---|
| Sideways scrolling | *"At 360 px width the page scrolls sideways. The console shows the `table` is too wide. Make it fit without horizontal scrolling."* |
| Navigation links squeezed into one row | *"Below 768 px, hide the navigation behind a menu button with `aria-expanded`, and show the links stacked."* |
| Three cards side by side, very narrow | *"Show the feature cards in one column on phones and in three columns from 768 px."* |
| Tiny buttons | *"Make all buttons and navigation links at least 44 × 44 px to tap."* |

**Key points:**
- The device toolbar is a good approximation, but test on a **real phone**
  before going live. Touch, font sizes and browser bars behave differently.
- WCAG 2.2 requires touch targets of at least 24 × 24 px. 44 × 44 px is the
  comfortable size recommended by Apple and others.
- Giving the **width**, the **element** and the **expected behaviour** turns
  a vague complaint into a request the AI can solve in one go.

</details>

---

## Task 7 — Accessibility and the Lighthouse Audit

**Accessibility** means people can use your page regardless of disability:
with a screen reader, only a keyboard, low vision or colour blindness. The
international standard is **WCAG 2.2** (Web Content Accessibility
Guidelines). Level AA is the usual target. In the EU, the European
Accessibility Act, implemented in Germany as the
*Barrierefreiheitsstärkungsgesetz* (BFSG), has made it a legal requirement
for many online shops and services since June 2025.

**Lighthouse** is a free audit built into Chrome and Edge. It checks
performance, accessibility, best practices and search engine basics.

**Your task:**

**1.** Open `index.html`, open DevTools, choose the **Lighthouse** tab
(behind `»` if hidden). Select *Mode: Navigation*, *Device: Mobile*, all
categories, and click **Analyze page load**. Write down the four scores and
every failed audit under *Accessibility*.

> If Lighthouse will not run on a file opened from your disk, do steps 1–3
> of Task 8 first and audit the published page instead.

**2.** **Keyboard test.** Click into the address bar, then press `Tab`
repeatedly through the whole page.

1. Can you always see *where* you are (a visible focus outline)?
2. Can you open the mobile menu and reach every link?
3. Does the first `Tab` offer a "Skip to content" link?

**3.** Send the findings to the chatbot as a list, for example: *"Lighthouse
reports: 'Background and foreground colors do not have a sufficient
contrast ratio' for the footer links, and there is no visible focus outline
on the navigation links. Fix only these two problems."*

**4.** Run Lighthouse again. Did the score go up?

<details>
<summary>Solution</summary>

Common Lighthouse findings on AI-generated pages and what they mean:

| Lighthouse says | Meaning | Fix |
|---|---|---|
| *Background and foreground colors do not have a sufficient contrast ratio* | Text too light on its background | Use a token pair with ≥ 4.5:1 (Task 4) |
| *Image elements do not have `[alt]` attributes* | Screen readers cannot describe the image | Add `alt` text, or `alt=""` for pure decoration |
| *Links do not have a discernible name* | An icon-only link, e.g. a social media icon | Add visible text or an `aria-label` |
| *Heading elements are not in a sequentially-descending order* | E.g. `h2` followed by `h4` | Use heading levels as an outline, not for font size |
| *Form elements do not have associated labels* | A field with only placeholder text | Add a `<label>` |

**Writing good alt text:** describe what the image *means in this place*,
in one short sentence. *"Mechanic adjusting the brakes of a city bike"* is
good. *"Image of bike"* is weak, and the file name is useless. A logo next
to the business name, or a purely decorative pattern, gets `alt=""`.

**Keyboard:** without a visible focus outline, keyboard users are lost. A
skip link lets them jump past the navigation on every page. The reference
solution [site/index.html](site/index.html) has both.

**Key points:**
- A Lighthouse score of 100 does **not** mean a page is accessible.
  Automatic tests only catch part of the problems. Whether alt text is
  *meaningful* or the order makes sense needs a human.
- Fixing accessibility usually improves the page for everybody: better
  contrast helps in sunlight, larger buttons help on a bumpy bus.
- *Performance* is usually high for single-file pages. Large photos are the
  main reason it drops: compress them (e.g. with
  [Squoosh](https://squoosh.app)) and use the WebP format.

</details>

---

## Task 8 — Going Live: GitHub Pages and a Pre-Flight Check

**GitHub Pages** publishes the files in a GitHub repository as a website,
for free, at `https://USERNAME.github.io/REPOSITORY/`.

**1. Create a repository.** On [github.com](https://github.com), click
**+** → **New repository**. Name: `vibe-site`. Visibility: **Public** (free
Pages need a public repository). Click **Create repository**.

**2. Upload your page.** On the new repository page, click **uploading an
existing file**, drag in your `index.html` (only this file), and click
**Commit changes**.

**3. Switch on Pages.** *Settings* → *Pages* → under *Build and deployment*,
*Source*: **Deploy from a branch**, *Branch*: **main**, folder **/ (root)**
→ **Save**. After one or two minutes, the address appears at the top of the
same page. Open it, also on your phone.

**4. Pre-flight check.** Before a page for a *real* business goes live, go
through this list. Which points does your practice page not meet?

| Area | Checklist item |
|---|---|
| **Content** | Every fact checked against the customer's information. No `[TODO]` left |
| | No invented reviews, awards, numbers or people |
| | Rights to every image and text: own photos, licensed stock, or AI images whose terms allow commercial use |
| **Legal (Germany)** | A legal notice (*Impressum*) reachable from every page |
| | A privacy policy (*Datenschutzerklärung*) |
| | No tracking, analytics or external fonts without a legal basis or consent |
| **Security** | Nothing secret in the code: no passwords, API keys or internal notes. A public repository is public |
| **Quality** | Tested at 360, 768 and 1280 px and on a real phone |
| | Lighthouse accessibility ≥ 90 and the keyboard test passed |
| | Every link and the phone number tested |

<details>
<summary>Solution</summary>

A practice page does not meet the **legal** items: it has no real legal
notice and no real privacy policy. That is fine for a practice page about an
invented business, but say so on the page, as in the reference solution's
footer. The reference also contains `<meta name="robots" content="noindex">`
so search engines do not list it.

**Updating the page later:** open `index.html` in the repository, click the
pencil icon to edit, or use *Add file → Upload files* again with the new
version. Pages updates itself within a minute or two. Every upload is
saved as a **commit**, so the history shows every version and you can go
back to any of them.

**Key points:**
- External fonts are a real issue in Germany: a court ruled in 2022 that
  loading Google Fonts from Google's servers without consent violated a
  visitor's privacy rights. A system font stack, or font files hosted
  together with your page, avoids the problem.
- GitHub Pages is meant for personal, project and portfolio pages. GitHub's
  terms do not allow running a commercial online shop on it. For a real
  business, use a host such as Netlify, Cloudflare Pages or a classic web
  host, which all accept the same `index.html`.
- An own domain (e.g. `kurbelwerk.de`) can be connected to all of these
  hosts. It costs a few euros a year at a domain registrar.
- AI-generated text and images: check the terms of the tool you used.
  Whether purely AI-generated content is protected by copyright at all is
  still unclear in many countries, so do not rely on it being exclusively
  yours.

</details>

---

## Optional Part — Going Further

### Task 9 — An Automatic Check in Python

The script `site_check.py` reads an HTML file and checks many of the points
from this workshop: the basics in `<head>`, the heading outline, alt texts,
link and button names, form labels, external resources and the contrast of
your colour tokens. It uses only Python's built-in modules and never changes
your file.

**1.** Install Python 3 from [python.org](https://www.python.org/downloads/)
if you don't have it yet.

**2.** Open
[site_check.py](https://github.com/cluebbe/ai-based-webdesign/blob/main/site_check.py)
in your browser, click the **Download raw file** button (the arrow icon
above the code, on the right), and save it into your `vibe-site` folder.

**3.** In the terminal, inside `vibe-site`:

```bash
python3 site_check.py index.html        # On Windows: python site_check.py index.html
python3 site_check.py first-try.html
```

**4.** Open the script in VS Code and change it:

1. At the top, add the pair `("--color-accent", "--color-surface")` to
   `CONTRAST_PAIRS` and run it again. Why does it fail, and does it matter?
2. In section 5, add `"learn more"` to the `VAGUE` set.

<details>
<summary>Solution</summary>

- `first-try.html` from Task 1 often passes almost every check, although
  half of its content is invented. The script, like Lighthouse, can check
  *structure*, but not whether "4.9/5 average rating" is true. That part
  stays your job.
- If the contrast checks say `SKIP`, the AI used other token names (e.g.
  `--ink` instead of `--color-text`). The line `Colour tokens found:` lists
  them. Put those names into `CONTRAST_PAIRS`.
- **1.** Amber on white is about 2:1, far too low for text. It does not
  matter as long as amber is only used as a background *behind dark text*
  or as a decorative line, as in the reference solution. Contrast is always
  about a *pair* actually used together.
- **2.** Sets in Python are written in curly braces:
  `VAGUE = {"click here", "here", "more", "read more", "link", "learn more"}`.

**Key points:**
- Section 7 contains the actual WCAG contrast formula in about 15 lines. It
  is the same calculation the WebAIM checker and DevTools do.
- Like Lighthouse, the script finds *missing* things, not *bad* ones: it
  cannot tell whether an alt text is meaningful.

</details>

### Task 10 — AI Inside the Editor

AI code editors work directly on your files instead of in a separate chat.
VS Code includes **GitHub Copilot**, which has a free plan for a GitHub
account. **Cursor** is a separate editor built on VS Code with similar
features.

**1.** Install one of them and sign in. In VS Code, open the Copilot
**Chat** view.

**2.** With `index.html` open, ask: *"Explain the structure of this file in
five bullet points."*

**3.** Select the CSS for the buttons and ask for a change, e.g. *"Add a
subtle hover effect to the buttons."* Read the proposed change **before**
accepting it.

<details>
<summary>Solution</summary>

- The AI editor sees the file, so you no longer copy code back and forth.
  It shows changes as a **diff**: removed lines in red, added lines in green.
- Accept or reject each change consciously. "Accept all" without reading is
  how unwanted changes slip in.
- Everything from this workshop still applies: precise requests, one change
  at a time, keep versions, check the result in the browser.

**Key points:**
- With an editor, it pays to put the project into Git (see *Where to Go
  Next*). Then every accepted change can be undone.
- Menu names and free plan limits change often. If something is not where
  described, look in the editor's chat or account settings.

</details>

---

## Where to Go Next

- **AI site builders** such as Bolt.new, v0 and Lovable show a live preview
  while they build, and can create multi-page sites and whole web
  applications. Their free plans are limited, so try them with your prompt
  template from Task 2 and compare the results with your chatbot page.
- **Git and GitHub Desktop.** Instead of uploading files by hand, keep your
  project in Git. Every change is saved as a version you can return to.
- **Your own design system.** Extend the tokens from Task 4 with fonts,
  spacing and button styles, write them into a short style guide, and paste
  it into every prompt.
- **Images.** Free stock sites such as Unsplash and Pexels have their own
  licences. Read them. AI image generators can create illustrations, but
  check the usage terms and never generate images of real people or other
  companies' brands.
- **Portfolio.** Use the same workflow to build a page about yourself:
  who you are, what you can do, two or three projects, and how to reach you.
