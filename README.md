# keep2md
Translates Google Keep notes into Markdown and vice versa.

## Features
- [ ] note to markdown
- [ ] markdown to note
- [ ] `gkeepapi` connection
- [ ] REST API via `flask`

## Mappings
| status | Keep | Markdown |
| - | - | - |
| high priority | server_id | yaml server_id |
| high priority | title | h1 on the first line |
| high priority | labels | yaml labels |
| low priority  | pinned | `#pin` label |
| low priority  | archieved | `#archive` label |
| low priority  | task list | task list |
| mid priority  | images | yaml media links |
