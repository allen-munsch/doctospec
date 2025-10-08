testing:
  - framework: playwright
  
  suite "Accessibility":
    test "form has proper labels":
      - setup: user is on "/signup"
      - expect: input with placeholder "Email" to have attribute aria-label
      - expect: input with type "password" to have attribute aria-label
      - expect: button "Submit" to have role "button"
    
    test "keyboard navigation works":
      - setup: user is on "/dashboard"
      - when: press tab
      - expect: first link to be focused
      - when: press tab 3 times
      - expect: navigation item "Settings" to be focused
      - when: press enter
      - expect: url to be "/settings"
    
    test "screen reader announcements":
      - setup: user is on "/products"
      - when: click filter button
      - expect: region with role "dialog" to be visible
      - expect: dialog to have attribute aria-label "Filter Products"
      - when: press escape
      - expect: dialog to be hidden
      - expect: screen reader text to contain "Filter dialog closed"
