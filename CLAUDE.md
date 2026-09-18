# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

This is a small test/demo project containing:
- **ascii_art.py**: A Python script that generates "Hello Claude" ASCII art and saves it to `hello_claude.txt`
- **welcome_claude.html**: A welcome page with interactive fireworks animation (click anywhere to trigger fireworks)

## Running the Project

### Python Script
```powershell
python ascii_art.py
```
This generates ASCII art and saves it to `hello_claude.txt` in the project root.

### HTML Page
Open `welcome_claude.html` directly in a web browser to view the welcome page with fireworks animation.

## Project Structure

- `ascii_art.py` - Python script for ASCII art generation
- `welcome_claude.html` - Interactive welcome page
- `.claude/` - Claude Code configuration directory

## Git Workflow & Committing

**IMPORTANT: Always commit work to git and push to GitHub to preserve the status of work.**

### Commit Guidelines
- Write clear, descriptive commit messages that explain **what changed and why**
- Use imperative mood: "Add feature" not "Added feature" or "Adds feature"
- Keep messages concise (1-2 lines), with details in the PR description if needed
- Example messages:
  - `Add ASCII art generation feature`
  - `Update welcome page with new animations`
  - `Fix fireworks particle decay calculation`

### Typical Workflow
1. Make changes to files
2. Test your changes locally
3. Stage and commit with a clear message:
   ```powershell
   git add .
   git commit -m "Description of changes"
   ```
4. Push to GitHub:
   ```powershell
   git push origin main
   ```

### Before Pushing
- Verify your commit message is clear and descriptive
- Ensure all changes are intentional (review `git diff` before committing)
- Check that tests/scripts still work as expected

Never leave uncommitted changes at the end of a session — commit and push all work to preserve progress.
