# SEO Engine Setup Guide

## Assignment Requirement

**Original task:** Install VS Code, install Claude Code, and generate an audit report of any website using the Claude SEO plugin.  
**GitHub repository provided:** https://github.com/ivankuznetsov/claude-seo  
**Copied deadline in assignment text:** March 31, 2026  
**Important date note:** As of August 27, 2026, March 31, 2026 is already in the past. Confirm the real deadline with the instructor or team.

## Can Codex Do It Instead?

Yes, Codex can create the SEO audit report. The file `SEO-Audit-Report-Ecommerized.md` in this folder is the completed alternative audit report.

However, if the instructor specifically checks for Claude Code installation screenshots, Codex cannot replace that proof. In that case, the student needs access to Claude Code.

## What Is Free and What May Cost Money?

| Item | Free? | Notes |
|---|---|---|
| Visual Studio Code | Yes | VS Code can be downloaded and installed for free. |
| Claude SEO GitHub plugin | Yes | The repository is public/open source. |
| Installing Claude Code | Usually free to install | The installer itself is available publicly. |
| Using Claude Code | Not always free | Claude Code requires login through a Claude subscription, Claude Console/API billing, Team/Enterprise access, or supported cloud provider access. |

## Official Claude Code Setup Path

These steps are only needed if the instructor requires Claude Code proof.

### Step 1: Install VS Code

Download and install VS Code from:

https://code.visualstudio.com/

### Step 2: Install Claude Code

Official Claude Code docs list Windows install options such as:

```powershell
winget install Anthropic.ClaudeCode
```

The official docs also show a PowerShell installer command:

```powershell
irm https://claude.ai/install.ps1 | iex
```

After installation, confirm it works:

```powershell
claude --version
```

### Step 3: Log In

Start Claude Code:

```powershell
claude
```

Claude Code will ask the user to authenticate. The student needs one of these:

- Claude Pro, Max, Team, or Enterprise account
- Claude Console account with API billing or credits
- Supported cloud provider access
- Organization-provided access

### Step 4: Install the SEO Plugin

Inside Claude Code, run:

```text
/plugin marketplace add ivankuznetsov/claude-seo
/plugin install agent-seo@ivankuznetsov-claude-seo
```

### Step 5: Run an SEO Audit

Inside Claude Code, run:

```text
/seo:analyze-existing https://ecommerized.com/
```

The plugin also supports other commands such as:

```text
/seo:research [topic]
/seo:write [topic]
/seo:optimize [file]
/seo:fact-check [file]
```

## Screenshots to Capture If Required

If the instructor asks for screenshots, capture:

| Screenshot | What It Should Show |
|---|---|
| 1 | VS Code installed/open |
| 2 | Terminal showing `claude --version` |
| 3 | Claude Code login/session screen |
| 4 | Plugin install commands completed |
| 5 | `/seo:analyze-existing https://ecommerized.com/` command |
| 6 | Generated SEO audit output |

## Submission Option Without Claude Access

If there is no Claude Code account available, submit:

1. `SEO-Audit-Report-Ecommerized.md`
2. A note saying:

```text
Claude Code requires authenticated access through a Claude subscription, Claude Console/API billing, Team/Enterprise account, or supported cloud provider. Since I did not have Claude Code access, I completed the required website SEO audit report using Codex as an AI-assisted alternative.
```

## Sources Used

- Claude Code quickstart: https://code.claude.com/docs/en/quickstart
- Claude SEO GitHub plugin: https://github.com/ivankuznetsov/claude-seo
- VS Code: https://code.visualstudio.com/
