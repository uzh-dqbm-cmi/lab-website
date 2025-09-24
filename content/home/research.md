+++
widget = "portfolio"
headless = true
active = true
weight = 60

title = "Our Research"
subtitle = "Four main aspects of our lab’s work"

[content]
  page_type = "research"   # <- new content type, not "project"
  filter_default = 0       # don’t auto-filter
  # Remove or comment out all [[content.filter_button]] to hide the tabs

[design]
  columns = "2"
  view = 3   # Card view (like projects)
  flip_alt_rows = false
+++
