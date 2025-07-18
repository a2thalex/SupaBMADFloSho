#!/usr/bin/env python3
"""
SupaBMADFloSho Unified Installer
Intelligently merges BMAD-METHOD, xText-PRP, and SuperClaude
"""

import os
import sys
import json
import shutil
import subprocess
from pathlib import Path
from datetime import datetime


class SupaBMADFloShoInstaller:
    def __init__(self):
        self.repo_dir = Path.cwd()
        self.name = "SupaBMADFloSho"
        self.version = "1.0.0"
        self.sources = {
            'bmad': 'https://github.com/bmadcode/BMAD-METHOD.git',
            'xtext': 'https://github.com/a2thalex/xtext-prp.git',
            'superclaude': 'https://github.com/NomenAK/SuperClaude.git'
        }
        
    def print_banner(self):
        print(f"""
╔═══════════════════════════════════════════════════════════╗
║         🚀 SupaBMADFloSho Unified Installer 🚀            ║
║                                                           ║
║  Merging the best of:                                     ║
║  • BMAD-METHOD - Agentic Planning & Workflows             ║
║  • xText-PRP - Context Engineering                        ║
║  • SuperClaude - Enhanced Commands & Personas             ║
║  • FloSho - Visual Testing & Documentation                ║
╚═══════════════════════════════════════════════════════════╝
        """)

    def check_dependencies(self):
        """Check for required dependencies"""
        print("\n🔍 Checking dependencies...")
        
        # Check Node.js
        try:
            result = subprocess.run(['node', '--version'], capture_output=True, text=True)
            node_version = result.stdout.strip()
            print(f"✅ Node.js {node_version}")
        except:
            print("❌ Node.js not found. Please install Node.js 20+")
            return False
            
        # Check npm
        try:
            result = subprocess.run(['npm', '--version'], capture_output=True, text=True)
            npm_version = result.stdout.strip()
            print(f"✅ npm {npm_version}")
        except:
            print("❌ npm not found")
            return False
            
        # Check git
        try:
            subprocess.run(['git', '--version'], capture_output=True, check=True)
            print("✅ git")
        except:
            print("❌ git not found")
            return False
            
        return True

    def create_directory_structure(self):
        """Create the unified directory structure"""
        print("\n📁 Creating SupaBMADFloSho directory structure...")
        
        directories = [
            # Planning layer (BMAD)
            'planning/agents',
            'planning/workflows', 
            'planning/templates',
            'planning/checklists',
            
            # Context layer (xText)
            'contexts/engineering',
            'contexts/prp',
            'contexts/sharding',
            
            # Implementation layer (SuperClaude)
            'implementation/personas',
            'implementation/commands',
            'implementation/mcp',
            
            # Testing layer (FloSho)
            'testing/flosho/core',
            'testing/flosho/flows',
            'testing/flosho/documentation',
            
            # Orchestration layer (SupaBMADFloSho)
            'orchestration/unified-workflow',
            'orchestration/conflict-resolution',
            'orchestration/optimization',
            
            # Shared resources
            '.claude/commands',
            '.claude/agents',
            'docs/guides',
            'docs/examples',
            'setup/profiles',
            'data/knowledge-base',
            'data/preferences'
        ]
        
        for dir_path in directories:
            Path(dir_path).mkdir(parents=True, exist_ok=True)
            
        print("✅ Directory structure created")

    def merge_bmad_components(self):
        """Integrate BMAD-METHOD components"""
        print("\n🔄 Integrating BMAD-METHOD components...")
        
        # Clone or update BMAD
        bmad_dir = Path('temp/bmad-method')
        if not bmad_dir.exists():
            print("  📥 Cloning BMAD-METHOD...")
            subprocess.run([
                'git', 'clone', '--depth=1',
                self.sources['bmad'],
                str(bmad_dir)
            ], check=True)
        
        # Copy planning agents
        if (bmad_dir / 'bmad-core/agents').exists():
            for agent in ['analyst.md', 'pm.md', 'architect.md', 'po.md', 'qa.md']:
                src = bmad_dir / f'bmad-core/agents/{agent}'
                if src.exists():
                    shutil.copy2(src, Path('planning/agents') / agent)
                    print(f"  ✅ Copied {agent}")
        
        # Copy workflows
        if (bmad_dir / 'bmad-core/workflows').exists():
            for workflow in (bmad_dir / 'bmad-core/workflows').glob('*.yaml'):
                shutil.copy2(workflow, Path('planning/workflows') / workflow.name)
                
        # Copy templates
        if (bmad_dir / 'bmad-core/templates').exists():
            for template in (bmad_dir / 'bmad-core/templates').glob('*.md'):
                shutil.copy2(template, Path('planning/templates') / template.name)
                
        print("✅ BMAD-METHOD components integrated")

    def merge_xtext_components(self):
        """Integrate xText-PRP components"""
        print("\n🔄 Integrating xText-PRP components...")
        
        # Clone or update xText
        xtext_dir = Path('temp/xtext-prp')
        if not xtext_dir.exists():
            print("  📥 Cloning xText-PRP...")
            subprocess.run([
                'git', 'clone', '--depth=1', 
                self.sources['xtext'],
                str(xtext_dir)
            ], check=True)
        
        # Copy context engineering files
        if (xtext_dir / 'src/contexts').exists():
            for context_file in (xtext_dir / 'src/contexts').glob('*.md'):
                shutil.copy2(context_file, Path('contexts/engineering') / context_file.name)
                
        # Copy PRP templates
        if (xtext_dir / 'templates').exists():
            for prp_file in (xtext_dir / 'templates').glob('*prp*.md'):
                shutil.copy2(prp_file, Path('contexts/prp') / prp_file.name)
                
        # Copy FloSho (already in xText)
        if (xtext_dir / 'flosho').exists():
            shutil.copytree(
                xtext_dir / 'flosho',
                Path('testing/flosho/core'),
                dirs_exist_ok=True
            )
            
        print("✅ xText-PRP components integrated")

    def merge_superclaude_components(self):
        """Integrate SuperClaude components"""
        print("\n🔄 Integrating SuperClaude components...")
        
        # Clone or update SuperClaude
        sc_dir = Path('temp/superclaude')
        if not sc_dir.exists():
            print("  📥 Cloning SuperClaude...")
            subprocess.run([
                'git', 'clone', '--depth=1',
                self.sources['superclaude'],
                str(sc_dir)
            ], check=True)
        
        # Copy personas
        if (sc_dir / '.claude/personas').exists():
            for persona in (sc_dir / '.claude/personas').glob('*.md'):
                shutil.copy2(persona, Path('implementation/personas') / persona.name)
                
        # Copy commands
        if (sc_dir / '.claude/commands').exists():
            for cmd in (sc_dir / '.claude/commands').glob('*.md'):
                shutil.copy2(cmd, Path('implementation/commands') / cmd.name)
                
        print("✅ SuperClaude components integrated")

    def create_unified_commands(self):
        """Create the unified command system"""
        print("\n🎯 Creating unified command system...")
        
        unified_commands = {
            "supa:init": {
                "description": "Initialize a new SupaBMADFloSho project",
                "triggers": ["bmad:analyst", "xt:prp", "sc:personas", "fs:setup"]
            },
            "supa:plan": {
                "description": "Run unified planning workflow",
                "triggers": ["bmad:plan", "xt:context", "auto-shard"]
            },
            "supa:implement": {
                "description": "Context-aware implementation",
                "triggers": ["read-prp", "sc:implement", "fs:test-gen"]
            },
            "supa:test": {
                "description": "Unified testing and documentation",
                "triggers": ["fs:flow", "bmad:qa", "auto-doc"]
            },
            "supa:optimize": {
                "description": "Optimize workflow and resolve conflicts",
                "triggers": ["analyze-performance", "resolve-conflicts", "cache-context"]
            }
        }
        
        # Write unified commands
        commands_file = Path('.claude/commands/unified-commands.json')
        with open(commands_file, 'w') as f:
            json.dump(unified_commands, f, indent=2)
            
        print("✅ Unified command system created")

    def create_orchestration_layer(self):
        """Create the SupaBMADFloSho orchestration layer"""
        print("\n🎼 Creating orchestration layer...")
        
        # Create the master orchestrator
        orchestrator_content = '''# SupaBMADFloSho Master Orchestrator

## Role
I am the Master Orchestrator for SupaBMADFloSho, coordinating between:
- BMAD planning agents
- xText context engineering
- SuperClaude implementation personas
- FloSho testing framework

## Core Responsibilities

### 1. Workflow Management
- Route tasks to appropriate framework
- Maintain context across all agents
- Optimize parallel execution
- Resolve conflicts between frameworks

### 2. Context Preservation
- Cache and distribute PRP documents
- Maintain technical preferences
- Track project state
- Share test results

### 3. Intelligent Routing
```python
def route_task(task):
    if task.type in ['research', 'planning', 'architecture']:
        return delegate_to_bmad(task)
    elif task.type in ['context', 'requirements', 'sharding']:
        return delegate_to_xtext(task)
    elif task.type in ['implement', 'build', 'develop']:
        return delegate_to_superclaude(task)
    elif task.type in ['test', 'document', 'validate']:
        return delegate_to_flosho(task)
    else:
        return handle_unified(task)
```

### 4. Quality Assurance
- Ensure all frameworks follow PRP
- Validate outputs match requirements
- Coordinate testing across components
- Generate unified documentation

## Startup Sequence
1. Load project PRP (if exists)
2. Initialize all framework agents
3. Establish communication channels
4. Begin orchestrated workflow

## Commands
- `/supa:status` - Show all active agents and tasks
- `/supa:route [task]` - Manually route a task
- `/supa:optimize` - Optimize current workflow
- `/supa:report` - Generate unified progress report
'''
        
        with open(Path('orchestration/master-orchestrator.md'), 'w') as f:
            f.write(orchestrator_content)
            
        print("✅ Orchestration layer created")

    def create_integration_tests(self):
        """Create integration tests for the unified system"""
        print("\n🧪 Creating integration tests...")
        
        test_flow = '''# SupaBMADFloSho Integration Test Flow

## Test: Complete Project Lifecycle

### 1. Initialization Test
```javascript
test('Project initialization creates all components', async () => {
  const result = await supa.init('Test SaaS Project');
  
  expect(result).toHaveProperty('bmad.brief');
  expect(result).toHaveProperty('xtext.prp');
  expect(result).toHaveProperty('superclaude.personas');
  expect(result).toHaveProperty('flosho.tests');
});
```

### 2. Planning Integration Test
```javascript
test('BMAD planning feeds xText PRP', async () => {
  const prd = await bmad.createPRD(brief);
  const prp = await xtext.generatePRP(prd);
  
  expect(prp.requirements).toMatchObject(prd.features);
  expect(prp.context).toContain(prd.technical_requirements);
});
```

### 3. Implementation Integration Test
```javascript
test('SuperClaude personas use PRP context', async () => {
  const prp = await xtext.loadPRP();
  const implementation = await superclaude.implement(prp);
  
  expect(implementation.matches_requirements).toBe(true);
  expect(implementation.uses_preferred_tech).toBe(true);
});
```

### 4. Testing Integration Test
```javascript
test('FloSho generates tests from PRP', async () => {
  const prp = await xtext.loadPRP();
  const tests = await flosho.generateTests(prp);
  
  expect(tests.scenarios).toMatchObject(prp.user_stories);
  expect(tests.coverage).toBeGreaterThan(0.9);
});
```
'''
        
        with open(Path('testing/integration-tests.md'), 'w') as f:
            f.write(test_flow)
            
        print("✅ Integration tests created")

    def create_configuration(self):
        """Create unified configuration"""
        print("\n⚙️ Creating unified configuration...")
        
        config = {
            "name": "SupaBMADFloSho",
            "version": "1.0.0",
            "frameworks": {
                "bmad": {
                    "enabled": True,
                    "agents": ["analyst", "pm", "architect", "po", "qa", "sm", "dev"],
                    "planning_mode": "collaborative"
                },
                "xtext": {
                    "enabled": True,
                    "auto_prp": True,
                    "context_engineering": True,
                    "smart_sharding": True
                },
                "superclaude": {
                    "enabled": True,
                    "personas": "context-aware",
                    "parallel_execution": True,
                    "mcp_integration": True
                },
                "flosho": {
                    "enabled": True,
                    "auto_test": True,
                    "visual_testing": True,
                    "auto_documentation": True
                }
            },
            "orchestration": {
                "mode": "intelligent",
                "routing": "automatic",
                "context_preservation": "maximum",
                "conflict_resolution": "smart",
                "performance_optimization": True
            },
            "defaults": {
                "workflow": "unified",
                "planning_first": True,
                "test_driven": True,
                "documentation": "automatic"
            }
        }
        
        with open(Path('.claude/supa-config.json'), 'w') as f:
            json.dump(config, f, indent=2)
            
        print("✅ Configuration created")

    def create_example_project(self):
        """Create an example project to demonstrate the unified system"""
        print("\n📚 Creating example project...")
        
        example = '''# Example: Building a Team Collaboration Platform

## Using SupaBMADFloSho

### 1. Initialize Project
```bash
/supa:init "Team collaboration platform with real-time features"
```

This triggers:
- BMAD Analyst researches collaboration tools market
- xText generates initial PRP structure
- SuperClaude assigns specialized personas
- FloSho sets up test framework

### 2. Planning Phase
```bash
/supa:plan collaborative
```

Results in:
- Comprehensive PRD from BMAD PM
- Technical architecture from BMAD Architect
- Enhanced PRP with full context from xText
- Persona assignments from SuperClaude
- Test scenarios from FloSho

### 3. Implementation Phase
```bash
/supa:implement parallel
```

Executes:
- Frontend persona builds UI components
- Backend persona creates API endpoints
- Database persona designs schema
- DevOps persona sets up infrastructure
- All reading from same PRP context

### 4. Testing & Documentation
```bash
/supa:test comprehensive
```

Generates:
- Visual regression tests
- API endpoint tests
- Integration test suite
- Complete documentation
- Deployment guide

## Timeline Comparison

### Traditional Approach: 3-4 weeks
- Week 1: Planning and design
- Week 2-3: Implementation
- Week 4: Testing and documentation

### SupaBMADFloSho: 3-4 days
- Day 1: Automated planning with human refinement
- Day 2-3: Parallel implementation with context
- Day 3-4: Automated testing and documentation

## Key Advantages Demonstrated

1. **No Context Loss**: Every agent knows the full picture
2. **Parallel Execution**: Multiple personas work simultaneously  
3. **Automatic Quality**: Tests generated from requirements
4. **Living Documentation**: Updates automatically with code

The result is a production-ready application with:
- ✅ Comprehensive planning documents
- ✅ Clean, well-architected code
- ✅ Full test coverage
- ✅ Complete documentation
- ✅ Deployment automation

All in a fraction of the time! 🚀
'''
        
        with open(Path('docs/examples/team-collaboration-example.md'), 'w') as f:
            f.write(example)
            
        print("✅ Example project created")

    def cleanup_temp_files(self):
        """Clean up temporary files"""
        print("\n🧹 Cleaning up temporary files...")
        temp_dir = Path('temp')
        if temp_dir.exists():
            shutil.rmtree(temp_dir)
        print("✅ Cleanup complete")

    def install(self):
        """Run the complete installation"""
        self.print_banner()
        
        if not self.check_dependencies():
            print("\n❌ Missing dependencies. Please install required tools.")
            return False
            
        try:
            self.create_directory_structure()
            self.merge_bmad_components()
            self.merge_xtext_components()
            self.merge_superclaude_components()
            self.create_unified_commands()
            self.create_orchestration_layer()
            self.create_integration_tests()
            self.create_configuration()
            self.create_example_project()
            self.cleanup_temp_files()
            
            print(f"""
╔═══════════════════════════════════════════════════════════╗
║           ✨ Installation Complete! ✨                    ║
╚═══════════════════════════════════════════════════════════╝

🚀 SupaBMADFloSho is ready to use!

📝 Next Steps:
1. Review the architecture: ARCHITECTURE.md
2. Read the unified rules: .claude/SUPA_RULES.md
3. Try the example: docs/examples/team-collaboration-example.md
4. Start a project: /supa:init "your idea"

🌊 The future of AI development is here!
""")
            return True
            
        except Exception as e:
            print(f"\n❌ Installation failed: {str(e)}")
            return False


if __name__ == "__main__":
    installer = SupaBMADFloShoInstaller()
    installer.install()
