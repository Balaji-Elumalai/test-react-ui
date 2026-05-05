#!/usr/bin/env python3
"""
Example: Stage 4 Component Picking with Nested Sections

Shows how to use the updated stage_4_component_picking() function 
with both simple (flat) and complex (nested sections) layouts.

Both layouts now work seamlessly without manual flattening!
"""

import json
from components_search import stage_4_component_picking


# ============ EXAMPLE 1: SIMPLE LAYOUT (Flat Elements) ============

def example_simple_layout():
    """Login form with flat elements array."""
    print("=" * 80)
    print("EXAMPLE 1: SIMPLE LAYOUT (Flat Elements)")
    print("=" * 80 + "\n")
    
    layout_json = {
        "component_type": "Login Form",
        "variant": "Standard",
        "elements": [
            {
                "id": "email_input",
                "name": "Email Address",
                "description": "Email field with validation",
                "type_hint": "text input email"
            },
            {
                "id": "password_input",
                "name": "Password",
                "description": "Password field, masked",
                "type_hint": "text input password"
            },
            {
                "id": "remember_me",
                "name": "Remember Me",
                "description": "Keep me logged in",
                "type_hint": "checkbox"
            },
            {
                "id": "submit_button",
                "name": "Login",
                "description": "Submit login button",
                "type_hint": "button primary"
            }
        ]
    }
    
    # Process with Stage 4 (no flattening needed!)
    result = stage_4_component_picking(layout_json)
    
    print("Input Layout Type: Simple (flat elements)")
    print(f"Elements to map: {len(layout_json['elements'])}\n")
    
    print("Output Mapping:")
    print(json.dumps(result, indent=2))
    print()


# ============ EXAMPLE 2: COMPLEX LAYOUT (Nested Sections) ============

def example_complex_layout():
    """Admin dashboard with nested sections."""
    print("=" * 80)
    print("EXAMPLE 2: COMPLEX LAYOUT (Nested Sections)")
    print("=" * 80 + "\n")
    
    layout_json = {
        "component_type": "Admin Dashboard",
        "variant": "Classic Admin Dashboard",
        "aesthetic": "Refined Minimalism",
        "layout_grid": "header-sidebar-main",
        "sections": [
            {
                "section_id": "header",
                "section_name": "Header",
                "description": "Fixed top navigation bar",
                "responsive": "fixed",
                "elements": [
                    {
                        "id": "logo",
                        "name": "Company Logo",
                        "description": "Brand logo image or text",
                        "type_hint": "logo image brand"
                    },
                    {
                        "id": "notification_icon",
                        "name": "Notification Bell",
                        "description": "Bell icon with notification count badge",
                        "type_hint": "icon button notification bell badge"
                    },
                    {
                        "id": "user_profile_menu",
                        "name": "User Profile Menu",
                        "description": "User avatar with dropdown menu",
                        "type_hint": "dropdown menu user profile avatar"
                    }
                ]
            },
            {
                "section_id": "sidebar",
                "section_name": "Sidebar Navigation",
                "description": "Left collapsible sidebar",
                "responsive": "collapsible",
                "elements": [
                    {
                        "id": "nav_menu",
                        "name": "Navigation Menu",
                        "description": "Vertical navigation with collapsible items",
                        "type_hint": "sidebar navigation menu collapsible accordion"
                    }
                ]
            },
            {
                "section_id": "main_content",
                "section_name": "Main Content Area",
                "description": "Primary content area",
                "responsive": "flexible",
                "elements": [
                    {
                        "id": "page_title",
                        "name": "Page Title",
                        "description": "Dashboard page heading",
                        "type_hint": "heading title text"
                    },
                    {
                        "id": "kpi_cards",
                        "name": "KPI Cards",
                        "description": "Metric cards displaying key statistics",
                        "type_hint": "card grid statistics metrics"
                    },
                    {
                        "id": "chart_section",
                        "name": "Chart Components",
                        "description": "Visual data charts for insights",
                        "type_hint": "chart visualization graph line bar"
                    },
                    {
                        "id": "data_grid",
                        "name": "Data Grid Table",
                        "description": "Data table with sorting and pagination",
                        "type_hint": "data grid table sortable filterable paginated"
                    }
                ]
            }
        ]
    }
    
    # Process with Stage 4 (sections auto-handled!)
    result = stage_4_component_picking(layout_json)
    
    print("Input Layout Type: Complex (nested sections)")
    total_elements = sum(len(s.get('elements', [])) for s in layout_json.get('sections', []))
    print(f"Sections: {len(layout_json['sections'])}")
    print(f"Total elements: {total_elements}\n")
    
    print("Output Mapping:")
    print(json.dumps(result, indent=2))
    print()
    
    # Show section organization
    print("\nSection Organization:")
    for section in result.get("mapped_sections", []):
        print(f"  [{section['section_id']}] {section['section_name']}")
        for elem_id in section['elements']:
            print(f"    - {elem_id}")
    print()


# ============ EXAMPLE 3: MIXED COMPLEXITY (Sections + Custom Fields) ============

def example_mixed_layout():
    """Layout with sections and additional custom fields."""
    print("=" * 80)
    print("EXAMPLE 3: MIXED COMPLEXITY (Sections with Custom Fields)")
    print("=" * 80 + "\n")
    
    layout_json = {
        "component_type": "E-commerce Dashboard",
        "variant": "Premium",
        "aesthetic": "Modern Corporate",
        "layout_grid": "2-column",
        "sections": [
            {
                "section_id": "filters",
                "section_name": "Filters",
                "responsive": "sticky",
                "elements": [
                    {
                        "id": "search_filter",
                        "name": "Search",
                        "type_hint": "text input search filter",
                        "description": "Filter products by search"
                    },
                    {
                        "id": "category_filter",
                        "name": "Category Filter",
                        "type_hint": "dropdown select filter",
                        "description": "Filter by product category"
                    },
                    {
                        "id": "price_range",
                        "name": "Price Range",
                        "type_hint": "slider range price",
                        "description": "Filter by price range"
                    }
                ]
            },
            {
                "section_id": "products",
                "section_name": "Product Grid",
                "responsive": "flexible",
                "elements": [
                    {
                        "id": "product_grid",
                        "name": "Product Grid",
                        "type_hint": "grid card product image price",
                        "description": "Grid of product cards with images"
                    },
                    {
                        "id": "pagination",
                        "name": "Pagination",
                        "type_hint": "pagination controls",
                        "description": "Page navigation controls"
                    }
                ]
            }
        ]
    }
    
    result = stage_4_component_picking(layout_json)
    
    print("Input Layout Type: Mixed (sections with custom properties)")
    total_elements = sum(len(s.get('elements', [])) for s in layout_json.get('sections', []))
    print(f"Sections: {len(layout_json['sections'])}, Elements: {total_elements}\n")
    
    print("Output Mapping with Section Context:")
    for comp in result['mapped_components']:
        section = comp.get('section_id', 'N/A')
        print(f"  [{section}] {comp['element_id']}")
        print(f"    → {comp['component']} (Score: {comp['score']})")
    print()


# ============ MAIN ============

if __name__ == '__main__':
    # Run all examples
    example_simple_layout()
    example_complex_layout()
    example_mixed_layout()
    
    print("\n" + "=" * 80)
    print("✓ All examples completed!")
    print("=" * 80)
    print("""
KEY IMPROVEMENTS:
  ✓ No manual flattening needed
  ✓ Handles both flat and nested layouts
  ✓ Preserves section context in output
  ✓ Returns section organization mapping
  ✓ Works seamlessly in chat context
  ✓ Ready for Stage 5 (code generation)
""")
