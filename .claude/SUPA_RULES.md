# SupaBMADFloSho Unified Rules

## 🎯 System Philosophy
SupaBMADFloSho operates on the principle of "One Truth, Many Views" - a single source of requirements (PRP) that all agents understand and act upon.

## 🚫 What We're Eliminating (The Worst Parts)

### From xText-PRP:
- ❌ Redundant context commands that duplicate BMAD planning
- ❌ Overly complex PRP templates (simplified with BMAD structure)
- ❌ Manual context switching between phases

### From SuperClaude:
- ❌ Generic personas without project context
- ❌ Commands that duplicate BMAD agent capabilities
- ❌ Isolated implementation without planning phase

### From BMAD-METHOD:  
- ❌ Web-only planning limitation (integrated with IDE)
- ❌ Manual story creation (automated with xText)
- ❌ Separate document sharding (unified with context)

## ✅ What We're Keeping (The Best Parts)

### From BMAD-METHOD:
- ✅ **Agentic Planning Workflow** - Analyst → PM → Architect flow
- ✅ **Structured Templates** - PRD, Architecture, Epic formats
- ✅ **Quality Checklists** - PO validation and QA reviews
- ✅ **Human-in-the-loop refinement** - Collaborative planning

### From xText-PRP:
- ✅ **Context Engineering** - AI-optimized requirements
- ✅ **PRP Core Concept** - Single source of truth
- ✅ **Automatic Sharding** - Smart document splitting
- ✅ **FloSho Integration** - Built-in testing framework

### From SuperClaude:
- ✅ **Smart Personas** - Now context-aware via PRP
- ✅ **MCP Integrations** - External tool connections
- ✅ **Parallel Commands** - Concurrent development
- ✅ **Enhanced Claude features** - All 16 commands

## 🔄 Unified Command Mapping

### Planning Commands (Merged)
```yaml
Old Commands:
  BMAD: *analyst, *pm, *architect
  xText: /xt:plan, /xt:requirements
  SuperClaude: /sc:analyze

New Unified Command:
  /supa:plan [phase]
  - Runs BMAD planning agents
  - Generates xText PRP automatically
  - Assigns SuperClaude personas
  - Sets up FloSho tests
```

### Context Commands (Merged)
```yaml
Old Commands:
  BMAD: shard-doc, shard-epic
  xText: /xt:context, /xt:shard
  SuperClaude: /sc:understand

New Unified Command:
  /supa:context [auto|manual]
  - Uses BMAD document structure
  - Applies xText engineering
  - Distributes to personas
  - Preserves all context
```

### Implementation Commands (Enhanced)
```yaml
Enhanced Commands:
  /supa:implement [story]
  - Reads BMAD story format
  - Uses xText context
  - Executes with SuperClaude persona
  - Triggers FloSho test generation
```

## 🧠 Intelligent Agent Routing

### Automatic Agent Selection
```python
def route_to_agent(task_type, context):
    if task_type == "market_research":
        return "bmad:analyst"
    elif task_type == "requirements":
        return "bmad:pm + xt:prp"
    elif task_type == "architecture":
        return "bmad:architect + sc:system"
    elif task_type == "implementation":
        return "sc:persona[best_fit]"
    elif task_type == "testing":
        return "fs:flow + bmad:qa"
```

### Context Preservation
All agents share:
- Current PRP document
- Technical preferences
- Project history
- Test scenarios
- Implementation status

## 📋 Workflow Optimization

### Old Way (3 Separate Workflows):
1. BMAD: Plan → Document → Shard → Implement
2. xText: Context → PRP → Init → Build  
3. SuperClaude: Analyze → Design → Implement → Test

### New Way (1 Unified Workflow):
```mermaid
graph LR
    A[/supa:init] --> B[Planning + PRP]
    B --> C[Context + Sharding]
    C --> D[Parallel Implementation]
    D --> E[Auto Testing + Docs]
    E --> F[Continuous Improvement]
    F --> C
```

## 🚀 Performance Optimizations

### 1. Parallel Processing
- Multiple BMAD agents work simultaneously
- SuperClaude personas develop in parallel
- FloSho tests run during development

### 2. Smart Caching
- PRP cached and reused across agents
- Context preserved between commands
- Test results inform future iterations

### 3. Automatic Handoffs
- BMAD → xText: PRD becomes PRP
- xText → SuperClaude: Context maps to personas
- SuperClaude → FloSho: Code triggers tests
- FloSho → BMAD: Results update requirements

## 🎯 Key Integration Points

### 1. Document Flow
```
BMAD PRD → xText PRP Enhancement → SuperClaude Implementation Guide → FloSho Test Spec
```

### 2. Agent Communication
```
BMAD Agents ← Shared Context → xText Engine ← Project State → SuperClaude Personas ← Test Results → FloSho
```

### 3. Quality Feedback Loop
```
FloSho Tests → BMAD QA → xText Context Update → SuperClaude Fixes → FloSho Validation
```

## 🔧 Configuration

### Minimal Setup
```yaml
# .claude/supa-config.yaml
mode: unified
frameworks:
  bmad: 
    planning: true
    agents: [analyst, pm, architect, qa]
  xtext:
    context_engineering: true
    auto_prp: true
  superclaude:
    personas: smart
    mcp_enabled: true
  flosho:
    auto_test: true
    auto_document: true

workflow: optimized
parallel_execution: true
context_preservation: maximum
```

## 💡 Why This Works

1. **No Redundancy**: Each framework handles what it does best
2. **Full Context**: Information flows seamlessly between all parts
3. **Automatic Integration**: Commands trigger appropriate workflows
4. **Quality Built-In**: Testing and documentation are automatic
5. **Extensible**: Easy to add new capabilities without conflicts

## 🎉 The Result

SupaBMADFloSho isn't just the sum of its parts - it's a multiplication of capabilities:

- **BMAD's Structure** × **xText's Context** = Perfect Requirements
- **Perfect Requirements** × **SuperClaude's Personas** = Flawless Implementation  
- **Flawless Implementation** × **FloSho's Testing** = Quality Guaranteed
- **Quality Guaranteed** × **Unified Workflow** = 10x Development Speed

This is the future of AI-assisted development - one system, infinite possibilities!
