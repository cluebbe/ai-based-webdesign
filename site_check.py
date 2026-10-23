# AI-Based Webdesign — Site Check
#
# AI tools write web pages fast, but they do not check their own work. This
# script reads an HTML file and checks the things the workshop talked about:
# the basics in <head>, the heading outline, alt texts, link and button names,
# form labels, external resources, and the colour contrast of your design
# tokens. Run it, read the output, then experiment by changing the checks.
#
# USAGE
# -----
#   python3 site_check.py index.html        (Windows: python site_check.py index.html)
#
# No Python packages are required — only the standard library is used.
# The script only reads your file. It never changes it.

import re
import sys
from html.parser import HTMLParser

# Pairs of colour tokens (text colour, background colour) to check for
# contrast. Change the names to the ones used in your own :root block.
CONTRAST_PAIRS = [
    ("--color-text", "--color-bg"),
    ("--color-muted", "--color-bg"),
    ("--color-on-primary", "--color-primary"),
    ("--color-primary", "--color-surface"),
]

# Addresses that load something from another company's server. Every one of
# them sends your visitors' IP address there, which matters for privacy law.
THIRD_PARTY_HINTS = [
    "fonts.googleapis.com",
    "fonts.gstatic.com",
    "googletagmanager.com",
    "google-analytics.com",
    "facebook.net",
    "unpkg.com",
    "cdn.jsdelivr.net",
    "cdnjs.cloudflare.com",
]

if len(sys.argv) != 2:
    print("Usage: python3 site_check.py index.html")
    sys.exit(1)

with open(sys.argv[1], encoding="utf-8") as file:
    html = file.read()

print("=" * 40)
print("  AI-Based Webdesign — Site Check")
print("=" * 40)

problems = 0


def ok(message):
    print(f"  OK    {message}")


def problem(message):
    global problems
    problems += 1
    print(f"  FIX   {message}")


# ---------------------------------------------------------------------------
# 1. READING THE PAGE
# ---------------------------------------------------------------------------
# A browser turns HTML into a tree of elements. Python's built-in HTMLParser
# walks through the file and calls handle_starttag for every opening tag. We
# collect what we need for the checks below.

class PageReader(HTMLParser):
    def __init__(self):
        super().__init__()
        self.tags = []              # (tag name, attributes) for every element
        self.headings = []          # (level, text) for h1 … h6
        self.links = []             # [attributes, visible text] for <a>
        self.buttons = []           # [attributes, visible text] for <button>
        self.title = ""
        self.label_targets = set()  # ids that a <label for="…"> points to
        self._open = []             # elements whose text we are collecting

    def handle_starttag(self, tag, attrs):
        attrs = dict(attrs)
        self.tags.append((tag, attrs))
        if tag == "label" and attrs.get("for"):
            self.label_targets.add(attrs["for"])
        if tag in ("title", "h1", "h2", "h3", "h4", "h5", "h6", "a", "button"):
            self._open.append([tag, attrs, ""])
        if tag == "img" and self._open:
            # An image inside a link or button gives it a name through its alt text
            self._open[-1][2] += attrs.get("alt", "")

    def handle_data(self, data):
        for element in self._open:
            element[2] += data

    def handle_endtag(self, tag):
        if not self._open or self._open[-1][0] != tag:
            return
        tag, attrs, text = self._open.pop()
        text = " ".join(text.split())
        if tag == "title":
            self.title = text
        elif tag == "a":
            self.links.append([attrs, text])
        elif tag == "button":
            self.buttons.append([attrs, text])
        else:
            self.headings.append((int(tag[1]), text))


reader = PageReader()
reader.feed(html)

print("\n--- 1. Reading the Page ---")
print(f"  {len(reader.tags)} elements, {len(reader.headings)} headings, "
      f"{len(reader.links)} links, {len(reader.buttons)} buttons")


def find(tag, **wanted):
    """All elements with this tag whose attributes contain the wanted values."""
    return [attrs for name, attrs in reader.tags
            if name == tag and all(attrs.get(k) == v for k, v in wanted.items())]


# ---------------------------------------------------------------------------
# 2. THE BASICS IN <head>
# ---------------------------------------------------------------------------
# Visitors never see these lines, but browsers, screen readers and search
# engines do. AI tools sometimes forget one of them.

print("\n--- 2. The Basics ---")

html_tag = find("html")
if html_tag and html_tag[0].get("lang"):
    ok(f'Language is set: lang="{html_tag[0]["lang"]}"')
else:
    problem('No lang attribute on <html>. Screen readers then guess the language.')

if reader.title:
    ok(f'Title: "{reader.title}"')
else:
    problem("No <title>. It is shown in the browser tab and in search results.")

if find("meta", name="viewport"):
    ok("Viewport meta tag found, so phones show the page at the right size.")
else:
    problem("No viewport meta tag. Phones will show a tiny desktop page.")

if find("meta", name="description"):
    ok("Meta description found.")
else:
    problem("No meta description. Search engines then pick a text themselves.")


# ---------------------------------------------------------------------------
# 3. HEADING OUTLINE
# ---------------------------------------------------------------------------
# Headings are the table of contents of a page. Screen reader users jump
# through them. There should be one h1, and levels should not skip (h2 → h4).

print("\n--- 3. Heading Outline ---")

for level, text in reader.headings:
    print(f"  {'  ' * (level - 1)}h{level}  {text}")

h1_count = sum(1 for level, _ in reader.headings if level == 1)
if h1_count == 1:
    ok("Exactly one h1.")
else:
    problem(f"{h1_count} h1 headings found. Use exactly one, for the page's main topic.")

previous = 0
for level, text in reader.headings:
    if level > previous + 1:
        problem(f'Skipped heading level before h{level} "{text}".')
    previous = level


# ---------------------------------------------------------------------------
# 4. IMAGES AND ALT TEXT
# ---------------------------------------------------------------------------
# Every <img> needs an alt attribute. Describe what matters in the image, or
# use alt="" for purely decorative images so screen readers skip them.

print("\n--- 4. Images and Alt Text ---")

images = find("img")
if not images:
    print("  (no <img> elements)")
for attrs in images:
    src = attrs.get("src", "?")
    if "alt" not in attrs:
        problem(f"Image without alt attribute: {src}")
    elif attrs["alt"] == "":
        ok(f"Decorative image (alt=\"\"): {src}")
    elif re.search(r"\b(image|picture|photo) of\b", attrs["alt"], re.IGNORECASE):
        problem(f'Alt text starts with "image of": say what it shows instead: {src}')
    else:
        ok(f'alt="{attrs["alt"]}"')


# ---------------------------------------------------------------------------
# 5. LINKS, BUTTONS AND FORMS
# ---------------------------------------------------------------------------
# A link or button needs a name a screen reader can read out. "Click here"
# is a name, but a useless one when you hear a list of all links on a page.

print("\n--- 5. Links, Buttons and Forms ---")

VAGUE = {"click here", "here", "more", "read more", "link"}

for kind, items in (("Link", reader.links), ("Button", reader.buttons)):
    for attrs, text in items:
        name = text or attrs.get("aria-label", "")
        if not name:
            problem(f"{kind} without a readable name: {attrs}")
        elif name.lower() in VAGUE:
            problem(f'{kind} named "{name}": say where it leads instead.')
    print(f"  {len(items)} {kind.lower()}s checked")

for tag in ("input", "select", "textarea"):
    for attrs in find(tag):
        if attrs.get("type") in ("hidden", "submit", "button"):
            continue
        if attrs.get("id") not in reader.label_targets and not attrs.get("aria-label"):
            problem(f"<{tag}> without a <label>: {attrs.get('name', attrs)}")

if find("form"):
    print("  A <form> was found. A static page cannot receive form data on its own:")
    print("  check where it is sent, and whether that service needs a privacy notice.")


# ---------------------------------------------------------------------------
# 6. EXTERNAL RESOURCES
# ---------------------------------------------------------------------------
# Everything loaded from another server makes the page depend on it, and
# tells that server who is visiting. http:// (without s) is blocked on most
# https pages anyway.

print("\n--- 6. External Resources ---")

# Links (<a href>) are only followed when clicked. These tags load at once.
loaded = [attrs.get("src") or attrs.get("href", "")
          for tag, attrs in reader.tags
          if tag in ("script", "link", "img", "iframe", "source", "video", "audio")]
loaded += re.findall(r'url\(\s*["\']?(https?://[^"\')]+)', html)
loaded = [address for address in loaded if address.startswith(("http://", "https://", "//"))]

if not loaded:
    ok("Nothing is loaded from other servers.")
for address in loaded:
    if address.startswith("http://"):
        problem(f"Insecure http:// address: {address}")
    elif any(hint in address for hint in THIRD_PARTY_HINTS):
        problem(f"Loaded from a third party (privacy!): {address}")
    else:
        print(f"  CHECK {address}")


# ---------------------------------------------------------------------------
# 7. COLOUR CONTRAST OF YOUR DESIGN TOKENS
# ---------------------------------------------------------------------------
# WCAG defines contrast as a ratio between two colours' relative luminance,
# from 1:1 (same colour) to 21:1 (black on white). Normal text needs at least
# 4.5:1, large text (about 24 px, or 19 px bold) and icons at least 3:1.

print("\n--- 7. Colour Contrast ---")


def relative_luminance(hex_colour):
    """How bright a colour looks to the human eye, from 0 (black) to 1 (white)."""
    hex_colour = hex_colour.lstrip("#")
    if len(hex_colour) == 3:
        hex_colour = "".join(c * 2 for c in hex_colour)
    channels = []
    for i in (0, 2, 4):
        c = int(hex_colour[i:i + 2], 16) / 255
        # Screens store colours "gamma encoded". Undo that to get real light.
        channels.append(c / 12.92 if c <= 0.04045 else ((c + 0.055) / 1.055) ** 2.4)
    red, green, blue = channels
    return 0.2126 * red + 0.7152 * green + 0.0722 * blue   # Eyes see green best


def contrast_ratio(colour_a, colour_b):
    lighter, darker = sorted(
        (relative_luminance(colour_a), relative_luminance(colour_b)), reverse=True)
    return (lighter + 0.05) / (darker + 0.05)


tokens = dict(re.findall(r"(--[\w-]+)\s*:\s*(#[0-9a-fA-F]{6}|#[0-9a-fA-F]{3})\b", html))

if not tokens:
    print("  No colour tokens like --color-text: #1c2321; found in the file.")
else:
    print("  Colour tokens found: " + ", ".join(tokens))

for text_token, bg_token in CONTRAST_PAIRS:
    if text_token not in tokens or bg_token not in tokens:
        print(f"  SKIP  {text_token} on {bg_token} (token not in this file)")
        continue
    ratio = contrast_ratio(tokens[text_token], tokens[bg_token])
    label = f"{text_token} on {bg_token}: {ratio:.2f}:1"
    if ratio >= 4.5:
        ok(label)
    elif ratio >= 3:
        problem(label + " (only enough for large text and icons)")
    else:
        problem(label + " (too low)")


# ---------------------------------------------------------------------------
# SUMMARY
# ---------------------------------------------------------------------------
# Passing this script does not make a page accessible: no automatic check
# can. Always test with the keyboard and on a real phone as well.

print("\n" + "=" * 40)
print(f"  {problems} thing(s) to fix" if problems else "  No problems found by this script")
print("=" * 40)
