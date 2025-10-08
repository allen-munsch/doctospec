testing:
  - framework: vitest
  - runner: vitest
  - coverage:
    - statements: 80%
    - branches: 75%
    - functions: 80%
    - lines: 80%
  
  suite "Button Component":
    test "renders with correct text":
      - setup: button with text "Click me"
      - expect: button to be visible
      - expect: button to have text "Click me"
    
    test "handles click events":
      - setup: button with text "Submit"
      - when: click button
      - expect: handleClick to be called once
    
    test "can be disabled":
      - setup: button (disabled)
      - expect: button to be disabled
      - when: click button
      - expect: handleClick to never be called
    
    test "shows loading state":
      - setup: button (loading)
      - expect: button to have text "Loading..."
      - expect: spinner to be visible
      - expect: button to be disabled

  suite "Form Validation":
    test "validates email format":
      - setup: user is on "/signup"
      - when: type "invalid-email" in email field
      - when: click submit button
      - expect: error message to have text "Invalid email address"
      - expect: form not to be submitted
    
    test "submits valid form":
      - setup: user is on "/signup"
      - when: type "user@example.com" in email field
      - when: type "password123" in password field
      - when: click submit button
      - expect: POST /api/signup to be called with { email: "user@example.com" }
      - expect: url to contain "/dashboard"
