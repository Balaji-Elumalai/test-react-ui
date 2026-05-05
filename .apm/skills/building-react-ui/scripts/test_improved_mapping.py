#!/usr/bin/env python3
"""
Test improved CSV keywords with your admin dashboard layout.
Shows how the updated component keywords now better match AI-generated type hints.
"""

import json
from components_search import stage_4_component_picking

# Your AI-generated layout JSON
layout_json = {
    "component_type": "Admin Dashboard",
    "variant": "Professional Enterprise Dashboard",
    "layout_grid": "header-sidebar-main",
    "sections": [
        {
            "section_id": "header",
            "section_name": "Header",
            "description": "Fixed top navigation bar",
            "responsive": "fixed",
            "elements": [
                {
                    "id": "company_logo",
                    "name": "Company Logo",
                    "description": "Brand logo image",
                    "type_hint": "image logo"
                },
                {
                    "id": "notification_icon",
                    "name": "Notifications",
                    "description": "Bell icon with notification badge",
                    "type_hint": "icon button notification badge"
                },
                {
                    "id": "user_profile_menu",
                    "name": "User Profile",
                    "description": "User avatar dropdown menu for profile settings logout",
                    "type_hint": "dropdown menu profile avatar"
                }
            ]
        },
        {
            "section_id": "sidebar",
            "section_name": "Sidebar Navigation",
            "description": "Left collapsible sidebar with navigation menu",
            "responsive": "collapsible",
            "elements": [
                {
                    "id": "nav_menu",
                    "name": "Navigation Menu",
                    "description": "Vertical navigation menu with icons and collapsible submenus",
                    "type_hint": "sidebar navigation menu collapsible icons vertical"
                }
            ]
        },
        {
            "section_id": "main_content",
            "section_name": "Main Content Area",
            "description": "Main dashboard content with charts and data grid",
            "responsive": "flexible",
            "elements": [
                {
                    "id": "kpi_cards",
                    "name": "KPI Cards",
                    "description": "Metric summary cards in grid layout with statistics",
                    "type_hint": "card grid dashboard statistics metrics"
                },
                {
                    "id": "chart_area",
                    "name": "Chart Visualization",
                    "description": "Visual chart component for data insights bar line area",
                    "type_hint": "chart visualization bar line area column"
                },
                {
                    "id": "data_grid",
                    "name": "Data Table",
                    "description": "Data grid table with sorting filtering pagination and row selection",
                    "type_hint": "data grid table sortable filterable paginated"
                }
            ]
        }
    ]
}

print("=" * 80)
print("ADMIN DASHBOARD COMPONENT MAPPING (WITH IMPROVED CSV KEYWORDS)")
print("=" * 80)
print()

# Process with updated components.csv
result = stage_4_component_picking(layout_json)

# Display results with section organization
print("MAPPED COMPONENTS BY SECTION:")
print()

for section in result.get("mapped_sections", []):
    section_id = section["section_id"]
    section_name = section["section_name"]
    print(f"[{section_id.upper()}] {section_name}")
    print("-" * 80)
    
    for elem_id in section["elements"]:
        # Find component mapping
        comp = next((c for c in result["mapped_components"] if c["element_id"] == elem_id), None)
        if comp:
            skill_short = comp["skill"].replace("syncfusion-react-", "").replace("-", " ").title() if comp["skill"] else "Native"
            print(f"  • {comp['element_name']:<20} → {comp['component']:<25} (Score: {comp['score']:>5.2f}) [{skill_short}]")
    print()

# Summary
print("=" * 80)
print("SUMMARY")
print("=" * 80)
total_elements = len(result["mapped_components"])
native_count = sum(1 for c in result["mapped_components"] if c["component"] == "NATIVE_HTML")
syncfusion_count = total_elements - native_count

print(f"Total elements: {total_elements}")
print(f"Syncfusion components: {syncfusion_count}")
print(f"Native HTML fallback: {native_count}")
print()

if syncfusion_count == total_elements:
    print("✅ EXCELLENT! All elements mapped to Syncfusion components")
elif syncfusion_count >= total_elements * 0.8:
    print("✓ GOOD! 80%+ mapped to Syncfusion components")
else:
    print("⚠ Consider refining type_hints for better component matching")

print()
print("Component distribution:")
component_counts = {}
for comp in result["mapped_components"]:
    comp_name = comp["component"]
    component_counts[comp_name] = component_counts.get(comp_name, 0) + 1

for comp_name in sorted(component_counts.keys()):
    count = component_counts[comp_name]
    print(f"  - {comp_name}: {count}")

print()
print("=" * 80)
print("DETAILED MAPPING")
print("=" * 80)
print(json.dumps(result, indent=2))
