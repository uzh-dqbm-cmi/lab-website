---
title: MRIdle
summary: Helping reduce idle time in the USZ Radiology department
tags:
- Data Science
- Featured
date: "2020-01-01T00:00:00Z"
authors:
- markmcmahon

# Optional external URL for project (replaces project detail page).
# external_link: ""

image:
  caption: Mock-up of the MRIdle software tool
  focal_point: Smart

links:
- icon: github
  icon_pack: fab
  name: View Code
  url: https://github.com/uzh-dqbm-cmi/mridle
url_code: ""
url_pdf: ""
url_slides: ""
url_video: ""

# Slides (optional).
#   Associate this project with Markdown slides.
#   Simply enter your slide deck's filename without extension.
#   E.g. `slides = "example-slides"` references `content/slides/example-slides.md`.
#   Otherwise, set `slides = ""`.
# slides: example
---

MRIdle solves the problem of underutilization of MRI machines in the radiology department. Currently, USZ’s MRI machines spend 17% of the day idle, equivalent to nearly 2 hours per day. Idle time is a common but costly problem with estimated missed revenue of around CHF 150,000 per MRI machine per year. This underutilization is caused by rudimentary appointment planning and the fact that 12% of patients miss their appointments. With the goal of improving the occupancy of the MRI machines, MRIdle will harness historical data to recommend optimal appointment schedules and to predict and mitigate no-show patients.

The general objective of the project is to improve the efficiency of the USZ Radiology department by improving patient attendance and reducing machine idle time. Over the next two years, we aim to achieve this goal by building the MRIdle smart scheduling tool that fulfills the following specific objectives:

- **Power targeted appointment** reminders to reduce the frequency with which patients miss their MRI appointments. The scheduling tool will identify patients that are at risk for not showing to their appointments. With these predictions, the scheduling staff may proactively reach out to these patients to increase the likelihood of them attending their appointments.

- **Improve schedule density** with a smart scheduling application that assists staff in scheduling appointments. The smart scheduling tool’s AI-powered algorithms will recommend optimal durations and timings of appointments to guide the scheduling staff in creating an optimal schedule with minimal idle time.

- **Make the Radiology department more robust to changes in staff**. In our interviews with the radiology department’s scheduling staff, we learned that scheduling the department’s many kinds of appointments requires experience and expertise. Today, that knowledge is stored only in the minds of the department’s long-time staff. MRIdle’s machine learning models learn from years of appointment scheduling data to make new staff just as powerful schedulers as long-time ones.