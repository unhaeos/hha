import importlib.util
from pathlib import Path
import re
import tempfile
import unittest


spec = importlib.util.spec_from_file_location('hha_install', Path(__file__).with_name('install.py'))
installer = importlib.util.module_from_spec(spec)
spec.loader.exec_module(installer)


class InstallationTests(unittest.TestCase):
    def test_no_git_preserve_instructions_and_resolve_resources(self):
        with tempfile.TemporaryDirectory() as directory:
            project = Path(directory)
            (project / 'AGENTS.md').write_text('Existing project instructions.\n', encoding='utf-8')
            installer.install(project, 'agents')
            self.assertFalse((project / '.git').exists())
            agent_text = (project / 'AGENTS.md').read_text(encoding='utf-8')
            self.assertTrue(agent_text.startswith('Existing project instructions.\n'))
            entries = list((project / '.agents/skills').glob('*/SKILL.md'))
            self.assertEqual(len(entries), 5)
            for entry in entries:
                for link in re.findall(r'\]\(([^)]+)\)', entry.read_text(encoding='utf-8')):
                    if not re.match(r'^[a-zA-Z]+://|^#', link):
                        self.assertTrue((entry.parent / link).is_file(), (entry, link))
            installer.install(project, 'agents')
            self.assertEqual((project / 'AGENTS.md').read_text(encoding='utf-8'), agent_text)

    def test_conflict_writes_nothing(self):
        with tempfile.TemporaryDirectory() as directory:
            project = Path(directory)
            entry = project / '.agents/skills/hha-plan/SKILL.md'
            entry.parent.mkdir(parents=True)
            entry.write_text('User content', encoding='utf-8')
            with self.assertRaises(ValueError):
                installer.install(project, 'agents')
            self.assertEqual(entry.read_text(encoding='utf-8'), 'User content')
            self.assertFalse((project / 'AGENTS.md').exists())
            self.assertFalse((project / '.hha').exists())

    def test_codex_layout(self):
        with tempfile.TemporaryDirectory() as directory:
            project = Path(directory)
            installer.install(project, 'codex')
            self.assertEqual(len(list((project / '.codex/skills').glob('*/SKILL.md'))), 5)
            self.assertFalse((project / '.agents').exists())


if __name__ == '__main__':
    unittest.main()
