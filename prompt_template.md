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
[e.g. call or email to book a repair].

**Content:** Use ONLY the facts from the business brief below. Do not invent
names, prices, opening hours, reviews, awards or photos. If something is
missing, write a visible placeholder like `[TODO: photo of the workshop]`.

**Sections, in this order:**
1. Header with the business name and a navigation menu
2. Hero: one headline, one sentence, one button for the main action
3. [Services and prices]
4. [What makes us different]
5. [Opening hours and contact]
6. Footer with a link to the legal notice (Impressum)

**Look and feel:** [three adjectives, e.g. friendly, calm, practical].
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
