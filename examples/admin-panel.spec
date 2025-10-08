global styles:
  - primary: #6366F1
  - dark mode: enabled
  - font: system-ui

routes:
  - / → DashboardPage
  - /users → UsersPage (requires admin)
  - /analytics → AnalyticsPage (requires admin)
  - /settings → SettingsPage

page: admin users

sidebar nav (fixed left, w 250px, bg dark, color white):
  - logo "AdminHub"
  - nav:
    - Dashboard with icon "grid" → / (active if currentRoute == '/')
    - Users with icon "users" → /users (active)
    - Analytics with icon "chart" → /analytics
    - divider
    - Settings with icon "settings" → /settings

main content (ml 250px desktop, ml 0 mobile, p 2rem):
  
  header (flex space-between, items-center, mb 2rem):
    - heading "User Management"
    - actions (flex, gap 1rem):
      - btn outlined "Export CSV" → exportUsers
      - btn primary "Add User" → openAddUserModal

  filters bar (flex wrap, gap 1rem, p 1.5rem, bg white, radius lg, shadow sm, mb 2rem):
    - search input with placeholder "Search users..." triggers searchUsers (debounced 300ms)
    - select "Role" options: [All, Admin, User, Guest] triggers filterByRole
    - select "Status" options: [All, Active, Inactive] triggers filterByStatus
    - date range "Joined Date" triggers filterByDate

  users table (bg white, radius lg, shadow sm)
    columns: Avatar, Name, Email, Role, Status, Joined, Actions
    
    for each user in users:
      - row (hover bg gray-50, transition smooth)
        - cell: avatar img user.avatar with size md
        - cell: text user.name (fw medium)
        - cell: text user.email (color gray-600)
        - cell: badge user.role (variant based on role)
        - cell: 
          - if user.active, show badge "Active" (bg success)
          - if not user.active, show badge "Inactive" (bg gray)
        - cell: text user.joinedDate (formatted)
        - cell: dropdown actions:
          - "Edit" triggers editUser
          - "View Details" → /users/{user.id}
          - divider
          - "Deactivate" triggers deactivateUser (color error, if user.active)
          - "Activate" triggers activateUser (if not user.active)
          - "Delete" triggers confirmDeleteUser (color error)
    
    sortable: yes
    pagination: 20 rows per page
    shows: "Showing {start}-{end} of {total} users"

  if loading, show loading overlay with spinner

  if error, show alert error saying error.message (dismissable)

modal addUser:
  - h2 "Add New User"
  - form with fields:
    - input text "Name" (required, min 2 chars)
    - input email "Email" (required, validated)
    - select "Role" options: [Admin, User, Guest] (required)
    - checkbox "Send welcome email" (default checked)
  
  - footer (flex justify-end, gap 1rem):
    - btn outlined "Cancel" → closeModal
    - btn primary "Create User" → createUser (disabled if form invalid)

modal confirmDelete:
  - icon "alert-triangle" size xl (color error)
  - h2 "Delete User?"
  - text "This action cannot be undone. User data will be permanently removed."
  - form:
    - checkbox "I understand the consequences" (required)
  
  - footer (flex justify-end, gap 1rem):
    - btn outlined "Cancel" → closeModal  
    - btn danger "Delete User" → deleteUser (disabled if not confirmed)

command palette (triggered by cmd+k):
  - Search users...
  - Jump to Dashboard → /
  - Jump to Analytics → /analytics
  - separator "Actions"
  - Add User → openAddUserModal
  - Export Data → exportUsers
  - separator "Settings"
  - Preferences → /settings

context menu on user row:
  - "Quick Edit" → quickEditUser
  - "Copy Email" → copyToClipboard
  - "Send Message" → openMessageModal
  - divider
  - "View Activity Log" → /users/{user.id}/activity
