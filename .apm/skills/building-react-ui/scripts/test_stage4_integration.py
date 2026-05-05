#!/usr/bin/env python3
"""
Test Stage 4 Integration: Layout JSON → Component Mapping

This demonstrates how Stage 4 will use ComponentMapper to process Stage 3 output
and produce structured component mappings for Stage 5.
"""

from components_search import stage_4_component_picking
import json

# Stage 3 Output (from chat context)
stage_3_output = {
    "component_type": "Professional Admin Dashboard",
    "variant": "Standard",
    "elements": [
        {
            "id": "header",
            "name": "Header",
            "description": "Fixed header with logo and notifications",
            "type_hint": "header app bar"
        },
        {
            "id": "sidebar",
            "name": "Sidebar",
            "description": "Collapsible left navigation",
            "type_hint": "navigation sidebar"
        },
        {
            "id": "stat_cards",
            "name": "KPI Cards",
            "description": "Metric stat cards",
            "type_hint": "card metrics kpi"
        },
        {
            "id": "chart_1",
            "name": "Sales Chart",
            "description": "Line chart showing sales data",
            "type_hint": "data visualization chart"
        },
        {
            "id": "chart_2",
            "name": "Growth Chart",
            "description": "Area chart for trends",
            "type_hint": "chart visualization area"
        },
        {
            "id": "data_grid",
            "name": "Users Table",
            "description": "Data grid with sorting and filtering",
            "type_hint": "data grid table sorting filtering"
        },
        {
            "id": "notifications",
            "name": "Notification Bell",
            "description": "Icon button for notifications",
            "type_hint": "notification icon button"
        }
    ]
}

print("=" * 80)
print("STAGE 4 INTEGRATION TEST")
print("=" * 80)

print(f"\n📥 Input: Stage 3 Layout JSON")
print(f"   Component Type: {stage_3_output['component_type']}")
print(f"   Variant: {stage_3_output['variant']}")
print(f"   Elements: {len(stage_3_output['elements'])}\n")

# Process with ComponentMapper (Stage 4)
print("⚙️  Processing with ComponentMapper (BM25 search)...\n")
stage_4_output = stage_4_component_picking(stage_3_output)

print("=" * 80)
print("STAGE 4 OUTPUT: Component Mapping")
print("=" * 80)

# Display as table
print(f"\n{'Element ID':<20} {'Element Name':<20} {'Component':<25} {'Skill':<35}")
print("-" * 100)

for comp in stage_4_output['mapped_components']:
    skill = comp['skill'] if comp['skill'] else "(native)"
    print(f"{comp['element_id']:<20} {comp['element_name']:<20} {comp['component']:<25} {skill:<35}")

print("\n" + "=" * 80)
print("STAGE 4 OUTPUT JSON (for Stage 5):")
print("=" * 80)
print(json.dumps(stage_4_output, indent=2))

# Validation
print("\n" + "=" * 80)
print("VALIDATION SUMMARY:")
print("=" * 80)
syncfusion = [c for c in stage_4_output['mapped_components'] if c['skill']]
native = [c for c in stage_4_output['mapped_components'] if not c['skill']]

print(f"✓ Total elements: {len(stage_4_output['mapped_components'])}")
print(f"✓ Syncfusion components: {len(syncfusion)}")
print(f"✓ Native HTML elements: {len(native)}")
print(f"✓ All elements mapped: {len(stage_4_output['mapped_components']) == len(stage_3_output['elements'])}")

print("\n✅ Stage 4 Complete! Ready for Stage 5: Code Generation")
print(f"   Input to Stage 5: {len(syncfusion)} Syncfusion + {len(native)} Native components")
