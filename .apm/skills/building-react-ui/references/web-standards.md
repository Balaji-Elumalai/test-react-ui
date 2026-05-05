# Web Standards & Compliance Reference

**Version:** 2.0.0  
**Last Updated:** April 17, 2026  
**Purpose:** WCAG 2.2 AA, security, performance, and code quality standards enforced during Stage 5 validation

---

## Table of Contents

1. [Accessibility Standards (WCAG 2.2 AA)](#accessibility-standards-wcag-22-aa)
2. [Security Standards](#security-standards)
3. [Performance Standards](#performance-standards)
4. [Code Quality Standards](#code-quality-standards)
5. [Validation Checklist](#validation-checklist)
6. [Auto-Fix Rules](#auto-fix-rules)

---

## Accessibility Standards (WCAG 2.2 AA)

### WCAG Principles: POUR

| Principle | Description |
|-----------|-------------|
| **P**erceivable | Content can be perceived through different senses (text alternatives, contrast, clear structure) |
| **O**perable | Interface can be operated by all users (keyboard, no traps, sufficient target size) |
| **U**nderstandable | Content and interface are understandable (clear language, predictable, error guidance) |
| **R**obust | Content works with assistive technologies (semantic HTML, proper ARIA, screen reader compatible) |

---

### Perceivable: Content Must Be Perceivable

#### 1.1 Text Alternatives

**Images require descriptive alt text:**

```html
<!-- ❌ Missing alt -->
<img src="chart.png">

<!-- ✅ Descriptive alt for informative image -->
<img src="chart.png" alt="Bar chart showing 40% increase in Q3 sales">

<!-- ✅ Empty alt for decorative image -->
<img src="decorative-border.png" alt="" role="presentation">

<!-- ✅ Complex image with detailed description -->
<figure>
  <img src="infographic.png" alt="2024 market trends infographic" 
       aria-describedby="infographic-desc">
  <figcaption id="infographic-desc">
    <!-- Detailed description here -->
  </figcaption>
</figure>
```

**Icon buttons need accessible names:**

```html
<!-- ❌ No accessible name -->
<button><svg><!-- menu icon --></svg></button>

<!-- ✅ Using aria-label -->
<button aria-label="Open menu">
  <svg aria-hidden="true"><!-- menu icon --></svg>
</button>

<!-- ✅ Using visually hidden text -->
<button>
  <svg aria-hidden="true"><!-- menu icon --></svg>
  <span class="visually-hidden">Open menu</span>
</button>
```

**Validation Rules:**
- [ ] All informative images have descriptive alt text
- [ ] Decorative images have empty alt (`alt=""`)
- [ ] Icon-only buttons have `aria-label` or hidden text
- [ ] Complex images have `aria-describedby` with detailed description

---

#### 1.2 Media Alternatives

```html
<!-- Video with captions and descriptions -->
<video controls>
  <source src="video.mp4" type="video/mp4">
  <track kind="captions" src="captions.vtt" srclang="en" label="English" default>
  <track kind="descriptions" src="descriptions.vtt" srclang="en" label="Descriptions">
</video>

<!-- Audio with transcript -->
<audio controls>
  <source src="podcast.mp3" type="audio/mp3">
</audio>
<details>
  <summary>Transcript</summary>
  <p>Full transcript text...</p>
</details>
```

**Validation Rules:**
- [ ] Videos have captions
- [ ] Videos have audio descriptions
- [ ] Auto-playing audio can be paused/stopped

---

#### 1.4 Color Contrast

**Minimum Ratios (WCAG 2.2 AA):**

| Text Type | Minimum Ratio |
|-----------|---------------|
| Normal text (< 18px / < 14px bold) | 4.5:1 |
| Large text (≥ 18px / ≥ 14px bold) | 3:1 |
| UI components & graphics | 3:1 |
| Focus indicators | 3:1 |

```css
/* ✓ GOOD - High contrast */
.button {
  color: #000000;        /* Dark text */
  background: #ffffff;   /* Light background */
  /* Contrast ratio: 21:1 */
}

/* ✗ BAD - Low contrast (fails) */
.hint {
  color: #cccccc;        /* Light gray */
  background: #ffffff;   /* Light background */
  /* Contrast ratio: 1.9:1 FAILS */
}

/* ✓ GOOD - Focus indicator with sufficient contrast */
:focus-visible {
  outline: 2px solid #0066cc;
  outline-offset: 2px;
  /* Contrast: 8.6:1 ✓ */
}
```

**Don't rely on color alone to convey information:**

```html
<!-- ❌ Only color indicates error -->
<input class="error-border">

<!-- ✅ Color + icon + text -->
<div class="field-error">
  <input aria-invalid="true" aria-describedby="email-error">
  <span id="email-error" class="error-message">
    <svg aria-hidden="true"><!-- error icon --></svg>
    Please enter a valid email address
  </span>
</div>
```

**Validation Rules:**
- [ ] All text has contrast ≥ 4.5:1 (normal) or 3:1 (large)
- [ ] Focus indicators have contrast ≥ 3:1
- [ ] Placeholder text has minimum 4.5:1 contrast
- [ ] Icons conveying information have 3:1 contrast
- [ ] Information not conveyed by color alone

---

### Operable: Users Must Be Able to Operate the Interface

#### 2.1 Keyboard Accessibility

**All functionality must be accessible via keyboard—no mouse-only actions:**

```javascript
// ❌ BAD - Only handles click (mouse-only)
element.addEventListener('click', handleAction);

// ✅ GOOD - Handles click and keyboard
element.addEventListener('click', handleAction);
element.addEventListener('keydown', (e) => {
  if (e.key === 'Enter' || e.key === ' ') {
    e.preventDefault();
    handleAction();
  }
});
```

**No keyboard traps—users must be able to Tab out of every component:**

```tsx
// ✓ GOOD - Escape closes modal, focus can exit
<DialogComponent
  onKeyDown={(e) => {
    if (e.key === 'Escape') handleClose();
  }}
/>

// ✗ BAD - Focus can't escape
<CustomComponent
  onKeyDown={(e) => {
    if (e.key === 'Tab') e.preventDefault(); // TRAP!
  }}
/>
```

**Validation Rules:**
- [ ] All interactive elements in tab order (no negative tabindex)
- [ ] Tab order is logical (left-to-right, top-to-bottom)
- [ ] Can Tab into and out of every component
- [ ] Escape key closes modals and dropdowns
- [ ] Enter key submits forms and activates buttons
- [ ] Arrow keys work for lists, dropdowns, tabs

---

#### 2.4 Focus Management

**Users must see where keyboard focus is—focus indicators must be visible:**

```css
/* ❌ NEVER remove focus outlines (accessibility violation) */
:focus {
  outline: none;  /* REMOVES keyboard focus visibility! */
}

/* ✅ GOOD - Always provide visible focus */
:focus-visible {
  outline: 2px solid #0066cc;
  outline-offset: 2px;
}

/* ✅ GOOD - Custom focus styles work too */
button:focus-visible {
  box-shadow: 0 0 0 3px rgba(0, 95, 204, 0.5);
}

/* ✅ GOOD - Focus not obscured by sticky headers (NEW in 2.2) */
:focus {
  scroll-margin-top: 80px;
  scroll-margin-bottom: 60px;
}
```

**Manage focus when opening modals or dialogs:**

```jsx
const DialogComponent = ({ isOpen, onClose }) => {
  const submitButtonRef = useRef(null);

  useEffect(() => {
    if (isOpen) {
      // Focus first input when dialog opens
      submitButtonRef.current?.focus();
    }
  }, [isOpen]);

  return (
    <dialog onKeyDown={(e) => e.key === 'Escape' && onClose()}>
      {/* content */}
    </dialog>
  );
};
```

**Validation Rules:**
- [ ] Focus indicators always visible (never outline: none)
- [ ] Focus outline ≥ 2px thick, ≥ 3:1 contrast
- [ ] Focus order logical (top-to-bottom, left-to-right)
- [ ] Focus managed when modal/dialog opens
- [ ] Focused element not obscured by sticky headers/footers

---

#### 2.5 Target Size (NEW in 2.2)

**Interactive targets must be at least 24 × 24 CSS pixels:**

```css
/* ✓ GOOD - Minimum target size */
button,
[role="button"],
a,
input[type="checkbox"] + label,
input[type="radio"] + label {
  min-width: 24px;
  min-height: 24px;
}

/* ✓ GOOD - Comfortable target size (recommended 44×44 for touch) */
.touch-target {
  min-width: 44px;
  min-height: 44px;
  display: inline-flex;
  align-items: center;
  justify-content: center;
}
```

**Exceptions:** Inline text links, elements controlled by browser (video player), targets where a 24px circle centered on the bounding box doesn't overlap another target.

**Validation Rules:**
- [ ] All buttons ≥ 24×24 CSS pixels
- [ ] All links ≥ 24×24 CSS pixels
- [ ] All form inputs ≥ 24×24 CSS pixels
- [ ] Adequate spacing to prevent accidental activation

---

#### 2.5 Dragging Movements Alternative (NEW in 2.2)

**Any action triggered by dragging must offer a single-pointer alternative:**

```html
<!-- ❌ Drag-only reorder (fails accessibility) -->
<ul class="sortable-list" draggable="true">
  <li>Item 1</li>
  <li>Item 2</li>
</ul>

<!-- ✅ Drag + button alternatives -->
<ul class="sortable-list">
  <li>
    <span>Item 1</span>
    <button aria-label="Move Item 1 up">↑</button>
    <button aria-label="Move Item 1 down">↓</button>
  </li>
</ul>
```

**Applies to:** Sliders, map panning, color pickers, image cropping, and all drag-based interactions.

---

### Understandable: Content Must Be Understandable

#### 3.1 Language & Structure

```html
<!-- ✅ Page language specified -->
<html lang="en">

<!-- ✅ Language changes marked -->
<p>The French word is <span lang="fr">bonjour</span>.</p>

<!-- ✅ Proper heading hierarchy (no skipping) -->
<h1>Page Title</h1>
<h2>Section Heading</h2>  <!-- Correct: h2 after h1 -->
<h3>Subsection</h3>       <!-- Correct: h3 after h2 -->

<!-- ❌ BAD: Skipped h2 and h3 -->
<h1>Page Title</h1>
<h4>Section</h4>  <!-- Wrong! Should be h2 -->
```

**Validation Rules:**
- [ ] Page language specified in `<html lang="...">`
- [ ] Language changes marked with `lang` attribute
- [ ] Headings use proper hierarchy (h1-h6, no skipping)
- [ ] Headings are descriptive

---

#### 3.2 Predictable Behavior

**Users must be able to predict what happens when they interact:**

```html
<!-- ✓ GOOD - Links navigate, buttons submit/trigger -->
<a href="/page">Navigate to page</a>
<button type="submit">Submit form</button>

<!-- ❌ BAD - Unexpected behavior -->
<a href="#" onclick="openModal()">Click me</a> <!-- Confusing -->
<button onclick="navigate('/page')">Go</button> <!-- Unexpected -->

<!-- ✓ GOOD - Focus doesn't trigger changes -->
<input onfocus="highlightField()" />  <!-- OK: only highlight -->
<select onchange="submitForm()" />   <!-- BAD: unexpected submit -->
```

**Consistent help (NEW in 2.2)—help mechanisms appear in same relative order:**

```html
<!-- Help consistently placed on all pages -->
<footer>
  <a href="/contact">Contact us</a>
  <a href="/faq">FAQs</a>
  <a href="/help">Help</a>
</footer>
```

---

#### 3.3 Forms & Error Handling

**Every input needs an associated label:**

```html
<!-- ❌ No label association -->
<input type="email" placeholder="Email">

<!-- ✅ Explicit label with for/id -->
<label for="email">Email address</label>
<input type="email" id="email" name="email"
       autocomplete="email" required>

<!-- ✅ Implicit label (wrapping) -->
<label>
  Email address
  <input type="email" name="email" autocomplete="email" required>
</label>

<!-- ✅ With instruction text -->
<label for="password">Password</label>
<input type="password" id="password"
       aria-describedby="pwd-requirements">
<p id="pwd-requirements">At least 8 characters with one number</p>
```

**Error messages must be clear and linked to fields:**

```html
<!-- ❌ Error unclear -->
<span class="error">Error</span>
<input type="email">

<!-- ✅ Clear error with aria-describedby -->
<label for="email">Email</label>
<input type="email" id="email" 
       aria-invalid="true" 
       aria-describedby="email-error">
<p id="email-error" role="alert">
  <svg aria-hidden="true"><!-- error icon --></svg>
  Please enter a valid email address (example: name@domain.com)
</p>
```

**Don't force users to re-enter information (NEW in 2.2):**

```html
<!-- ✅ Auto-fill shipping from billing -->
<fieldset>
  <legend>Shipping address</legend>
  <label>
    <input type="checkbox" id="same-billing" checked>
    Same as billing address
  </label>
  <!-- Auto-populate when checked -->
</fieldset>
```

**Login must not rely solely on cognitive tests (NEW in 2.2):**

```html
<!-- ❌ Cognitive test only (puzzle, remember pattern) -->
<button>Solve puzzle to login</button>

<!-- ✅ Cognitive test + alternative -->
<button>Email me a login link</button>
<button>Sign in with passkey</button>
```

**Validation Rules:**
- [ ] Every input has associated label
- [ ] Required fields marked with * or text
- [ ] Error messages clear and specific
- [ ] Errors linked via `aria-describedby`
- [ ] Error messages include how to fix
- [ ] Validation happens at appropriate times (blur, submit)
- [ ] Information not re-requested (auto-fill where possible)
- [ ] Login not purely cognitive (offer alternatives)

---

### Robust: Content Must Work with Assistive Technologies

#### 4.1 Semantic HTML

**Prefer native elements—they have accessibility built in:**

```html
<!-- ❌ Non-semantic with ARIA (harder to maintain) -->
<div role="button" tabindex="0" onclick="submit()">Submit</div>

<!-- ✅ Native button (automatic: keyboard, focus, role) -->
<button type="submit">Submit</button>

<!-- ❌ ARIA checkbox (hard to manage) -->
<div role="checkbox" aria-checked="false" onclick="toggle()">
  Option
</div>

<!-- ✅ Native checkbox (simple, accessible) -->
<label>
  <input type="checkbox"> Option
</label>

<!-- ✗ Non-semantic form -->
<div onclick="submitData()">
  <div>Email</div>
  <input type="text">
</div>

<!-- ✓ Semantic form -->
<form onsubmit="submitData()">
  <label for="email">Email</label>
  <input type="email" id="email" required>
</form>
```

**Use ARIA only when native HTML won't work:**

```html
<!-- ✓ GOOD - ARIA when native doesn't exist (custom tablist) -->
<div role="tablist" aria-label="Product info">
  <button role="tab" id="tab-1" aria-selected="true"
          aria-controls="panel-1">Description</button>
  <button role="tab" id="tab-2" aria-selected="false"
          aria-controls="panel-2" tabindex="-1">Reviews</button>
</div>
<div role="tabpanel" id="panel-1" aria-labelledby="tab-1">
  <!-- content -->
</div>

<!-- ✓ GOOD - aria-label for icon buttons -->
<button aria-label="Close dialog">×</button>

<!-- ✓ GOOD - aria-describedby for error messages -->
<input aria-invalid="true" aria-describedby="error">
<span id="error">Error: Invalid email format</span>
```

**Validation Rules:**
- [ ] Buttons are `<button>` elements
- [ ] Links are `<a>` elements
- [ ] Forms use `<form>` element
- [ ] Inputs have associated labels
- [ ] No `role`, `aria-*` when native HTML works
- [ ] Icon buttons have `aria-label`
- [ ] Custom components have proper roles
- [ ] Error messages have `aria-describedby`

---

## Testing Accessibility

**Automated tools:**
```bash
# Lighthouse (built into Chrome DevTools)
# DevTools → Lighthouse → Analyze page load

# axe-core browser extension
# https://www.deque.com/axe/

# WAVE browser extension  
# https://wave.webaim.org/
```

**Manual testing—test with assistive technologies:**
- [ ] **Keyboard navigation:** Tab through entire interface
- [ ] **Screen reader (NVDA/VoiceOver):** Listen to page content
- [ ] **Zoom:** Test at 200% zoom (no horizontal scroll)
- [ ] **High Contrast:** Windows High Contrast Mode
- [ ] **Reduced motion:** `prefers-reduced-motion: reduce`

---

## Security Standards

### 2.1 Input Validation

**Requirement:** Prevent XSS and injection attacks

**What to Check:**

```tsx
// ✗ BAD - Unsanitized user input
const userBio = "<img src=x onerror='alert(1)'>";
<div dangerouslySetInnerHTML={{ __html: userBio }} />

// ✓ GOOD - User input rendered as text (safe)
<div>{userBio}</div>

// ✓ GOOD - Sanitize if HTML is truly needed
import DOMPurify from 'dompurify';
const cleanHTML = DOMPurify.sanitize(userBio);
<div dangerouslySetInnerHTML={{ __html: cleanHTML }} />
```

**Validation Rules:**
- [ ] No `dangerouslySetInnerHTML` with user input
- [ ] No `eval()` or `Function()` constructors
- [ ] No inline event handlers (onClick="code()")
- [ ] User input sanitized before display
- [ ] URL validation before navigation

---

### 2.2 Secrets & Environment Variables

**Requirement:** Never expose API keys or secrets

**What to Check:**

```tsx
// ✗ BAD - Hardcoded secret
const API_KEY = "sk_live_12345abcde";
fetch(`/api/data?key=${API_KEY}`);

// ✓ GOOD - Environment variable (Next.js)
const apiKey = process.env.NEXT_PUBLIC_API_KEY;
fetch(`/api/data?key=${apiKey}`);

// ✓ GOOD - Secret in .env.local (never committed)
// .env.local
SYNCFUSION_LICENSE_KEY=xxx...xxx
```

**Validation Rules:**
- [ ] No hardcoded API keys
- [ ] No hardcoded database URLs
- [ ] Environment variable names prefixed (e.g., NEXT_PUBLIC_)
- [ ] .env files in .gitignore
- [ ] Secrets documented as required env vars

---

### 2.3 Dependency Security

**Requirement:** Use trustworthy, well-maintained packages

**What to Check:**

```json
{
  "dependencies": {
    "@syncfusion/ej2-react-inputs": "^20.0.0",
    "@syncfusion/ej2-react-buttons": "^20.0.0"
  }
}
```

**Validation Rules:**
- [ ] All packages from official npm registry
- [ ] No typosquatted package names
- [ ] Syncfusion packages only from @syncfusion org
- [ ] Run `npm audit` regularly
- [ ] No deprecated packages

---

## Performance Standards

### 3.1 Rendering Optimization

**Requirement:** Prevent unnecessary re-renders

**What to Check:**

```tsx
// ✗ BAD - Re-renders on every parent update
export const SearchInput = ({ onSearch }) => {
  return (
    <TextBoxComponent onChange={(e) => onSearch(e.value)} />
  );
};

// ✓ GOOD - Memoized to prevent re-renders
export const SearchInput = React.memo(({ onSearch }) => {
  return (
    <TextBoxComponent onChange={(e) => onSearch(e.value)} />
  );
});

// ✓ GOOD - useCallback prevents handler recreation
const memoizedOnSearch = useCallback((value) => {
  onSearch(value);
}, []);
```

**Validation Rules:**
- [ ] Large components wrapped with React.memo
- [ ] Stable callbacks use useCallback
- [ ] useMemo used for expensive computations
- [ ] No infinite loops in useEffect
- [ ] Cleanup functions in useEffect (subscriptions, timers)

---

### 3.2 Bundle Size

**Requirement:** Keep component bundle size reasonable

**Validation Rules:**
- [ ] Component code < 50KB (uncompressed)
- [ ] No duplicate dependencies
- [ ] Tree-shakeable exports
- [ ] No large images embedded
- [ ] Lazy-loadable for components > 100KB

---

## Code Quality Standards

### 4.1 TypeScript & Type Safety

**Requirement:** Full type safety, no implicit any

**What to Check:**

```tsx
// ✗ BAD - Implicit any
const handleChange = (e) => {
  setValue(e.value);
};

// ✓ GOOD - Explicit types
interface ChangeEvent {
  value: string;
}

const handleChange = (e: ChangeEvent): void => {
  setValue(e.value);
};
```

**Validation Rules:**
- [ ] No `any` types (except explicit escape)
- [ ] Props have TypeScript interface
- [ ] Event handlers properly typed
- [ ] State types defined
- [ ] Return types on functions
- [ ] tsconfig strict mode enabled

---

### 4.2 Code Hygiene

**Requirement:** Clean, maintainable code

**What to Check:**

```tsx
// ✗ BAD - var, console.log in production
var name = "user";
console.log("Debug:", name);
export const Component = () => {
  return <div>{name}</div>;
};

// ✓ GOOD - const, no console, clean
const name = "user";
export const Component: React.FC = () => {
  return <div>{name}</div>;
};
```

**Validation Rules:**
- [ ] No `var` declarations (use `const`/`let`)
- [ ] No `console.log` in production code
- [ ] No unused variables or imports
- [ ] No commented-out code blocks
- [ ] Consistent indentation (2 spaces)
- [ ] Semicolons on all statements
- [ ] Single quotes or double (consistent)

---

## Validation Checklist

**WCAG 2.2 AA Accessibility Checklist—run for every component:**

```
PERCEIVABLE
  ✓ All images have descriptive alt text (or empty alt if decorative)
  ✓ Icon buttons have aria-label or hidden text
  ✓ Videos have captions
  ✓ Videos have audio descriptions
  ✓ Color contrast ≥ 4.5:1 for text (or 3:1 for large)
  ✓ Color contrast ≥ 3:1 for UI components
  ✓ Information not conveyed by color alone
  ✓ No auto-playing audio
  ✓ Focus indicators have 3:1 contrast

OPERABLE
  ✓ All functionality accessible via keyboard
  ✓ Tab order logical (left-to-right, top-to-bottom)
  ✓ No keyboard traps (can Tab out)
  ✓ Focus indicators visible (never outline: none)
  ✓ Focus outline ≥ 2px, ≥ 3:1 contrast
  ✓ Focused element not obscured by sticky headers
  ✓ Interactive targets ≥ 24×24 CSS pixels
  ✓ Dragging has single-pointer alternative (buttons)
  ✓ Escape closes modals/dropdowns
  ✓ Enter submits forms, Space activates buttons
  ✓ Arrow keys work for lists/dropdowns/tabs
  ✓ Skip link present (if repetitive navigation)

UNDERSTANDABLE
  ✓ Page language specified in <html lang="...">
  ✓ Language changes marked with lang attribute
  ✓ Heading hierarchy correct (h1-h6, no skipping)
  ✓ Headings descriptive
  ✓ Every form field has associated label
  ✓ Required fields marked (* or text)
  ✓ Error messages clear and specific
  ✓ Error messages linked via aria-describedby
  ✓ Form validation at appropriate times (blur, submit)
  ✓ Information not re-requested (auto-fill where possible)
  ✓ Links have descriptive text
  ✓ Navigation consistent across pages
  ✓ Help mechanisms in same relative order (NEW in 2.2)
  ✓ Login not purely cognitive test (NEW in 2.2)

ROBUST
  ✓ Native <button>, <a>, <form>, <input> elements used
  ✓ ARIA only when native HTML won't work
  ✓ Icon buttons have aria-label
  ✓ Error fields have aria-invalid="true"
  ✓ Error messages have aria-describedby
  ✓ Custom components have proper roles
  ✓ Proper ARIA attributes (aria-selected, aria-expanded, etc.)

SECURITY
  ✓ No dangerouslySetInnerHTML with user input
  ✓ No eval() or Function()
  ✓ No inline event handlers (onclick="code()")
  ✓ User input sanitized before display
  ✓ No hardcoded API keys or secrets
  ✓ Environment variables for sensitive data
  ✓ All packages from official npm registry

PERFORMANCE
  ✓ Large components wrapped with React.memo
  ✓ Stable callbacks use useCallback
  ✓ Expensive computations use useMemo
  ✓ No infinite loops in useEffect
  ✓ useEffect cleanup functions (subscriptions, timers)
  ✓ Component code < 50KB uncompressed

CODE QUALITY
  ✓ Full TypeScript types (no implicit any)
  ✓ Props have TypeScript interface
  ✓ Event handlers properly typed
  ✓ Return types on all functions
  ✓ No `var` declarations (use const/let)
  ✓ No console.log in production
  ✓ No unused variables or imports
  ✓ No commented-out code
  ✓ Consistent indentation (2 spaces)
  ✓ Semicolons on all statements
```

---

## Auto-Fix Rules

**Stage 5 automatically fixes these issues:**

| Issue | Auto-Fix |
|-------|----------|
| Missing aria-label on icon button | Add based on icon context |
| Missing aria-describedby on error field | Add id to error message |
| Missing htmlFor on label | Match with input id |
| Var declarations | Convert to const/let |
| Console.log statements | Remove completely |
| Unused imports | Remove from import list |
| Heading hierarchy gaps | Reorder to proper hierarchy |
| Missing focus indicator | Add visible outline (never remove) |
| Non-semantic buttons | Convert div role="button" to <button> |
| Missing alt text | Add descriptive alt (requires manual review) |

---

**End of Web Standards Reference**  
Updated for **WCAG 2.2 AA** with NEW criteria: Focus not obscured (2.4.11), Target size (2.5.8), Dragging alternatives (2.5.7), Redundant entry (3.3.7), Accessible authentication (3.3.8)   
For Build issues, see `build.md`
