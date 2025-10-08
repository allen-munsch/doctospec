testing:
  - framework: vitest
  
  suite "Product Catalog with Mocks":
    test "displays products from API":
      - setup: mock GET /api/products returns generated product
      - setup: user is on "/products"
      - expect: product grid to be visible
      - expect: product cards to have count 12
    
    test "handles API errors gracefully":
      - setup: mock GET /api/products returns { status: 500, error: "Server Error" }
      - setup: user is on "/products"
      - expect: error alert to have text "Failed to load products"
      - expect: retry button to be visible
      - when: click retry button
      - expect: GET /api/products to be called twice
    
    test "uses fixture data for testing":
      - setup: mock database returns from fixtures/users.json
      - setup: user is logged in as admin
      - when: navigate to "/admin/users"
      - expect: user table to have count 50
      - expect: first row to have text matching /John|Jane/
