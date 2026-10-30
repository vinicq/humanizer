# Humanizer

**English** · [Português (Brasil)](README.pt-BR.md)

An Agent Skill for writing, editing and reviewing English and Brazilian Portuguese so the text reads like a person wrote it for a reader. It removes the habits that make model output easy to spot, and it keeps the facts, the meaning, the technical terms and the author's voice intact.

> **Before** (raw model output)
> We're known for our used maritime history section—a good place to browse if your interests run to ships, seafaring, and life along the coast. [...] Stop in and spend some time among the shelves.
>
> **After**
> We're known for our used maritime history section. On Saturday mornings we hold a children's reading hour.

The skill does not detect authorship and does not promise to pass AI detectors. It edits for the reader.

Version 7.0.0 · by Vinicius Queiroz · MIT

## What's in the repository

| Path | What it does |
|---|---|
| `SKILL.md` | The skill. Scope, priorities, preservation rules R01-R12, the editing procedure and the final check. Loads on every run. |
| `references/` | Detail that loads only when the task needs it: `en/` (English catalog EN01-EN78, final pass, examples) and `pt-br/` (Portuguese catalog PT01-PT86, final pass, examples, in Portuguese), plus `voice-and-genres.md` and `sources.md`, shared by both languages. |
| `agents/humanizer-revisor.md` | Read-only reviewer subagent for Claude Code. It lists findings and does not edit. |
| `codex/humanizer-revisor.toml` | The same reviewer as a Codex custom agent. |
| `agents/openai.yaml` | How the skill appears in Codex. |
| `.claude-plugin/` | Claude Code plugin and marketplace manifests. |
| `plugins/codex/` | The Codex plugin: a generated copy of the skill. Do not edit it by hand. |
| `.agents/plugins/marketplace.json` | Codex marketplace manifest that points to `plugins/codex`. |
| `assets/icon.png` | Plugin icon. |
| `scripts/build-codex-plugin.py` | Generates `plugins/codex` from the repository root. |
| `scripts/check-wikipedia.py` | Tells you when the Wikipedia pages behind the catalogs have changed. |
| `wikipedia/` | Section-by-section extraction of those pages. Maintenance material; the skill does not read it. |
| `AGENTS.md` | Instructions for coding agents that edit this repository. |
| `CHANGELOG.md` · `LICENSE` | Version history and license. |

The skill and the reviewer split the work:

| | Skill `humanizer` | Subagent `humanizer-revisor` |
|---|---|---|
| Use it to | write or rewrite text | review text that already exists |
| Runs | in your conversation | in a separate context, without the writer's bias |
| Returns | the final text | findings: excerpt, pattern ID, problem, minimal fix, confidence |
| Edits files | when asked | never |

## Installation

`SKILL.md` sits at the repository root next to the references, so for Claude the repository is the skill folder. Codex reads a generated copy in `plugins/codex`.

All clone commands use HTTPS. SSH also works: `git@github.com:vinicq/humanizer.git`.

### Claude Code

As a plugin, with the skill and the reviewer:

```text
/plugin marketplace add vinicq/humanizer
/plugin install humanizer@humanizer
```

From a shell: `claude plugin marketplace add vinicq/humanizer` and `claude plugin install humanizer@humanizer`. The plugin skill is called `/humanizer:humanizer`.

To get the short name `/humanizer`, clone into your skills folder instead and copy the reviewer:

```bash
git clone https://github.com/vinicq/humanizer.git ~/.claude/skills/humanizer
cp ~/.claude/skills/humanizer/agents/humanizer-revisor.md ~/.claude/agents/
```

On Windows (PowerShell):

```powershell
git clone https://github.com/vinicq/humanizer.git "$HOME\.claude\skills\humanizer"
Copy-Item "$HOME\.claude\skills\humanizer\agents\humanizer-revisor.md" "$HOME\.claude\agents\"
```

Pick one method. With both, two `humanizer` skills show up.

### Claude desktop app and claude.ai

- **Code tab of the desktop app:** it reads the same `~/.claude` folder and the same user-scope plugins as the CLI, so the steps above already cover it. In the app you can also add the plugin from the `+` button next to the prompt box, under Add plugins.
- **Chat and Cowork (desktop app and claude.ai):** these take skills from your account, not from `~/.claude`. Build a ZIP whose root is a `humanizer/` folder, then upload it under **Customize > Skills** and switch it on:

```bash
git clone https://github.com/vinicq/humanizer.git && cd humanizer
git archive --format=zip --prefix=humanizer/ -o humanizer.zip HEAD
```

`git archive` honors the `export-ignore` lines in `.gitattributes`, so the ZIP leaves out the maintenance folders (`plugins/`, `codex/`, `scripts/`, `wikipedia/`, `assets/`, `.agents/`, `.claude-plugin/`) and holds only the skill. GitHub's "Download ZIP" button gives a folder named `humanizer-main`, which must be renamed to `humanizer` before you zip it again, so the `git archive` command is simpler.

Uploaded skills need code execution turned on. Team accounts have it by default; on Enterprise an owner has to enable code execution and Skills. The subagent does not apply here: chat has no subagents.

### Codex CLI

Install the plugin:

```bash
codex plugin marketplace add vinicq/humanizer
codex plugin add humanizer@humanizer
```

Start a new chat. The skill is `humanizer:humanizer`: ask for it by name, pick it from `/skills`, or just describe the task; Codex also picks it from the description. The plugin lives in `plugins/codex` and is generated from the repository root by `scripts/build-codex-plugin.py`, so edit the root files, never the generated copy.

The reviewer is a separate Codex custom agent. Copy its file from a clone:

```bash
git clone https://github.com/vinicq/humanizer.git ~/src/humanizer
mkdir -p ~/.codex/agents
cp ~/src/humanizer/codex/humanizer-revisor.toml ~/.codex/agents/
```

It is then available as the `humanizer-revisor` subagent.

**Manual alternative** (Codex without the plugin, and other agents that read `~/.agents/skills`): clone anywhere, for example `~/src/humanizer`, and link or copy **only** `plugins/codex/skills/humanizer` into `~/.agents/skills/humanizer`. Do not clone the whole repository into `~/.agents/skills`: Codex then finds the skill twice, at the root and in `plugins/codex`.

```bash
git clone https://github.com/vinicq/humanizer.git ~/src/humanizer
mkdir -p ~/.agents/skills ~/.codex/agents
ln -s ~/src/humanizer/plugins/codex/skills/humanizer ~/.agents/skills/humanizer
cp ~/src/humanizer/codex/humanizer-revisor.toml ~/.codex/agents/
```

On Windows (PowerShell), with a junction (no administrator rights needed):

```powershell
git clone https://github.com/vinicq/humanizer.git "$HOME\src\humanizer"
New-Item -ItemType Directory -Force "$HOME\.agents\skills", "$HOME\.codex\agents" | Out-Null
New-Item -ItemType Junction -Path "$HOME\.agents\skills\humanizer" -Target "$HOME\src\humanizer\plugins\codex\skills\humanizer"
Copy-Item "$HOME\src\humanizer\codex\humanizer-revisor.toml" "$HOME\.codex\agents\"
```

Use the plugin or the manual link, not both: with both, the skill shows up twice. To update, run `git pull` in the clone (the link follows it) or update the plugin.

### Codex app

The Codex app runs on the same Codex configuration as the CLI. Open the **Plugins** tab, find Humanizer, install it and start a new chat. The manual link above and the agent file in `~/.codex/agents/` cover the app too. Closing the window may leave the app running in the system tray with the old configuration; quit it from the tray if the skill does not show up.

### Other agents

Most agents that support Agent Skills read `~/.agents/skills`, so the manual link in the Codex section often covers them. Per agent, link or copy `plugins/codex/skills/humanizer` (not the repository root) into the skill folder:

| Agent | Skill folder (user / project) | Reviewer |
|---|---|---|
| OpenCode | `~/.config/opencode/skills/humanizer` · `.opencode/skills/humanizer` (also reads `~/.agents/skills` and `~/.claude/skills`) | Own agent format in `~/.config/opencode/agents/`; adapt the Markdown file |
| Cursor | `~/.cursor/skills/humanizer` · `.cursor/skills/humanizer` (also reads `~/.agents/skills` and `~/.claude/skills`) | Reads `agents/humanizer-revisor.md` as is from `~/.cursor/agents/` or `.claude/agents/` |
| GitHub Copilot in VS Code | `~/.copilot/skills/humanizer` · `.github/skills/humanizer` (also reads `~/.agents/skills` and `~/.claude/skills`) | Reads the Claude format from `~/.claude/agents/` or `.claude/agents/` |
| Gemini CLI | `gemini skills install https://github.com/vinicq/humanizer`, or `~/.gemini/skills/humanizer` | `~/.gemini/agents/`, own format |
| Antigravity | `.agents/skills/humanizer` in the project | - |
| Windsurf | `~/.codeium/windsurf/skills/humanizer` · `.windsurf/skills/humanizer` | - |

In the Gemini row, the `install` command takes the repository itself; the other rows use the link or copy of `plugins/codex/skills/humanizer`. These paths come from each vendor's documentation as of October 2026. If a client changes how it finds skills, its documentation wins.

### Without installing

Attach `SKILL.md` and the catalog for your language (`references/en/patterns.md` for English, `references/pt-br/padroes.md` for Portuguese) to the conversation, plus `references/en/final-pass.md` or `references/pt-br/revisao-final.md` for the final pass, and say:

```text
Use the attached files as your writing and review guide for this conversation.
SKILL.md is the core and wins over the catalog.
Keep facts, sources, technical terms, conditions, negations and degree of certainty.
Do not translate or summarize unless I ask. Return only the final version.
```

Open a new session after installing and check that the client lists `humanizer`. To update, run `git pull` in the clone (or reinstall the plugin).

## Usage

Call it by name:

```text
/humanizer

[paste the text]
```

Or ask in plain words:

```text
Use the humanizer skill on this release note. Keep the facts and the version numbers.
Revise this e-mail with the humanizer skill and return only the final version.
```

The skill works the same way on Brazilian Portuguese text; the [Portuguese README](README.pt-BR.md) shows it with Portuguese examples.

Point it at a file:

```text
/humanizer docs/proposal.md
```

Ask the reviewer when you want a second reading without edits:

```text
Ask humanizer-revisor to review docs/proposal.md.
Language: English. Genre: technical proposal. Reader: the steering committee.
Do not touch: the numbers in section 3 and the quotations.
```

It returns findings with the excerpt, the pattern (EN01-EN78, PT01-PT86 or R01-R12), the problem, a minimal fix and a confidence level. You decide what to apply. A good routine for an important text: write with the skill, review with the subagent, apply what makes sense.

### Match your voice

If you want the rewrite to sound like you, include a sample of your own writing:

```text
/humanizer

Here's a sample of my writing for voice matching:
[paste 2-3 paragraphs of your own writing]

Now humanize this text:
[paste the text to humanize]
```

The skill reads the sample for observable traits (sentence and paragraph length, punctuation, contractions, person, register, how you open and close, how you use lists) and writes the new text with them. It does not copy your typos, your opinions, your biography or any claim from the sample, and the sample never overrides the facts of the text being edited. With a sample under about 150 words the match is approximate, and the skill says so. Ask for a short voice note if you want to see which traits it used.

### Make it the default

Add this to your `CLAUDE.md`, `AGENTS.md` or equivalent:

```markdown
## Writing and review

For natural-language writing, apply the `humanizer` skill installed in this
environment. To review a finished text, use the `humanizer-revisor` subagent.
Keep facts, sources, meaning, technical terms, conditions, negations and
degree of certainty. Do not translate, summarize, invent evidence or change
requirements unless asked. For ordinary rewrites, return only the final version.
```

## How it works

Language models settle on the safe, frequent choice: the phrase that fits any topic, the three-item list, the upbeat close, the heading on every paragraph. Each choice is reasonable alone. Together they give text that says less than its length and sounds like nobody in particular. The fix is not to sprinkle "human" quirks on top; it is to say the specific thing the reader needs.

The skill runs in six steps:

1. **Set the task contract.** Language, genre, reader, format, length and limits. If you gave a voice sample, it is separated from the text to edit here.
2. **Mark what cannot change.** Quotations, code, commands, identifiers, URLs, numbers, dates, names and normative terms.
3. **Diagnose real problems** against the catalog for the text's language. A pattern is a reason to look, not an order to cut: a correct sentence stays.
4. **Write or revise** with the smallest change that fixes the problem.
5. **Review in two passes:** meaning first (nothing added, dropped or made more certain), then the language-specific pass in `references/pt-br/revisao-final.md` or `references/en/final-pass.md`.
6. **Deliver in the format asked**, usually just the final text.

Twelve rules (R01-R12) sit above the catalog. The main ones: no invented facts, experiences or sources (R02); quotations and code are protected (R03); no translation or summary unless asked; the register follows the genre and the author, not a fixed style (R07). When a rule and a pattern disagree, the rule wins. A clean text comes back almost untouched; see the pull request example below.

## The English catalog (78 patterns)

The English catalog is [`references/en/patterns.md`](references/en/patterns.md), with IDs EN01-EN78. It follows the English Wikipedia page [Signs of AI writing](https://en.wikipedia.org/wiki/Wikipedia:Signs_of_AI_writing) (S01), revision 1382823144, in page order, and the groups below use the page's own section names. Wikipedia is the source of truth for what counts as a sign. The page's historical, ineffective and human-writing sections are in the catalog so the skill does **not** act on them (EN47-EN61). EN62-EN78 are additions from other sources or editorial practice, marked as such in their **Sources** line. Each entry has the trigger, why it reads as AI, a fix, an exception and a **Sources** line that names the source and the page section. Signs that only make sense inside Wikipedia (wikitext, user pages, edit permissions) are listed at the end of the catalog as not applied.

Portuguese text uses its own catalog, built from the Portuguese Wikipedia: `references/pt-br/padroes.md` (PT01-PT86), listed in [README.pt-BR.md](README.pt-BR.md).

### Content

| ID | Pattern | Watch for |
|---|---|---|
| EN01 | Undue emphasis on significance, legacy, and broader trends | "a pivotal moment", "stands as a testament", "indelible mark" |
| EN02 | Emphasis on ecosystem and conservation (text about biology) | ecosystem or conservation role stressed when the status is unknown |
| EN03 | Canned emphasis on notability, attribution, and media coverage | "featured in leading outlets", a list of where the subject appeared |
| EN04 | Superficial analyses | a trailing -ing clause: "highlighting", "ensuring", "reflecting", "contributing to" |
| EN05 | Promotional and advertisement-like language | "boasts", "vibrant", "nestled", "in the heart of", "groundbreaking" |
| EN06 | Vague expression of connection or association | "in connection with", "associated with", "became associated with" with no link stated |
| EN07 | Vague attributions and overgeneralization of opinions | "industry reports", "experts argue", "several sources" when few are cited |
| EN08 | Outline-like conclusions about challenges and future prospects | "Despite these challenges...", "Future Outlook" closers |
| EN09 | "Awards and recognition" section | a section titled "Awards and recognition"; headings built as "X and Y" |

### Language and grammar

| ID | Pattern | Watch for |
|---|---|---|
| EN10 | High density of "AI vocabulary" words | "delve", "tapestry", "bolstered", "crucial" in high density |
| EN11 | Avoidance of basic copulatives ("is"/"are" phrases) | "serves as", "stands as", "boasts", "refers to" where "is" or "has" would do |
| EN12 | Negative parallelisms: Not just X, but also Y | "not only ... but also ...", "it's not just X, it's Y" |
| EN13 | Negative parallelisms: Not X, but Y | "it's not X, it's Y"; "no X, no Y, just Z" |
| EN14 | Negative parallelisms: Y rather than X | "Rather than X, Y"; "Y rather than X" closing a sentence |
| EN15 | Leads treating Wikipedia lists or broad article titles as proper nouns | an opening that defines the title as an object: "'X' refers to" |
| EN16 | Rule of three | three adjectives, phrases or nouns in a row: "tiles, metals, and plastics" |

### Style

| ID | Pattern | Watch for |
|---|---|---|
| EN17 | Title case | Title Case in section headings |
| EN18 | Overuse of boldface | bold on every occurrence of a chosen term |
| EN19 | Inline-header vertical lists | bullet, bold header, colon, text: "**Standard Rotary Saws**: ..." |
| EN20 | Heading errors | a heading that repeats the document title, skipped levels, a lone level 1 |
| EN21 | Emoji as formatting | emoji before headings and bullets |
| EN22 | Unusual use of tables | a small table that would fit in a sentence |
| EN23 | Curly quotation marks and apostrophes | curly quotation marks and apostrophes mixed with straight ones |

### Communication intended for the user

| ID | Pattern | Watch for |
|---|---|---|
| EN24 | Collaborative communication | "I hope this helps", "Certainly!", "You're absolutely right!", "let me know" |
| EN25 | Hedging disclaimers: didactic disclaimers (2023-24) | "it's important to note", "it is crucial to differentiate", "may vary" (2023-24) |
| EN26 | Hedging disclaimers: source availability (2024-25) | "specific details are limited", "in the provided search results" (2024-25) |
| EN27 | Hedging disclaimers: corrective framings (mid-2026-present) | "should be treated as... rather than...", "does not by itself establish" (mid-2026) |
| EN28 | Phrasal templates and placeholder text | "[Your Name]", "[Article Title 1]", unfilled template text |
| EN29 | Date placeholders | dates such as `2025-XX-XX` |
| EN30 | URL placeholders | `INSERT_SOURCE_URL_##`, `example.com` links, "[Year]" |

### Markup irregularities

| ID | Pattern | Watch for |
|---|---|---|
| EN31 | Markup irregularities | Markdown where it does not render, a code fence around the whole answer, leaked internal markers |

### Citations

| ID | Pattern | Watch for |
|---|---|---|
| EN32 | Broken external links | dead links that probably never existed |
| EN33 | Invalid DOI and ISBNs | a DOI that does not resolve, an ISBN with a wrong check digit |
| EN34 | DOIs that lead to unrelated articles | a valid DOI that opens a different article than the one cited |
| EN35 | Book citations without page numbers or URLs | a real book with no page, or a page that does not support the text |
| EN36 | Incorrect or unconventional use of references | `<sup>[3]</sup>` after every sentence, `↩` in footnotes, reference URLs built by position |
| EN37 | utm_source= | `utm_source=openai`, `utm_source=chatgpt.com` |

### Comment-specific indicators

| ID | Pattern | Watch for |
|---|---|---|
| EN38 | Comment-specific indicators | customer-service tone in comments: "I understand your concerns regarding..." |

### Edit summaries

| ID | Pattern | Watch for |
|---|---|---|
| EN39 | Edit summaries: general examples | first-person edit reports in AI vocabulary: "I revised the content to provide a neutral..." |
| EN40 | Edit summaries: canned assurance of adherence to Wikipedia policies and guidelines | "ensured that... adheres to", "in compliance with", "refined, enhanced" |
| EN41 | Edit summaries: specific mentions of "preserved" or "retained" information, "avoided" mistakes, and other procedural statements | "while preserving the original meaning", "avoided", "ensured" |
| EN42 | Edit summaries: overemphasis on presence/reliability of citations | "added sourced content", "improved attribution", "with independent sources" |

### Miscellaneous

| ID | Pattern | Watch for |
|---|---|---|
| EN43 | Pronounced shift in writing style | an abrupt change in one author's style, such as impeccable text beside error-filled comments |
| EN44 | "Submission statements" in AfC drafts | a note to the evaluator inside the document that defends its own quality |
| EN45 | Differences between LLMs | no text trigger: each model and version has its own idiolect |
| EN46 | Pro-authoritarian bias | no text trigger: pro-authoritarian bias in some answers |

### Signs of human writing

_Not problems to fix. These are signs that point to a human author; the skill does not edit for them._


| ID | Pattern | Watch for |
|---|---|---|
| EN47 | Age of text relative to ChatGPT launch | human sign: text written before November 30, 2022 |
| EN48 | Ability to explain one's own editorial choices | human sign: the author can explain how an error got in |
| EN49 | Syntax (constructions most common in human text) | human sign: simple "there is a", plain verbs (wrote, moved, used) |

### Ineffective indicators

_Listed so the skill does not act on them. Wikipedia says they do not distinguish AI text from human text._


| ID | Pattern | Watch for |
|---|---|---|
| EN50 | Perfect grammar | ineffective: correct grammar and spelling |
| EN51 | Combination of casual and formal registers, or language that sounds both "clinical" and "emotional" | ineffective: mixed registers in one text |
| EN52 | "Bland" or "robotic" prose | ineffective: "bland" or "robotic" prose |
| EN53 | "Fancy", "academic", or "formal" prose | ineffective: formal, academic or ornate prose |
| EN54 | Transition words (in isolation) | ineffective: "Additionally,", "Consequently," taken alone |
| EN55 | Unsourced content | ineffective: claims with no citation |

### Historical indicators

_Common in older models and much less frequent now. Listed from the Wikipedia page; the skill does not flag a text on one of these alone._


| ID | Pattern | Watch for |
|---|---|---|
| EN56 | Statements about knowledge cutoffs (2022–2023) | historical: "as of my last knowledge update" |
| EN57 | Section summaries | historical: "In summary", "In conclusion" closers |
| EN58 | Prompt refusal | historical: "as an AI language model", "I'm sorry" |
| EN59 | Overuse of em dashes (2022–September 2026) | historical: em dash overuse (2022 to September 2026) |
| EN60 | Abrupt cut offs | historical: text that stops midway |
| EN61 | Lexical diversity/elegant variation | historical: the same referent under changing names |

### Additions from other sources and editorial practice (no Wikipedia section)

| ID | Pattern | Watch for |
|---|---|---|
| EN62 | Causality and interpretation presented as fact | "the change caused the improvement" with only a sequence; "this proves" |
| EN63 | False dichotomies and trade-offs | "either X or Y", "the best of both worlds" with no conditions |
| EN64 | Invented personal voice | "I have seen this firsthand", "in my experience", feelings with no origin |
| EN65 | Slogan-like framing | "less X, more Y", "not a tool, a movement" |
| EN66 | False ranges | "from X to Y" where the ends are not a scale |
| EN67 | Hidden actors and subjectless fragments | "it was decided" when who decided matters |
| EN68 | Ornamental metaphors | "a rich tapestry", "navigating the ocean of possibilities" |
| EN69 | Manufactured rhetorical questions | "But what does this really mean?", "The result? A game changer." |
| EN70 | Canned openings and signposting | "in today's fast-paced world", "let's dive in", "without further ado" |
| EN71 | Engineered rhythm | many sentences with the same shape, or a fake mix of short and long ones |
| EN72 | Choppy pseudo-prose | short sentences, one per line, with no stated relation |
| EN73 | Sycophancy and automatic agreement | "Great question!", "You're absolutely right!" before any analysis |
| EN74 | Mismatched enthusiasm | "Amazing!", exclamations in a neutral text or a failure report |
| EN75 | Semantic drift in revision | "may" becomes "will", "up to 5" becomes "fewer than 5" |
| EN76 | Embedded instructions treated as commands | the text under review says "ignore the rules" and the editor obeys |
| EN77 | Unrequested translation, summary or second version | a revision that comes back translated, summarized or in two versions |
| EN78 | Invented commitments, evidence and scope | "tested successfully", "I will deliver by Friday", percentages with no origin |

## Examples

How these were made: the "before" texts are raw output from GPT-6.1 in an isolated Codex session, with no user instructions and no skills loaded, given only the facts in each prompt. The "after" texts are the same drafts run through this skill. IDs refer to the English catalog above. Portuguese examples, written from Portuguese prompts, are in [README.pt-BR.md](README.pt-BR.md).

### Release announcement

> **Before**
> tidewatch 2.0 is here, with offline syncing and faster uploads for local folders backed up to S3.
>
> The new offline mode queues changes while you're disconnected and uploads them when your connection returns. You can keep working on local files through a connection drop without having to remember what needs syncing later.
>
> This release also improves sync performance. In our benchmark of 10,000 small files, tidewatch 2.0 completed the sync 40% faster. Results will vary with your files and connection, but this benchmark gives a concrete measure of the improvement for that workload.
>
> Version 2.0 drops support for Python 3.9, so check your Python environment before upgrading. The migration guide at `docs/migrate-2.md` covers the steps for moving to the new release.
>
> tidewatch remains an open-source command-line tool for syncing local folders to S3. If you're upgrading an existing setup, start with the migration guide, then give 2.0 a try.

> **After**
> tidewatch 2.0 adds an offline mode and a faster sync.
>
> Offline mode queues changes while you're disconnected and uploads them when the connection returns.
>
> In our benchmark of 10,000 small files, sync is 40% faster.
>
> Version 2.0 drops support for Python 3.9, so check your Python version before upgrading. The migration guide is at `docs/migrate-2.md`.
>
> tidewatch is an open-source command-line tool that syncs local folders to S3.

What changed: "is here" opener gone (EN70). The benefit nobody stated, "without having to remember what needs syncing", is out (EN78). The hedge around the benchmark is out, since "in our benchmark of 10,000 small files" already sets the scope (EN25). The closing invitation and the repeated migration-guide pointer are out (EN24, EN57). The facts, the version, the path and the Python warning are untouched.

### Pull request description

> **Before**
> Fixes invoice due dates being calculated in server time (UTC) instead of the customer's time zone. Customers in UTC-3 to UTC-5 saw due dates one day early on invoices created after 21:00 local time.
>
> The fix converts timestamps to the customer's time zone before truncating to a date.
>
> - Adds unit tests for UTC-3, UTC-5, and UTC+9.
> - No database migration required.

**After:** unchanged. The draft states the bug, who was affected, the fix, the tests and the migration status, with nothing inflated. The skill leaves a clean text alone; editing it would only add risk.

### LinkedIn post, plain and with a voice sample

> **Before**
> Ledgerly reached 1,000 active users this October!
>
> We launched our budgeting app in March 2026. Seven months later, our team of three is celebrating a milestone that means a lot to us: 1,000 people actively using something we built.
>
> Thank you to everyone who has tried Ledgerly, shared feedback, or recommended it to someone else. You've helped us get here.
>
> Next up: CSV export, so you can take your budgeting data with you.
>
> We're excited to keep building.

> **After**
> Ledgerly, our budgeting app, now has 1,000 active users.
>
> We launched in March 2026 and reached the mark in October. The team is three people.
>
> Thanks to everyone who uses it. Next up is CSV export.

What changed: the exclamation mark and "We're excited to keep building" are out (EN74). "Means a lot to us" is a feeling the facts did not give (EN64). "Shared feedback, or recommended it" and "take your budgeting data with you" are actions and benefits that were never stated (EN78). "Seven months later" was build-up for a date already given (EN70).

With this voice sample:

```text
Shipped the importer fix today. Short version: the vendor changed date formats, we didn't
notice, invoices broke for two days. That's on us. Tests now cover the three formats we've
seen in the wild, and the parser fails loudly instead of guessing. If you hit something odd,
ping me directly. I'd rather hear about it twice than not at all.
```

> **After, in that voice**
> Ledgerly passed 1,000 active users in October. Short version: we launched in March 2026, there are three of us, and the next feature is CSV export. Thanks to everyone using it.

Traits taken: short declarative sentences, the "Short version:" lead, contractions, a flat tone with no hype. Not taken: "That's on us" and "ping me directly", which belong to the sample's own story and are not facts about Ledgerly.

### Team e-mail

> **Before**
> Subject: Reports module delivery moved to November 21
>
> Hi team,
>
> Delivery of the reports module is moving from November 14 to November 21. The vendor changed its API's date format without notice, so we need to adjust the importer and rerun the tests.
>
> The rest of the schedule remains unchanged. We'll review the tests at our meeting on Thursday at 10 a.m.
>
> Thanks,
> [Your name]

**After:** the same text. The skill flags `[Your name]` as placeholder text (EN28) for the author to fill in; it does not invent a name. The rest already states the change, the reason and the next step.

### Teaching paragraph

> **Before**
> A unit test checks whether a small piece of code, such as a single function, behaves as expected. For example, if a function applies a 10% discount to orders over $100, you could test that a $150 order becomes $135 and a $50 order stays $50. You should also check an order of exactly $100: because the discount applies only to orders over $100, the total should remain $100. Testing this boundary helps catch mistakes such as applying the discount to orders of $100 or more.

**After:** unchanged. The paragraph defines the term, gives one worked example with real numbers and explains why the boundary matters. There is nothing to cut, and rewording it would only put the arithmetic at risk.

### "About us" page

> **Before**
> # About us
>
> Harbor Street Books is an independent bookstore in Portland, Maine, founded by Ellen Park in 2004.
>
> We're known for our used maritime history section—a good place to browse if your interests run to ships, seafaring, and life along the coast. On Saturday mornings, our children's reading hour brings younger readers together for stories.
>
> Stop in and spend some time among the shelves. We're open Tuesday through Sunday, 10 a.m. to 6 p.m.

> **After**
> # About us
>
> Harbor Street Books is an independent bookstore in Portland, Maine, founded by Ellen Park in 2004.
>
> We're known for our used maritime history section. On Saturday mornings we hold a children's reading hour.
>
> We're open Tuesday through Sunday, 10 a.m. to 6 p.m.

What changed: "a good place to browse if your interests run to ships, seafaring, and life along the coast" is a sales line built on a list of three the facts never gave (EN05, EN16). "Brings younger readers together for stories" dressed up a plain fact (EN04). "Stop in and spend some time among the shelves" is a stock invitation (EN05). The em dash went with the clause it introduced, not because of the dash: on its own it is ordinary punctuation (EN59).

## Keeping up with Wikipedia

The Wikipedia guides on AI writing change often. In the revision of October 30, 2026, for example, both the English and the Portuguese pages list em dash overuse as a historical indicator, valid from 2022 to September 2026. Before each release, run:

```bash
python scripts/check-wikipedia.py
```

The script compares each page's current revision with the last recorded one (`wikipedia/revisions.json`), lists the sections that were added or removed, and prints the diff link. When a page changed, read the diff, update the extraction in `wikipedia/` and the catalogs, then run `python scripts/check-wikipedia.py --record`. A Wikipedia change is a prompt to review, not an automatic rule: it goes through the same priorities (R01-R12) as any other source.

## Limits

- The core sources were read between October 23 and 30, 2026. For anything that depends on current facts about models, detectors or tools, check again.
- The repository is checked for structure: frontmatter, R01-R12, EN01-EN78, PT01-PT86, links between the core and the references, and the plugin manifest (`claude plugin validate .`). That is not a benchmark of writing quality.
## Contributing

Rules live in `SKILL.md` and `references/`; installation and usage live in the READMEs. [`AGENTS.md`](AGENTS.md) lists the repository conventions. A sign that Wikipedia documents goes into the catalog of its language, in the page's order; an addition from another source goes in the last section of that catalog with the source named. To propose a pattern, describe the observable problem, the intervention, the exception and a test case, and name the primary source if there is one. Keep personal preference apart from research findings.

## Sources

The patterns rest on primary sources only: Wikipedia editorial guides, academic research, research institutes, vendor documentation and a style guide. The main ones:

- [Wikipedia: Signs of AI writing](https://en.wikipedia.org/wiki/Wikipedia:Signs_of_AI_writing), maintained by WikiProject AI Cleanup
- [Wikipédia: Sinais de texto gerado por inteligência artificial](https://pt.wikipedia.org/wiki/Wikip%C3%A9dia:Sinais_de_texto_gerado_por_intelig%C3%AAncia_artificial) and [Wikipédia: Grandes modelos de linguagem](https://pt.wikipedia.org/wiki/Wikip%C3%A9dia:Grandes_modelos_de_linguagem)
- Rodrigues, Sturm and Pinheiro, *A linguistic comparison between human- and AI-generated content*, iScience, 2026
- Kobak et al., *Delving into LLM-assisted writing in biomedical publications through excess vocabulary*, Science Advances, 2025
- Liang et al., *GPT detectors are biased against non-native English writers*, Patterns, 2023

The full list, with the patterns each source supports, is in the appendix below. How each source is used, and its limits, is in [`references/sources.md`](references/sources.md) under the same ID.

## Version history

See [CHANGELOG.md](CHANGELOG.md).

- **7.0.0** (2026-10-30): first public release. Skill at the repository root; two catalogs with independent numbering, each following its own Wikipedia page (EN01-EN78 and PT01-PT86), with sources per pattern; the em dash is no longer banned, since Wikipedia lists it only as a historical indicator; Codex plugin in `plugins/codex`; plugin icon; voice matching; reviewer subagent for Claude Code and Codex; Wikipedia revision check.

## License

MIT, by Vinicius Queiroz (2026). Parts of this package derive from work published under the same license by Siqi Chen (2025); [LICENSE](LICENSE) keeps both notices, as the license requires. Cited sources keep their own licenses.

## Appendix: research and guides behind the patterns

**Core** sources support the catalog or its current cautions. **Under review** means the record (title, authors, date, identifier) was checked on 2026-10-30 but the content has not entered the catalog yet. No source becomes a rule on its own; each goes through the core priorities.

The **Patterns and rules** column shows what each source supports. The reverse lookup is in the catalog: every pattern in `references/en/patterns.md` and `references/pt-br/padroes.md` ends with a **Sources** (or **Fontes**) line giving the ID and the page section. In this README the column lists EN IDs; the Portuguese README lists PT IDs. Fifteen English patterns (EN62, EN63, EN64, EN66, EN67, EN68, EN69, EN70, EN71, EN73, EN74, EN75, EN76, EN77, EN78) are editorial additions with no external source recorded. A source with Portuguese entries only shows "Portuguese catalog only". Wikipedia pages count at the revision shown; the maintenance script tells you when it changes.

### Wikipedia editorial guides

| ID | Source | Status | Patterns and rules |
|---|---|---|---|
| S01 | [Wikipedia: Signs of AI writing](https://en.wikipedia.org/wiki/Wikipedia:Signs_of_AI_writing), WikiProject AI Cleanup (revision 1382823144, 2026-10-30) | core | EN01, EN02, EN03, EN04, EN05, EN06, EN07, EN08, EN09, EN10, EN11, EN12, EN13, EN14, EN15, EN16, EN17, EN18, EN19, EN20, EN21, EN22, EN23, EN24, EN25, EN26, EN27, EN28, EN29, EN30, EN31, EN32, EN33, EN34, EN35, EN36, EN37, EN38, EN39, EN40, EN41, EN42, EN43, EN44, EN45, EN46, EN47, EN48, EN49, EN50, EN51, EN52, EN53, EN54, EN55, EN56, EN57, EN58, EN59, EN60, EN61 |
| S02 | [Wikipédia: Sinais de texto gerado por inteligência artificial](https://pt.wikipedia.org/wiki/Wikip%C3%A9dia:Sinais_de_texto_gerado_por_intelig%C3%AAncia_artificial) (revision 73274816, 2026-10-23) | core | Portuguese catalog only |
| S03 | [Wikipédia: Grandes modelos de linguagem](https://pt.wikipedia.org/wiki/Wikip%C3%A9dia:Grandes_modelos_de_linguagem) (revision 73268669, 2026-10-22) | core | Portuguese catalog only |

These are editorial observation guides, not policy and not authorship tests. Both pages keep sections of historical indicators and of indicators that do not work.

### Academic research

| ID | Work | Status | Patterns and rules |
|---|---|---|---|
| S04 | Rodrigues, Sturm and Pinheiro. A linguistic comparison between human- and AI-generated content. iScience, 2026. [DOI 10.1016/j.isci.2026.114976](https://doi.org/10.1016/j.isci.2026.114976), [PubMed 41809036](https://pubmed.ncbi.nlm.nih.gov/41809036/) | core | EN08, EN09, EN53 |
| S05 | Geng and Trotta. Human-LLM Coevolution: Evidence from Academic Writing. Findings of ACL, 2025. [ACL Anthology](https://aclanthology.org/2025.findings-acl.657/) | core | EN10 |
| S06 | Kobak et al. Delving into LLM-assisted writing in biomedical publications through excess vocabulary. Science Advances, 2025. [arXiv 2406.07016](https://arxiv.org/abs/2406.07016) | core | EN10 |
| S07 | Juzek and Ward. Why Does ChatGPT "Delve" So Much? Exploring the Sources of Lexical Overrepresentation in Large Language Models. COLING, 2025. [arXiv 2412.11385](https://arxiv.org/abs/2412.11385) | under review | none yet |
| S08 | Liang et al. GPT detectors are biased against non-native English writers. Patterns, 2023. [arXiv 2304.02819](https://arxiv.org/abs/2304.02819) | core | R08 |
| S09 | Basani et al. Diversity Boosts AI-Generated Text Detection, 2025. [arXiv 2509.18880](https://arxiv.org/abs/2509.18880) | core | R08 |
| S10 | Russell et al. StoryScope: Investigating idiosyncrasies in AI fiction, 2026. [arXiv 2604.03136](https://arxiv.org/abs/2604.03136) | under review | none yet |
| S11 | Guo et al. How Close is ChatGPT to Human Experts? Comparison Corpus, Evaluation, and Detection, 2023. [arXiv 2301.07597](https://arxiv.org/abs/2301.07597) | under review | none yet |
| S12 | Paech et al. Antislop: A Comprehensive Framework for Identifying and Eliminating Repetitive Patterns in Language Models, 2025. [arXiv 2510.15061](https://arxiv.org/abs/2510.15061) | under review | none yet |
| S13 | Xu et al. Base Models Look Human To AI Detectors, 2026. [arXiv 2605.19516](https://arxiv.org/abs/2605.19516) | under review | none yet |
| S14 | Cheng et al. Adversarial Paraphrasing: A Universal Attack for Humanizing AI-Generated Text, 2025. [arXiv 2506.07001](https://arxiv.org/abs/2506.07001). Recorded to mark the scope: the skill does not adopt evasion techniques | under review | none yet |
| S15 | Bitton et al. Detecting Stylistic Fingerprints of Large Language Models, 2025. [arXiv 2503.01659](https://arxiv.org/abs/2503.01659) | under review | none yet |
| S16 | Wu et al. A Survey on LLM-Generated Text Detection: Necessity, Methods, and Future Directions, 2023. [arXiv 2310.14724](https://arxiv.org/abs/2310.14724) | under review | none yet |
| S17 | Mitchell et al. DetectGPT: Zero-Shot Machine-Generated Text Detection using Probability Curvature, 2023. [arXiv 2301.11305](https://arxiv.org/abs/2301.11305) | under review | none yet |
| S18 | Hans et al. Spotting LLMs With Binoculars: Zero-Shot Detection of Machine-Generated Text, 2024. [arXiv 2401.12070](https://arxiv.org/abs/2401.12070) | under review | none yet |
| S19 | Verma et al. Ghostbuster: Detecting Text Ghostwritten by Large Language Models, 2023. [arXiv 2305.15047](https://arxiv.org/abs/2305.15047) | under review | none yet |
| S20 | Dugan et al. RAID: A Shared Benchmark for Robust Evaluation of Machine-Generated Text Detectors, 2024. [arXiv 2405.07940](https://arxiv.org/abs/2405.07940) | under review | none yet |

### Research institutes and companies

| ID | Work | Status | Patterns and rules |
|---|---|---|---|
| S21 | Graphite. [AI Tells](https://graphite.io/five-percent/research/ai-tells), 2026-09-16, and [AI Tells: Opus 5.5 Update](https://graphite.io/five-percent/research/ai-tells-opus-5-5-update), 2026-10-01 | core | EN05, EN12, EN13, EN14, EN45, EN54, EN65 |
| S22 | Pew Research Center. [How Much of the Internet Is Written With AI?](https://www.pewresearch.org/data-labs/2026/08/20/how-much-of-the-internet-is-written-with-ai/), 2026-08-20 | core | none yet |

### Vendor documentation and style guide

| ID | Work | Status | Patterns and rules |
|---|---|---|---|
| S23 | Anthropic. [Prompting Claude Fable 5.1](https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/prompting-claude-fable-5-1), sections Writing density and Formatting in chat | core | EN19, EN72, R10 |
| S24 | Google developer documentation style guide. [Hyphens](https://developers.google.com/style/hyphens) | core | EN59, R09 |
