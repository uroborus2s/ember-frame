# Director Room Artifact Contract

Every child Codex agent returns a single structured envelope. The parent Codex
coordinator writes files to disk after checking the envelope.

## Envelope

```json
{
  "status": "success",
  "summary": "One sentence result.",
  "artifacts": [
    {
      "path": "{episode-id}/shots/shot-list.json",
      "kind": "json",
      "content": "{ \"shots\": [] }"
    }
  ],
  "next_actions": ["cinematographer-agent"],
  "warnings": [],
  "handoff": {
    "main_output": "{episode-id}/shots/shot-list.json",
    "assumptions": [],
    "quality_notes": [],
    "blocked_questions": []
  }
}
```

## Status Values

- `success`: output is ready for the next agent.
- `warning`: output is usable but contains risks the parent should preserve.
- `blocked`: the agent cannot continue without parent or user input.

## Artifact Rules

- Use project-relative paths only.
- Use Markdown for director briefs, camera notes, and storyboard plans.
- Use JSON for machine-readable scene breakdowns, shot lists, visual continuity,
  generation strategy, and shot prompt drafts.
- Do not include absolute paths in child-agent output; the parent resolves them.
- Keep artifact content complete enough to write directly to disk.
- Do not modify or restate source artifacts unless a downstream output needs a
  short citation or source reference.

## Required Handoff Fields

- `main_output`: one project-relative path.
- `assumptions`: concrete assumptions made by the role.
- `quality_notes`: role-specific risks, tradeoffs, or strengths.
- `blocked_questions`: questions only when `status` is `blocked`.
