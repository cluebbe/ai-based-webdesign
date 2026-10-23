# AI-Based Webdesign Workshop

A hands-on, 90-minute beginner workshop on building web pages by talking to
an AI ("vibe coding"). Participants see what an AI invents when given too
little to go on, write a reusable prompt template, learn to find their way
around the generated HTML, give the page a palette that is easy to read, fix
bugs with good bug reports, test it on phone and desktop widths, audit
accessibility with Lighthouse, and publish it on GitHub Pages. It ends with
a checklist to go through before a page goes live.

**No programming experience needed.** The AI writes the code. Participants
learn to steer it, read it and check it. An optional final part adds an
automatic checker in Python and AI inside the code editor.

---

## Getting Started

**Requirements:** a free account with an AI chatbot (ChatGPT, Claude, Gemini
or Microsoft Copilot), Google Chrome or Microsoft Edge,
[Visual Studio Code](https://code.visualstudio.com) and a free
[GitHub](https://github.com) account. Python 3.9+ is only needed for the
optional part.

Participants **do not need this repository**. They create their own
`vibe-site` project folder and copy each file from the workshop text into
it, as explained in the workshop's *Before the Workshop* section. The files in
this repository are the finished versions, for instructors and for checking.

Work through the `.md` file: read a section, try the task yourself, then open
the solution to compare.

---

## Workshop

### AI-Based Webdesign with Vibe Coding
**Workshop:** [VIBE_CODING_BASICS.md](VIBE_CODING_BASICS.md)

**Reference files** (participants create these themselves during the tasks):
[content/business_brief.md](content/business_brief.md) (Task 2) ·
[prompt_template.md](prompt_template.md) (Task 2) ·
[site/index.html](site/index.html) (a finished example result, Tasks 2–8) ·
[bug.html](bug.html) (Task 5) ·
[site_check.py](site_check.py) (optional part, downloaded from GitHub)

| Time | Part |
|---|---|
| 0:00 – 0:10 | What a web page is, what vibe coding is, the describe–generate–check–refine loop |
| 0:10 – 0:20 | From one sentence to a web page, and what the AI invents |
| 0:20 – 0:30 | A prompt that works: a reusable template and real content |
| 0:30 – 0:40 | Reading the code the AI wrote, first steps in DevTools |
| 0:40 – 0:50 | Design basics: hierarchy, type, colour, contrast and design tokens |
| 0:50 – 1:00 | Small steps and good bug reports |
| 1:00 – 1:10 | Mobile first and responsive design |
| 1:10 – 1:20 | Accessibility and the Lighthouse audit |
| 1:20 – 1:30 | Going live on GitHub Pages and the pre-flight checklist |
| Optional | An automatic check in Python, AI inside the editor |

The business in all examples, *Kurbelwerk* in *Musterstadt*, is invented.
`site/index.html` uses no external fonts, scripts or images, and is marked
`noindex` so a published copy does not show up in search engines.
