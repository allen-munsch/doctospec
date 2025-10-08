styles:
  - primary: #FF6B6B
  - font: Roboto
  - spacing: 8px base

page: product detail

header (sticky, bg white, shadow sm):
  - logo "ShopFast" → /
  - search bar with placeholder "Search products..."
  - cart icon with badge value cartCount → /cart

main (max-w 1200px, mx auto, p 2rem):
  
  breadcrumbs:
    - Home → /
    - Products → /products
    - product.category → /products/{category}
    - product.name (current)
  
  product section (grid 2 cols desktop / 1 col mobile, gap 3rem):
    
    - gallery (lightbox enabled)
      for each image in product.images:
        - img: image.url
      
      styled: aspect 1:1, radius lg
    
    - details:
      - h1: product.name (fs 2.5rem, fw bold)
      - rating stars: product.rating with text "({product.reviews} reviews)"
      - price: product.price (fs 2rem, color primary, fw bold)
      - if product.onSale, show badge "Sale" (bg error, color white)
      
      - text: product.description (mt 1rem, color gray-600)
      
      - form:
        - select "Size" options: product.sizes (required)
        - select "Color" options: product.colors (required)
        - number input "Quantity" min 1, max product.stock, value 1
        
        - btn primary lg "Add to Cart" → addToCart (w full, mt 2rem)
          styled: animate pulse on update
        - btn outlined "Add to Wishlist" → addToWishlist (w full, mt 1rem)
  
  tabs:
    - tab "Description":
      - text: product.fullDescription
    
    - tab "Reviews" ({product.reviews}):
      foreach review in product.reviews:
        - review card (stack, gap 1rem, p 1.5rem, bg gray-50, radius md)
          - rating: review.stars
          - text: review.comment
          - text: "by {review.author}" (fs sm, color gray-500)
    
    - tab "Shipping":
      - text: "Free shipping on orders over $50"
      - text: "Estimated delivery: 3-5 business days"

  section "Related Products" (mt 4rem):
    - h2 "You May Also Like"
    
    for each related in relatedProducts:
      - card (grid 4 cols desktop / 2 tablet / 1 mobile, gap 1.5rem)
        - img: related.image (aspect 1:1)
        - h3: related.name
        - price: related.price
        - btn "Quick View" → openQuickView

modal quickView:
  - product quick preview with add to cart
  - close on backdrop click

drawer cart from right (w 500px desktop / full mobile):
  - h2 "Shopping Cart"
  
  if cart.items.length > 0:
    foreach item in cart.items:
      - cart item (flex, gap 1rem, p 1rem, border-b)
        - img: item.image (size 80px)
        - details (flex col, flex-1):
          - text: item.name (fw medium)
          - text: "Size: {item.size}, Color: {item.color}" (fs sm)
          - quantity selector: item.quantity
        - price: item.price
        - remove btn → removeFromCart
    
    - divider
    - total (flex space-between, fs xl, fw bold):
      - text "Total:"
      - text: cart.total
    - btn primary lg "Checkout" → /checkout (w full)
  
  if cart.items.length == 0:
    - empty state:
      - icon "shopping-cart" lg
      - text "Your cart is empty"
      - btn "Start Shopping" → /products
