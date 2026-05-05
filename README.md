# Building React UI - APM Package

An Agent Package Manager (APM) package for orchestrating production-ready React UI generation with Syncfusion components.

## Overview

This package provides:

- **`react-ui-build-orchestrator` Agent**: A comprehensive agent that guides the entire React UI building process
- **`building-react-ui` Skill**: Auto-activates when users ask about building React interfaces, generating web components, or creating frontend code

## What's Inside

```
.apm/
├── agents/
│   └── react-ui-build-orchestrator.agent.md      # Main orchestrator agent
└── skills/
    └── building-react-ui/
        ├── SKILL.md                               # Skill definition & activation rules
        ├── assets/
        │   └── validation-rules.md                # Validation criteria
        ├── references/                            # 8-stage workflow documentation
        │   ├── stage-1-intent-analysis.md
        │   ├── stage-2-project-detection.md
        │   ├── stage-3-layout-analysis.md
        │   ├── stage-4-theming-and-design-system.md
        │   ├── stage-5-code-generation.md
        │   ├── stage-6-validation.md
        │   ├── stage-7-dependencies.md
        │   ├── bootstrap-implementation.md
        │   ├── material-implementation.md
        │   ├── tailwind-implementation.md
        │   ├── syncfusion-themes.md
        │   ├── build.md
        │   ├── greenfield-implementation.md
        │   └── web-standards.md
        └── scripts/
            ├── components_search.py
            ├── components.csv
            ├── icons.csv
            ├── test_improved_mapping.py
            ├── test_stage4_integration.py
            ├── example_stage4_with_sections.py
            └── CSV-KEYWORD-ENHANCEMENT.md
```

## Installation

### Local Installation
```bash
apm install
```

This deploys the skill and agent to:
- `.agents/skills/` - cross-client universal location
- `.github/agents/` - GitHub Copilot specific
- `.claude/skills/` - Claude Code specific (if available)

### Package Installation (from registry)
```bash
apm install syncfusion/building-react-ui
```

## Usage

### Automatic Skill Activation
Ask your AI runtime about React UI building:
- "Build a React UI for a dashboard"
- "Generate a responsive web component"
- "Create a form with Syncfusion components"

The `building-react-ui` skill auto-activates based on context.

### Agent Invocation
Summon the orchestrator agent directly:
```
@react-ui-build-orchestrator generate a React component for [description]
```

## 8-Stage Workflow

1. **Intent Analysis** - Understand requirements and user intent
2. **Project Detection** - Identify project type and setup
3. **Layout Analysis** - Plan component structure and hierarchy
4. **Theming & Design System** - Select colors, typography, spacing
5. **Code Generation** - Create React component files
6. **Validation** - Check accessibility (WCAG 2.1 AA), responsive design
7. **Dependencies** - Manage Syncfusion packages and imports
8. **Build & Deploy** - Generate build artifacts and documentation

## Features

✅ **Syncfusion React Components** - Production-ready component library
✅ **WCAG 2.1 AA Compliant** - Accessibility built-in
✅ **Responsive Design** - Mobile-first approach
✅ **Multi-Theme Support** - Bootstrap, Material, Tailwind, Syncfusion themes
✅ **Code Quality** - Validation and testing guidelines
✅ **AI Runtime Compatible** - Works with Copilot, Claude, Cursor, and more

## Requirements

- APM v1.0.0+
- Node.js 16+
- React 17+
- Syncfusion React packages

## License

MIT

## Author

Syncfusion Inc

## More Info

- [APM Documentation](https://microsoft.github.io/apm/)
- [Syncfusion React Components](https://www.syncfusion.com/react-components)
- [Web Accessibility Guidelines](https://www.w3.org/WAI/WCAG21/quickref/)
