Release integration

After the approved project passed its final gate and was applied, origin/main advanced to da537241 with the AI Lab wording changes. These were merged cleanly in cb161e0b. The merge preserves the exact new project files and the exact upstream AI Lab source and generated output.

The combined release passed all 35 unit tests, complete static repeat-build verification (688 unchanged files), independent content checks, the AI Lab browser suite in both languages and themes at 1440, 768, 390 and 320 pixels, offline behavior, and GRACE lint with zero errors. Evidence is retained in evidence/integration. Publication will use the combined committed tree.
