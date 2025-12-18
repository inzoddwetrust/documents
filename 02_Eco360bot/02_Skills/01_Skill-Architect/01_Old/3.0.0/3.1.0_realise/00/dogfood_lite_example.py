#!/usr/bin/env python3
"""
Skill Architect Lite v3.0.0 - Dogfooding Checker
Measures how well this skill follows skill-architect recommendations

This is an EXAMPLE implementation showing how to add dogfood.py to components
that don't have it yet.
"""

import os
import sys
from pathlib import Path


def count_lines_in_directory(directory, extensions):
    """Count lines in files with specified extensions"""
    total = 0
    for ext in extensions:
        for filepath in Path(directory).rglob(f"*.{ext}"):
            try:
                with open(filepath, 'r', encoding='utf-8') as f:
                    total += len(f.readlines())
            except:
                pass
    return total


def check_config_driven(root_dir):
    """
    Check if skill is config-driven (YAML configs)
    Target: ≥30% of total lines should be config
    """
    print("\n📋 Config-Driven Architecture:")
    
    config_dir = os.path.join(root_dir, "config")
    src_dir = os.path.join(root_dir, "src")
    
    if not os.path.exists(config_dir):
        print("  ❌ No config/ directory")
        return 0.0
    
    yaml_lines = count_lines_in_directory(config_dir, ['yaml', 'yml'])
    py_lines = count_lines_in_directory(src_dir, ['py'])
    total_lines = yaml_lines + py_lines
    
    if total_lines == 0:
        print("  ⚠️  No code found")
        return 0.0
    
    ratio = (yaml_lines / total_lines) * 100
    
    print(f"  YAML lines: {yaml_lines}")
    print(f"  Total lines: {total_lines}")
    print(f"  Ratio: {ratio:.2f}% (target: 30%)")
    
    # Score: 1.0 if ratio >= 30%, proportional below
    score = min(1.0, ratio / 30.0)
    print(f"  Score: {score:.2f}/1.0")
    
    return score


def check_templates(root_dir):
    """
    Check if skill uses templates (Jinja2)
    """
    print("\n📝 Template Usage:")
    
    templates_dir = os.path.join(root_dir, "src", "templates")
    build_script = os.path.join(root_dir, "scripts", "build.py")
    
    has_templates = os.path.exists(templates_dir)
    has_build = os.path.exists(build_script)
    
    if has_templates:
        print("  ✓ Templates directory exists")
    else:
        print("  ✗ No templates directory")
    
    if has_build:
        print("  ✓ Build script exists")
    else:
        print("  ✗ No build script")
    
    score = 0.0
    if has_templates:
        score += 0.5
    if has_build:
        score += 0.5
    
    print(f"  Score: {score:.2f}/1.0")
    return score


def check_validation(root_dir):
    """
    Check if skill has validation automation
    """
    print("\n✅ Validation Automation:")
    
    validate_script = os.path.join(root_dir, "scripts", "validate.py")
    validation_config = os.path.join(root_dir, "config", "validation_rules.yaml")
    
    has_script = os.path.exists(validate_script)
    has_config = os.path.exists(validation_config)
    
    if has_script:
        print("  ✓ Validation script exists")
    else:
        print("  ✗ No validation script")
    
    if has_config:
        print("  ✓ Validation config exists")
    else:
        print("  ⚠️  No validation config (optional)")
    
    score = 0.0
    if has_script:
        score += 0.7
    if has_config:
        score += 0.3
    
    print(f"  Score: {score:.2f}/1.0")
    return score


def check_documentation(root_dir):
    """
    Check if skill has self-documentation
    """
    print("\n📚 Self-Documentation:")
    
    docs = {
        "ARCHITECTURE.md": "Architecture documentation",
        "LEARNING.md": "Learning guide",
        "examples/how_i_work": "Living examples"
    }
    
    score = 0.0
    for doc, description in docs.items():
        doc_path = os.path.join(root_dir, doc)
        if os.path.exists(doc_path):
            print(f"  ✓ {description}: {doc}")
            score += 1.0 / len(docs)
        else:
            print(f"  ⚠️  Missing {description}: {doc}")
    
    print(f"  Score: {score:.2f}/1.0")
    return score


def check_transparency(root_dir):
    """
    Check if source code is visible and documented
    """
    print("\n🔍 Transparency:")
    
    src_dir = os.path.join(root_dir, "src")
    config_dir = os.path.join(root_dir, "config")
    
    has_src = os.path.exists(src_dir)
    has_config = os.path.exists(config_dir)
    
    if has_src:
        print("  ✓ Source code visible")
    else:
        print("  ✗ No source code")
    
    if has_config:
        print("  ✓ Configuration visible")
    else:
        print("  ✗ No configuration")
    
    score = 0.0
    if has_src:
        score += 0.5
    if has_config:
        score += 0.5
    
    print(f"  Score: {score:.2f}/1.0")
    return score


def check_build_automation(root_dir):
    """
    Check if skill has build automation scripts
    """
    print("\n🤖 Build Automation:")
    
    scripts = {
        "build.py": "Build script",
        "validate.py": "Validation script",
        "package.sh": "Packaging script"
    }
    
    score = 0.0
    for script, description in scripts.items():
        script_path = os.path.join(root_dir, "scripts", script)
        if os.path.exists(script_path):
            print(f"  ✓ {description}")
            score += 1.0 / len(scripts)
        else:
            print(f"  ⚠️  Missing {description}")
    
    print(f"  Score: {score:.2f}/1.0")
    return score


def print_progress_bar(label, score, weight):
    """Print a visual progress bar"""
    bar_length = 20
    filled = int(bar_length * score)
    bar = "█" * filled + "░" * (bar_length - filled)
    print(f"  {label:30} {bar} {score:.2f}")


def main():
    if len(sys.argv) < 2:
        print("Usage: python dogfood.py <root_directory>")
        sys.exit(1)
    
    root_dir = sys.argv[1]
    
    if not os.path.exists(root_dir):
        print(f"Error: Directory '{root_dir}' does not exist")
        sys.exit(1)
    
    print("=" * 60)
    print("Skill Architect Lite v3.0.0 - Dogfooding Checker")
    print("=" * 60)
    print("\nMeasuring how well I follow my own advice...")
    
    # Run all checks
    scores = {
        "config_driven": check_config_driven(root_dir),
        "templates": check_templates(root_dir),
        "validation": check_validation(root_dir),
        "documentation": check_documentation(root_dir),
        "transparency": check_transparency(root_dir),
        "build_automation": check_build_automation(root_dir)
    }
    
    # Weights for each metric (Lite version has adjusted weights)
    weights = {
        "config_driven": 0.20,      # 20% - Config-driven
        "templates": 0.20,          # 20% - Template usage
        "validation": 0.20,         # 20% - Validation
        "documentation": 0.15,      # 15% - Documentation
        "transparency": 0.10,       # 10% - Transparency
        "build_automation": 0.15    # 15% - Automation
    }
    
    # Calculate weighted total
    total_score = sum(scores[k] * weights[k] * 10 for k in scores.keys())
    
    print("\n" + "=" * 60)
    print("DOGFOODING REPORT")
    print("=" * 60)
    print("\nIndividual Metrics:")
    
    print_progress_bar(
        f"Config-Driven ({int(weights['config_driven']*100)}%)",
        scores['config_driven'],
        weights['config_driven']
    )
    print_progress_bar(
        f"Template Usage ({int(weights['templates']*100)}%)",
        scores['templates'],
        weights['templates']
    )
    print_progress_bar(
        f"Validation Automation ({int(weights['validation']*100)}%)",
        scores['validation'],
        weights['validation']
    )
    print_progress_bar(
        f"Self-Documentation ({int(weights['documentation']*100)}%)",
        scores['documentation'],
        weights['documentation']
    )
    print_progress_bar(
        f"Transparency ({int(weights['transparency']*100)}%)",
        scores['transparency'],
        weights['transparency']
    )
    print_progress_bar(
        f"Build Automation ({int(weights['build_automation']*100)}%)",
        scores['build_automation'],
        weights['build_automation']
    )
    
    print("\n" + "=" * 60)
    print(f"TOTAL DOGFOOD SCORE: {total_score:.1f}/10.0")
    print("=" * 60)
    print()
    
    # Interpretation
    if total_score >= 9.0:
        print("✅ EXCELLENT! Exceeds target (≥9.0)")
        print("   This skill truly practices what it preaches!")
        return_code = 0
    elif total_score >= 7.0:
        print("⚠️  GOOD but has room for improvement")
        print("   Target: ≥9.0 for production skills")
        return_code = 0
    elif total_score >= 5.0:
        print("⚠️  NEEDS IMPROVEMENT")
        print("   Not yet at production quality")
        return_code = 1
    else:
        print("❌ CRITICAL - Does not follow own advice")
        print("   Major refactoring needed")
        return_code = 1
    
    print()
    sys.exit(return_code)


if __name__ == "__main__":
    main()
