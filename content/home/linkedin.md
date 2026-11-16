+++
# LinkedIn feed section, loaded live from the SociableKIT data feed
# via layouts/shortcodes/linkedin_live.html.

widget = "blank"  # See https://sourcethemes.com/academic/docs/page-builder/
headless = true  # This file represents a page section.
active = true  # Activate this widget? true/false
weight = 66  # After Recent Posts (65), before Talks (70).

title = "LinkedIn"
subtitle = ""

[design]
  # Full width so the embeds sit side by side (default is 2 columns).
  columns = "1"
+++

<!-- Live feed with filter buttons, loaded from the SociableKIT data feed
     (see layouts/shortcodes/linkedin_live.html). Offline fallback from
     the archived data file: {{</* linkedin_feed count="3" */>}} -->
{{< linkedin_live count="3" >}}

<p style="text-align:center">
  <a href="https://www.linkedin.com/company/krauthammerlab" target="_blank" rel="noopener">Follow us on LinkedIn</a>
  &nbsp;&middot;&nbsp;
  <a href="/linkedin/">See all posts</a>
</p>
