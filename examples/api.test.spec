testing:
  - framework: vitest
  
  suite "User API":
    test "GET /api/users returns user list":
      - setup: mock database returns [{ id: 1, name: "John" }, { id: 2, name: "Jane" }]
      - when: GET /api/users
      - expect: GET /api/users to return [{ id: 1, name: "John" }, { id: 2, name: "Jane" }]
      - expect: GET /api/users to have status ok
    
    test "POST /api/users creates new user":
      - setup: mock database.users.create returns { id: 3, name: "Bob" }
      - when: POST /api/users with { name: "Bob", email: "bob@test.com" }
      - expect: database.users.create to be called with { name: "Bob", email: "bob@test.com" }
      - expect: POST /api/users to have status created
      - expect: POST /api/users to return { id: 3, name: "Bob" }
    
    test "PUT /api/users/:id requires authentication":
      - setup: user is not authenticated
      - when: PUT /api/users/1 with { name: "Updated" }
      - expect: PUT /api/users/1 to have status unauthorized
      - expect: database.users.update to never be called

  suite "Product Search":
    test "searches products by name":
      - setup: mock GET /api/products returns from fixtures/products.json
      - when: GET /api/products with query "laptop"
      - expect: GET /api/products to be called with { q: "laptop" }
      - expect: results to have length 5
      - expect: first result to have attribute name containing "laptop"
