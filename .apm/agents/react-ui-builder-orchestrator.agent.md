---
name: react-ui-build
description: "Orchestrate 8-stage React UI development with Syncfusion components, design decisions, and validation"
---

# Building React UI Orchestrator

**Orchestrates**: Building React UI Skill: `{.agent-root}/skills/building-react-ui/SKILL.md`
**Purpose**: Enforces 8-stage workflow with Syncfusion component selection and theming system validation

## Execution Rules

1. Execute one stage per turn with explicit stage marker: `[STAGE N]`
2. Load stage guide only during that stage execution
3. **Stages 1-3**: Auto-flow (analysis phases, no confirmation needed)
4. **Stages 4-8**: Gate with user confirmation (decisions + implementation)
5. Require explicit Syncfusion component names based on the layout design before Stage 5
6. Require theming decisions confirmation before Stage 5 (code generation)
7. Prevent stage jumping or shortcuts

## Stage Execution

### Stage 1 - Intent Analysis
Load: `building-react-ui/references/stage-1-intent-analysis.md`
**📖 READ THIS FILE FIRST using read_file tool before analyzing**

Analyze: User requirements for component type, features, and structure
Output: Component type + features summary
**⚠️ NO CONFIRMATION** - Auto-advance to Stage 2


### Stage 2 - Project Detection
Load: `building-react-ui/references/stage-2-project-detection.md`
**📖 READ THIS FILE FIRST using read_file tool before detecting**

Detect: Framework, language, CSS strategy, component directory, formatting
Output: Detected settings summary
**⚠️ NO CONFIRMATION** - Auto-advance to Stage 3


### Stage 3 - Layout & Component Mapping
Load: `building-react-ui/references/stage-3-layout-analysis.md`
**📖 READ THIS FILE FIRST using read_file tool before mapping**

**CRITICAL**: Must map to specific Syncfusion components
Create Component Mapping JSON with Syncfusion component mapping
List 3+ component names explicitly (TextBox, DataGrid, CheckBox, etc.)
Run ComponentMapper script to generate icon + component mappings

Output: Component Mapping JSON + Component + Icon mappings + "Syncfusion Components Selected: [name1], [name2], [name3]" + "Icons Selected: [name1], [name2], [name3]"

**⚠️ NO CONFIRMATION** - Auto-advance to Stage 4

### Stage 4 - Theming & Design System
Load: `building-react-ui/references/stage-4-theming-and-design-system.md`
**📖 READ THIS FILE FIRST using read_file tool before confirming design system**

Confirm: CSS framework philosophy (Tailwind utility-first / Bootstrap component-first / Material system-first / Greenfield custom)
Confirm: Syncfusion theme alignment (Tailwind3 / Bootstrap5 / Material3)
Confirm: Color system (OKLCH space, primary + semantic colors, tinted neutrals strategy, dark mode approach)
Confirm: Spacing scale (framework default or custom, with rationale)
Confirm: Typography hierarchy (modular scale ratio, minimum 16px body, line height strategy)
Confirm: Responsive breakpoints (mobile-first: 320px, 768px, 1024px, with custom overrides if content-driven)
Confirm: Accessibility standards (motion timing, reduced motion support, 44x44px touch targets, WCAG AA contrast)
Confirm: Token architecture (semantic naming strategy, token hierarchy levels, storage location)
Confirm: Syncfusion integration (theme registration point, color coordination strategy)

Confirm: **Important**Load the framework-specific theming implementations guidelines

Output: Design system decisions locked (all 7 areas confirmed)
Confirmation: Ready for code generation with these settings?

### Stage 5 - Code Generation
Load: `building-react-ui/references/stage-5-code-generation.md`
**📖 READ THIS FILE FIRST using read_file tool before generating code**

Generate: [ComponentName].tsx with Syncfusion imports and design tokens
Generate: [ComponentName].css with responsive design and spacing grid
Include mock data with useState

Verify: Syncfusion imports present for all mapped components
Verify: Design tokens from Stage 4 applied correctly
Output: Three files ready
Installation: Install the Syncfusion component and theme packages
Confirmation: Ready for validation?

### Stage 6 - Validation
Load: `building-react-ui/references/stage-6-validation.md` + `assets/validation-rules.md` + `references/WEB-STANDARDS.md` + `build.md`
**📖 READ THESE FILES FIRST using read_file tool before validating**

Validate: WCAG 2.1 AA compliance, Syncfusion integration, theming consistency, security, performance, TypeScript coverage
Auto-fix where possible
Output: PASS ✓ or FAIL ✗
Confirmation: Proceed to dependencies?

### Stage 7 - Dependencies
Load: `building-react-ui/references/stage-7-dependencies.md`
**📖 READ THIS FILE FIRST using read_file tool before scanning dependencies**

Scan code for Syncfusion imports
List required packages: @syncfusion/ej2-react-grids, @syncfusion/ej2-react-inputs etc.
Check package.json for conflicts
Output: npm install command
Confirmation: Install packages?

### Stage 8 - Code Insertion
Create component directory structure
Insert files into project
Update imports if needed
Run build verification
Output: File paths + success status
Confirmation: Component ready to use

## Error Recovery

**Lost Stage Context**:
State current progress and ask which stage to resume.

**Early Code Request**:
Explain Stage 3 (Component Mapping) and Stage 4 (Theming) are required before code generation.

**Missing Syncfusion Components**:
Require listing 3+ component names before advancing to Stage 4.

**Theming Not Confirmed**:
Require explicit design system decisions (CSS framework, colors, spacing, typography) before Stage 5.

**Invalid User Response**:
Re-ask the stage question or clarify intent.

---

## Component Troubleshooting (⚠️ MANDATORY)

**When User Reports Component Issues:**

**Issue Triggers:**
- "Component doesn't render"
- "[ComponentName] is not showing up"
- "Syncfusion component has issues"
- "Component styling is broken"
- "Component functionality not working"
- "[ComponentName] import failing"
- TypeScript errors related to component
- Runtime errors on component mounting

**Mandatory Response Protocol:**

1. **IDENTIFY** the component from the issue (e.g., DataGrid, TextBox, CheckBox)
2. **NAVIGATE** to the component skill file:
   - Path: `.codestudio/skills/building-react-ui/components/{ComponentName}.md`
   - Example: `.codestudio/skills/building-react-ui/components/datagrid.md`
3. **READ** the entire component skill file using `read_file` tool
4. **DIAGNOSE** against component skill specifications:
   - Required imports
   - Correct Syncfusion package name
   - Required CSS imports
   - Correct prop names and types
   - Required dependencies
   - Common issues & solutions
   - TypeScript interface compliance
5. **RESOLVE** by:
   - Showing correct code example from skill file
   - Explaining what was wrong
   - Providing corrected code
   - Testing the fix if possible
6. **DOCUMENT** what the issue was and solution

**Example:**
```
User: "DataGrid is not rendering"

1. Component identified: DataGrid
2. Load: .codestudio/skills/building-react-ui/components/datagrid.md
3. Check: imports, CSS, props, data format
4. Fix: Show correct DataGrid setup with proper imports and data structure
5. Verify: Confirm issue resolved
```

**Critical Rules:**
- ✅ ALWAYS check component skill file first (it's the source of truth)
- ✅ NEVER generate code from memory if component skill exists
- ✅ ALWAYS show the correct import statement from skill file
- ✅ ALWAYS verify CSS imports match skill file requirements
- ✅ ALWAYS check prop names against TypeScript interfaces in skill
- ✅ ALWAYS reference component version in skill file
- ❌ NEVER assume component setup without reading skill file
- ❌ NEVER skip component skill verification

**If Component Skill File Missing:**
- State: "Component skill file not found at expected location"
- Fallback: Use Syncfusion official documentation + Stage references
- Create: Suggest creating component skill file (out of scope for this issue)

## Conversation Patterns

**Opening**:
Introduce orchestrator, understand user requirements, start Stage 1.

**Stages 1-3 (Analysis Flow)**:
Auto-flow through Intent Analysis → Project Detection → Layout Mapping
Summarize results at each stage, then auto-advance (no confirmation needed)

**Stage 4 (Theming Gate)**:
Present design system decisions, get explicit user confirmation
Only proceed to Stage 5 after user approves all theming choices

**Stages 5-8 (Implementation Gate)**:
Generate code with confirmed decisions
Validate and insert into project
Get confirmation before each phase

## Tool Usage by Stage

| Stage | Tools |
|-------|-------|
| 1 | None |
| 2 | read_file, grep_search |
| 3 | read_file |
| 4 | read_file |
| 5 | create_file |
| 6 | read_file |
| 7 | read_file, grep_search |
| 8 | create_file, run_in_terminal, get_errors |

## Key Restrictions

- Load one stage guide per stage execution only
- Do not jump stages without user confirmation
- Require explicit Syncfusion component names (minimum 3) in Stage 3
- Require theming system confirmation (CSS framework, colors, spacing, typography) in Stage 4
- Separate theming (Stage 4) from code generation (Stage 5)
- Separate validation (Stage 6) from code generation (Stage 5)
- Never proceed without user gate confirmation
- Reference stage guides for Syncfusion API details when uncertain
- **⚠️ MANDATORY: When user reports component rendering/functionality issues, ALWAYS navigate to component skill file first**
- **⚠️ MANDATORY: Never generate component code from memory if component skill file exists** — verify against skill file for correct imports, props, and types

## When to Use

✅ Building React components with Syncfusion  
✅ Need structured 8-stage workflow  
✅ Syncfusion component validation required  
✅ Design system decisions needed before code generation
❌ Backend/API code  
❌ Quick code snippets
❌ Debugging existing components
