<!-- .claude/skills/ui-designer/references/design-system.md -->

# Design System

## Colors

### Primary Palette

```css
--primary: #2563eb; /* Modern Blue - buttons, links, highlights */
--primary-dark: #1e40af; /* Hover states */
--primary-light: #dbeafe; /* Backgrounds */
```

### Neutrals

```css
--bg-primary: #fafbfc; /* Main background - soft off-white */
--bg-secondary: #f1f5f9; /* Card backgrounds - light blue-gray */
--bg-accent: #e0f2fe; /* Highlight sections - very light cyan */
--text-primary: #1e293b; /* Main text */
--text-secondary: #64748b; /* Muted text */
--border: #e2e8f0; /* Borders, dividers */
```

### Semantic Colors

```css
--success: #10b981; /* Success messages */
--error: #ef4444; /* Errors, warnings */
--info: #3b82f6; /* Info messages */
```

## Typography

### Font Family

```css
font-family: Inter, system-ui, -apple-system, sans-serif;
```

### Font Sizes

```css
--text-xs: 12px; /* Small labels */
--text-sm: 14px; /* Secondary text */
--text-base: 16px; /* Body text (default) */
--text-lg: 18px; /* Emphasized text */
--text-xl: 20px; /* Small headings */
--text-2xl: 24px; /* H3 */
--text-3xl: 30px; /* H2 */
--text-4xl: 36px; /* H1 */
```

### Line Height

```css
body {
  line-height: 1.6;
}
h1,
h2,
h3 {
  line-height: 1.2;
}
```

## Spacing

**Base Unit:** 4px

**Scale:**

```css
--space-1: 4px;
--space-2: 8px;
--space-3: 12px;
--space-4: 16px;
--space-5: 20px;
--space-6: 24px;
--space-8: 32px;
--space-10: 40px;
--space-12: 48px;
--space-16: 64px;
```

**Usage:**

- Padding inside cards/buttons: 16px (--space-4)
- Margin between sections: 32px (--space-8)
- Margin between elements: 16px (--space-4)
- Body padding: 20px (--space-5)

## Border Radius

```css
--radius-sm: 4px; /* Inputs, small elements */
--radius-md: 8px; /* Cards, buttons (default) */
--radius-lg: 12px; /* Large containers */
--radius-full: 9999px; /* Pills, avatars */
```

## Shadows

```css
--shadow-sm: 0 1px 2px rgba(0, 0, 0, 0.05);
--shadow-md: 0 4px 6px rgba(0, 0, 0, 0.1);
--shadow-lg: 0 10px 15px rgba(0, 0, 0, 0.1);
```

## Components

### Button

```css
.btn {
  padding: 12px 24px; /* --space-3 --space-6 */
  background: #2563eb; /* --primary */
  color: white;
  border-radius: 8px; /* --radius-md */
  font-size: 16px; /* --text-base */
  border: none;
  cursor: pointer;
}

.btn:hover {
  background: #1e40af; /* --primary-dark */
}
```

### Card

```css
.card {
  background: #f1f5f9; /* --bg-secondary */
  border: 1px solid #e2e8f0; /* --border */
  border-radius: 8px; /* --radius-md */
  padding: 24px; /* --space-6 */
  box-shadow: 0 1px 2px rgba(0, 0, 0, 0.05); /* --shadow-sm */
}
```

### Input

```css
.input {
  padding: 12px 16px; /* --space-3 --space-4 */
  border: 1px solid #e2e8f0; /* --border */
  border-radius: 4px; /* --radius-sm */
  font-size: 16px; /* --text-base */
  width: 100%;
}

.input:focus {
  border-color: #2563eb; /* --primary */
  outline: none;
}
```

## Responsive Breakpoints

```css
/* Mobile first - default styles for mobile */

/* Tablet */
@media (min-width: 768px) {
}

/* Desktop */
@media (min-width: 1024px) {
}
```

## Quick Reference

**Every design must:**

- Use colors from the palette above
- Use spacing in multiples of 4px
- Use 8px border-radius for cards/buttons
- Use Inter font family
- Be mobile responsive
- Have minimum 16px body text

**Never:**

- Use random colors not in the palette
- Use odd spacing (e.g., 13px, 27px)
- Forget mobile responsiveness
- Use text smaller than 14px
