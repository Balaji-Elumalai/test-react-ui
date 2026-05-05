# Bootstrap 5 Projects: Stage 4 Framework Implementation

**Back to:** [Stage 4: Core Design System Decisions](stage-4-theming-and-design-system.md)

**Framework:** Bootstrap 5 (Component-First, Utility-First)  
**Syncfusion Theme:** Bootstrap5  
**Implementation Stage:** Stage 4 (Design System) → Stage 5 (Code Generation) → Stage 6 (Validation)

---

## Overview

Bootstrap 5 is a component framework with utility-first styling. You use semantic color names, 8pt spacing grid, and responsive utilities to build consistent UIs.

**Output:** Bootstrap 5 design system decisions documented for Stage 5 code generation.

---

## Table of Contents

1. [Setup & Installation](#setup--installation)
2. [Bootstrap Philosophy](#bootstrap-philosophy)
3. [Color System (Semantic)](#color-system-semantic)
4. [Spacing Grid (8pt)](#spacing-grid-8pt)
5. [Typography System](#typography-system)
6. [Responsive Breakpoints](#responsive-breakpoints)
7. [Grid System](#grid-system)
8. [Configuration](#configuration)
9. [Stage 5: Code Generation](#stage-5-code-generation)
10. [Stage 6: Validation Checklist](#stage-6-validation-checklist)

---

## Setup & Installation

### 1. Install Bootstrap

```bash
npm install bootstrap
```

### 2. Create SCSS Configuration (`src/bootstrap-config.scss`)

```scss
// Override Bootstrap defaults BEFORE importing Bootstrap
$primary: #0891b2;
$secondary: #536d7e;
$success: #10b981;
$danger: #ef4444;
$warning: #f59e0b;
$info: #3b82f6;
$light: #f9fafb;
$dark: #1f2937;

// Spacing
$spacer: 1rem; // 16px
$spacers: (
  xs: ($spacer * 0.25),  // 4px
  sm: ($spacer * 0.5),   // 8px
  md: ($spacer * 1),     // 16px
  lg: ($spacer * 1.5),   // 24px
  xl: ($spacer * 2),     // 32px
  '2xl': ($spacer * 3),  // 48px
);

// Typography
$font-size-base: 16px;
$font-size-sm: 14px;
$font-size-lg: 18px;
$line-height-base: 1.5;

// Import Bootstrap
@import '../../node_modules/bootstrap/scss/functions';
@import '../../node_modules/bootstrap/scss/variables';
@import '../../node_modules/bootstrap/scss/bootstrap';
```

### 3. Import in `src/main.tsx`

```tsx
import React from 'react'
import ReactDOM from 'react-dom/client'
import App from './App.tsx'

// Syncfusion Bootstrap5 theme
import '@syncfusion/ej2-bootstrap5-theme/styles/bootstrap5.css'

// Bootstrap config and styles
import './bootstrap-config.scss'

ReactDOM.createRoot(document.getElementById('root')!).render(
  <React.StrictMode>
    <App />
  </React.StrictMode>,
)
```

---

## Bootstrap Philosophy

**Utility-First Foundation:** Bootstrap provides utilities for spacing, colors, display, and responsive design.

- **Semantic Colors:** 9 semantic names (primary, secondary, success, danger, warning, info, light, dark, body)
- **8pt Spacing Grid:** Base unit is 1rem (16px); scale: 0.25x, 0.5x, 1x, 1.5x, 2x, 3x
- **Responsive Utilities:** Mobile-first prefixes (`sm:`, `md:`, `lg:`, `xl:`, `xxl:`)
- **12-Column Grid:** Layout system with responsive breakpoints
- **Component Utilities:** Reusable patterns for common UI elements

**You're committing to:** Bootstrap's conventions for speed and consistency.

---

## Color System (Semantic)

### Bootstrap Semantic Colors

**9 Named Colors:**
```ts
primary:   #0891b2  // Brand color, CTAs
secondary: #536d7e  // Secondary actions
success:   #10b981  // Success states
danger:    #ef4444  // Errors, destructive
warning:   #f59e0b  // Warnings
info:      #3b82f6  // Information
light:     #f9fafb  // Light backgrounds
dark:      #1f2937  // Dark backgrounds
body:      #1c1b1f  // Body text
```

### Usage as CSS Classes/Variables

```tsx
// Background colors
<div className="bg-primary">Primary background</div>
<div className="bg-success">Success background</div>
<div className="bg-danger">Danger background</div>

// Text colors
<p className="text-primary">Primary text</p>
<p className="text-secondary">Secondary text</p>

// Borders
<div className="border border-primary">Primary border</div>
<div className="border border-success">Success border</div>

// CSS variables (if using SCSS)
<div style={{ backgroundColor: 'var(--bs-primary)', color: 'var(--bs-light)' }}>
  Using Bootstrap CSS variables
</div>
```

### Dark Mode

Toggle dark mode by adding `data-bs-theme="dark"` to `<html>`:

```tsx
// In your theme provider
const toggleDarkMode = (isDark) => {
  document.documentElement.setAttribute('data-bs-theme', isDark ? 'dark' : 'light')
}
```

---

## Spacing Grid (8pt)

Bootstrap uses **1rem = 16px** as base. Scale multipliers: 0.25x, 0.5x, 1x, 1.5x, 2x, 3x...

### Spacing Scale

```ts
--bs-spacer: 1rem (16px)

xs: 4px   (0.25rem)
sm: 8px   (0.5rem)
md: 16px  (1rem)
lg: 24px  (1.5rem)
xl: 32px  (2rem)
2xl: 48px (3rem)
```

### Usage as Utilities

```tsx
// Padding
<div className="p-3">Padding 16px</div>
<div className="p-md">Padding 16px (Bootstrap alias)</div>
<div className="px-4 py-2">Horizontal 24px, vertical 8px</div>

// Margin
<div className="m-2">Margin 8px</div>
<div className="mt-3 mb-2">Margin top 16px, bottom 8px</div>
<div className="ms-auto">Margin-left auto (push right)</div>

// Gap (flexbox/grid)
<div className="d-flex gap-3">Gap 16px</div>
<div className="row g-4">Grid gutter 24px</div>
```

**Rule:** Use Bootstrap spacing scale. Never arbitrary values like `px-7` or `p-18`.

---

## Typography System

### Bootstrap Typography Scale

```ts
Body text (base):      16px / 1.5 line-height / 400 weight
Small text:            14px / 1.5 line-height / 400 weight
Large text:            18px / 1.5 line-height / 400 weight

Display 1:             56px / 1.2 line-height / 300 weight
Display 2:             48px / 1.2 line-height / 300 weight
Display 3:             40px / 1.2 line-height / 300 weight
Display 4:             32px / 1.2 line-height / 300 weight
Display 5:             28px / 1.2 line-height / 300 weight
Display 6:             24px / 1.2 line-height / 300 weight

H1: 36px / 700 weight
H2: 32px / 700 weight
H3: 28px / 700 weight
H4: 24px / 700 weight
H5: 20px / 700 weight
H6: 16px / 700 weight

Lead: 20px / 1.5 line-height (emphasized body)
Small/Muted: 14px / 400 weight
```

### Usage as Classes

```tsx
// Headings
<h1>H1 automatic Bootstrap styling</h1>
<h2 className="display-3">Display text</h2>

// Body text utilities
<p className="lead">Lead text (emphasized)</p>
<p className="small">Small text</p>
<p className="text-muted">Muted text</p>

// Custom sizing
<p className="fs-3">Font size 3 (28px)</p>
<p className="fw-bold">Font weight bold</p>
```

---

## Responsive Breakpoints

### Bootstrap's 6 Breakpoints

```ts
xs:  < 576px   (mobile, default)
sm:  ≥ 576px   (small phones)
md:  ≥ 768px   (tablets)
lg:  ≥ 992px   (desktops)
xl:  ≥ 1200px  (large desktops)
xxl: ≥ 1400px  (extra large)
```

### Mobile-First Utilities

```tsx
// Responsive padding
<div className="p-2 md:p-3 lg:p-4">
  Mobile 8px → Tablet 16px → Desktop 24px
</div>

// Responsive display
<div className="d-none d-md-block">Hide on mobile, show on tablet+</div>
<div className="d-md-none">Show on mobile, hide on tablet+</div>

// Responsive grid columns
<div className="row">
  <div className="col-12 col-md-6 col-lg-4">Responsive column</div>
</div>

// Responsive text alignment
<p className="text-start text-md-center text-lg-end">
  Left on mobile → center on tablet → right on desktop
</p>
```

**Rule:** Start with mobile (base), add `md:`, `lg:`, `xl:` prefixes for larger screens.

---

## Grid System

### 12-Column Responsive Grid

```tsx
// Basic grid
<div className="row">
  <div className="col">Auto-width column</div>
  <div className="col">Auto-width column</div>
</div>

// Responsive columns
<div className="row">
  <div className="col-12 col-md-6 col-lg-4">
    Mobile: 100% width
    Tablet: 50% width
    Desktop: 33% width
  </div>
</div>

// Grid with gutters
<div className="row g-3">  {/* 16px gutter */}
  <div className="col-md-6"></div>
  <div className="col-md-6"></div>
</div>

// Nested grid
<div className="row">
  <div className="col-md-8">
    <div className="row">
      <div className="col-6">Nested</div>
      <div className="col-6">Nested</div>
    </div>
  </div>
</div>
```

---

## Configuration

All Bootstrap decisions live in:
- `src/bootstrap-config.scss` — SCSS variables (colors, spacing, typography)
- Bootstrap CSS variables — Runtime access via `var(--bs-primary)`, etc.
- `tailwind.config.js` or similar — If using responsive utilities

---

## Stage 5: Code Generation

### Generated Components Use Bootstrap Utilities

```tsx
// ✅ CORRECT: Bootstrap semantic colors + utilities
<div className="bg-primary text-white p-4 rounded">
  Primary card with padding
</div>

<div className="row g-3">
  <div className="col-md-6">
    <p className="text-secondary small">Secondary text</p>
  </div>
</div>

// Status colors
<span className="badge bg-success">Success</span>
<span className="badge bg-danger">Error</span>
<span className="badge bg-warning">Warning</span>
```

### Syncfusion Components

Syncfusion Bootstrap5 theme automatically styles components:

```tsx
import { GridComponent, ColumnsDirective, ColumnDirective } from '@syncfusion/ej2-react-grids'

export function DataGrid() {
  return (
    <GridComponent dataSource={data}>
      {/* Inherits Bootstrap5 styling automatically */}
      <ColumnsDirective>
        <ColumnDirective field="name" />
      </ColumnsDirective>
    </GridComponent>
  )
}
```

---

## Stage 6: Validation Checklist

- ✅ All colors use Bootstrap semantic names (primary, secondary, success, danger, warning, info)
- ✅ All spacing from Bootstrap scale (xs, sm, md, lg, xl, 2xl)
- ✅ Typography uses Bootstrap scale (body, h1-h6, display, lead)
- ✅ Responsive utilities follow mobile-first pattern (`col-md-6`, `d-lg-block`)
- ✅ Grid system uses 12 columns correctly
- ✅ No hardcoded colors, spacing, or font sizes
- ✅ Dark mode works with `data-bs-theme="dark"` toggle
- ✅ Text contrast ≥ 4.5:1 (WCAG AA)
- ✅ Touch targets ≥ 44x44px
- ✅ Syncfusion Bootstrap5 theme imports at app entry
- ✅ Build succeeds without CSS conflicts
