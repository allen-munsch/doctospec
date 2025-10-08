testing:
  - framework: playwright
  - runner: playwright
  
  suite "User Authentication Flow":
    test "user can log in":
      - setup: user is logged out
      - setup: user is on "/login"
      - when: type "user@test.com" in input with label "Email"
      - when: type "password123" in input with label "Password"
      - when: click button "Log In"
      - expect: url to be "/dashboard"
      - expect: page title to be "Dashboard"
      - expect: element with text "Welcome back" to be visible
    
    test "shows error for invalid credentials":
      - setup: user is on "/login"
      - when: type "wrong@test.com" in email field
      - when: type "wrongpass" in password field
      - when: click submit button
      - expect: alert error to have text "Invalid credentials"
      - expect: url to be "/login"
    
    test "redirects unauthenticated users":
      - setup: user is logged out
      - when: navigate to "/dashboard"
      - expect: url to be "/login"
      - expect: toast to have text "Please log in to continue"

  suite "Shopping Cart":
    test "adds product to cart":
      - setup: user is logged in
      - setup: user is on "/products"
      - when: click button "Add to Cart" with timeout 5s
      - expect: cart icon badge to have text "1"
      - expect: toast success to have text "Added to cart"
    
    test "updates quantity in cart":
      - setup: user has product in cart
      - setup: user is on "/cart"
      - when: click button "+"
      - expect: quantity input to have value "2"
      - expect: total price to be greater than 0
    
    test "removes item from cart":
      - setup: user has 2 products in cart
      - setup: user is on "/cart"
      - when: click first remove button
      - expect: cart items to have count 1
      - expect: cart icon badge to have text "1"
