# Changelog

All notable changes to this project are recorded here. Versions follow [Semantic Versioning](https://semver.org/): a new or removed pattern is a minor change, a change to the core rules (R01-R12) or to the file layout is a major change.

## [7.0.0] - 2026-10-30

First public release.

### Changed

- The em dash is no longer banned. Wikipedia lists its overuse only as a historical indicator (2022 to September 2026), so the skill keeps it as ordinary punctuation.

### Added

- `SKILL.md` at the repository root, so the whole repository is the skill folder. The core holds scope, priorities, rules R01-R12, the procedure and the modes; detail lives in `references/` and loads on demand.
- Two catalogs with independent numbering, each following its own Wikipedia page: `references/en/patterns.md` (EN01-EN78, from English Wikipedia) and `references/pt-br/padroes.md` (PT01-PT86, from Portuguese Wikipedia). Additions from other sources or editorial practice are marked as such. Each entry ends with a **Sources** line, and each catalog ends with a mapping table from the old P01-P50 IDs.
- Wikipedia is the source of truth for what counts as a sign. Historical and ineffective indicators are listed so they are not acted on.
- Codex plugin in `plugins/codex`, built by `scripts/build-codex-plugin.py`.
- Plugin icon in `assets/icon.png`.
- Voice matching: paste a sample of your own writing and the rewrite follows its observable traits without copying opinions, typos or facts from it.
- `humanizer-revisor` subagent, read-only, in two formats: `agents/humanizer-revisor.md` (Claude Code) and `codex/humanizer-revisor.toml` (Codex).
- Claude Code plugin and marketplace manifests in `.claude-plugin/`.
- `scripts/check-wikipedia.py`, which reports when the Wikipedia pages behind the catalog changed since the last recorded revision.
- `wikipedia/`: section-by-section extraction of the English and Portuguese pages, with the revisions recorded on 2026-10-30.
- Before/after examples generated from raw model output.
- README in English and Portuguese.
