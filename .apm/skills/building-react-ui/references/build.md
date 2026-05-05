# Troubleshooting & FAQ (AI Agent Reference)

---

## ⚠️ AGENT PROTOCOL: Build/Component Issues

**When user reports build errors or component issues:**
1. **Identify the component type** (e.g., TextBoxComponent, GridComponent, etc.)
2. **Load the corresponding component skill** immediately (TextBox Skill, Grid Skill, etc.)
3. **Reference the component skill's troubleshooting section** for setup, imports, and solutions
4. **Direct user to component skill** if issue persists
5. Do NOT generate solutions without consulting component skill documentation first

---

## Table of Contents

1. [Installation & Setup](#installation--setup)
2. [Build & Runtime Errors](#build--runtime-errors)
3. [Component Issues](#component-issues)

---

## Installation & Setup Issues

When user encounters setup errors:

### @syncfusion package not found
→ **Direct to component skill** for exact package list. Each component skill lists required `@syncfusion/ej2-react-*` packages.

### package.json not found
→ **Verify user is in React project root.** Guide to project detection (Stage 1).

### React version incompatible (< 18.0.0)
→ **Inform user** to upgrade: `npm install react@^18.0.0 react-dom@^18.0.0`

---

## Build & Runtime Error Protocol

### CSS import errors
→ Verify generated CSS file path and import statement. Suggest dev server restart.

### Missing component imports (e.g., "Cannot find TextBoxComponent")
→ **Load component skill** (TextBox, Grid, etc.). Reference required imports and package names.

### registerLicense errors
→ Ensure `@syncfusion/ej2-base` installed. Check if license registration code is in app entry point.

### Event handler issues
→ **Load component skill.** Each component has specific event structure (args.value vs e.target.value, etc.).

---

## Component-Specific Issues Protocol

**Any component-specific issue → Load corresponding component skill IMMEDIATELY**

Examples of component-specific issues:
- TextBox not showing value → TextBox Skill troubleshooting
- Grid pagination not working → Grid Skill troubleshooting
- DatePicker format wrong → DatePicker Skill troubleshooting
- DropDown filtering not enabled → DropDown Skill troubleshooting

**Component skill structure always includes:**
- Required props and default values
- Event handler patterns (args structure)
- Common pitfalls and solutions
- Syncfusion service injections (if needed)

---

## Agent Guidelines

**When user reports issues:**
1. Classify error type (setup / build / component-specific / feature request)
2. Setup/build issues → Use this troubleshooting guide
3. Component issues → **Load component skill** immediately
4. Feature gaps → Suggest component skill or custom implementation
5. Ambiguous errors → Ask clarifying questions before loading skills

**When checking component skills:**
- Navigate to component skill (TextBox, Grid, Button, etc.)
- Review "Getting Started" for setup
- Check "Common Issues" section for troubleshooting
- Reference "Props" and "Events" for implementation details

**If issue NOT resolved by component skill:**
→ Escalate to user with component skill reference
→ Suggest manual fix with code example
→ Do NOT generate new code without understanding root cause

