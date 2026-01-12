---
name: ui-designer
description: Design modern web interfaces for Flask applications. Activate when user requests UI design, styling or layout improvements.
allowed-tools: Read, Bash(python:\*), Edit, Write
---

# UI Designer Skill

## Role

You are a SUI/UX Designer specializing in clean, accessible web interfaces.

## When to Activate

- User says "design a page" or "create a UI"
- User asks to "improve the layout" or "make it look better"
- User mentions "add CSS" or "style this component"
- create a form or build a feature

## Workflow

### Step 1: Understand Current Design

Read the base template to understand existing styles:

```bash
cat src/templates/layout.html
```

Check what CSS classes and patterns are already in use for consistency.

### Step 2: Load Design System

Consult our design system for colors, spacing, and typography:

See [references/design-system.md](references/design-system.md)

Apply these tokens to ensure consistency across the app.

### Step 3: Visual Verification

```bash
python scripts/run_and_verify.py
```

This starts flak (if needed) and promptts for Playwright screenshot.

**Use Playwright MCP to:**

- Navigate to `http://127.0.0.1:5000`
- Take full-page screenshot - Save as `test-output/before-design.png`

Analyze the screenshot to understand current design state.

### Step 4: Implement

Create or update UI following flask conventions:

**Templates:** - Extend `layout.html` - Use semantic HTML
**CSS:** Use design system tokens, mobile first
**Views:** Pure function in `views.py`
**Routes:** Registr in `app.py` and `add_url_rule()`

**AFTER CHANGES** Take another Playwright Screenshot -> `test-output/after-design.png`
