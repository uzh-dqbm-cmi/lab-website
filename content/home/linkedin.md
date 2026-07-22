+++
# LinkedIn feed section, rendered from data/linkedin_posts.yaml
# via layouts/shortcodes/linkedin_feed.html.

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

<!-- SociableKIT widget trial. Fallback to official embeds:
     replace the line below with {{</* linkedin_feed count="3" */>}} -->
{{< sociablekit_feed id="25477913" >}}

<p style="text-align:center">
  <a href="https://www.linkedin.com/company/krauthammerlab" target="_blank" rel="noopener">Follow us on LinkedIn</a>
  &nbsp;&middot;&nbsp;
  <a href="/linkedin/">See all posts</a>
</p>
