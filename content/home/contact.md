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

  <div class="col-sm">
    <ul class="ul-edu fa-ul">
      <li>
        <i class="fa-li fas fa-user"></i>
        <div class="description">
          <p class="course">{{% mention "michaelkrauthammer" %}}</p>
          <p class="institution"><i>Chair of Medical Informatics</i></p>
          <p class="institution">Department of Quantitative Biomedicine</p>
          <p class="institution">Schmelzbergstrasse 26</p>
          <p class="institution">8006 Zürich</p>
          <p class="institution">Building/Room: SHM 26 C2</p>
          <p class="institution">
            <a href="#" onclick="u='michael.krauthammer'; d='uzh.ch'; prompt('Copy address to clipboard',u+'@'+d); return false">
              <i class="fas fa-envelope"></i>
             </a>
          </p>
        </div>
      </li>
    </ul>
  </div>
  
  <div class="col-sm">
    <ul class="ul-edu fa-ul">
      <li>
        <i class="fa-li fas fa-user"></i>
        <div class="description">
          <p class="course">{{% mention "claudiastenger" %}}</p>
          <p class="institution"><i>Administrative Assistant</i></p>
          <p class="institution">Department of Quantitative Biomedicine</p>
          <p class="institution">Schmelzbergstr. 26</p>
          <p class="institution">8006 Zürich</p>
          <p class="institution">Building/Room: SHM26, D1</p>
          <p class="institution">phone: +41 44 635 66 31</p>
          <p class="institution">
            <a href="#" onclick="u='claudia.stenger-gysling'; d='uzh.ch'; prompt('Copy address to clipboard',u+'@'+d); return false">
              <i class="fas fa-envelope"></i>
             </a>
          </p>
        </div>
      </li>
    </ul>
  </div>

</div>

