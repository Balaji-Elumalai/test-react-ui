# Syncfusion Theming Resources

**⚠️ MANDATORY:** After making your framework choice, you MUST consult **Skill: syncfusion-react-themes** for detailed implementation guidance before proceeding to Stage 5:

## Quick Reference: Syncfusion Themes

| Framework | Syncfusion Theme | Package Name | Import Statement |
|-----------|------------------|--------------|------------------|
| **Tailwind**/**Greenfield** | Tailwind3 | `@syncfusion/ej2-tailwind3-theme` | `import '@syncfusion/ej2-tailwind3-theme/styles/tailwind3.css'` |
| **Bootstrap** | Bootstrap5 | `@syncfusion/ej2-bootstrap5-theme` | `import '@syncfusion/ej2-bootstrap5-theme/styles/bootstrap5.css'` |
| **Material** | Material3 | `@syncfusion/ej2-material3-theme` | `import '@syncfusion/ej2-material3-theme/styles/material3.css'` |
| **Fluent** | Fluent2 | `@syncfusion/ej2-fluent2-theme` | `import '@syncfusion/ej2-fluent2-theme/styles/fluent2.css'` |

**Note:** Import the theme CSS at your app entry point (before components render) to ensure consistent styling across all Syncfusion components.

## By Use Case:

Read the **Skill: syncfusion-react-themes** for below features

### Applying a Theme
- Refer to **Built-in Themes** for npm vs CDN import methods
- Check version matching requirements
- Review optimized (lite) CSS options

### Implementing Dark Mode
- Refer to **Dark Mode Implementation** for:
  - Global dark mode with `e-dark-mode` class
  - Per-component dark mode customization
  - Runtime theme switching patterns

### Customizing Colors & Tokens
- Refer to **CSS Variables Customization** for:
  - Theme-specific CSS variable structures (Material 3, Fluent 2, Bootstrap 5.3, Tailwind 3.4)
  - RGB vs hex value formats
  - Runtime color modifications

### Using Icons
- Refer to **Icon Library** for:
  - Setting up Syncfusion icons package
  - Sizing modes (small, medium, large)
  - Icon customization and styling

### Advanced Theming
- Refer to **Advanced Features** for:
  - Touch mode / size modes
  - Font customization across components
