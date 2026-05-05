"""
ComponentMapper: BM25-based component search for Stage 4

Maps user queries (element type + content hints) to Syncfusion React components
using BM25 ranking on component keywords.

Usage:
    # Direct import for Stage 4
    from components_search import ComponentMapper, stage_4_component_picking
    
    component_mapping_json = {...}  # From Stage 3 (component-mapping.json)
    result = stage_4_component_picking(component_mapping_json)
    # Returns: Stage 4 output JSON with mapped components

    # Or standalone CLI
    mapper = ComponentMapper(csv_path='components.csv')
    results = mapper.search('button primary action', top_k=5)
    # Returns: [(component_name, skill_name, score), ...]
"""

import csv
import math
import json
from pathlib import Path
from typing import List, Tuple, Optional, Dict, Any
from collections import defaultdict


class BM25:
    """BM25 ranking algorithm for component keyword search."""
    
    def __init__(self, documents: List[str], k1: float = 1.5, b: float = 0.75):
        """
        Initialize BM25 with documents and parameters.
        
        Args:
            documents: List of documents (keyword strings)
            k1: Saturation parameter (controls term frequency contribution)
            b: Length normalization parameter (0.0 = no length norm, 1.0 = full)
        """
        self.k1 = k1
        self.b = b
        self.documents = documents
        self.corpus_size = len(documents)
        
        # Tokenize and build index
        self.tokenized_docs = [self._tokenize(doc) for doc in documents]
        self.idf_cache = {}
        self.avg_doc_length = sum(len(doc) for doc in self.tokenized_docs) / max(1, self.corpus_size)
        self._compute_idf()
    
    def _tokenize(self, text: str) -> List[str]:
        """Simple tokenization: split on whitespace and commas."""
        return [token.strip() for token in text.lower().replace(',', ' ').split() if token.strip()]
    
    def _compute_idf(self):
        """Precompute IDF scores for all terms."""
        term_doc_count = defaultdict(int)
        
        for doc in self.tokenized_docs:
            for term in set(doc):  # Use set to count term once per doc
                term_doc_count[term] += 1
        
        for term, doc_count in term_doc_count.items():
            # BM25 IDF formula: log((N - n(t) + 0.5) / (n(t) + 0.5))
            idf = math.log((self.corpus_size - doc_count + 0.5) / (doc_count + 0.5) + 1.0)
            self.idf_cache[term] = idf
    
    def score(self, query: str, doc_index: int) -> float:
        """
        Score a document against a query using BM25.
        
        Args:
            query: Query string
            doc_index: Index of document to score
            
        Returns:
            BM25 score (higher = better match)
        """
        query_terms = self._tokenize(query)
        doc = self.tokenized_docs[doc_index]
        doc_length = len(doc)
        
        score = 0.0
        for term in query_terms:
            idf = self.idf_cache.get(term, 0.0)
            
            # Count term occurrences in document
            term_freq = doc.count(term)
            
            # BM25 formula
            numerator = idf * term_freq * (self.k1 + 1)
            denominator = term_freq + self.k1 * (1 - self.b + self.b * (doc_length / self.avg_doc_length))
            
            score += numerator / denominator
        
        return score


class ComponentMapper:
    """Map user queries to Syncfusion React components using BM25 search."""
    
    def __init__(self, csv_path: str = 'components.csv'):
        """
        Initialize ComponentMapper by loading components.csv.
        
        Args:
            csv_path: Path to components.csv file
            
        Raises:
            FileNotFoundError: If components.csv does not exist
        """
        self.csv_path = Path(csv_path)
        
        if not self.csv_path.exists():
            raise FileNotFoundError(f"Components CSV not found: {csv_path}")
        
        # Load CSV data
        self.components = []
        self.keywords_list = []
        
        with open(self.csv_path, 'r', encoding='utf-8') as f:
            reader = csv.DictReader(f)
            for row in reader:
                self.components.append({
                    'id': row['Component ID'],
                    'name': row['Component Name'],
                    'skill': row['Skill Name'],
                    'keywords': row['Keywords']
                })
                self.keywords_list.append(row['Keywords'])
        
        if not self.components:
            raise ValueError("No components found in CSV")
        
        # Initialize BM25 with keywords
        self.bm25 = BM25(self.keywords_list, k1=1.5, b=0.75)
    
    def search(self, query: str, top_k: int = 5) -> List[Tuple[str, str, float]]:
        """
        Search for components matching the query.
        
        Args:
            query: User query (e.g., "button primary action")
            top_k: Number of top results to return
            
        Returns:
            List of tuples: [(component_name, skill_name, score), ...]
            Sorted by score (highest first)
        """
        if not query or not query.strip():
            return []
        
        # Score all documents
        scores = []
        for i in range(len(self.components)):
            score = self.bm25.score(query, i)
            if score > 0:  # Only include matches with positive score
                component = self.components[i]
                scores.append((
                    component['name'],
                    component['skill'],
                    score
                ))
        
        # Sort by score descending
        scores.sort(key=lambda x: x[2], reverse=True)
        
        return scores[:top_k]
    
    def get_by_name(self, component_name: str) -> Optional[Tuple[str, str]]:
        """
        Get component skill by exact component name.
        
        Args:
            component_name: Exact component name
            
        Returns:
            Tuple of (component_name, skill_name) or None if not found
        """
        for component in self.components:
            if component['name'] == component_name:
                return (component['name'], component['skill'])
        return None
    
    def get_by_skill(self, skill_name: str) -> List[Tuple[str, str]]:
        """
        Get all components for a specific skill.
        
        Args:
            skill_name: Skill name (e.g., 'syncfusion-react-buttons')
            
        Returns:
            List of tuples: [(component_name, skill_name), ...]
        """
        return [
            (c['name'], c['skill'])
            for c in self.components
            if c['skill'] == skill_name
        ]
    
    def list_skills(self) -> List[str]:
        """Get all unique skill names in the database."""
        return sorted(set(c['skill'] for c in self.components))
    
    def list_all(self) -> List[Tuple[str, str]]:
        """Get all components."""
        return [(c['name'], c['skill']) for c in self.components]


def stage_4_component_picking(layout_json: Dict[str, Any], csv_path: str = 'components.csv', icons_csv_path: str = 'icons.csv') -> Dict[str, Any]:
    """
    Map Stage 3 component-mapping.json elements to Syncfusion components and EJ2 icons.
    
    Args:
        layout_json: Stage 3 output JSON with components/sections/icon_elements
        csv_path: Path to components.csv
        icons_csv_path: Path to icons.csv
        
    Returns:
        Dict with mapped_components, mapped_icon_elements, mapped_sections
    """
    mapper = ComponentMapper(csv_path)
    icon_mapper = IconMapper(icons_csv_path)
    mapped_components = []
    mapped_icon_elements = []
    mapped_sections = []
    
    # AUTO-FLATTEN: Handle both nested sections and flat elements
    elements_to_map = []
    has_sections = "sections" in layout_json and layout_json["sections"]
    
    if has_sections:
        # COMPLEX MAPPING: Extract elements from sections
        for section in layout_json.get("sections", []):
            section_id = section.get("section_id", "")
            section_elements = []
            
            for element in section.get("elements", []):
                # Preserve section context
                element["_section_id"] = section_id
                elements_to_map.append(element)
                section_elements.append(element.get("id", ""))
            
            # Store section mapping for output
            if section_elements:
                mapped_sections.append({
                    "section_id": section_id,
                    "section_name": section.get("section_name", ""),
                    "elements": section_elements
                })
    else:
        # SIMPLE MAPPING: Use flat elements array
        elements_to_map = layout_json.get("elements", [])
    
    # MAP ELEMENTS TO COMPONENTS AND ICONS
    for element in elements_to_map:
        # Build search query from element metadata
        query = f"{element.get('type_hint', '')} {element.get('description', '')}"
        
        # Search for best component (top-1 match)
        results = mapper.search(query.strip(), top_k=1)
        
        component_map = {
            "element_id": element['id'],
            "element_name": element['name'],
        }
        
        # Include section_id if present (complex mappings)
        if "_section_id" in element:
            component_map["section_id"] = element["_section_id"]
        
        if results:
            # Found Syncfusion component
            component_name, skill_name, score = results[0]
            component_map.update({
                "component": component_name,
                "skill": skill_name,
                "score": round(score, 2)
            })
        else:
            # No Syncfusion match - use native HTML
            component_map.update({
                "component": "NATIVE_HTML",
                "skill": None,
                "score": 0
            })
        
        # MAP ICON if icon_hint provided
        if element.get('icon_hint'):
            icon_query = element.get('icon_hint', '')
            icon_results = icon_mapper.search(icon_query.strip(), top_k=1)
            
            if icon_results:
                icon_name, icon_class, icon_score = icon_results[0]
                component_map["icon"] = {
                    "name": icon_name,
                    "iconCss": icon_class,
                    "score": round(icon_score, 2)
                }
        
        mapped_components.append(component_map)
    
    # MAP ICON-ONLY ELEMENTS
    for icon_element in layout_json.get("icon_elements", []):
        icon_map = {
            "element_id": icon_element.get('id', ''),
            "element_name": icon_element.get('name', ''),
            "element_type": icon_element.get('type', 'icon'),
        }
        
        # Map icon
        icon_query = icon_element.get('icon_hint', '')
        icon_results = icon_mapper.search(icon_query.strip(), top_k=1)
        
        if icon_results:
            icon_name, icon_class, icon_score = icon_results[0]
            icon_map["icon"] = {
                "name": icon_name,
                "iconCss": icon_class,
                "score": round(icon_score, 2)
            }
        else:
            icon_map["icon"] = {
                "name": "Unknown",
                "iconCss": "e-icons e-help",
                "score": 0
            }
        
        mapped_icon_elements.append(icon_map)
    
    # BUILD OUTPUT
    output = {
        "component_type": layout_json.get('component_type', 'Unknown'),
        "variant": layout_json.get('variant', 'Default'),
        "mapped_components": mapped_components
    }
    
    # Include icon-only elements if present
    if mapped_icon_elements:
        output["mapped_icon_elements"] = mapped_icon_elements
    
    # Include section organization for complex mappings
    if has_sections and mapped_sections:
        output["mapped_sections"] = mapped_sections
    
    return output


class IconMapper:
    """Map user queries to Syncfusion EJ2 icons using BM25 search."""
    
    def __init__(self, csv_path: str = 'icons.csv'):
        """
        Initialize IconMapper by loading icons.csv.
        
        Args:
            csv_path: Path to icons.csv file
            
        Raises:
            FileNotFoundError: If icons.csv does not exist
        """
        self.csv_path = Path(csv_path)
        
        if not self.csv_path.exists():
            raise FileNotFoundError(f"Icons CSV not found: {csv_path}")
        
        # Load CSV data
        self.icons = []
        self.keywords_list = []
        
        with open(self.csv_path, 'r', encoding='utf-8') as f:
            reader = csv.DictReader(f)
            for row in reader:
                self.icons.append({
                    'id': row['Icon ID'],
                    'name': row['Icon Name'],
                    'icon_class': row['Icon Class'],
                    'keywords': row['Keywords']
                })
                self.keywords_list.append(row['Keywords'])
        
        if not self.icons:
            raise ValueError("No icons found in CSV")
        
        # Initialize BM25 with keywords
        self.bm25 = BM25(self.keywords_list, k1=1.5, b=0.75)
    
    def search(self, query: str, top_k: int = 1) -> List[Tuple[str, str, float]]:
        """
        Search for icons matching the query.
        
        Args:
            query: User query (e.g., "save persist store")
            top_k: Number of top results to return
            
        Returns:
            List of tuples: [(icon_name, icon_class, score), ...]
            Sorted by score (highest first)
        """
        if not query or not query.strip():
            return []
        
        # Score all documents
        scores = []
        for i in range(len(self.icons)):
            score = self.bm25.score(query, i)
            if score > 0:  # Only include matches with positive score
                icon = self.icons[i]
                scores.append((
                    icon['name'],
                    icon['icon_class'],
                    score
                ))
        
        # Sort by score descending
        scores.sort(key=lambda x: x[2], reverse=True)
        
        return scores[:top_k]
    
    def get_by_name(self, icon_name: str) -> Optional[Tuple[str, str]]:
        """
        Get icon class by exact icon name.
        
        Args:
            icon_name: Exact icon name
            
        Returns:
            Tuple of (icon_name, icon_class) or None if not found
        """
        for icon in self.icons:
            if icon['name'] == icon_name:
                return (icon['name'], icon['icon_class'])
        return None
    
    def get_by_category(self, category: str) -> List[Tuple[str, str]]:
        """
        Get all icons for a specific category.
        
        Args:
            category: Category name (e.g., 'user_actions', 'data_visualization')
            
        Returns:
            List of tuples: [(icon_name, icon_class), ...]
        """
        return [
            (i['name'], i['icon_class'])
            for i in self.icons
            if i.get('category') == category
        ]
    
    def list_all(self) -> List[Tuple[str, str, str]]:
        """Get all icons with names, classes, and categories."""
        return [(i['name'], i['icon_class'], i['keywords']) for i in self.icons]


def demo_search():
    """Demo: Search for components and print results."""
    print("=" * 80)
    print("COMPONENT MAPPER - BM25 Search Demo")
    print("=" * 80)
    
    mapper = ComponentMapper()
    
    test_queries = [
        "button primary action",
        "data grid table sorting filtering",
        "date picker calendar selection",
        "navigation drawer menu",
        "chart visualization dashboard",
        "file upload form input",
        "notification toast alert",
        "modal dialog popup",
    ]
    
    for query in test_queries:
        print(f"\nQuery: '{query}'")
        print("-" * 80)
        results = mapper.search(query, top_k=3)
        
        if results:
            for i, (name, skill, score) in enumerate(results, 1):
                print(f"  {i}. {name:30} | {skill:35} | Score: {score:.4f}")
        else:
            print("  No matches found.")
    
    print("\n" + "=" * 80)
    print(f"Total components in database: {len(mapper.components)}")
    print(f"Total skills: {len(mapper.list_skills())}")
    print("=" * 80)


if __name__ == '__main__':
    import sys
    import os
    
    # Check for Stage 4 JSON input
    if len(sys.argv) > 1:
        # Stage 4 mode: Process component-mapping.json file
        json_file = sys.argv[1]
        
        # Get the directory where this script is located
        script_dir = Path(__file__).parent
        
        # Resolve path: try absolute first, then relative to script
        json_path = Path(json_file)
        if not json_path.is_absolute():
            json_path = script_dir / json_file
        
        # For Stage 5 code generation, also look for icons.csv next to component-mapping.json
        layout_dir = json_path.parent
        components_csv = script_dir / 'components.csv'
        icons_csv = script_dir / 'icons.csv'
        
        try:
            if not json_path.exists():
                raise FileNotFoundError(f"JSON file not found: {json_file}\nTried: {json_path.absolute()}")
            
            with open(json_path, 'r', encoding='utf-8') as f:
                layout_json = json.load(f)
            
            result = stage_4_component_picking(
                layout_json,
                csv_path=str(components_csv),
                icons_csv_path=str(icons_csv)
            )
            print(json.dumps(result, indent=2))
        except FileNotFoundError as e:
            print(f"Error: {e}", file=sys.stderr)
            sys.exit(1)
        except json.JSONDecodeError as e:
            print(f"Error: Invalid JSON in {json_file}: {e}", file=sys.stderr)
            sys.exit(1)
        except Exception as e:
            print(f"Error: {e}", file=sys.stderr)
            sys.exit(1)
    else:
        # Demo mode: Run test queries
        demo_search()
