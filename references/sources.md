# Sources and evidence

Sources behind the catalog and the cautions in this skill: Wikipedia editorial guides, academic research, institute research, vendor documentation and a style guide. None of them becomes a rule on its own. Core rules R01-R12 prevail, and a research finding enters the catalog only after passing through them.

Each source has a status:

- **Core:** supports the current catalog or cautions. The entry describes the use.
- **Under review:** record checked on 10/30/2026 (title, authors, date and identifier); the content has not yet been incorporated into the catalog.

The catalogs follow Wikipedia: `references/en/patterns.md` (EN01-EN78) follows the English page (S01) and `references/pt-br/padroes.md` (PT01-PT86) follows the Portuguese pages (S02, S03). Entries marked as additions come from other sources or editorial practice and have no section on those pages. Nothing here is a list published by a university.

## 1. Wikipedia editorial guides

**S01. Wikipedia: Signs of AI writing.** WikiProject AI Cleanup. An editorial observation guide, not Wikipedia policy and not a scientific test of authorship. Guides the English catalog, the handling of formatting and references, and the cautions about isolated signs. It keeps sections on historical signs and on signs that do not work, which should be read before treating a sign as current. Core. Recorded revision: 1382823144, of 10/30/2026.

https://en.wikipedia.org/wiki/Wikipedia:Signs_of_AI_writing

**S02. Wikipédia: Sinais de texto gerado por inteligência artificial.** Essay in Portuguese, adapted from the English page, with its own cautions about translation and varieties of Portuguese. Stresses that isolated signs can come from translation, editing or language differences. Core. Recorded revision: 73274816, of 10/23/2026.

https://pt.wikipedia.org/wiki/Wikip%C3%A9dia:Sinais_de_texto_gerado_por_intelig%C3%AAncia_artificial

**S03. Wikipédia: Grandes modelos de linguagem.** Guidance on reviewing text produced with language models. Core for the cautions on fidelity and sources. Recorded revision: 73268669, of 10/22/2026.

https://pt.wikipedia.org/wiki/Wikip%C3%A9dia:Grandes_modelos_de_linguagem

## 2. Academic research

**S04. Rodrigues, Sturm and Pinheiro, A linguistic comparison between human- and AI-generated content, iScience, 2026.** Compares Portuguese texts, including true and fake news, with outputs from GPT-4o, Mistral Large and Llama 3.3 70B, and reports tendencies in formality, structure and tone in that set. Checked against the PubMed record and abstract. The results are not generalized to every genre or model. Core.

https://pubmed.ncbi.nlm.nih.gov/41809036/

https://doi.org/10.1016/j.isci.2026.114976

**S05. Geng and Trotta, Human-LLM Coevolution: Evidence from Academic Writing, Findings of ACL 2025.** Describes changes in word frequency after marker words became publicly known. Supports the caution against fixed lists used as diagnosis; it does not establish a list of words to avoid. Core.

https://aclanthology.org/2025.findings-acl.657/

**S06. Kobak et al., Delving into LLM-assisted writing in biomedical publications through excess vocabulary, Science Advances, 2025.** Lexical frequency analysis of biomedical abstracts (first version in 2024 under the title "Delving into ChatGPT usage in academic writing through excess vocabulary"). Supports attention vocabulary as a signal of frequency, not of authorship. Does not support a sentence-length rule. Core.

https://arxiv.org/abs/2406.07016

**S07. Juzek and Ward, Why Does ChatGPT "Delve" So Much? Exploring the Sources of Lexical Overrepresentation in Large Language Models, COLING 2025.** Investigates why certain words appear in excess in model text. Under review.

https://arxiv.org/abs/2412.11385

**S08. Liang et al., GPT detectors are biased against non-native English writers, Patterns, 2023.** Detector false positives on texts by non-native speakers. Supports not treating fluency, restricted vocabulary or a detector score as proof of authorship, and the rule against impoverishing the writing of non-native speakers (R08). Core.

https://arxiv.org/abs/2304.02819

**S09. Basani, Chen et al., Diversity Boosts AI-Generated Text Detection (DivEye), 2025.** Surprisal features and the importance of feature groups in a trained detector: second-order 39.4%, distributional 34.2% and first-order differences 23.7%. These are contributions within that experiment, not detection rates. None of these numbers became a writing rule. Core.

https://arxiv.org/abs/2509.18880

**S10. Russell et al., StoryScope: Investigating idiosyncrasies in AI fiction, 2026.** Narrative-structure traits in model-generated fiction. Under review.

https://arxiv.org/abs/2604.03136

**S11. Guo et al., How Close is ChatGPT to Human Experts? Comparison Corpus, Evaluation, and Detection (HC3), 2023.** Comparative corpus of human and model answers, with analysis of length and lexical diversity. Under review.

https://arxiv.org/abs/2301.07597

**S12. Paech et al., Antislop: A Comprehensive Framework for Identifying and Eliminating Repetitive Patterns in Language Models, 2025.** Identification and removal of repetitive patterns, during generation and after it. Under review.

https://arxiv.org/abs/2510.15061

**S13. Xu et al., Base Models Look Human To AI Detectors, 2026.** Indicates that detectors react to the assistant register produced by fine-tuning, not to model use as such. Under review.

https://arxiv.org/abs/2605.19516

**S14. Cheng et al., Adversarial Paraphrasing: A Universal Attack for Humanizing AI-Generated Text, 2025.** Paraphrase attack against detectors. Recorded to delimit scope: this skill does not chase detectors and does not adopt evasion techniques. Under review.

https://arxiv.org/abs/2506.07001

**S15. Bitton et al., Detecting Stylistic Fingerprints of Large Language Models, 2025.** Style traits that distinguish model families. Under review; does not support a per-model rule selector.

https://arxiv.org/abs/2503.01659

**S16. Wu et al., A Survey on LLM-Generated Text Detection: Necessity, Methods, and Future Directions, 2023.** Review of the detection literature. Under review.

https://arxiv.org/abs/2310.14724

**S17 to S20. Detection literature.** Mitchell et al., DetectGPT (2023); Hans et al., Spotting LLMs With Binoculars (2024); Verma et al., Ghostbuster (2023); Dugan et al., RAID (2024). Context on what detectors measure and how robustly. No detector is a goal of this skill. Under review.

https://arxiv.org/abs/2301.11305

https://arxiv.org/abs/2401.12070

https://arxiv.org/abs/2305.15047

https://arxiv.org/abs/2405.07940

## 3. Company and institute research

**S21. Graphite, AI Tells, 09/16/2026, and AI Tells: Opus 5.5 Update, 10/01/2026.** Research on English articles, nine models and a shared prompt, plus the follow-up update. Illustrates differences between versions and families in that corpus; the methodology itself acknowledges the influence of the shared task. Does not support universal profiles or prohibitions in PT-BR. Core.

https://graphite.io/five-percent/research/ai-tells

https://graphite.io/five-percent/research/ai-tells-opus-5-5-update

**S22. Pew Research Center, How Much of the Internet Is Written With AI?, 08/20/2026.** Estimate of how much AI-generated text is on the internet. Context; no percentage enters how the skill works. Core.

https://www.pewresearch.org/data-labs/2026/08/20/how-much-of-the-internet-is-written-with-ai/

## 4. Vendor documentation

**S23. Anthropic, Prompting Claude Fable 5.1, sections Writing density and Formatting in chat.** Discusses dense prose and too little structure in some cases. Supports intervening according to the observed problem, not permanent bans on lists, headings or long sentences. Core.

https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/prompting-claude-fable-5-1

## 5. Style guide

**S24. Google developer documentation style guide, Hyphens.** Contextual recommendations for compounds and precedence of the project's own convention. Supports not removing hyphens just because they appear often (R09). Core.

https://developers.google.com/style/hyphens

## 6. What can be said about model families

| Family or set | Usable observation | Limit |
|---|---|---|
| GPT in the S21 corpus | certain corrective contrasts and qualifications deserve review when excessive | English-only, specific versions and task; not exclusive to the family |
| Claude in the S21 corpus | "less X, more Y" comparisons and emphatic evaluations show up as points of attention | do not attribute to every version; keep pertinent comparisons |
| Gemini in the S21 corpus | intensifiers, formal transitions and guide-like language show up in the studied set | do not conclude that all Gemini text has this form |
| GPT-4o, Mistral Large and Llama 3.3 70B in S04 | tendencies in formality, structure and positivity in Portuguese | do not extrapolate to every field, version and configuration |
| DeepSeek, Grok, Qwen, GLM, Kimi and others | apply the same general editorial rules | there is no validated comparative signature for each family |

This table guides attention; it is not a per-model rule selector. Citation artifacts can come from the interface, the integration or the export; they do not necessarily reveal which model wrote the text.

## 7. Claims in circulation that were not adopted

| Claim | Decision and reason |
|---|---|
| "AI is 87.3% more analytical"; "LIWC, 500K+ texts" | No primary source found with that scope. Not used, without declaring all LIWC research invalid. |
| Fixed detectability percentages per family; 23% hedges; 3x parentheses; 2.4x punctuation | No comparable primary source supports these profiles as a general rule. Not used. |
| DeepSeek with 74.2% overlap and about 18% fabrication | Not confirmed for the scope described. Not used as characteristics of the family. |
| Sentences of 15 to 25 words, or length sequences, as an authorship classification | Not supported by the lexical research (S06) and unsuitable as an editing rule. |
| "Asking for naturalness is useless" and "swapping words never changes the distribution" | Generalizations without enough support. Replaced by contextual editorial guidance. |
| Grammar checker always increases detectability; 81% bypass and 68% preservation | Numbers without recoverable methodology for this use. Not used. |
| Binoculars as the "best detector" and a divergence that is "impossible to fake" | Superlative and universal guarantee. The skill does not rank detectors. |
| Commercial rankings and universal accuracy ranges | They depend on corpus, version, language, threshold and task. Outside the core and the criteria. |
| Misinformation-detection statistics treated as AI detection | Different tasks. Results from S04 do not become an authorship identification rate. |
| Universal timeline for replacing detectors with watermarks | A prediction the task does not need. Not used as fact or rule. |
| Regulation, fines and individual accusation cases | Outside the scope of a writing skill. No legal opinion. |

"Not confirmed" describes the result of the check, not proof that something does not exist. Editorial decisions such as protecting modality and separating translation from editing are project choices, not findings attributed to this research.

## 8. Where the catalogs cite each source

| Source | Cited by |
|---|---|
| S01 | EN01 to EN61 (page sections); the other EN entries are additions |
| S02 | PT01 to PT69 (page sections) |
| S03 | PT70 to PT76 |
| S04 | EN08, EN09, EN53, PT09, PT10, PT44, PT58, PT60 |
| S05, S06 | EN10, PT11 |
| S21 | EN05, EN12, EN13, EN14, EN45, EN54, EN65, PT06, PT13, PT14, PT15, PT61, PT78 |
| S23 | EN19, EN72, PT20, PT83 |
| S24 | EN59, PT66 |
| S07 to S20, S22 | not cited by an entry; context for the cautions in the core |

Editorial additions (EN62 to EN78, PT77 to PT86) without a source in this table are marked "editorial" in their **Sources** line.

## 9. Maintenance

When adding an empirical claim, record the primary source, date, language, models and versions, task, sample, metric and limitations. A new number does not automatically become a writing instruction. For an editorial rule, record the problem, the fix, the exception and a regression case.

Before each release, check whether pages S01 to S03 changed since the incorporated revision (procedure in the README). When moving a source from "under review" to "core", describe the use in the entry.

External sources keep their own licenses; the notice below does not relicense the articles, research or pages cited.

## License notice

Parts of this package derive from work published under the MIT license. The original notice accompanies the package, as the license requires; the full text for the package is in the `LICENSE` file.

```text
MIT License

Copyright (c) 2025 Siqi Chen

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
```
