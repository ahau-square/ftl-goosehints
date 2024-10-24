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


![image](https://github.com/user-attachments/assets/ebdc196c-7f43-4fb5-9fb1-7848df90a238)

![image](https://github.com/user-attachments/assets/f984d783-5eff-46a2-9cec-158d0a20057a)

![image](https://github.com/user-attachments/assets/f80c320a-2b7c-43d4-8427-38e40e16ab86)


![image](https://github.com/user-attachments/assets/6ce23f91-1403-4c5f-b439-d3e74bc36dfe)

![image](https://github.com/user-attachments/assets/7b4028b7-7796-4704-ac40-84ac3b4ee807)

