# Wikipedia: Signs of AI writing (en)

## Identification

| Field | Value |
|---|---|
| Page | https://en.wikipedia.org/wiki/Wikipedia:Signs_of_AI_writing |
| Revision (revid) | 1382823144 |
| Revision date | 2026-10-30T14:02:48Z |
| Page shortcuts | WP:AISIGNS, WP:AITELLS, WP:LLMSIGNS |
| Maintainer | WikiProject AI Cleanup (project advice page, protected: `pp-protected`) |
| Language of the patterns | en (the page warns that it is a guide "on Wikipedia" and that some signs may not hold outside it) |
| Type | list (descriptive field guide, with real examples from articles, drafts, comments and edit summaries) |
| License | not declared in the wikitext; Wikipedia text follows the site's standard license (CC BY-SA 4.0). Inference: not confirmed in the file read |
| Files read | raw wikitext of the revision above, whole (1,688 lines), read in parts |
| Catalog IDs | The **Catalog:** labels below use the old P01-P50 numbering. The mapping to EN01-EN78 is the table at the end of `references/en/patterns.md`. |
| Files skipped and why | none; the references were read only to see who supports each claim. Cited subpages (`/Markup`, `Signs of AI use in comments`, `Canned user pages`, `/Examples/*`) were not read because they are not in the input file |

Notes on the revision:

- The page declares itself "descriptive, not prescriptive; it consists of observations, not rules" and asks: "Please do not merely treat these signs as the problems to be fixed; that could just make detection harder."
- It points to a section "§ Sudden shift in English variety use" (under "Perfect grammar") that does not exist in this revision. Only "Pronounced shift in writing style" exists.
- This revision has no section on false ranges ("from X to Y"), neither as a current sign nor as a historical one.
- A hidden comment in the vocabulary table says a word is only added if its overuse is "corroborated by at least one reliable, non-pop-science external source, and is seen on Wikipedia often too". It is an editorial rule of the page, recorded here as data.

## How the page organizes the patterns

- Axis: where the sign appears. Top-level sections: Caveats, Content, Language and grammar, Style, Communication intended for the user, Markup irregularities, Citations, Comment-specific indicators, Edit summaries, Miscellaneous, Signs of human writing, Ineffective indicators, Historical indicators.
- There is no numbered severity. Strength comes from the text: "one of the strongest tells" (vocabulary in quantity), "unambiguous indicator" (internal citation markup, Markdown code block), "strong indicator" (pre-declined AfC template), "near-definitively proves" (`utm_source`), "not a strong tell" (isolated connectives), "less reliable" (the 2026 "should not be confused").
- Dating: several signs come with an era or model (vocabulary lists by era, notices from 2023-24, 2024-25 and mid-2026-present, a whole "Historical indicators" section with an approximate period).
- The page's own overview: "As of October 2026, the most common signs of newly AI-generated text on Wikipedia (besides the unambiguous indicators above) are Markdown presence, AI edit summaries, hedging disclaimers about source availability and usage, vague expression of connection or association, and canned emphasis on source attribution and media coverage."
- Underlying thesis (Content section): the model "tends to regress to the mean", swaps specific, rare facts for generic, positive descriptions, and RLHF pulls the output toward "the most broadly palatable prose". "The subject becomes simultaneously less specific and more exaggerated."
- In this extract: 70 blocks. The two requested fields were added to each block: **Status on page** (current, historical, ineffective or human sign/NAO) and **Catalog** (the P01-P50 of `references/patterns.md`, checked against the text of each P; "new" when no P covers it; "not applicable" when the pattern only exists on Wikipedia). The "Humanizer 6.2" field of the template was merged into the Catalog field.
- Wikipedia-specific blocks (wiki markup, citations, DOI, edit summaries, AfC, user pages, permissions) stayed short, with Category GEN and the note "Wikipedia-specific".

## Extracted patterns

### 1. Undue emphasis on significance, legacy, and broader trends

- **Category:** CONT
- **Language:** en
- **Status on page:** current. The page adds: "As of mid-2026, LLMs frequently include these alongside hedging disclaimers, editorializing about how a particular distinction or nuance is important."
- **Signal on page:** not classified; "a distinct and easily identifiable repertoire".
- **What it is:** the text inflates the importance of the subject by saying that arbitrary aspects represent or contribute to a larger theme. It includes placing the subject in "debates" or "public discussions", and it shows up even in etymology or population data. Sometimes it comes with a preamble that admits the low importance and then talks about it anyway.
- **Why it sounds like AI:** regression to the mean described in the Content section: rare facts become generic, positive description.
- **Literal triggers:** stands/serves as; is a testament/reminder; a crucial/pivotal/vital/significant/key role/moment; underscores/highlights its importance/significance; reflects broader; symbolizing its ongoing/enduring/lasting; contributing to the; setting the stage for; marking/shaping the; represents/marks a shift; key turning point; evolving landscape; focal point; indelible mark; deeply rooted; distinction [matters/is important] because. In the examples: "marking a pivotal moment", "represented a significant shift", "was part of a broader movement", "solidify its role as a regional hub", "generated debate", "shaped emerging policy discussions", "prompted broader reflection", "raising philosophical questions", "This etymology highlights the enduring legacy", "the transformative power", "Though it saw only limited application", "contributes to the broader history".
- **Bad example → fixed:** "The Statistical Institute of Catalonia was officially established in 1989, marking a pivotal moment in the evolution of regional statistics in Spain." The page gives no corrected version.
- **What to avoid / how to fix:** the page does not prescribe; it points to the policies (puffery).
- **Exceptions / when not to act:** nothing specific in this section.
- **Catalog:** P01 (covers). The trigger "distinction [matters/is important] because" falls under P24 (announced authority and importance). The low-importance preamble is in no P.
- **Source:** Content > Undue emphasis on significance, legacy, and broader trends (WP:AILEGACY, WP:AITREND).

### 1.1. Emphasis on ecosystem and conservation (text about biology)

- **Category:** CONT
- **Language:** en
- **Status on page:** current (subcase of section 1)
- **Signal on page:** not classified
- **What it is:** when writing about an animal or plant species, the model exaggerates links to the ecosystem and insists on conservation status and preservation efforts "even if the status is unknown and no serious efforts exist".
- **Why it sounds like AI:** same regression to the mean.
- **Literal triggers:** "there is no specific conservation assessment"; "crucial for the survival of this and other endemic species"; "could potentially impact their populations"; "plays a role in the ecosystem"; "contributes to Hawaii's rich cultural heritage"; "Preserving this endemic species is vital".
- **Bad example → fixed:** "It plays a role in the ecosystem and contributes to Hawaii's rich cultural heritage." No corrected version.
- **What to avoid / how to fix:** does not prescribe.
- **Exceptions / when not to act:** nothing.
- **Catalog:** P01 partly covers (inflated importance); missing is the case of invented content to fill the section (close to P50 and rule R02, with no trigger of its own).
- **Source:** Content > Undue emphasis..., paragraph on biology.

### 2. Canned emphasis on notability, attribution, and media coverage

- **Category:** CONT
- **Language:** en
- **Status on page:** current; one of the five most common signs in October 2026. "This is more common in text from AI tools released in 2025 or later."
- **Signal on page:** not classified; described as "narrow and distinct".
- **What it is:** the text proves notability by listing where the subject appeared and what kind of source it is (trade publications, regional media), instead of summarizing what the sources say. It often attributes the model's own superficial analysis to the source. It echoes the vocabulary of Wikipedia's guidelines ("independent coverage").
- **Why it sounds like AI:** "as if the LLM has collapsed the context between the edit and its justification". The difference from a human press release is the phrasing and the focus on the characteristics of the sources themselves.
- **Literal triggers:** independent coverage; local/regional/national/[country name] media outlets; music/business/tech outlets; trade publications; cited/featured/profiled in; written by a leading expert; active social media presence; was identified by. In the examples: "featured in", "other prominent media outlets", "documented in archived school event programs and regional press coverage", "maintains a strong digital presence", "has also been mentioned in ABC News coverage relating to", "profiled in multiple high-quality, independent, and widely-read outlets", "significant, substantial, secondary coverage", "Repeated national media coverage", "highlighted by multiple independent reports", "significant, sustained, and verifiable coverage". "maintain an active social media presence" is "particularly idiosyncratic to AI text and relatively uncommon on Wikipedia before ~2024".
- **Bad example → fixed:** "Her insights have also been featured in *Wired*, *Refinery29*, and other prominent media outlets." No corrected version. In one of the examples, "the reference added for this sentence did not exist".
- **What to avoid / how to fix:** does not prescribe; points to "In-text attribution".
- **Exceptions / when not to act:** human press releases also cite press clippings "for decades"; the sign is the phrasing and the focus on the sources.
- **Catalog:** P03 (covers the mechanism); the triggers "independent coverage", "active social media presence" and "trade publications" are missing. Attributing own analysis to the source falls under P05 and P44.
- **Source:** Content > Canned emphasis on notability, attribution, and media coverage (WP:OVERATTRIBUTION, WP:AIATTR).

### 3. Superficial analyses

- **Category:** SIN
- **Language:** en
- **Status on page:** current (examples from 2023 to July 2026)
- **Signal on page:** not classified
- **What it is:** superficial analysis attached to information, tied to meaning, recognition or impact, almost always with a present participle (-ing) clause at the end of the sentence, sometimes with vague attribution. Chatbots with search (RAG) now hang the analysis on a named source ("Roger Ebert highlighted the lasting influence") "regardless of whether those sources say anything close".
- **Why it sounds like AI:** for Wikipedia it is synthesis or unattributed opinion (cites Reinhart et al., PNAS 2025).
- **Literal triggers:** highlighting/underscoring/emphasizing ...; ensuring ...; reflecting/symbolizing ...; contributing to ...; cultivating/fostering ...; encompassing ...; enhancing ...; valuable insights; align/resonate with. In the examples: "creating a lively community within its borders", "further enhancing its significance as a dynamic hub of activity and culture", "facilitating the movement of passengers and goods", "contributing to the socio-economic development of the region", "reflecting its continued relevance", "embodying the spirit of unity", "creating a space where the past and present come together", "demonstrating the ongoing relevance", "confirming its relevance in modern research".
- **Bad example → fixed:** "As of the April 2008 census, the population of Douera stood at approximately 56,998 inhabitants, creating a lively community within its borders." No corrected version. A July 2026 example shows the chatbot offering three paraphrases ("Recommended", "More formal", "Closer to the original"), all with the -ing tail.
- **What to avoid / how to fix:** does not prescribe.
- **Exceptions / when not to act:** nothing.
- **Catalog:** P20 (covers). The form with a named source that does not say that falls under P44 and P05.
- **Source:** Content > Superficial analyses (WP:SUPERFICIAL).

### 4. Promotional and advertisement-like language

- **Category:** LEX
- **Language:** en
- **Status on page:** current
- **Signal on page:** not classified. "LLMs have serious problems keeping a neutral tone."
- **What it is:** even when asked for an encyclopedic style, the output pulls toward advertising or a travel guide, also in rewrites (an edit summary that says "removed promotional tone" while introducing the tone). Subtypes: cultural heritage (keeps reminding of importance) and people or companies (press-release tone).
- **Why it sounds like AI:** "LLMs tend to over-use the same set of promotional phrases no matter what the topic."
- **Literal triggers:** boasts a; vibrant; rich; profound; enhancing; showcasing; exemplifies; commitment to; natural beauty; nestled; in the heart of; groundbreaking; renowned; featuring; diverse array. In the examples: "Nestled within the breathtaking region", "stands as a vibrant town with a rich cultural heritage", "From its scenic landscapes to its historical landmarks", "offers visitors a fascinating glimpse into the diverse tapestry", "a town worth visiting", "celebrated for its resilience, cultural richness, and natural beauty", "made remarkable strides", "offers a dynamic blend of tradition and progress that continues to inspire the world", "acts as the gateway", "dependable, value-driven experiences", "align with KQ's goals", "emphasized the airline's commitment to sustainability", "communicates a powerful emotional presence", "imparts a sense of refined dynamism", "showcasing the brand's dedication to craftsmanship and historical reverence".
- **Bad example → fixed:** "TTDC acts as the gateway to Tamil Nadu's diverse attractions, seamlessly connecting the beginning and end of every traveller's journey." No corrected version.
- **What to avoid / how to fix:** points to "Words to watch#Puffery".
- **Exceptions / when not to act:** "Not all promotional or spammy writing is AI-generated." Era: "older LLMs (e.g., GPT-4) tend to output more blatantly positive text than newer LLMs, which are more subtly positive and tend to avoid obviously superlative statements like 'the best.'"
- **Catalog:** P02 (covers). The era note weakens the explicit superlative as a current sign (see Changes).
- **Source:** Content > Promotional and advertisement-like language (WP:AIPUFFERY, WP:AIPEACOCK).

### 5. Vague expression of connection or association

- **Category:** CONT
- **Language:** en
- **Status on page:** current; one of the five most common signs in October 2026 (examples from March 2025 to August 2026).
- **Signal on page:** not classified
- **What it is:** instead of stating the relationship ("In 2017, John Doe was the CEO of ExampleCorp"), the text says the two are "connected to" or "associated with" ("sources identified John Doe as being associated with leadership of ExampleCorp"). It combines with promotional language and AI vocabulary ("particularly/widely associated"), sometimes iteratively.
- **Why it sounds like AI:** the page gives no explanation beyond the description.
- **Literal triggers:** in connection with/to ...; connected with/to; in association with ...; associated with. In the examples: "has been associated with", "is associated with", "became associated with", "associated principally with", "Contemporary material associated with the ensemble".
- **Bad example → fixed:** the page itself gives the pair: "Professor Jane Doe taught science at Example University" (direct) against "Professor Jane Doe was connected with science education at Example University" (AI form).
- **What to avoid / how to fix:** implicit: state the concrete relationship.
- **Exceptions / when not to act:** nothing.
- **Catalog:** P04 partly covers (vague relationships, asks to identify the relationship and mechanism); the triggers "associated with" and "in connection with" and the example pair are missing.
- **Source:** Content > Vague expression of connection or association (WP:AICONNECT, WP:AIASSOCIATION).

### 6. Vague attributions and overgeneralization of opinions

- **Category:** CONT
- **Language:** en
- **Status on page:** current
- **Signal on page:** not classified
- **What it is:** opinion attributed to a vague authority (weasel wording) and exaggeration of the number of sources: one or two sources become a broad view; "reviewers" or "scholars" in the plural with one person cited; example lists presented as non-exhaustive without basis.
- **Why it sounds like AI:** no explanation beyond the description.
- **Literal triggers:** Industry reports; Observers have cited; Experts argue; Some critics argue; several sources/publications (when only few sources are cited); such as (before exhaustive word lists). In the examples: "researchers and conservationists", "according to Indian sources,", "described in scholarship", "modern researchers treat", "Toy industry publications such as".
- **Bad example → fixed:** "Toy industry publications such as The Toy Insider and Mojo Nation have presented Rubik's WOWCube as a STEM-oriented platform" (the two named were the only ones). No corrected version.
- **What to avoid / how to fix:** points to "Unsupported attributions".
- **Exceptions / when not to act:** nothing.
- **Catalog:** P05 (covers vague attribution). "Such as" before a list that is exhaustive and the inflated plural sit between P05 and P07; no P cites these two triggers.
- **Source:** Content > Vague attributions and overgeneralization of opinions (WP:AIWEASEL).

### 7. Outline-like conclusions about challenges and future prospects

- **Category:** EST
- **Language:** en
- **Status on page:** current (examples from 2023 to July 2026)
- **Signal on page:** not classified
- **What it is:** a "Challenges" section that opens with "Despite its [positive words], [subject] faces challenges..." and closes with a vaguely positive assessment or speculation about future initiatives, at the end of a rigid-skeleton article, sometimes with a separate "Future Prospects" section.
- **Why it sounds like AI:** rigid formula.
- **Literal triggers:** Despite its... faces several challenges...; Despite these challenges; Challenges and Legacy; Future Outlook. In the examples: "Challenges and Future Directions", "faces new challenges and opportunities", "adapt to these emerging trends", "This section would speculate on potential developments", "continues to thrive", "embodying the synergy", "continue to provide a vital service", "positions them as critical components", "SCE continues to evolve in response to these challenges.", "main contemporary challenge", "for the coming decades".
- **Bad example → fixed:** "Despite its success, the Panama Canal faces challenges, including[...] Future investments in technology [...] could enhance the canal's efficiency and maintain its relevance in global trade." No corrected version.
- **What to avoid / how to fix:** does not prescribe.
- **Exceptions / when not to act:** "This sign is about the rigid formula, not simply the mention of challenges or challenging."
- **Catalog:** P09 (mandatory optimism and future) and P28 (structure by habit; P28 itself cites "overview, benefits, challenges, future outlook").
- **Source:** Content > Outline-like conclusions about challenges and future prospects (WP:FACESCHALLENGES).

### 8. "Awards and recognition" section

- **Category:** EST
- **Language:** en
- **Status on page:** current
- **Signal on page:** "nearly ubiquitous in AI generated articles", more common than in human articles flagged as promotional.
- **What it is:** headings in the form "X and Y" and, especially, the "Awards and recognition" section (or just "Recognition").
- **Why it sounds like AI:** it combines the focus on legacy (block 1) and the allusion to "coverage" and "recognition" (block 2).
- **Literal triggers:** "Awards and recognition"; "Recognition"; headings "<var>X</var> and <var>Y</var>".
- **Bad example → fixed:** none in this section (it appears in block 27, in a template with "Awards and Recognition").
- **What to avoid / how to fix:** does not prescribe.
- **Exceptions / when not to act:** "common in (but not exclusive to)" AI text; humans also write legacy sections.
- **Catalog:** partly covers: P28 (section applied by habit) and P03 (decorative prestige); the "X and Y" heading is in no P.
- **Source:** Content > "Awards and recognition" section.

### 9. High density of "AI vocabulary" words

- **Category:** LEX
- **Language:** en
- **Status on page:** current, with lists by era (see "Vocabulary lists"); the list itself changes over time ("delve" dropped in 2025).
- **Signal on page:** "One or two of these words appearing in an edit may be coincidental, but an edit (post-2022) introducing lots of them, lots of times, is one of the strongest tells for AI use."
- **What it is:** words that models have used much more than people since 2022, and that appear together ("where there is one, there are likely others"). It also applies to LLM-generated encyclopedias, such as Grokipedia.
- **Why it sounds like AI:** cited studies (Juzek and Ward 2025; Kobak et al. 2025; Kousha and Thelwall 2025; Geng and Trotta 2025; Russell et al. 2025; Reinhart et al. 2025; Kriss, NYT 2025; The Economist, Jul. 2026).
- **Literal triggers:** see "Vocabulary lists", copied in full.
- **Bad example → fixed:** "Somali cuisine is an intricate and diverse fusion of a multitude of culinary influences, drawing from the rich tapestry of Arab, Indian, and Italian flavours. This culinary tapestry is a direct result of Somalia's longstanding heritage of vibrant trade and bustling commerce." No corrected version.
- **What to avoid / how to fix:** "This section is to be taken as literally as possible: a word being overused by AI does not imply that its synonyms are also overused."
- **Exceptions / when not to act:** context: "underscore" can be the literal underline or incidental music. Distribution varies by chatbot.
- **Catalog:** P11 (covers the mechanism and says a frequent word is a reason to assess, not an order to swap). The list in `references/en/final-pass.md` has no dating by era and lacks most of the GPT-5 and GPT-6 words (see Changes).
- **Source:** Language and grammar > High density of "AI vocabulary" words (WP:AIVOCAB, WP:AIWORDS).

### 10. Avoidance of basic copulatives ("is"/"are" phrases)

- **Category:** LEX
- **Language:** en
- **Status on page:** current. "Sometimes, especially in more recent AI output, these constructions are more elaborate."
- **Signal on page:** not classified; observed in GPT and Gemini models.
- **What it is:** swapping "is/are" and "has" for "serves as a", "mark the", "features", "offers". The recent form ties in with the vague association of block 5: "ventured into politics as a candidate" in place of "was a candidate", "began his career as" in place of "was". In opening sentences, "refers to" as if the article were about the term. Appears a lot in AI text revisions ("improve").
- **Why it sounds like AI:** a drop of more than 10% in "is" and "are" in 2023 academic writing (Geng and Trotta); a similar drop on Wikipedia (Huang et al.); GPT-3.5 reduced "is/are" when revising 10,000 abstracts.
- **Literal triggers:** serves as/stands as/marks/functions as/operates as/represents [a]; boasts/features/maintains/offers [a]; refers to; "holds the distinction of being"; "ventured into politics as a candidate"; "began his career as".
- **Bad example → fixed:** the page gives the pair (human → AI): "Gallery 825 on La Cienega Boulevard [...] is LAAA's exhibition arm for contemporary art. There are four individual gallery spaces" → "Gallery 825 on La Cienega Boulevard serves as LAAA's exhibition space for contemporary art. The gallery features four separate spaces". The direction of correction is the reverse: the human version is the first.
- **What to avoid / how to fix:** implicit: use "is" and "has".
- **Exceptions / when not to act:** "Do not confuse this with has used in the present perfect form, as in has been featured." Opening paragraphs follow the "[subject] is..." format and skew the count.
- **Catalog:** P13 (covers); missing are "maintains", "operates as", "refers to" in openings, "holds the distinction of being" and the recent long forms.
- **Source:** Language and grammar > Avoidance of basic copulatives (WP:AINOCOPULA, WP:AIREPRESENTS).

### 11. Negative parallelisms: Not just X, but also Y

- **Category:** ENC
- **Language:** en
- **Status on page:** current (examples from 2024 to June 2026)
- **Signal on page:** "stereotypically an 'AI sign'".
- **What it is:** the text seems to correct a misconception nobody holds, pointing to another characteristic next to the first. Also across several sentences ("Eugenio's life, however, took a path that intertwined...").
- **Why it sounds like AI:** a contrast that tries to "retroactively challenge such thinking".
- **Literal triggers:** Not only ... but ...; It is not just ..., it's ...; "not only dismissive but also unnecessarily harsh"; "doesn't just undermine the editor's argument; it questions"; "not just dismissive—they're outright disrespectful"; "isn't just sourcing—it's framing"; "That's not just a sourcing issue—it's a systemic bias"; "doesn't mean it doesn't exist".
- **Bad example → fixed:** "Self-Portrait [...] constitutes not only a work of self-representation, but a visual document of her obsessions". No corrected version.
- **What to avoid / how to fix:** does not prescribe.
- **Exceptions / when not to act:** "it is common among human writers (especially in 'common misconceptions' or 'myths busted' listicles)".
- **Catalog:** P14 (covers).
- **Source:** Language and grammar > Negative parallelisms > Not just X, but also Y (WP:AIPARALLEL).

### 12. Negative parallelisms: Not X, but Y

- **Category:** ENC
- **Language:** en
- **Status on page:** current
- **Signal on page:** "Another common LLM pattern".
- **What it is:** the parallelism denies that the item has the first characteristic.
- **Why it sounds like AI:** same logic as block 11.
- **Literal triggers:** It's not ..., it's ...; no ..., no ..., just ...; "is not grounded in visual mastery, but in"; "This dispersal is not dissolution. Rather, it constitutes"; "not a mirror but a portal: not a representation of self, but a mechanism"; "This isn't WP:NBIO — it's WP:1EVENT in disguise"; "Not a career, not a body of work, not sustained relevance — just an algorithmic moment"; "This ain't bludgeoning — it's surgical teardown".
- **Bad example → fixed:** cited above; no corrected version.
- **What to avoid / how to fix:** does not prescribe.
- **Exceptions / when not to act:** the same as block 11.
- **Catalog:** P14 (covers). When the denied half rebuts an accusation nobody made ("This ain't bludgeoning"), P15 applies too.
- **Source:** Language and grammar > Negative parallelisms > Not X, but Y.

### 13. Negative parallelisms: Y rather than X

- **Category:** ENC
- **Language:** en
- **Status on page:** current; "a construction particularly common in recent LLM output" (examples from April and October 2026).
- **Signal on page:** not classified
- **What it is:** the inverted form of the negative parallelism.
- **Why it sounds like AI:** same logic.
- **Literal triggers:** "prioritizing empirical consolidation of power amid fragmented loyalties rather than ideological purity"; "Rather than introducing a new decompiler, REA acts as an interface"; "a bridge between AI coding agents and existing reverse-engineering tools rather than a replacement for conventional disassemblers".
- **Bad example → fixed:** cited above; no corrected version.
- **What to avoid / how to fix:** does not prescribe.
- **Exceptions / when not to act:** nothing.
- **Catalog:** P14 (covers; P14 already lists "Y rather than X"). The form is the basis of the 2026 corrective notice (block 26).
- **Source:** Language and grammar > Negative parallelisms > Y rather than X.

### 14. Leads treating Wikipedia lists or broad article titles as proper nouns

- **Category:** CONT (applies to any document with a title; the typical case is Wikipedia's)
- **Language:** en
- **Status on page:** current
- **Signal on page:** not classified
- **What it is:** the first sentence defines the title of a list or broad topic as if it were an entity in the world.
- **Why it sounds like AI:** the page only says these openings "tend not to be so natural".
- **Literal triggers:** "'''Catchment area (health)''' refers to"; "EuroGames editions is the chronological list"; "The 'List of songs about Mexico' is a curated compilation".
- **Bad example → fixed:** cited above; no corrected version.
- **What to avoid / how to fix:** the MOS allows including the title "in a natural way".
- **Exceptions / when not to act:** natural inclusion of the title.
- **Catalog:** new. P13 covers only "refers to"; no P deals with the document title described as an object ("is a curated compilation").
- **Source:** Language and grammar > Leads treating Wikipedia lists or broad article titles as proper nouns.

### 15. Rule of three

- **Category:** RIT
- **Language:** en
- **Status on page:** current
- **Signal on page:** "This sign is stronger when it appears in contexts where most people would not bother to include such stylistic flourishes, like edit summaries."
- **What it is:** overuse of the rule of three, from "adjective, adjective, adjective" to "short phrase, short phrase and short phrase", to make the superficial analysis look complete.
- **Why it sounds like AI:** Russell et al., Kriss and The Economist are cited.
- **Literal triggers:** "tiles, metals, and plastics"; "drywall, plywood, and other construction materials"; "electrical outlets, switches, and plumbing fixtures"; "model making, woodworking, and other craft projects"; "mythological image, magical weapons, and spirit of resistance"; "contemporary values, modern aesthetics, and digital animation technology".
- **Bad example → fixed:** cited above; no corrected version.
- **What to avoid / how to fix:** does not prescribe.
- **Exceptions / when not to act:** nothing beyond the gradation by context.
- **Catalog:** P17 (covers); the gradation "stronger in a short context, where nobody would embellish" is missing.
- **Source:** Language and grammar > Rule of three (WP:RO3).

### 16. Title case

- **Category:** FMT
- **Language:** en
- **Status on page:** current
- **Signal on page:** "AI chatbots strongly tend to capitalize all main words" in section headings.
- **What it is:** Title Case in section headings.
- **Why it sounds like AI:** Russell et al. is cited.
- **Literal triggers:** "Impact of Technology and Digitalization"; "Sustainable Development and Environmental Law"; "Human Rights and Economic Law".
- **Bad example → fixed:** cited; no corrected version.
- **What to avoid / how to fix:** points to the MOS on capitalization.
- **Exceptions / when not to act:** nothing.
- **Catalog:** P41 (covers: "Title Case imported without criterion"); `references/en/final-pass.md` already treats sentence case as a default, not a law.
- **Source:** Style > Title case (WP:AITITLECASE).

### 17. Overuse of boldface

- **Category:** FMT
- **Language:** en
- **Status on page:** current; "Some newer large language models or apps have instructions to avoid overuse of boldface."
- **Signal on page:** not classified
- **What it is:** mechanical bold, especially on every occurrence of a chosen word, in the "key takeaways" style, inherited from readmes, fan wikis, how-tos, sales pitches, slides and listicles.
- **Why it sounds like AI:** inheritance from the cited training genres.
- **Literal triggers:** "A '''leveraged buyout (LBO)''' is characterized by the extensive use of '''debt financing'''"; "'''50 Scientists and Thinkers in AI Safety with significant''' influence".
- **Bad example → fixed:** cited; no corrected version.
- **What to avoid / how to fix:** points to the MOS on formatting.
- **Exceptions / when not to act:** nothing.
- **Catalog:** P40 (covers).
- **Source:** Style > Overuse of boldface (WP:AIBOLD).

### 18. Inline-header vertical lists

- **Category:** FMT
- **Language:** en
- **Status on page:** current (examples up to March 2026)
- **Signal on page:** not classified
- **What it is:** a list where the bullet is followed by a bold header, a colon and the text. The bullet can be •, hyphen, en dash, #, emoji; numbered lists with an explicit "1.". Sometimes with no punctuation between the title and the text. In text pasted from the screen, line breaks disappear.
- **Why it sounds like AI:** format of the chatbot interface.
- **Literal triggers:** "**Standard Rotary Saws**: Typically used"; "Conflict of Interest (COI)/Autobiography:"; "1. Historical Context Post-WWII Era:"; "9. Key Takeaways Understanding the Madness:"; "10. Questions to Consider"; "Key highlights:"; "'''Route Details''':"; "Mass Content Removal:"; "Durability", "The Fire Hazard", "The Solution" (no punctuation).
- **Bad example → fixed:** cited; no corrected version.
- **What to avoid / how to fix:** points to "Use prose where understood easily".
- **Exceptions / when not to act:** do not confuse with the bold of "Keep" and "Delete" in XfD votes.
- **Catalog:** P30 (covers the list with "**Term:** explanation"). The swapped bullet and the loss of line breaks are markup (P42).
- **Source:** Style > Inline-header vertical lists (WP:AILIST).

### 19. Heading errors

- **Category:** FMT (partly Wikipedia-specific: levels 1 and 2 are a MediaWiki convention)
- **Language:** en
- **Status on page:** current (examples from August 2026)
- **Signal on page:** skipping a level is "very unlikely" in hand-formatted text.
- **What it is:** four forms: a heading with the article name before the content; skipping level 2 and starting at 3; overuse of level 1 (maybe from Markdown conversion); a heading that only contains other headings, with no text.
- **Why it sounds like AI:** the chatbot "don't usually imagine the title header [...] as being already there".
- **Literal triggers:** `= '''[https://www.youtube.com/@Pixaroo-kid Pixaroo]''' =`; `= History =`; `= Main Characters =`; `= External Links =`; "Programming" followed straight by "Pixy's Adventure Club".
- **Bad example → fixed:** cited; no corrected version.
- **What to avoid / how to fix:** points to the accessibility rules for headings.
- **Exceptions / when not to act:** nothing.
- **Catalog:** partly covers: P29 (coherent heading levels) and P42 (wrong format); the heading that repeats the document name and the empty heading are not named.
- **Source:** Style > Heading errors.

### 20. Emoji as formatting

- **Category:** FMT
- **Language:** en
- **Status on page:** current, but declining: "AI chatbots have used emoji in the past [...] while they are more rare now, they may still be seen." Most recent example: October 2026.
- **Signal on page:** not classified
- **What it is:** emoji in front of headings and bullets, almost always on talk pages and edit summaries.
- **Why it sounds like AI:** no explanation.
- **Literal triggers:** "👋 Welcome to the User Page of"; "🧑‍💻 About Me"; "🌏 My Interests"; "🎯 What I'm Working On"; "📬 Let's Connect!"; "🙏 Gratitude"; "🧠 Cognitive Dissonance Pattern:"; "🧱 Structural Gatekeeping:"; "🚨 Underlying Motivation:"; "🧭 What You're Actually Dealing With:"; "🌍 My Mission:"; "📚 My Interests:"; "🤝 My Goals on Wikipedia:".
- **Bad example → fixed:** cited; no corrected version.
- **What to avoid / how to fix:** does not prescribe.
- **Exceptions / when not to act:** nothing.
- **Catalog:** P40 (covers).
- **Source:** Style > Emoji as formatting (WP:AIEMOJI).

### 21. Unusual use of tables

- **Category:** FMT
- **Language:** en
- **Status on page:** current (examples from November 2025 to July 2026)
- **Signal on page:** not classified
- **What it is:** small, barely formatted tables that would fit in prose or an infobox. Sometimes a Markdown table inside a wikitable, which comes out scrambled.
- **Why it sounds like AI:** no explanation.
- **Literal triggers:** "Key Statistics of Indian Biobanking (2024-2025)" with two columns "Metric / Figure"; a "Name !! Designation" table with four rows; "Comparison of Shan Hsun-Ok and Assamese Xorai".
- **Bad example → fixed:** cited; no corrected version.
- **What to avoid / how to fix:** implicit: prose or infobox.
- **Exceptions / when not to act:** nothing.
- **Catalog:** P31 (covers). The Markdown table inside a wikitable is P42.
- **Source:** Style > Unusual use of tables (WP:AITABLE).

### 22. Curly quotation marks and apostrophes

- **Category:** FMT
- **Language:** en
- **Status on page:** current. Hidden comment in the wikitext: "appears to have risen some time in mid-2025".
- **Signal on page:** "Curly quotes alone do not prove LLM use."
- **What it is:** ChatGPT and DeepSeek use curly quotes and a curly apostrophe (’), sometimes mixed with straight quotes in the same answer.
- **Why it sounds like AI:** a model habit, not a genre habit.
- **Literal triggers:** “...”; ‘...’; ’ in contractions and possessives; a mix of curly and straight.
- **Bad example → fixed:** none.
- **What to avoid / how to fix:** points to the MOS.
- **Exceptions / when not to act:** Chicago Manual of Style; "smart quotes" in Word, macOS and iOS; LanguageTool; newspapers; citation tools such as Citer that copy the page title; fonts that show a curly apostrophe as straight. "Gemini and Claude models typically do not use curly quotes."
- **Catalog:** P41 (covers, and already protects "valid typographic quotes"); `references/en/final-pass.md` says typographic quotes do not prove authorship.
- **Source:** Style > Curly quotation marks and apostrophes (WP:AICURLY).

### 23. Collaborative communication

- **Category:** RES
- **Language:** en
- **Status on page:** current (examples from 2023 to August 2026)
- **Signal on page:** not classified
- **What it is:** text pasted from the chatbot that was correspondence, a draft or advice to the user, in the article or in a hidden comment. The 2026 forms are submission notes: instructions to delete the section, to declare a conflict of interest, to check before publishing.
- **Why it sounds like AI:** the text addresses the chatbot's user.
- **Literal triggers:** a Wikipedia-style article; I hope this helps; Of course!; Certainly!; You're absolutely right!; Would you like...; is there anything else; let me know; more detailed breakdown; here is a ...; [check/verify/confirm]... ...before [publishing/publication/submitting]. In the examples: "In this section, we will discuss the background information"; "If you plan to add this information [...] ensure that the content is presented in a neutral tone"; "Here's a template for your wiki user page. You can copy and paste this"; "would enrich the article's section"; "Final important tip:"; "Delete this section before submission."; "<!-- SUBMISSION NOTES -->"; "Before creating a real Wikipedia page".
- **Bad example → fixed:** cited; no corrected version.
- **What to avoid / how to fix:** does not prescribe.
- **Exceptions / when not to act:** nothing.
- **Catalog:** P37 (assistant formulas) and P38 (meta-comment and draft in the final artifact). The "check before publishing" note left in the text is not named.
- **Source:** Communication intended for the user > Collaborative communication (WP:CERTAINLY, WP:COLLABCOMM).

### 24. Hedging disclaimers: didactic disclaimers (2023-24)

- **Category:** SIN
- **Language:** en
- **Status on page:** current by position (it is outside "Historical indicators"), but dated: "Older LLMs (~2023) often added didactic disclaimers".
- **Signal on page:** not classified
- **What it is:** a didactic warning that something is "important to note", advice to an imagined reader about safety or a controversial topic, or disambiguation by region or jurisdiction. The GPT-4 system card has examples such as "partial refusals".
- **Why it sounds like AI:** the Pangram technical report (Spero and Emi) is cited.
- **Literal triggers:** "However, it's important to note"; "may vary"; "It is crucial to differentiate"; "to prevent confusion"; "It's important to remember"; "always check before you use something".
- **Bad example → fixed:** "It's important to remember that what's free in one country might not be free in another, so always check before you use something." No corrected version.
- **What to avoid / how to fix:** does not prescribe.
- **Exceptions / when not to act:** nothing.
- **Catalog:** P24 ("it is essential to point out") and P12 (filler). Safety advice to the imagined reader is not named.
- **Source:** Communication intended for the user > Hedging disclaimers... > 2023-24 (WP:DIDACTIC).

### 25. Hedging disclaimers: source availability (2024-25)

- **Category:** RES
- **Language:** en
- **Status on page:** current; the section "hedging disclaimers about source availability and usage" is one of the five most common signs in October 2026. Examples up to 2026.
- **Signal on page:** not classified
- **What it is:** a chatbot with search that finds no source states that the information "is not publicly available" and then fills in what it "likely" would be and why it matters. About personal life: "maintains a low profile", "keeps personal details private".
- **Why it sounds like AI:** "This information is entirely speculative (including the very claim that it's 'not documented') and may be based on loosely related topics or completely fabricated."
- **Literal triggers:** While specific details are limited/scarce...; not widely available/documented/disclosed; ...in the provided/available sources / search results...; based on available information; "aren't widely documented"; "is limited in the provided search results"; "are not extensively documented in readily available sources"; "the mountain likely supports"; "My analysis is based on available track titles"; "I've inferred common motifs from similar trap tracks"; "aren't fully documented in public sources"; "maintains a low profile"; "keeps personal details private".
- **Bad example → fixed:** "While specific information about the fauna of Studniční hora is limited in the provided search results, the mountain likely supports..." No corrected version.
- **What to avoid / how to fix:** does not prescribe.
- **Exceptions / when not to act:** nothing.
- **Catalog:** partly covers: P37 (operational limitation only when it affects the task) and P06 (inference as fact, in the "likely"). Rule R04 already forbids turning missing data into an invented claim. No P lists these triggers.
- **Source:** Communication intended for the user > Hedging disclaimers... > 2024-25.

### 26. Hedging disclaimers: corrective framings (mid-2026-present)

- **Category:** CONT
- **Language:** en
- **Status on page:** current and new: "This pattern is extremely uncommon, verging on unheard-of, in AI output prior to mid-2026 (roughly coinciding with the July release of GPT-5.6). If an edit containing these disclaimers predates July 2026, it is far less likely to be AI-generated."
- **Signal on page:** the first two patterns count for more; the third "is less reliable than the above two".
- **What it is:** a warning about how the source should be used ("corrective framings", a term from Druck et al., Graphite, Sep. 2026). Three patterns: (1) a negative parallelism with "rather than", saying the source should be treated as something speculative or symbolic and not as something verified; (2) a warning that the available information does not establish a firm conclusion; (3) disambiguation with "should not be confused with".
- **Why it sounds like AI:** the page only dates the pattern.
- **Literal triggers:** [claim] should be [treated/presented] as... rather than...; ...does not by itself establish...; should not be confused; "should be treated as religious tradition rather than as an archaeological explanation"; "undergoing testing and evaluation, rather than validated production or clinical systems"; "It does not establish that Benjakitti has a particular contamination problem".
- **Bad example → fixed:** "The guidance explains why subsurface conditions require separate attention from visible planting. It does not establish that Benjakitti has a particular contamination problem or groundwater configuration." No corrected version.
- **What to avoid / how to fix:** does not prescribe.
- **Exceptions / when not to act:** before July 2026 it is much less likely to be AI.
- **Catalog:** partly covers: P14 ("rather than" form) and P23 (calibrated caveat). New for "does not by itself establish" and "should not be confused with". Note: R04, R05 and P44 say to flag what was not confirmed; that can produce this sign inside the text (see Changes).
- **Source:** Communication intended for the user > Hedging disclaimers... > Mid-2026-present (WP:AIDISCLAIMER).

### 27. Phrasal templates and placeholder text

- **Category:** RES
- **Language:** en
- **Status on page:** current (examples from 2024 to August 2026)
- **Signal on page:** not classified
- **What it is:** a fill-in-the-blanks template (Mad Libs) left unfilled. In infoboxes, comments such as "Add if available with citation" and instructions to upload an image to Commons.
- **Why it sounds like AI:** the user forgets to fill it in.
- **Literal triggers:** "I hope this message finds you well. I am writing to request an edit"; "[Describe the specific section or content that needs editing and provide clear reasons why the edit is necessary, including reliable sources if applicable]"; "[Article Title 1]"; "[Your Email Address]"; "[Interesting Article Title]"; "[brief reason]"; "[Award or Recognition Title]"; "[Join Date]"; "[My Blog or Personal Website]"; "[link to the revised article]"; "Best regards, [Your Name] and Chloe"; "[Entertainer's Name]"; "(Add your channel URL here)"; "(If available)"; "<!-- Add if available with citation -->".
- **Bad example → fixed:** cited; no corrected version.
- **What to avoid / how to fix:** does not prescribe.
- **Exceptions / when not to act:** there are human templates for drafts (Artist biography article template/Preload, Category:Article creation templates). Standard infobox comments ("Add spouse if reliably sourced" in Infobox military person) do not count: "check whether the comment in question is part of the infobox template".
- **Catalog:** P45 (covers).
- **Source:** Communication intended for the user > Phrasal templates and placeholder text (WP:AIPLACEHOLDER).

### 28. Date placeholders

- **Category:** GEN (Wikipedia-specific: citation fields)
- **Language:** en
- **Status on page:** current (example from November 2025)
- **Signal on page:** not classified
- **What it is:** fake dates such as "{{CURRENTYEAR}}-xx-xx" in `access-date` and, rarely, in `date`.
- **Literal triggers:** `|access-date=2025-XX-XX`; `|url=URL`; search `insource:/20[0-9][0-9]-(XX|xx)-(XX|xx)/`.
- **What applies to ordinary text:** a date with "XX" in a finished version is template residue.
- **Catalog:** P45 (covers: "XXXXX").
- **Source:** Phrasal templates... > Date placeholders.

### 29. URL placeholders

- **Category:** GEN (Wikipedia-specific: citation fields)
- **Language:** en
- **Status on page:** current by position, but the page says "Historically, LLMs have used strings such as..."; examples from December 2025 to August 2026.
- **Signal on page:** not classified
- **What it is:** strings in the URL field and example.com subpages as a source.
- **Literal triggers:** `INSERT_SOURCE_URL_##`; `INSERT_WEBSITE_URL_HERE`; `INSERT_SOURCE_URL_30`; `SOURCE_PUBLISHER`; `2022-11-XX`; `PASTE_SPOTIFY_TRACK_URL_HERE`; `PASTE_YOUTUBE_VIDEO_URL_HERE`; `https://example.com/article`; `https://example.com/news`; "Example Source Title"; "[Year]"; "[Founder Names]".
- **What applies to ordinary text:** a link to example.com or a fill-in URL in a reference presented as real.
- **Catalog:** P45 (template residue) and P44 (link whose destination differs from the label).
- **Source:** Phrasal templates... > URL placeholders.

### 30. Markup irregularities

- **Category:** GEN (Wikipedia-specific: wikitext)
- **Language:** en
- **Status on page:** current; Markdown is the first of the five most common signs in October 2026.
- **Signal on page:** a code block with three backticks, often preceded by "wikitext", is "most unambiguous of all"; exposed internal citation structure "is an unambiguous indicator".
- **What it is:** Markdown in place of wikitext (asterisks for bold, # for headings, `---` or `----` as a divider, `[url](text)` link); internal citation structure leaking; nonexistent categories and templates.
- **Literal triggers:** `**`; `#`; `---`; `----`; `[url](text)`; ```` ``` ````; "wikitext"; `contentReference[oaicite:1]`.
- **What applies to ordinary text:** Markdown in a destination that does not render it, and an internal citation token in the final text.
- **Catalog:** P42 (Markdown in a plain-text field, a code fence around the whole answer) and P43 (internal markers). Nonexistent categories and templates: not applicable outside Wikipedia.
- **Source:** Markup irregularities (`/Markup` subpage not read).

### 31. Broken external links

- **Category:** GEN (Wikipedia-specific: citations)
- **Language:** en
- **Status on page:** current
- **Signal on page:** several broken links in a new article, which not even the Internet Archive has, "is a strong sign".
- **What it is:** nonexistent sites or 404s that probably never existed.
- **What applies to ordinary text:** an invented reference. It does not apply to a link that just does not open for you (library access), a link mangled by a bot, or a URL missing its start or end (human copying).
- **Catalog:** P44 (covers; already says an inaccessible bibliography is not false for that reason).
- **Source:** Citations > Broken external links (WP:AIFICTREF).

### 32. Invalid DOI and ISBNs

- **Category:** GEN (Wikipedia-specific: citations)
- **Language:** en
- **Status on page:** current
- **Signal on page:** an invalid ISBN checksum "is a very likely sign that an ISBN is incorrect".
- **What it is:** a DOI that does not resolve and an ISBN with a wrong check digit point to a hallucinated reference.
- **What applies to ordinary text:** an invalid DOI and an invalid ISBN as a sign of an invented reference.
- **Catalog:** P44 (covers: "nonexistent DOI"); the ISBN checksum check is not in P44.
- **Source:** Citations > Invalid DOI and ISBNs.

### 33. DOIs that lead to unrelated articles

- **Category:** GEN (Wikipedia-specific: citations)
- **Language:** en
- **Status on page:** current
- **Signal on page:** not classified
- **What it is:** a valid DOI that points to another article. In the ChatGPT example, both Proceedings of the IEEE articles "are completely made up"; C. L. Fortescue had died more than 30 years before the claimed date.
- **What applies to ordinary text:** check that the DOI leads to the cited article, not just that it resolves.
- **Catalog:** P44 (covers: "source on a different subject"). Exception from the page: from 2018 to 2023 a VisualEditor defect inserted low PMIDs by mistake ("rat livers (PMID 9)"), which look like hallucination and are not.
- **Source:** Citations > DOIs that lead to unrelated articles.

### 34. Book citations without page numbers or URLs

- **Category:** GEN (Wikipedia-specific: citations)
- **Language:** en
- **Status on page:** current
- **Signal on page:** not classified
- **What it is:** a real book with no page, which cannot be used to verify; or a real book with a page that does not confirm the text, usually a broad-topic book with no URL.
- **Literal triggers:** "Dorf, R. C., & Svoboda, J. A. (2010). Introduction to Electric Circuits (8th ed.)"; "Goldwater, Barry (1960). The Conscience of a Conservative. Victor Publishing. p. 12." (searching for "Burke" in the online version turns up nothing).
- **What applies to ordinary text:** a citation of a known book without a page, or with a page that does not contain the subject.
- **Catalog:** P44 partly covers ("unsupported citation"); the missing page is not named.
- **Source:** Citations > Book citations without page numbers or URLs.

### 35. Incorrect or unconventional use of references

- **Category:** GEN (Wikipedia-specific: citations)
- **Language:** en
- **Status on page:** current (examples from 2023 and August 2025)
- **Signal on page:** not classified
- **What it is:** wrong reference-reuse syntax repeated "after every single full stop" (`<sup>[3]</sup>`); a real but irrelevant source (PMID 3); the ↩ character in footnotes, coming from the chatbot interface.
- **Literal triggers:** `<sup>[3]</sup>`; `https://pubmed.ncbi.nlm.nih.gov/3`; `↩`; `↩<sup>2</sup>`; "Would you like help formatting and submitting this to Wikipedia".
- **What applies to ordinary text:** ↩ in notes and a loose note number with no destination.
- **Catalog:** partly covers: P43 (export residue) and P44 (irrelevant source); the ↩ is not named.
- **Source:** Citations > Incorrect or unconventional use of references (WP:AICITESTYLE).

### 36. utm_source=

- **Category:** GEN (Wikipedia-specific: citations; applies to any link)
- **Language:** en
- **Status on page:** current
- **Signal on page:** "near-definitively proves ChatGPT's involvement", but does not prove that ChatGPT wrote the text.
- **What it is:** parameters the tool adds to the URL.
- **Literal triggers:** `utm_source=openai`; `utm_source=chatgpt.com`; `utm_source=copilot.com`; `referrer=grok.com`. Gemini and Claude use them less.
- **What applies to ordinary text:** the parameter shows the source came from a chatbot. Exceptions from the page: Google sometimes indexed URLs with the parameter; people who use AI only to find a citation for existing text.
- **Catalog:** partly covers: P44 (and it says not to strip URL parameters that may be functional); P43 does not cite tracking parameters.
- **Source:** Citations > utm_source=.

### 37. Named references declared in references section but unused in article body

- **Category:** GEN (Wikipedia-specific: citations)
- **Language:** en
- **Status on page:** current (examples from May 2025)
- **Signal on page:** "A common referencing error produced by LLMs".
- **What it is:** references defined in `<references>` and never used in the body, or named references never defined (can also be copied from another article).
- **What applies to ordinary text:** little; at most, a list of sources the text never cites.
- **Catalog:** not applicable.
- **Source:** Citations > Named references declared in references section but unused in article body.

### 38. Comment-specific indicators

- **Category:** GEN (Wikipedia-specific: talk pages)
- **Language:** en
- **Status on page:** current
- **Signal on page:** not classified
- **What it is:** beyond the general signs, people who use an LLM in comments tend to cite wrong policies and invented shortcuts ("WP" alone); transclude maintenance banners; post long comments in sections with a heading; downplay the use of AI ("put some human effort", "comments reflect their thoughts"); ask critics to say what to improve; call the suspicion "unsubstantiated speculation" instead of "concrete" facts; ask for a focus on content. Customer-service tone: "carefully reviewed", apologies for the inconvenience they "may have" caused.
- **Literal triggers:** "If there are specific issues that need to be resolved, please point them out to me, and I will try to resolve them."; "I understand your concerns regarding AI-generated..."; "Dear Wikipedia Editorial Team"; "I am writing to ..."; "I hope/trust this message finds you well."; "concrete".
- **What applies to ordinary text:** the customer-service tone in a reply to a reviewer, the "I hope this message finds you well" and the habit of citing a nonexistent rule.
- **Catalog:** partly covers: P37 (assistant formulas), P39 (register) and P44 (citing a rule that does not exist). The customer-service tone in a reply to a review is not named.
- **Source:** Comment-specific indicators (WP:AICOMMENT).

### 39. Edit summaries: general examples

- **Category:** GEN (Wikipedia-specific: edit summaries)
- **Language:** en
- **Status on page:** current; AI edit summaries are the second of the five most common signs in October 2026.
- **Signal on page:** an AI summary "strongly suggests that the edits themselves are also AI-generated". They are "rigid formulae": the further it strays, the less likely.
- **What it is:** the old ones come in first person, with AI vocabulary, emoji, a list or Markdown; the new ones are "exhaustively procedural" about the process and about following the rules.
- **Literal triggers:** "ChatGPT I revised the content to provide a neutral and informative description"; "**Concise edit summary:** Improved clarity, flow, and readability"; "Claude responded: That last sentence is the killer".
- **What applies to ordinary text:** a generic, procedural change report, see block 41.
- **Exceptions:** common abbreviations such as "ce" (copy edit) point to a human.
- **Catalog:** P38 partly covers (meta-comment and change report).
- **Source:** Edit summaries > General examples (WP:AISUMMARY).

### 40. Edit summaries: canned assurance of adherence to Wikipedia policies and guidelines

- **Category:** GEN (Wikipedia-specific: edit summaries)
- **Language:** en
- **Status on page:** current (examples from July 2026)
- **Signal on page:** the more assurances stacked in the same summary, the stronger.
- **What it is:** the summary assures that the edit follows neutrality, sourcing and the MOS, at length and without much specificity; humans cite the exact rule ("removed excessive links per MOS:OVERLINK"). Humans also do not say the edit is "for" Wikipedia.
- **Literal triggers:** ensured that... adheres to, refined, enhanced, enriched, streamlined, improved, in compliance/complies with, Wikipedia [guidelines/style/standards], revised, verifiability, neutrality, neutral tone, encyclopedic tone, clarity, flow; "clarity and compliance with the Manual of Style"; "corrected promotional wording"; "improved sourcing and neutrality."; "for a more neutral tone."
- **What applies to ordinary text:** a revision report that lists generic virtues (clarity, flow, tone) without saying what changed.
- **Catalog:** P38 partly covers; the generic list of virtues is not named.
- **Source:** Edit summaries > Canned assurance... (WP:AIASSURE).

### 41. Edit summaries: specific mentions of "preserved" or "retained" information, "avoided" mistakes, and other procedural statements

- **Category:** GEN (Wikipedia-specific: edit summaries; the format applies to any rewrite report)
- **Language:** en
- **Status on page:** current (examples from July 2026)
- **Signal on page:** not classified
- **What it is:** the summary mentions what was not edited. The page explains: it is what you expect from an AI told to do X and Y "but to specifically preserve or avoid changing Z". Format: "Revised [section] to [improve/ensure/etc] [neutrality/verifiability/etc] while preserving [whatever]".
- **Literal triggers:** preserved/preserving, retained/retaining, avoided/avoiding, ensured/ensuring, aimed/aiming to; "while preserving the original meaning and technical details."; "preserved existing structure and lead emphasis"; "preserved references and categories"; "while preserving sourced criticisms."
- **What applies to ordinary text:** the phrase "I rewrote for X while preserving the meaning" is the typical form of a rewriting tool's report.
- **Catalog:** P38 partly covers (it only says to show decisions when asked); no P names "while preserving". See Changes.
- **Source:** Edit summaries > Specific mentions of "preserved"...

### 42. Edit summaries: overemphasis on presence/reliability of citations

- **Category:** GEN (Wikipedia-specific: edit summaries)
- **Language:** en
- **Status on page:** current (examples from July 2026)
- **Signal on page:** not classified
- **What it is:** the summary says the content is "sourced", that citations were added, that the sources are independent or secondary, without saying the content; a human writes "Added info about the artist's debut".
- **Literal triggers:** added sourced [information/content/infobox/section], added verified [information/content/infobox/section], added [coverage/citations/references], improved attribution, with [independent/secondary/third-party/peer-reviewed] sources; "with sourced content;"; "with ESSA citations"; "added sourced information, references,"; "sourced Military culture section".
- **What applies to ordinary text:** the same mechanism as block 2 (talking about the source, not the content).
- **Catalog:** P03 partly covers.
- **Source:** Edit summaries > Overemphasis on presence/reliability of citations.

### 43. Edit summaries: overemphasis on parameter/template names and markup idiosyncracies

- **Category:** GEN (Wikipedia-specific: edit summaries)
- **Language:** en
- **Status on page:** current (example from February 2026)
- **Signal on page:** not classified
- **What it is:** the summary lists parameter and template names with the original markup and terms such as "inline citations", "internal links".
- **Literal triggers:** "Corrected infobox parameters (image_size)"; "Comprehensive formatting update:".
- **What applies to ordinary text:** nothing beyond block 40.
- **Catalog:** not applicable.
- **Source:** Edit summaries > Overemphasis on parameter/template names...

### 44. Edit summaries: reference to AfC review

- **Category:** GEN (Wikipedia-specific: AfC)
- **Language:** en
- **Status on page:** current (examples from June and July 2026)
- **Signal on page:** not classified
- **What it is:** after a decline at AfC, the summary says the edit addresses the reviewer's opinion, "a statement so obvious that a human would not typically feel the need to state it".
- **Literal triggers:** "Addressing reviewer feedback"; "per reviewer feedback."; "Addressed reviewer feedback"; "All claims verified."
- **What applies to ordinary text:** stating the obvious ("addressing reviewer feedback") instead of what changed.
- **Catalog:** not applicable ("All claims verified" without proof would fall under P50).
- **Source:** Edit summaries > Reference to AfC review.

### 45. Pronounced shift in writing style

- **Category:** VOZ
- **Language:** en
- **Status on page:** current
- **Signal on page:** not classified
- **What it is:** an abrupt change in an editor's style, such as impeccable grammar in the article text against error-filled comments, more so if the earlier writing predates November 2022. People who have used AI for years change style along with the tool of the day. The reverse holds: a stable style from before chatbots (frequent bold, lists) makes AI less likely.
- **Literal triggers:** none.
- **Bad example → fixed:** none.
- **What to avoid / how to fix:** does not prescribe.
- **Exceptions / when not to act:** the reverse described above.
- **Catalog:** new (depends on the author's history, outside Humanizer's editing scope).
- **Source:** Miscellaneous > Pronounced shift in writing style.

### 46. "Submission statements" in AfC drafts

- **Category:** GEN (Wikipedia-specific: AfC)
- **Language:** en
- **Status on page:** current (examples from October 2025 and October 2026)
- **Signal on page:** the result is that the reviewer knows it is an LLM.
- **What it is:** at least one LLM inserts a note to the reviewer explaining why the subject is notable and the draft meets the rules. It includes an AI-use declaration that guarantees "full compliance with Wikipedia guidelines".
- **Literal triggers:** "Reviewer note (for AfC): This draft is a neutral and well-sourced biography"; "It meets WP:RS and WP:BLP standards and demonstrates clear notability per WP:NBIO"; "Thank you for your review."; "ensure full compliance with Wikipedia guidelines".
- **What applies to ordinary text:** a note to the evaluator embedded in the document, defending its own quality.
- **Catalog:** P38 partly covers.
- **Source:** Miscellaneous > "Submission statements" in AfC drafts.

### 47. Pre-placed maintenance templates

- **Category:** GEN (Wikipedia-specific: AfC and templates)
- **Language:** en
- **Status on page:** current
- **Signal on page:** the "submission declined" header with no content is "a strong indicator".
- **What it is:** a draft that is born with `{{AfC submission|d}}` (pre-declined) or with maintenance and protection tags that make no sense.
- **Literal triggers:** `{{AfC submission|d|date=January 2025}}`; `{{Use mdy dates|date=February 2025}}`; `{{Use American English|date=September 2022}}`; `{{BLP sources|date=January 2025}}`.
- **What applies to ordinary text:** nothing.
- **Catalog:** not applicable.
- **Source:** Miscellaneous > Pre-placed maintenance templates (WP:AIDECLINE).

### 48. Canned user pages

- **Category:** GEN (Wikipedia-specific: user pages)
- **Language:** en
- **Status on page:** current
- **Signal on page:** Markdown bold is a "less ambiguously" sign.
- **What it is:** a user page with a rigid format, with inline-header lists, emoji, bold and fixed headings.
- **Literal triggers:** "Welcome To My User Page!"; "About Me"; "My Interests"; "Let's Connect!"; "My Contributions"; "How I Contribute"; "Let's Collaborate"; "Happy Editing! 🚀".
- **What applies to ordinary text:** a profile bio built from these headings and emoji.
- **Catalog:** partly covers: P40 (emoji and bold) and P28 (structure by habit).
- **Source:** Miscellaneous > Canned user pages (WP:AIUSERPAGE).

### 49. Permissions gaming

- **Category:** GEN (Wikipedia-specific: permissions)
- **Language:** en
- **Status on page:** current
- **Signal on page:** "This sign should only be used in one direction."
- **What it is:** many quick, benign edits to raise the access level; after 2023 done with disposable AI rewrites.
- **What applies to ordinary text:** nothing.
- **Catalog:** not applicable.
- **Source:** Miscellaneous > Permissions gaming.

### 50. Differences between LLMs

- **Category:** MOD
- **Language:** en
- **Status on page:** current
- **Signal on page:** not classified
- **What it is:** each model and version has an idiolect (Rudnicka 2025; Sun et al.). ChatGPT (GPT-4o-2024-08-06) and Grok (Grok-Beta, late 2024 and early 2025) focus more on the broad context; Gemini (1.5 Pro) and Claude (3.5 Sonnet) are more concise. ChatGPT is historically the most used for editing Wikipedia.
- **Literal triggers:** none.
- **Catalog:** new (Humanizer does not attribute text to a model).
- **Source:** Miscellaneous > Differences between LLMs.

### 51. Pro-authoritarian bias

- **Category:** CONT
- **Language:** en
- **Status on page:** current ("as of 2026")
- **Signal on page:** not classified
- **What it is:** leading American models show pro-authoritarian bias on some questions, partly because they train on state-media propaganda; answers in Chinese are more authoritarian than in English; the models criticize governments of free countries more than repressive regimes, sometimes citing safety (WSJ and Fortune, Aug. 2026).
- **Literal triggers:** none.
- **Catalog:** new (content bias; Humanizer does not address it).
- **Source:** Miscellaneous > Biases in content > Pro-authoritarian bias.

### 52. Age of text relative to ChatGPT launch

- **Category:** NAO
- **Language:** en
- **Status on page:** human sign (NAO)
- **What it is:** text added before November 30, 2022 has AI use "safely ruled out". Tools for dating: Who Wrote That? and WikiBlame. A hidden comment suggests moving the cutoff back to mid-2021 because of OpenAI beta users.
- **Catalog:** new.
- **Source:** Signs of human writing > Age of text relative to ChatGPT launch (WP:HUMANSIGNS).

### 53. Ability to explain one's own editorial choices

- **Category:** NAO
- **Language:** en
- **Status on page:** human sign (NAO)
- **What it is:** ask the editor how an apparently invented URL got in; if they bring the right link and explain the error, or the passage from the real source, it is a common human error.
- **Catalog:** new.
- **Source:** Signs of human writing > Ability to explain one's own editorial choices.

### 54. Syntax (constructions most common in human text)

- **Category:** NAO
- **Language:** en
- **Status on page:** human sign (NAO). "empirically observed, over 25 years of Wikipedia writing, to be more common in Wikipedia articles written by humans than in AI-generated text".
- **What it is:** the LLM aims for a "formal, neutral, encyclopedic tone" and avoids common constructions that the MOS accepts. More common in human text:
  - Simple is/has phrases (Geng and Trotta): *there is a*, *it has a*.
  - Simple words in place of stiff or euphemistic synonyms: *wrote* (vs. *authored*), *moved* (vs. *relocated*), *used* (vs. *utilized*), *tried* (vs. *attempted*), *died* (vs. *passed away*).
  - Superlative or definitive statements: *one of the best*, *is the only*, *was the first*.
  - Qualifiers and intensifiers (Reinhart et al.): *very*, *perhaps*, *tends to*.
  - Isolated wordy constructions: *as a result of*, *in order to*, *all of the*, *a part of*, *the fact that*.
- **Catalog:** aligned with P13 (is/has) and P12 and P11 (direct verb). In tension with P02 (remove intensifiers), P07 ("the definitive list", "always", "all"), P12 ("due to the fact that") and P23 (caveats). See Changes.
- **Source:** Signs of human writing > Syntax.

### 55. Ineffective: Perfect grammar

- **Category:** FMT
- **Language:** en
- **Status on page:** ineffective
- **What it is:** LLMs have good grammar, but many editors write well or come from professional writing.
- **Catalog:** no P; R08 and `references/en/final-pass.md` ("Grammar before appearance") already do not treat correct grammar as a sign.
- **Source:** Ineffective indicators.

### 56. Ineffective: Combination of casual and formal registers, or language that sounds both "clinical" and "emotional"

- **Category:** VOZ
- **Language:** en
- **Status on page:** ineffective
- **What it is:** it can be someone from a technical field writing informally, youth, a preference for mixed register, playfulness, neurodivergence, or several editors on the same page.
- **Catalog:** P39 partly covers and can clash: P39 treats inadequate register as an editorial problem, which is legitimate, but it should not be read as a sign of AI.
- **Source:** Ineffective indicators.

### 57. Ineffective: "Bland" or "robotic" prose

- **Category:** VOZ
- **Language:** en
- **Status on page:** ineffective
- **What it is:** LLM output has specific traits, pulls toward the positive and the wordy; it may not seem "robotic" to someone unfamiliar with AI writing (Murray and Tersigni 2024).
- **Catalog:** new (no P treats "bland prose" as a sign or a non-sign).
- **Source:** Ineffective indicators.

### 58. Ineffective: "Fancy", "academic", or "formal" prose

- **Category:** VOZ
- **Language:** en
- **Status on page:** ineffective
- **What it is:** LLMs prefer certain words, many of them long, but "these are specific words. The correlation does not extend to all formal, academic, or 'fancy'-sounding prose" (Russell et al.).
- **Catalog:** P39 (its exception already says not to treat formal language as proof of AI).
- **Source:** Ineffective indicators.

### 59. Ineffective: Transition words (in isolation)

- **Category:** SIN
- **Language:** en
- **Status on page:** ineffective. "Older AI text tended to formulaically overuse certain transitions like Additionally, Consequently, and Notably, often to begin sentences. However, only a few transition words and phrases are known to be overused by AI in this way. This pattern also has precedence in essay-like writing by humans and is accepted by many style guides, so this is not a strong tell."
- **Literal triggers:** Additionally,; Consequently,; Notably,.
- **Catalog:** P21 (already says to keep connectives with a real relationship and impose no limit); `references/en/final-pass.md` lists "furthermore, moreover, additionally" as mechanical transitions without saying the sign is weak and dated. "Additionally" remains in the vocabulary list, era 2023 to mid-2024.
- **Source:** Ineffective indicators.

### 60. Ineffective: Unsourced content

- **Category:** CONT
- **Language:** en
- **Status on page:** ineffective
- **What it is:** more than 570,000 articles are tagged as unsourced, most of them predating LLMs; chatbots that search the web bring citations, not always correct.
- **Catalog:** new as a non-sign.
- **Source:** Ineffective indicators.

### 61. Ineffective: Bizarre wikitext

- **Category:** GEN (Wikipedia-specific: wikitext)
- **Language:** en
- **Status on page:** ineffective
- **What it is:** displaced `<span>` tags come from browser extensions or from a defect in the translation tool (T113137); displaced syntax such as "''Catch-22 i''s" comes from VisualEditor.
- **Catalog:** not applicable.
- **Source:** Ineffective indicators.

### 62. Ineffective: Correct wikitext

- **Category:** GEN (Wikipedia-specific: wikitext)
- **Language:** en
- **Status on page:** ineffective
- **What it is:** with the visual editor or the preview button, getting the formatting right, even of complex templates, is normal.
- **Catalog:** not applicable.
- **Source:** Ineffective indicators.

### 63. Statements about knowledge cutoffs (2022–2023)

- **Category:** RES
- **Language:** en
- **Status on page:** historical, 2022–2023
- **Signal on page:** not classified
- **What it is:** a warning that the information is valid up to the training date, typical of GPT-3.5 and GPT-4 (Strzelecki 2024).
- **Literal triggers:** Up to my last training update; as of my last knowledge update; "As of my last knowledge update in January 2022, I don't have specific information".
- **Bad example → fixed:** cited; no corrected version.
- **Exceptions / when not to act:** nothing.
- **Catalog:** P37 (covers as an assistant formula).
- **Source:** Historical indicators > Statements about knowledge cutoffs (WP:AICUTOFF).

### 64. Section summaries

- **Category:** EST
- **Language:** en
- **Status on page:** historical; the heading gives no period, the text says "older LLMs" and the examples are from 2023 and 2024.
- **Signal on page:** not classified
- **What it is:** "Conclusion" sections and paragraphs that end by summarizing and repeating the central idea (Ju et al., ACL 2025).
- **Literal triggers:** In summary; In conclusion; Overall; "Conclusion"; "Conclusion:".
- **Bad example → fixed:** "In summary, the educational and training trajectory for nurse scientists typically involves a progression from a master's degree [...]". No corrected version.
- **Exceptions / when not to act:** nothing.
- **Catalog:** P34 (covers).
- **Source:** Historical indicators > Section summaries (WP:CONCLUSION, WP:INCONCLUSION).

### 65. Prompt refusal

- **Category:** RES
- **Language:** en
- **Status on page:** historical; no period in the heading; "In the past [...] Outright refusals have become increasingly rare." Example from 2024.
- **Signal on page:** not classified
- **What it is:** a refusal with apologies and a reminder that it is a language model, followed by an alternative offer.
- **Literal triggers:** as an AI language model; as a large language model; I cannot offer medical advice, but I can...; I'm sorry; "As an AI language model, I can't directly add content to Wikipedia for you, but I can help you draft your bibliography."
- **Catalog:** P37 (covers: "as a language model").
- **Source:** Historical indicators > Prompt refusal.

### 66. Overuse of em dashes (2022–September 2026)

- **Category:** FMT
- **Language:** en
- **Status on page:** historical, 2022 to September 2026
- **Signal on page:** "This sign is most useful when taken in combination with other indicators, not by itself. It is much more common on discussion pages than in article text."
- **What it is:** LLMs use the em dash (U+2014) much more than non-professional text of the same genre, where humans would put a comma, parentheses, a colon, or a misused hyphen and en dash; formulaic use that imitates "punched up" sales writing, reinforcing clauses and parallelisms; the AI em dash is "usually surrounded by spaces, contrary to common typographic guidelines".
- **Why it became historical (page text):** "because LLMs' use of em-dashes has become somewhat notorious, some AI companies have attempted to make their newer chatbots suppress their use, most notably OpenAI's GPT-5.1." "A July 2026 study found that of contemporary models only Claude used em dashes more than professional writers, and ChatGPT used them less." (The Economist, Jul. 30, 2026). "While still produced today as many AI users don't use the latest AI models, those same latest AI models of late (September 2026 and onward) have more and more often been found to be hard coded to not use em dashes at all. This, however, has the unintended side effect of making LLMs not once dare to use any sort of alternate puctuation, so the overall variety has dropped significantly in their output; commas and periods are more likely now than even human text, and now that has become its own sign of AI writing." The sentence about commas and periods carries the mark `{{cn|date=October 2026}}` (citation needed).
- **Literal triggers:** — with spaces; "using AI to help me organize my thoughts and better explain the policies I was referencing — something that was reported by the user"; "they were my own — not mistakes caused by the AI"; "you're right about one thing — we do seem to have different interpretations"; "it grows from critique, correction, and clarity."
- **Bad example → fixed:** cited; no corrected version.
- **Exceptions / when not to act:** "human editors and writers often use em dashes"; a sign only in combination.
- **Catalog:** P41 and R10 (and the personal profile in SKILL.md, which forbids U+2014 in new prose). See Changes, item 1.
- **Source:** Historical indicators > Overuse of em dashes (WP:AIDASH).

### 67. Abrupt cut offs

- **Category:** RES
- **Language:** en
- **Status on page:** historical; no period; "AI tools used to abruptly stop generating content", with ChatGPT's "continue generating".
- **Signal on page:** "not foolproof".
- **What it is:** text that stops midway because of a token limit.
- **Exceptions / when not to act:** a bad copy from the local computer; it may indicate a copyright violation rather than an LLM.
- **Catalog:** P43 (covers: "truncated answer").
- **Source:** Historical indicators > Abrupt cut offs.

### 68. Outdated access-date parameters

- **Category:** GEN (Wikipedia-specific: citations)
- **Language:** en
- **Status on page:** historical; no period; "newer chatbots seldom produce this error".
- **What it is:** an `access-date` well before the edit (a December 2025 article with `|access-date=12 December 2024`).
- **Exceptions:** copied citation, offline work, batch merges.
- **Catalog:** P44 partly covers (citation match); the access date is not named.
- **Source:** Historical indicators > Outdated access-date parameters.

### 69. Lexical diversity/elegant variation

- **Category:** LEX
- **Language:** en
- **Status on page:** historical; the heading gives no period; the text speaks of "Older AI models" and the example is from February 2024.
- **Signal on page:** not classified
- **What it is:** older models could have a repetition penalty, which leads to varying the name of the same referent. Observed on Wikipedia by comparing text before and after 2023 and old text against "Wikipedia-style" articles generated by GPT-4o-mini and Gemini-1.5-Flash (Huang et al.).
- **Why it became historical (page text):** only the section's general sentence: "The following indicators were common in text generated by older AI models, but are much less frequent in newer models. They may still be useful for finding older undetected AI-generated edits. Dates are approximate." The section gives no reason of its own.
- **Literal triggers:** in the example, the same referent under different names: "the constraints of socialist realism" / "the challenging climate of Soviet artistic constraints" / "the confines of state-imposed artistic norms" / "the constraints imposed by the Soviet regime"; "non-conformist artists" / "these artists" / "like-minded artists" / "Russian avant-garde artists"; "their creativity" / "the immense talent" / "their artistic aspirations" / "his distinctive artistic vision".
- **Exceptions / when not to act:** several AI pieces in separate edits (each generated in isolation); non-native editors may avoid repetition because of schooling ("Italian schools often teach to avoid repeating words", Birattari 2020 and Cortelazzo).
- **Catalog:** P18 (covers as an editorial problem); the non-native speaker exception is missing.
- **Source:** Historical indicators > Lexical diversity/elegant variation (WP:AIELEVAR).

### 70. Historical indicators: section introduction

- **Category:** MET
- **Language:** en
- **Status on page:** historical (rule for the whole section)
- **What it is:** "The following indicators were common in text generated by older AI models, but are much less frequent in newer models. They may still be useful for finding older undetected AI-generated edits. Dates are approximate."
- **Catalog:** new as a dating rule (no P marks the era of a sign).
- **Source:** Historical indicators, opening paragraph.

## Vocabulary lists

Copied as they stand in revision 1382823144. In brackets, the sources the page cites for each word, when it cites any.

### "Words to watch" table of High density of "AI vocabulary" words

*Additionally* (especially beginning a sentence) [Geng and Trotta; Huang et al.]; *align with* [Juzek and Ward; Kobak et al.]; *boasts* (meaning "has") [Juzek and Ward, 2025b]; *bolstered* [Kobak]; *crucial* [Russell; Geng; Huang]; *deep dive* [The Economist, Jul. 2026]; *delve* [Juzek; Kobak; Russell; Kriss]; *emphasizing* [Juzek; Kobak]; *enduring* [Kobak]; *enhance* [Kobak; Russell]; *fostering* [Kobak; Russell]; *garner* [Juzek; Kobak]; *highlight* (as a verb) [Russell; Kriss]; *interplay* [Kobak]; *intricate/intricacies* [Juzek; Kobak; Reinhart; Kriss]; *landscape* (as an abstract noun) [Russell]; *meticulous/meticulously* [Juzek and Ward, 2025b; Kobak]; *pivotal* [Kobak; Russell]; *robust* [no source in the table]; *showcase* [Juzek; Kobak; Kriss]; *tapestry* (as an abstract noun) [Russell; Reinhart; Kriss]; *testament* [Russell]; *underscore* (as a verb) [Juzek; Kobak; Russell; Kriss]; *valuable* [Geng]; *vibrant* [Reinhart].

### By era (page text: "While these are not hard cutoffs, they should give you a rough idea")

- **2023 to mid-2024** (GPT-4): *Additionally*, *boasts*, *bolstered*, *crucial*, *delve*, *emphasizing*, *enduring*, *garner*, *intricate/intricacies*, *interplay*, *key*, *landscape*, *meticulously*, *pivotal*, *underscore*, *tapestry*, *testament*, *valuable*, *vibrant*
- **Mid-2024 to mid-2025** (GPT-4o): *align with*, *bolstered*, *crucial*, *emphasizing*, *enhance*, *enduring*, *fostering*, *highlighting*, *pivotal*, *showcasing*, *underscore*, *vibrant*
- **Mid-2025 to mid-2026** (GPT-5): *emphasizing*, *enhance*, *highlighting*, *showcasing* (plus words associated with "Canned emphasis on notability, attribution, and media coverage")
- **Mid-2026 and on** (GPT-6): *challenge*, *clearer*, *dependable*, *echoed*, *foster*, *leverage*, *matters*, *multifaceted*, *practical*, *prioritize*, *quietly*, *steady*, *universally* (with much more period and comma usage and shorter sentences around a strict 8–20 word limit). Single source: the review "ChatGPT-6 Astra for Writing Full Review", Intellectual Lead, Sep. 10, 2026. Inference: it is a website review, not a study; the list and the 8 to 20 word limit are weaker support than the earlier eras.
- Page note: "delve" was heavily used by ChatGPT in 2023 and early 2024, dropped in late 2024 and "dropped off sharply in 2025" (Washington Post, Nov. 2025; Geng and Trotta).

### By model

- **Grok:** "overuses superficially 'scientific' words like *causal*, *empirical*, *correlate*, and continues to overuse *underscore* as of 2026".

### Other "Words to watch" tables (copied by section)

- **Undue emphasis on significance, legacy, and broader trends:** *stands/serves as*, *is a testament/reminder*, *a crucial/pivotal/vital/significant/key role/moment*, *underscores/highlights its importance/significance*, *reflects broader*, *symbolizing its ongoing/enduring/lasting*, *contributing to the*, *setting the stage for*, *marking/shaping the*, *represents/marks a shift*, *key turning point*, *evolving landscape*, *focal point*, *indelible mark*, *deeply rooted*, *distinction [matters/is important] because*...
- **Canned emphasis on notability, attribution, and media coverage:** *independent coverage*, *local/regional/national/[country name] media outlets*, *music/business/tech outlets*, *trade publications*, *cited/featured/profiled in*, *written by a leading expert*, *active social media presence*, *was identified by*
- **Superficial analyses:** *highlighting/underscoring/emphasizing ...*, *ensuring ...*, *reflecting/symbolizing ...*, *contributing to ...*, *cultivating/fostering ...*, *encompassing ...*, *enhancing ...*, *valuable insights*, *align/resonate with*
- **Promotional and advertisement-like language:** *boasts a*, *vibrant*, *rich*, *profound*, *enhancing*, *showcasing*, *exemplifies*, *commitment to*, *natural beauty*, *nestled*, *in the heart of*, *groundbreaking*, *renowned*, *featuring*, *diverse array*, ...
- **Vague expression of connection or association:** *in connection with/to ...*, *connected with/to*, *in association with ...*, *associated with*
- **Vague attributions and overgeneralization of opinions:** *Industry reports*, *Observers have cited*, *Experts argue*, *Some critics argue*, *several sources/publications* (when only few sources are cited), *such as* (before exhaustive word lists), ...
- **Outline-like conclusions about challenges and future prospects:** *Despite its... faces several challenges...*, *Despite these challenges*, *Challenges and Legacy*, *Future Outlook*...
- **Avoidance of basic copulatives:** *serves as/stands as/marks/functions as/operates as/represents [a]*, *boasts/features/maintains/offers [a]*, *refers to*
- **Collaborative communication:** *a Wikipedia-style article*, *I hope this helps*, *Of course!*, *Certainly!*, *You're absolutely right!*, *Would you like...*, *is there anything else*, *let me know*, *more detailed breakdown*, *here is a ...*, *[check/verify/confirm]... ...before [publishing/publication/submitting]*
- **Hedging disclaimers about source availability and recommended usage:** *While specific details are limited/scarce...*, *not widely available/documented/disclosed*, *...in the provided/available sources / search results...*, *[claim] should be [treated/presented] as... rather than...*, *based on available information*, *...does not by itself establish...*...
- **Edit summaries, canned assurance:** ensured that... adheres to, refined, enhanced, enriched, streamlined, improved, in compliance/complies with, Wikipedia [guidelines/style/standards], revised, verifiability, neutrality, neutral tone, encyclopedic tone, clarity, flow
- **Edit summaries, procedural statements:** preserved/preserving, retained/retaining, avoided/avoiding, ensured/ensuring, aimed/aiming to
- **Edit summaries, citations:** added sourced [information/content/infobox/section], added verified [information/content/infobox/section], added [coverage/citations/references], improved attribution, with [independent/secondary/third-party/peer-reviewed] sources
- **Statements about knowledge cutoffs (2022–2023):** *Up to my last training update*, *as of my last knowledge update*...
- **Section summaries:** *In summary*, *In conclusion*, *Overall*...
- **Prompt refusal:** *as an AI language model*, *as a large language model*, *I cannot offer medical advice, but I can...*, *I'm sorry*...

### Constructions most common in human text (Signs of human writing > Syntax)

*there is a*, *it has a*; *wrote* (vs. *authored*), *moved* (vs. *relocated*), *used* (vs. *utilized*), *tried* (vs. *attempted*), *died* (vs. *passed away*); *one of the best*, *is the only*, *was the first*; *very*, *perhaps*, *tends to*; *as a result of*, *in order to*, *all of the*, *a part of*, *the fact that*.

## Metrics and thresholds (MET)

- Detectors (GPTZero, Pangram): "perform better than random chance" with "non-trivial error rates"; sensitive to paraphrase, markup, spacing and models unseen in training (Dugan et al., RAID, ACL 2024). A high percentage on a detector is not enough for criterion G15 (quick deletion).
- Human detection: a 2025 study (Cheng et al.) found accuracy "no better than random chance"; another (Fiedler and Döpke 2025, German theses) found a "recognition rate of 57 % for AI texts and 64 % for human-generated texts"; in a 2025 preprint (Russell et al.), expert annotators got 90% of AI texts right and wrongly flagged 3.3% of human ones; people who rarely use LLMs scored only slightly above chance.
- Reverse influence: human speech already showed LLM influence in 2024 (Yakura et al., podcasts); later studies confirm it (Geng et al. 2025; Galpin et al. 2025). "the reverse is not true: LLM output is not becoming more similar to that of human writing" (Druck et al., Graphite).
- Copula: a drop of more than 10% in "is" and "are" in 2023 academic writing (Geng and Trotta); GPT-3.5 reduced "is/are" when revising 10,000 abstracts.
- Vocabulary: qualitative threshold ("One or two [...] may be coincidental"; "lots of them, lots of times" is a strong sign).
- GPT-6: sentences "around a strict 8–20 word limit" (weak source, see above).
- Cutoff dates: public ChatGPT on 11/30/2022 (before that, AI "can be safely ruled out"); 2026 corrective framings start around July 2026 (GPT-5.6); em dash made historical from September 2026.
- Count: more than 570,000 articles tagged as unsourced.
- Mechanical verification: ISBN checksum; a DOI that resolves and leads to the right article.
- Searches the page publishes: `insource:/20[0-9][0-9]-(XX|xx)-(XX|xx)/`; `insource:"utm_source=chatgpt.com"`; `insource:"utm_source=openai"`; `insource:"utm_source=copilot.com"`; `insource:"referrer=grok.com"`; `"About Me" "My Interests" "How I Contribute"`; `"About Me" "Let's Connect"`; `"About Me" "Let's Collaborate"`; `"Dear Wikipedia Editorial Team" "I am writing to"`; `"Dear Wikipedia Editorial Team" "this message finds you well"`; `"Cite error: A list-defined reference named" "is not used in the content (see the help page)."`; replies from other users: "Fire your LLM", "Not done: your request appears to have been generated by a large language model".

## Genre and domain (GEN)

- The page applies to informational text and to Wikipedia. Note: "this guide is less useful for texts which are not informational writing"; fiction signs (whispering woods, Elara Voss) "are not listed here". Elements of AI writing also appear in editorials, blogs and fan fiction.
- Biology: ecosystem and conservation (block 1.1).
- Cultural heritage and tourism: travel-guide tone (block 4).
- People and companies: press-release tone (block 4); social media presence (block 2).
- Talk pages: em dash "much more common on discussion pages than in article text"; emoji almost always in comments and edit summaries; comments with sections and a customer-service tone (block 38).
- Edit summaries: rule of three stronger there; rigid formulas (blocks 39 to 44).
- AfC drafts, user pages and infoboxes: blocks 27, 46, 47, 48.

## Signature by model (MOD)

| Model or version | Trait the page attributes |
|---|---|
| GPT-3.5, GPT-4 | knowledge cutoff date notice (2022–2023) |
| GPT-4 (2023 to mid-2024) | first-era vocabulary list; more blatantly positive text than the new models |
| GPT-4o (May 2024 to August 2025) | "produces output with more variation from human writing than other contemporaneous language models" (Reinhart et al.); second-era list |
| GPT-4o-2024-08-06 and Grok-Beta | focus on broad context, longer answers than Gemini and Claude |
| GPT-4o-mini, Gemini-1.5-Flash | lexical variation in generated "Wikipedia-style" articles (Huang et al.) |
| GPT-5 (mid-2025 to mid-2026) | third-era list plus the notability vocabulary |
| GPT-5.1 | OpenAI's attempt to suppress the em dash |
| GPT-5.6 (July 2026) | approximate start of corrective framings ("rather than", "does not by itself establish") |
| GPT-6 (mid-2026 onward) | fourth-era list; more periods and commas, sentences of 8 to 20 words (weak source) |
| Models from September 2026 onward | em dash switched off "hard coded"; less punctuation variety, more commas and periods than human text ({{cn}}) |
| ChatGPT | `utm_source=openai`, `utm_source=chatgpt.com`; `contentReference[oaicite:1]`; curly quotes (hidden comment: rose around mid-2025); abrupt cut off with "continue generating"; the chatbot most used for editing Wikipedia (Zhou et al.) |
| Claude | the only current model with more em dashes than professional writers (The Economist, Jul. 2026); does not usually use curly quotes; edit summary with the preamble "Claude responded:"; a footnote about reasoning that leaks into the conversation |
| Gemini | does not usually use curly quotes; uses UTM little; avoids the copula like GPT (Huang et al.) |
| Gemini 1.5 Pro, Claude 3.5 Sonnet | more concise than ChatGPT and Grok |
| DeepSeek | curly quotes |
| Microsoft Copilot | `utm_source=copilot.com` |
| Grok | `referrer=grok.com`; *causal*, *empirical*, *correlate*, *underscore* in 2026 |
| Leading American models (2026) | pro-authoritarian bias on some questions |

## When not to act (NAO)

- The page's general rule: "Not all text featuring these indicators is AI-generated", because LLMs learned from human writing, including Wikipedia. The list is "descriptive, not prescriptive".
- Do not rely only on a detector or only on your own judgment (Caveats section); the detector percentage does not count for G15.
- A false accusation "can drive away new editors"; consider Dunning-Kruger and confirmation bias.
- Human signs: text from before 11/30/2022; an editor who explains the error; simple constructions, superlatives, intensifiers and isolated wordy expressions (blocks 52 to 54).
- Ineffective indicators: perfect grammar, mixed registers, "bland" prose, formal prose, isolated connectives, unsourced content, bizarre wikitext, correct wikitext (blocks 55 to 62).
- Exceptions by pattern: human press releases have cited press for decades; mentioning challenges is not the sign, the formula is; negative parallelism is common in "myths" listicles; curly quotes come from Word, macOS, iOS, LanguageTool, Chicago and citation tools; literal "underscore"; standard infobox comments; low PMIDs inserted by the VisualEditor defect (2018–2023); a link that just does not open for you; `utm_source` in a URL indexed by Google; "has been featured" (present perfect); an opening paragraph "X is..." skews the copula count; abbreviations such as "ce" in summaries; bold "Keep/Delete" in votes; repetition avoided by a non-native speaker; AI pieces generated separately; abrupt cut off from a bad copy or a copyright violation; a legitimately old `access-date`; permissions gaming in one direction only; LLM influence on human speech (people are writing more like AI).

## Rewriting techniques (TEC)

The page barely teaches rewriting, and says so: "Advice about formatting or language to avoid can be found in the policies and guidelines and the Manual of Style, but does not belong on this page." What it does give:

- Treat the sign as a clue to the real problem (verifiability, sourcing, originality), not as the problem: "Please do not merely treat these signs as the problems to be fixed; that could just make detection harder." Fix or flag according to the WikiProject AI Cleanup guide.
- Read the vocabulary list literally: a synonym of a flagged word is not flagged.
- Combine signs (em dash "most useful when taken in combination"; vocabulary counts in quantity).
- Date the text (Who Wrote That?, WikiBlame) and compare it with the era of the sign.
- Ask the editor how the error happened before concluding.
- Check the reference: open the DOI, test the ISBN checksum, search the term in the online version of the book, look for the link in the Internet Archive.

## Out of scope (FORA)

- The page does not teach evasion. It warns that fixing only the signs "could just make detection harder"; that describes using humanization as a disguise, which Humanizer does not adopt.
- It records that detectors fail with paraphrase, markup changes and spacing changes; this is data about detectors, not a technique to copy.
- Inference: the "Signs of human writing" list can be read as a recipe for looking human (inserting "very", "perhaps", "in order to"). Using it as a writing goal goes against R08; the right use is not to delete these constructions by reflex.

## What to carry into Humanizer

1. The dating of signs: several P treat as current what the page has already put under "Historical indicators" (em dash, lexical variation, summary conclusion, cutoff date, refusal).
2. The constructions the page observes as more common in human text, as protection against editing by reflex (block 54).
3. The 2026 corrective framings ("should be treated as... rather than...", "does not by itself establish", "should not be confused with"), which no P lists and which the rule on flagging gaps can itself produce.
4. The vocabulary list by era, with GPT-5 and GPT-6, and the rule "a synonym does not inherit the mark".
5. The triggers for vague association ("associated with", "in connection with") and notability ("independent coverage", "active social media presence"), two of the five most common signs today.
6. "While preserving..." and the generic list of virtues in change reports.
7. New copula forms ("ventured into politics as a candidate", "began his career as", "refers to" in openings, "holds the distinction of being").
8. The ineffective items as explicit exceptions (perfect grammar, mixed register, formal prose, isolated connectives).
9. A P18 exception for the non-native speaker; a P17 gradation for short contexts; a document title treated as an entity (block 14).

## Changes that affect Humanizer

In order of impact. "Inference" marks what the page does not say in those words.

1. **The em dash left the current signs and its absence became a sign.**
   - Page today: section "Overuse of em dashes (2022–September 2026)" inside "Historical indicators". Reason given: the sign's fame made companies suppress the em dash (GPT-5.1); in July 2026 only Claude used more em dashes than professional writers and ChatGPT used fewer; from September 2026 onward the newest models are found "hard coded to not use em dashes at all", punctuation variety dropped, "commas and periods are more likely now than even human text, and now that has become its own sign of AI writing" (this last sentence marked `{{cn}}`). The GPT-6 era of the vocabulary list adds "much more period and comma usage and shorter sentences around a strict 8–20 word limit" (source: a website review).
   - Humanizer: R10 and the personal profile forbid U+2014 in new prose; P41 says to respect that preference and not swap the em dash for "--". Nothing in the package treats comma-and-period-only punctuation as a problem.
   - Suggested change: keep the ban as a profile preference (it is the owner's decision, not an AI sign) and say so in R10 and P41; remove from any text in the package the idea that the em dash is a current sign; add to P41 or P32 that the replacement should vary (colon, parentheses, semicolon, rewrite) so as not to fall into the new uniform-punctuation sign. Inference: with the em dash banned, Humanizer tends to produce exactly the "only commas and periods" output the page describes. The page's claim has `{{cn}}`, so it counts as a warning, not measured data.

2. **Constructions Humanizer cuts are, according to the page, more common in human text.**
   - Page today: "Signs of human writing > Syntax" lists, as observed over 25 years of Wikipedia, as more common in human text: superlatives and definitive statements (*one of the best*, *is the only*, *was the first*), qualifiers and intensifiers (*very*, *perhaps*, *tends to*), isolated wordy expressions (*as a result of*, *in order to*, *all of the*, *a part of*, *the fact that*). In the promotion section: the new models "tend to avoid obviously superlative statements like 'the best'".
   - Humanizer: P02 says to remove intensifiers that do not change the information and lists "the single most", "absolutely", "incredibly"; P07 lists "the definitive list", "sempre", "todos"; P12 lists "due to the fact that"; P23 cuts a duplicated caveat. None says that these forms, in isolation, are a human mark.
   - Suggested change: add to the exceptions of P02, P07, P12 and P23 that a supported superlative, and isolated "very", "perhaps", "tends to", "in order to", "the fact that" are not signs and should not go out by reflex; the target remains accumulation and lack of support. Inference: cutting all these forms makes the text look more like current model output.

3. **Corrective warnings about sources became the newest sign, and Humanizer's rules can produce them.**
   - Page today: since July 2026 (GPT-5.6), "disclaimers about how sources should be used or other corrective framings": "[claim] should be treated as... rather than...", "...does not by itself establish...", "should not be confused with" (this one less reliable). Before July 2026 they were "verging on unheard-of". Source availability notices are among the five most common signs of October 2026.
   - Humanizer: R04 says to report incomplete access and not remove a needed caveat; R05 says to flag a material error "outside the text, if necessary"; P44 says to flag what could not be confirmed; P23 handles the calibrated caveat. No P lists these three formulas.
   - Suggested change: add the three formulas as a sign to P23 (or P14, for the "rather than" form); reinforce in R04 and P44 that the gap goes outside the delivered text (a note to the author), as R05 already does, and not as a sentence "the source does not establish X" inside the prose. Inference: the page does not mention Humanizer; the risk comes from crossing its text with R04 and P44.

4. **AI vocabulary has an era, and the package's list is stuck in the old eras.**
   - Page today: lists by era (GPT-4, GPT-4o, GPT-5, GPT-6), "delve" dropped in 2025, Grok with *causal*, *empirical*, *correlate*, and the rule "a word being overused by AI does not imply that its synonyms are also overused". The GPT-6 era brings *challenge*, *clearer*, *dependable*, *echoed*, *foster*, *leverage*, *matters*, *multifaceted*, *practical*, *prioritize*, *quietly*, *steady*, *universally*.
   - Humanizer: P11 has the right mechanism (assess, do not swap), but `references/en/final-pass.md` mixes eras without dates, has "delve" and "showcase" and lacks *align with*, *bolster*, *garner*, *intricate*, *meticulous*, *underscore*, *vibrant*, *valuable*, *emphasizing*, *enhance*, and the GPT-6 list (except *foster* and *leverage*).
   - Suggested change: date the watchlist in `references/en/final-pass.md` by the era the page gives, add the missing words and write in P11 that a synonym of a flagged word is not flagged. Mark the GPT-6 era as weakly sourced (website review).

5. **Vague association and emphasis on coverage are two of the five most common signs today, with weak coverage in the catalog.**
   - Page today: "vague expression of connection or association" (*associated with*, *in connection with*) and "canned emphasis on source attribution and media coverage" (*independent coverage*, *featured in*, *active social media presence*, *trade publications*) are in the October 2026 overview; the emphasis on coverage "is more common in text from AI tools released in 2025 or later".
   - Humanizer: P04 covers vague relationships with abstract examples ("conecta dimensões de um ecossistema complexo", that is, "connects dimensions of a complex ecosystem"); P03 covers prestige with "featured in leading outlets". Neither has the current triggers.
   - Suggested change: add to P04 the association triggers and the pair "taught science at" against "was connected with science education at"; add to P03 the coverage triggers and the rule to say what the source says, not where it appeared.

6. **Isolated connectives moved to "Ineffective indicators".**
   - Page today: "Transition words (in isolation)" is ineffective; only a few connectives are overused by AI, the habit exists in human essays and is accepted by style guides; "Additionally" remains in the vocabulary list, era 2023 to mid-2024.
   - Humanizer: P21 already says to keep the logical relationship and impose no limit (aligned). `references/en/final-pass.md` lists "furthermore, moreover, additionally" as a mechanical transition without saying the sign is weak.
   - Suggested change: write in `references/en/final-pass.md` and in P21 that an isolated connective is not a sign; the problem is the rotation without a logical relationship. The personal profile rule against opening a paragraph with "Além disso", "Portanto" or "Contudo" (Portuguese connectives) is a style preference for PT-BR; the page does not speak about Portuguese.

7. **The report format "I rewrote X preserving Y" is a sign of an AI summary.**
   - Page today: summaries with "preserved/retained/avoided/ensured" and "while preserving the original meaning" (July 2026) and generic lists of virtues (*clarity*, *flow*, *neutral tone*, *improved*); the explanation is that the AI was told to do X and Y "but to specifically preserve or avoid changing Z".
   - Humanizer: R12 and P38 only ask for a report when requested and an "objective summary of decisions". Nothing forbids the generic format.
   - Suggested change: add to P38 that, when there is a report, it says what changed in concrete terms, with no "preservei o sentido" ("I preserved the meaning") and no list of virtues (clarity, flow, tone). Inference: the page deals with Wikipedia edit summaries; applying it to rewrite reports is our extension.

8. **Copula: new and longer forms.**
   - Page today: "especially in more recent AI output" the copula avoidance comes elaborated and tied to vague association: "ventured into politics as a candidate", "began his career as", "refers to" in openings; also "maintains", "operates as", "holds the distinction of being".
   - Humanizer: P13 lists "serves as", "stands as", "functions as", "boasts".
   - Suggested change: add these triggers to P13.

9. **Lexical variation moved to "Historical indicators".**
   - Page today: "Lexical diversity/elegant variation" is under "Historical indicators", attributed to "Older AI models" with a repetition penalty; the heading gives no period; the reason is only the section's ("much less frequent in newer models"). It adds that non-native speakers avoid repetition because of schooling (Italian example).
   - Humanizer: P18 treats synonym rotation as an editorial problem (clarity of reference), not as an AI sign. That remains valid.
   - Suggested change: none to the mechanism; note in P18 that, as an AI sign, it is historical, and add to the exception the non-native speaker who varies because of training, so as not to "fix" the author's voice without being asked.

10. **Other signs the page made historical that the package treats as current.**
    - Page today: "Section summaries" (older LLMs), "Statements about knowledge cutoffs (2022–2023)", "Prompt refusal" ("increasingly rare"), "Abrupt cut offs" ("used to"), "Outdated access-date parameters" ("newer chatbots seldom"). Emoji stays in Style, but "more rare now". The didactic "important to note" is in the current section, dated "Older LLMs (~2023)".
    - Humanizer: P34, P37, P43 and P40 do not mark an era.
    - Suggested change: low impact, because these P deal with editorial problems that remain valid; just do not cite these items as a current AI sign in package text.

11. **Mixed register moved to "Ineffective indicators".**
    - Page today: "Combination of casual and formal registers" is ineffective (technical field, youth, neurodivergence, several authors).
    - Humanizer: P39 treats inadequate register as a fit problem, with academic and institutional exceptions.
    - Suggested change: add to P39 that mixed register is not an AI sign and is fixed only when it gets in the reader's or the request's way.

12. **False ranges disappeared from the page.**
    - Page today: no section on "from X to Y" in this revision, neither current nor historical.
    - Humanizer: P19 deals with false ranges.
    - Suggested change: keep P19 as an editorial problem and do not cite Wikipedia as its source. Inference: the absence does not say why it left.

13. **Fine adjustments.**
    - Rule of three "stronger" in a short context (P17); curly quotes tied to ChatGPT and DeepSeek, not to Gemini and Claude (P41 already protects); list title treated as an entity with no P (block 14); `utm_source` shows the origin of the source without proving authorship of the text (P44 already says not to strip functional parameters).
