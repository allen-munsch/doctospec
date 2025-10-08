styles for this app:
  - primary: #3B82F6
  - secondary: #10B981
  - font: Inter, sans-serif
  - spacing: 1rem base
  - border radius: 0.5rem
  - transition: smooth

create a dashboard page

add a sticky header with id "main-nav"
  styled:
    - background: white
    - shadow: small
    - sticky top
  
  containing:
    - logo "DashApp" going to /
    - navigation with:
      - link "Overview" → /dashboard
      - link "Analytics" → /analytics
      - link "Settings" → /settings
    - if authenticated, show user menu with:
      - avatar with image user.avatarUrl
      - dropdown containing:
        - profile → /profile
        - logout triggers handleLogout

add a sidebar from left with id "main-sidebar"
  styled:
    - width: 280px on desktop, hidden on mobile
    - background: gray-50
    - padding: 2rem
  
  containing:
    - heading "Navigation"
    - nav group "Main" with:
      - nav item "Dashboard" with icon "home" → /dashboard (active)
      - nav item "Reports" with icon "chart" → /reports
    - divider
    - nav group "Admin" with:
      - if user.isAdmin, show nav item "Users" with icon "users" → /admin/users

main section with class "dashboard-content"
  styled:
    - padding: 3rem on desktop, 1.5rem on mobile
    - max width: 1400px
    - margin: 0 auto
  
  containing:
    - heading "Welcome back" with value user.name
      styled:
        - font size: 2.5rem on desktop, 1.75rem on mobile
        - margin bottom: 2rem
    
    - stats grid (repeats in grid, 4 columns on desktop, 2 on tablet, 1 on mobile, gap 1.5rem)
      for each metric, display:
        - stat card
          styled:
            - background: white
            - padding: 1.5rem
            - border radius: 1rem
            - shadow: small
            - transition: smooth
            - on hover: shadow medium
          
          containing:
            - label with value metric.label
              styled: color gray-600, font size 0.875rem
            - value with value metric.value
              styled: font size 2rem, font weight bold, margin 0.5rem 0
            - change with value metric.change (trending up/down)
              styled: color success if positive, color error if negative
    
    - section "Recent Activity"
      styled:
        - margin top: 3rem
      
      containing:
        - heading "Recent Activity"
        - if activities exist, show:
          - table with columns: Date, User, Action, Status
            for each activity, display:
              - cell with value activity.date
              - cell with value activity.user
              - cell with value activity.action
              - cell: badge with value activity.status (variant based on status)
            
            styled: shadow small, border radius 1rem
            sortable: yes
            pagination: 10 rows per page
        
        - if no activities, show empty state:
          - icon "inbox" size large
          - text "No recent activity"
          - button "Refresh" triggers fetchActivities

include a drawer with id "filter-drawer" from right
  styled:
    - width: 400px on desktop, 100% on mobile
    - background: white
    - shadow: extra large
  
  containing:
    - header with:
      - heading "Filters"
      - close button triggers closeFilters
    
    - form with fields:
      - date range picker "Date Range" with value dateRange
      - multi-select "Categories" with options from categories
      - range slider "Amount" from 0 to 10000 with value amountRange
    
    - footer with:
      - button "Apply" triggers applyFilters
        styled: width 100%, background primary
      - button "Reset" triggers resetFilters
        styled: width 100%, variant outlined

show toast success saying "Dashboard loaded" positioned top-right, duration 3000
