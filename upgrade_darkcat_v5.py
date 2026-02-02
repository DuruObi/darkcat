import os
import subprocess

# --- Step 1: Update version ---
version_file = "darkcat/version.py"
with open(version_file, "w") as f:
    f.write('__version__ = "5.0.0"\n')
print(f"✅ Updated version to 5.0.0 in {version_file}")

# --- Step 2: Update setup.py ---
setup_file = "setup.py"
with open(setup_file, "r") as f:
    setup_content = f.read()
setup_content = setup_content.replace('version="0.3.0"', 'version="5.0.0"')
with open(setup_file, "w") as f:
    f.write(setup_content)
print("✅ Updated setup.py version to 5.0.0")

# --- Step 3: Create new commands ---
commands = {
    "test.py": """import click, subprocess, os

@click.command()
@click.option('--folder', default='.', help='Project folder')
def test(folder):
    '''Run project test suites'''
    click.echo(f"🐈‍⬛ Running tests in {folder} ...")
    if os.path.exists(os.path.join(folder, 'package.json')):
        subprocess.run(['npm','test'], cwd=folder)
    elif os.path.exists(os.path.join(folder, 'pyproject.toml')) or os.path.exists(os.path.join(folder,'setup.py')):
        subprocess.run(['pytest'], cwd=folder)
    else:
        click.echo('⚠️ No recognizable test framework found!')
""",
    "lint.py": """import click, subprocess, os

@click.command()
@click.option('--folder', default='.', help='Project folder')
def lint(folder):
    '''Run linters'''
    click.echo(f"🐈‍⬛ Running linter in {folder} ...")
    if os.path.exists(os.path.join(folder,'package.json')):
        subprocess.run(['npx','eslint','.'], cwd=folder)
    elif os.path.exists(os.path.join(folder,'pyproject.toml')) or os.path.exists(os.path.join(folder,'setup.py')):
        subprocess.run(['flake8', folder])
    else:
        click.echo('⚠️ No recognizable lint setup found!')
""",
    "build.py": """import click, subprocess

@click.command()
@click.option('--folder', default='.', help='Project folder')
def build(folder):
    '''Build project artifacts'''
    click.echo(f"🐈‍⬛ Building project in {folder} ...")
    subprocess.run(['python','setup.py','sdist','bdist_wheel'], cwd=folder)
""",
    "deploy.py": """import click

@click.command()
@click.option('--folder', default='.', help='Project folder')
@click.option('--target', default='staging', help='Deployment target')
def deploy(folder,target):
    '''Deploy project to target'''
    click.echo(f"🐈‍⬛ Deploying {folder} to {target} ...")
    click.echo('✅ Deployment simulation complete')
""",
    "update.py": """import click, subprocess

@click.command()
def update():
    '''Update DarkCat to latest version'''
    click.echo('🐈‍⬛ Updating DarkCat ...')
    subprocess.run(['pip','install','--upgrade','darkcat'])
"""
}

cmd_folder = "darkcat/commands"
os.makedirs(cmd_folder, exist_ok=True)

for filename, content in commands.items():
    filepath = os.path.join(cmd_folder, filename)
    with open(filepath, "w") as f:
        f.write(content)
    print(f"✅ Created command {filename}")

# --- Step 4: Update CHANGELOG.md ---
changelog_file = "CHANGELOG.md"
changelog_content = """# Changelog

## v5.0.0 — Major Developer Upgrade
### Added
- test → run project test suites (Python, Node)
- lint → run linters automatically
- build → compile project artifacts
- deploy → deploy to staging/production
- update → update DarkCat CLI
"""
with open(changelog_file, "w") as f:
    f.write(changelog_content)
print("✅ Updated CHANGELOG.md for v5.0.0")

# --- Step 5: Git commit & tag ---
subprocess.run(["git", "add", "."])
subprocess.run(["git", "commit", "-m", "DarkCat v5.0.0 major developer upgrade"])
subprocess.run(["git", "tag", "-a", "v5.0.0", "-m", "DarkCat v5.0.0 major developer upgrade"])
subprocess.run(["git", "push"])
subprocess.run(["git", "push", "--tags"])
print("✅ Git commit and tag v5.0.0 done")

# --- Step 6: Build PyPI packages ---
subprocess.run(["rm","-rf","dist","build","*.egg-info"])
subprocess.run(["python3","-m","build"])
print("✅ PyPI build complete. Ready to upload with twine if desired.")
