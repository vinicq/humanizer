"""Builds the Codex plugin in plugins/codex/ from the skill at the repository root.

Codex loads plugin skills only from skills/<name>/SKILL.md inside the plugin, so the
plugin carries a copy of SKILL.md, references/ and agents/openai.yaml. The root stays
the only place to edit.

Usage:
  python scripts/build-codex-plugin.py          rebuild the copy
  python scripts/build-codex-plugin.py --check  exit 1 if the copy is out of date
"""
import filecmp
import pathlib
import shutil
import sys

ROOT = pathlib.Path(__file__).resolve().parent.parent
PLUGIN = ROOT / 'plugins' / 'codex'
SKILL = PLUGIN / 'skills' / 'humanizer'
# source -> destination, relative to ROOT and PLUGIN
COPIES = {
    'SKILL.md': 'skills/humanizer/SKILL.md',
    'references': 'skills/humanizer/references',
    'agents/openai.yaml': 'skills/humanizer/agents/openai.yaml',
    'assets/icon.png': 'assets/icon.png',
}


def files(base, rel):
    p = base / rel
    return sorted(q.relative_to(base) for q in p.rglob('*') if q.is_file()) if p.is_dir() else [pathlib.Path(rel)]


def stale():
    out = []
    for src, dst in COPIES.items():
        want = {f.relative_to(src) if (ROOT / src).is_dir() else pathlib.Path('.') for f in files(ROOT, src)}
        have = {f.relative_to(dst) if (PLUGIN / dst).is_dir() else pathlib.Path('.') for f in files(PLUGIN, dst)} if (PLUGIN / dst).exists() else set()
        for f in want | have:
            a, b = ROOT / src / f, PLUGIN / dst / f
            if not (a.exists() and b.exists() and filecmp.cmp(a, b, shallow=False)):
                out.append((pathlib.Path(dst) / f).as_posix())
    return out


def build():
    for src, dst in COPIES.items():
        a, b = ROOT / src, PLUGIN / dst
        if b.is_dir():
            shutil.rmtree(b)
        b.parent.mkdir(parents=True, exist_ok=True)
        (shutil.copytree if a.is_dir() else shutil.copyfile)(a, b)


if __name__ == '__main__':
    if '--check' in sys.argv:
        diff = stale()
        for f in diff:
            print(f'out of date: plugins/codex/{f}')
        if diff:
            print('Run: python scripts/build-codex-plugin.py')
        sys.exit(1 if diff else 0)
    build()
    print('plugins/codex rebuilt' if not stale() else 'build failed')
