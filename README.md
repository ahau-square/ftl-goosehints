# Using goose for building FTL apps

Use the .goosehints and have it refer to the ftl.txt provided. 

That txt file is a summary of relevant docs using process_md.py (if need to regenerate). Works well.


profile:

```yaml
block:
  provider: block
  processor: claude-3-5-sonnet-2
  accelerator: claude-3-5-sonnet-2
  moderator: synopsis
  toolkits:
  - name: synopsis
    requires: {}
```
