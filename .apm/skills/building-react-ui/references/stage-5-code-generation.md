# Stage 4: Code Generation

**Purpose:** Generate production-ready React code, CSS, and TypeScript interfaces with accessibility and web standards compliance.

## CRITICAL: Read Component Skills BEFORE Code Generation

**THIS STEP IS NOT OPTIONAL - Must be completed before writing any code**

### Step 1: Identify All Component Skills from Stage 3

From Stage 3 output, extract ALL Syncfusion component skills used (e.g., `syncfusion-react-sidebar`, `syncfusion-react-grid`, `syncfusion-react-charts`, `syncfusion-react-buttons`, etc.)

### Step 2: Read Getting-Started for EACH Component Skill

**For every single component skill identified in Step 1:**

1. **Read:** `.codestudio/skills/<skill-name>/references/getting-started.md`
   - This is the ONLY authoritative source for imports, styles, and setup
   - Do NOT generate imports without reading this first
   
2. **Extract and document:**
   - Package name (e.g., `@syncfusion/ej2-react-grid`)
   - Exact import statement for the component
   - **Style imports (CRITICAL)** - e.g., `import '@syncfusion/ej2-react-grid/styles/material.css'`
   - Theme CSS if applicable
   - Required providers/setup (if any)
   - Base dependencies

### Step 3: If Complex Features Needed

- Read: `.codestudio/skills/<skill-name>/SKILL.md` for complete API documentation
- Read feature-specific guides: `<skill-name>/references/filtering.md`, `validation.md`, `styling.md`, etc.

### Step 4: (CRITICAL) Read the Syncfusion themes guide to install the overall single Syncfusion theme package:

1. **Read:** `.codestudio/skills/building-react-ui/references/syncfusion-themes.md`

### Step 5: NOW Generate Code Using Extracted Information

Only after completing Steps 1-3, generate the .tsx file using the exact imports and styles extracted from component skills.

**Common Mistake to Avoid:**
❌ Generate code, then try to add style imports later → Results in missing styles, broken UI
✅ Read getting-started FIRST, extract style imports, THEN generate code with all imports included

**Why This Order Is Critical:**
- Component skills contain the authoritative setup syntax
- Style imports are often forgotten and cause broken styling
- Reading first ensures: correct imports, correct styles, no missing dependencies, error-free code
- Compatibility with Syncfusion skill updates

---

## Code Generation Process

**After reading all component skills, AI Should:**

1. **Generate .tsx component file**:
   - React functional component with hooks
   - Proper Syncfusion imports
   - TypeScript interface for props
   - Event handlers and state management
   - Error handling and validation
   - WCAG 2.1 AA accessibility markup (ARIA labels, semantic HTML, focus management)
   - JSDoc comments explaining usage

2. **Generate CSS stylesheet** (based on project preference):
   - CSS Style: `.css` with class names
   - Tailwind: Class-based styling
   - Inline: Style objects in component
   - Responsive design: Mobile-first (320px, 768px, 1024px+)
   - Light/dark theme support if needed

3. **Generate TypeScript interfaces**:
   - Props interface with all prop types
   - State types if using hooks
   - Event handler signatures

4. **Reference code standards** from:
   - web-standards.md (accessibility + security rules)
   - Component skill's feature-specific guides (filtering.md, validation.md, styling.md, etc.)

**Code Generation Standards:**

- **Component Imports:** Use exact import syntax from component skill's getting-started.md
- **Style Imports:** Include the Syncfusion single package theme from `references/syncfusion-themes.md`
 **Read:** `.codestudio/skills/building-react-ui/references/syncfusion-themes.md`
- **Semantic HTML:** Use proper HTML5 elements (`<form>`, `<label>`, `<button>`, etc.)
- **Accessibility:** ARIA labels, roles, aria-describedby, aria-invalid where needed
- **TypeScript:** No `any` types, full type safety
- **Error Handling:** Try-catch blocks, user-friendly error messages
- **Responsive:** Flex/Grid layouts, media queries
- **Performance:** React.memo if needed, useCallback for handlers
- **Security:** No dangerouslySetInnerHTML, sanitize inputs, no hardcoded secrets
- **Comments:** JSDoc on component, explain complex logic

### Media (MANDATORY)

- **Placeholder Images:** Use [Unsplash](https://unsplash.com) for high-quality placeholder images
  - Format: `https://images.unsplash.com/photo-[id]?w=[width]&h=[height]&fit=crop`
  - Example: `https://images.unsplash.com/photo-1560472354-b33ff0c44a43?w=200&h=100&fit=crop`
  - Always specify dimensions (width x height) in the URL
  - Use relevant keywords for context-appropriate images

### Icon Handling (MANDATORY)

**Step 1: Attempt to find icon from Component Mapping**
- **Always run ComponentMapper script first** to get semantic icon mappings (BM25 search against EJ2 icons)
- **Use icon CSS class if score > 5:** `<span className="e-icons e-mail"></span>`
- **Never leave empty space** - either icon or emoji, not blank

**Step 2: If Icon Not Found or Score Too Low**
- ❌ DO NOT skip or use empty space
- ✅ Update the element's `icon_hint` in `component-mapping.json`
- ✅ Run the ComponentMapper script again: `py components_search.py ../component-mapping.json`
- ✅ Re-check the script output for improved icon match

**Step 3: If Still Not Found**
- ✅ Use emoji fallback: `<span>📧</span>` or appropriate emoji
- Document why icon wasn't found in code comments
- Maintain visual consistency with other components

**Example**:
```json
// Before: icon_hint was too vague
"icon_hint": "email"

// After: updated with more keywords
"icon_hint": "email envelope mail message send"
```

### Button & Icon Styling with Syncfusion (MANDATORY)

**Principle:** Let Syncfusion own button dimensions and styling. Use Tailwind only for layout around buttons.

❌ **INCORRECT** - Overriding Syncfusion button sizes with Tailwind:
```tsx
<button className="e-control e-btn e-large p-4 w-32 h-12">
  <span className="e-icons e-play"></span>
  Play
</button>
```

✅ **CORRECT** - Syncfusion owns button, Tailwind owns layout:
```tsx
<div className="flex gap-3">
  <button className="e-control e-btn e-lib e-large e-primary">
    <span className="e-icons e-video"></span>
    Play
  </button>

  <button className="e-control e-btn e-lib e-large e-outline">
    <span className="e-icons e-circle-info"></span>
    More Info
  </button>
</div>
```

**Why This Works:**
- Syncfusion defines sizing + alignment internally
- Icons align correctly with Syncfusion's design system
- No padding collision or override conflicts
- Consistent appearance across all Syncfusion components

---

### Component Reuse Across UI (Same Component, Multiple Places)

**Principle:** One Syncfusion component type can be reused throughout your UI with customizations. For example, `ButtonComponent` can serve as the Login button, Forgot Password link, and Sign Up button—each customized via CSS variables.

**Example - Button Used in Multiple Places:**
```tsx
// LoginForm.tsx
import { ButtonComponent } from '@syncfusion/ej2-react-buttons';
import './LoginForm.css';

// All use the same ButtonComponent, but different CSS classes for customization
<div className="login-button">
  <ButtonComponent isPrimary={true}>Login</ButtonComponent>
</div>

<div className="forgot-password">
  <ButtonComponent cssClass="e-flat esmall">Forgot Password?</ButtonComponent>
</div>

<div className="sign-up">
  <ButtonComponent cssClass="e-outline">Sign Up Here</ButtonComponent>
</div>
```

```css
/* LoginForm.css */
/* Primary button - main CTA */
.login-button .e-btn {
  --bs-primary: #0d6efd;
  width: 100%;
}

/* Flat button - link-style action */
.forgot-password .e-btn {
  --bs-primary: #6c757d;
  background: transparent;
  border: none;
  text-decoration: underline;
  font-size: 14px;
}

/* Outline button - secondary action */
.sign-up .e-btn {
  --bs-primary: #6c757d;
  border: 1px solid #6c757d;
}
```

---

### Reading Component Skills BEFORE Using generate code (MANDATORY)

**CRITICAL:** Do NOT assume component properties or APIs.

**Required Process:**
1. **Identify all mapped components** from Stage 3 output
   - E.g., GridComponent, ChartComponent, SidebarComponent, etc.

2. **For EACH component**, read the component skill:
   - Location: `.codestudio/skills/<component-skill>/references/getting-started.md`
   - Extract: imports, style imports, required props, setup code
   - Read: feature-specific guides (filtering, sorting, validation, styling, etc.)

3. **DO NOT generate code without reading** component skill documentation
   - Don't assume prop names or API structure
   - Don't guess at event handler names
   - Don't skip required setup or initialization

**Example - Reading GridComponent Skill:**
```
Before generating code:
1. Read: .codestudio/skills/syncfusion-react-grid/references/getting-started.md
   → Extract: import GridComponent from '@syncfusion/ej2-react-grids'
   → Read: required props, dataSource structure, column definitions

2. Read: .codestudio/skills/syncfusion-react-grid/references/sorting.md
   → Understand: allowSorting prop, sortSettings structure

3. Read: .codestudio/skills/syncfusion-react-grid/references/filtering.md
   → Understand: allowFiltering prop, filterSettings structure

4. NOW generate code with correct imports, props, and API calls
```

**What Component Skills Contain:**
- ✅ Authoritative import statements
- ✅ Complete API documentation
- ✅ Feature-specific patterns (sorting, filtering, validation)
- ✅ Best practices and performance considerations
- ✅ Accessibility requirements
- ✅ Theme customization options

**Common Mistakes to Avoid:**
- ❌ Guessing prop names → Read skill documentation
- ❌ Missing style imports → Extract from getting-started.md
- ❌ Wrong event handler names → Copy from component skill examples
- ❌ Incomplete setup code → Follow skill's recommended initialization

---

**Example Output Files:**

```
components/LoginForm/
  ├── LoginForm.tsx              (React component)
  ├── LoginForm.css              (Styles)
  └── index.ts                   (Barrel export)
```

---

## Syncfusion component and theme Package Installation

**CRITICAL:** After code generation completes, you MUST install all Syncfusion component and theme packages that were used in the generated code. Run the appropriate `npm install` command for each package identified during the component skill reading phase (Stage 4, Steps 1-3).

Example:
```bash
npm install @syncfusion/ej2-react-grid @syncfusion/ej2-react-charts @syncfusion/ej2-react-buttons @syncfusion/ej2-tailwind3-theme
```

**Without installing these packages, the generated code will fail to render.**

## Component Integration & File Mapping

**Generated files MUST be wired to display in the app:**

1. **Barrel Export** (`components/LoginForm/index.ts`):
   ```ts
   export { LoginForm } from './LoginForm';
   ```

2. **Import in App.tsx**:
   ```tsx
   import { LoginForm } from './components/LoginForm';
   
   function App() {
     return <LoginForm />;
   }
   ```

3. **Ensure CSS is loaded**:
   - If no framework/greenfield CSS styles: Automatically imported in component
   - If Tailwind: Classes applied directly
   - If Syncfusion theme: Already imported at app entry point (Stage 4)

**Without this mapping, component won't render in sample.**

**User Interaction:** 
Optional review of generated code. No blocking confirmation.

**Status:** AI generates without user decision. User can review/adjust if needed.
