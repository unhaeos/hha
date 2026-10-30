#!/usr/bin/env python3
"""Install hha in one project without Git, global configuration or dependencies."""
import argparse
import os
from pathlib import Path
import re
import sys


def install(project, layout):
    source = Path(__file__).resolve().parents[1]
    project = project.resolve()
    if not project.is_dir():
        raise ValueError('Project directory does not exist.')
    bundle = project / '.hha'
    skills_root = project / ('.codex' if layout == 'codex' else '.agents') / 'skills'
    files = {}
    for name in ('AGENTS.md', 'LICENSE', 'THIRD_PARTY.md'):
        files[bundle / name] = (source / name).read_bytes()
    for name in ('skills', 'templates'):
        for item in (source / name).rglob('*'):
            if item.is_file():
                files[bundle / item.relative_to(source)] = item.read_bytes()
    for skill in sorted((source / 'skills').iterdir()):
        entry = skill / 'SKILL.md'
        if not entry.is_file():
            continue
        destination = skills_root / skill.name / 'SKILL.md'
        body = entry.read_text(encoding='utf-8')

        def rewrite(match):
            link = match.group(1)
            if re.match(r'^[a-zA-Z]+://|^#', link):
                return match.group(0)
            relative = os.path.relpath(bundle / 'skills' / skill.name / link, destination.parent)
            return '](' + Path(relative).as_posix() + ')'

        files[destination] = re.sub(r'\]\(([^)]+)\)', rewrite, body).encode('utf-8')
    agent_path = project / 'AGENTS.md'
    marker = '<!-- hha:start -->'
    block = (marker + '\nRead `.hha/AGENTS.md` for the hha workflow and writing rules. '
             'Paths inside it are relative to `.hha/`; application output belongs in this project.\n'
             '<!-- hha:end -->\n')
    old = agent_path.read_text(encoding='utf-8') if agent_path.exists() else ''
    if marker in old:
        if block not in old:
            raise ValueError('Existing hha AGENTS block differs; review it manually.')
    else:
        files[agent_path] = (old + ('\n\n' if old else '') + block).encode('utf-8')
    for path, content in files.items():
        if not path.resolve().is_relative_to(project):
            raise ValueError(f'Path leaves project: {path}')
        if path != agent_path and path.exists() and path.read_bytes() != content:
            raise ValueError(f'Existing file differs; nothing written. Review before updating: {path}')
    written = 0
    for path, content in files.items():
        if path.exists() and path.read_bytes() == content:
            continue
        path.parent.mkdir(parents=True, exist_ok=True)
        with path.open('wb') as output:
            output.write(content)
        written += 1
    print(f'Installed hha: {skills_root}; {written} file(s) written.')
    print('Project AGENTS.md preserves prior instructions. No global settings were changed.')
    print('Check the skill list in Codex; restart it if these skills do not appear.')


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('project', type=Path)
    parser.add_argument('--layout', choices=('agents', 'codex'), default='agents',
                        help='agents: current documented project path; codex: compatibility layout')
    args = parser.parse_args()
    try:
        install(args.project, args.layout)
    except (OSError, ValueError) as error:
        print(f'Install failed: {error}', file=sys.stderr)
        sys.exit(1)
