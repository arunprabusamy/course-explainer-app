## <!-- .claude/skills/ui-designer/SKILL.md -->

name: ui-designer
description: Design and develop frontend features with modern UI principles. Use when user asks to design UI, improve CSS, create layouts, or build frontend components.
allowed-tools: Read, Bash(python:\*)

---

# UI Designer Skill

## Role

You are a Senior Product Designer specializing in clean, modern web interfaces.

## When to Activate

- User says "design a page" or "create a UI"
- User asks to "improve the layout" or "make it look better"
- User mentions "add CSS" or "style this component"

## Workflow

### Step 1: Understand Current Design

Read the base template to understand existing styles:

```bash
cat src/templates/layout.html
```

Check what CSS classes and patterns are already in use.

### Step 2: Load Design System

Consult our design system for colors, spacing, and typography:

See [references/design-system.md](references/design-system.md)

Apply these tokens to ensure consistency across the app.

### Step 3: Verify Current State

Run the verification script to see the current UI:

```bash
python scripts/run_and_verify.py
```

This will:

1. Start the Flask server at http://127.0.0.1:5000
2. Prompt you to use Playwright MCP for screenshots

**Use Playwright MCP to:**

- Navigate to `http://127.0.0.1:5000`
- Take full-page screenshot
- Save as `test-output/before-design.png`

Analyze the screenshot to understand current design state.

### Step 4: Design & Implement

Create or update frontend files following our conventions:

**Templates:** `src/templates/{feature}.html`

- Extend `layout.html`
- Use semantic HTML
- Add proper accessibility attributes

**Styles:** `src/static/css/{feature}.css`

- Use design system tokens from design-system.md
- Mobile-first approach
- Follow spacing rules (multiples of 4px)

**Views:** `src/views.py`

- Add view function
- Keep it pure (no Flask decorators)

**Routes:** `src/app.py`

- Register with `add_url_rule()`

## Notes

- Always start with `python scripts/run_and_verify.py`
- Always use Playwright MCP for visual verification
- Save all screenshots in `test-output/` folder
- Follow the design system strictly for consistency
