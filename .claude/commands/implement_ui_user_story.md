Custom Command: /implement_ui_user_story

Description: Orchestrates the complete UI feature workflow: Design → Implement → Verify

Arguments:

- user_story (required): The UI feature to design and implement

---

You are implementing a complete UI feature using a three-phase workflow:

Phase 1: UX Design

Launch the ux-design-planner agent using the Task tool:

- subagent_type: "ux-design-planner"
- prompt: The user story below
- Wait for "Ready for coding." signal

Phase 2: Implementation

After design approval:

1. Implement the feature following the design specifications
2. Write and run unit tests
3. Ensure all tests pass before proceeding

Phase 3: Visual Verification

Launch the feature-verifier agent using the Task tool:

- subagent_type: "feature-verifier"
- prompt: Description of what was implemented
- Review the verification report and screenshots
