+++
# Contact widget.
widget = "contact"  # See https://sourcethemes.com/academic/docs/page-builder/
headless = true  # This file represents a page section.
active = true  # Activate this widget? true/false
weight = 130  # Order that this section will appear.

title = "Contact"
subtitle = ""

# Automatically link email and phone?
autolink = true

# Email form provider
#   0: Disable email form
#   1: Netlify (requires that the site is hosted by Netlify)
#   2: formspree.io
email_form = 0
+++

<div class="row">

  <div class="col-md-7">
    <ul class="ul-edu fa-ul">
      <li>
        <i class="fa-li fas fa-user"></i>
        <div class="description">
          <p class="course">{{% mention "michaelkrauthammer" %}}</p>
          <p class="institution">Chair of Medical Informatics</p>
          <p class="institution">Department of Quantitative Biomedicine</p>
          <p class="institution">Schmelzbergstrasse 26</p>
          <p class="institution">8006 Zürich</p>
        </div>
      </li>
      {{ end }}
    </ul>
  </div>
  
  <div class="col-md-7">
    <ul class="ul-edu fa-ul">
      <li>
        <i class="fa-li fas fa-user"></i>
        <div class="description">
          <p class="course">Claudia Stenger</p>
          <p class="institution">Administrative Assistant</p>
          <p class="institution">Winterthurerstrasse 190</p>
          <p class="institution">CH-8057 Zürich</p>
          <p class="institution">Building/Room: Y32-F-01</p>
          <p class="institution">phone: +41 44 635 66 29</p>
        </div>
      </li>
      {{ end }}
    </ul>
  </div>

</div>

{{% mention "michaelkrauthammer" %}}<br>
*Chair of Medical Informatics*

Department of Quantitative Biomedicine <br>
Schmelzbergstrasse 26 <br>
8006 Zürich <br>



{{% mention "claudiastenger" %}}<br>
*Administrative Assistant*

Winterthurerstrasse 190 <br>
CH-8057 Zürich <br>
Building/Room: Y32-F-01 <br>
phone: +41 44 635 66 29 <br>

---
