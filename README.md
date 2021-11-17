# Krauthammer Lab Website

## Contributing

Below is an overview of how to:
* Add or edit the content on our website
* Preview your changes before they go live (without breaking the public website!)
* Request for someone to review your changes (a pull request) before merging and making them live

### First: create a branch
To avoid accidentally breaking the website while you make your changes, make your changes on a branch. To make a new branch in git...

* **If you're working on the command line:** 
  ```
  # update master to the latest version of the code
  git checkout master
  git pull

  # give your branch a descriptive name
  git checkout -b my_awesome_change
  ```
* **If you're working on GitHub.com:** before you click the big green "Commit changes" button at the bottom of the screen, choose to "Create a new branch for this commit and start a pull request" (not "Commit directly to the master branch"). On the next page, Submit the Pull Request. 

Now you're ready to make changes worry-free!

### Write a Blog Post, Make Project Project Page, or Post a Job Ad
All of these pages function similarly. Their content is located in `lab-website/content/`. Within that directory, blog posts are in `post/`, project pages are in `project/`, and job ads are in `opportunity/`. For all of these kinds of content, each webpage has its own subdirectory within its respective page type. These page subdirectories hold all of the page's content and images, namely: 

  * `index.md` contains the post content. There is excellent [documentation](https://sourcethemes.com/academic/docs/managing-content/) about writing posts and the metadata that can go in the front matter. 
  * `featured.jpg`: This image will be at the top of your post, and will serve as the icon on the front page. The file must be named *featured*, but can be any file type.
  * *additional images:* To add additional images to your post, put the image files inside `lab-website/content/post/<post-name>/<image-name>.jpg`, and reference them in your post using `{{< figure src="<image-namme>.jpg" title="Your image title here." >}}`

### Add a Publication
Publications are located in `lab-website/content/publication`, where each publication has a subdirectory with the following:

  * `index.md`: Contains metadata about the publication. Beyond the basics, some cool things you can include are:
    * `doi`: will create a DOI button under the article title to link directly to the publication. 
    * `url_pdf`: will create a PDF button under the article title to link directly to the pdf. 
    * `projects`: will establish a link between a publication and a project page, with links to go back and forth.
    * `tags`: The publication will show up under the "Related" section on pages that share the same tags.
    * `featured`: This bool controls whether the publication shows up on the front page in the "Featured Publications" section.
  * `cite.bib`: the `.bib` entry for the publication

### Fill out your Bio
Information about people in the lab is located in `lab-website/content/authors/`. Within that directory, there is a subdirectory for each person, containing:
* `_index.md`: markdown file containing all information to be displayed on the biography page. You can fill in the following tags:
  * `bio`: This short snippet appears with your name under posts you author.
  * `interests`: These will display under your name on the front page.
  * `education`: Enter your degrees, and they will display with little graduation caps next to them on your biography page. 
  * `social`: you can create as many icons as you like for various ways to contact you (email, github, personal twitter, etc)
  * at the bottom of the file, below the `---`, you can enter any long form text you'd like to display on your Biography page.
* `avatar.jpg`: Your photo, displayed on Biography page and post pages you author. 


### Preview Your Changes & Submit them for Review
To see your changes before they go live on the master branch, open a pull request and a preview will automatically be built for you! 

* **If you're working on the command line:** commit and push your changes to your branch, and then open a pull request on GitHub.com. 
* **If you're working on GitHub.com:** Before you click the big green "Commit changes" button at the bottom of the page, choose to "Create a new branch for this commit and start a pull request" (not "Commit directly to the master branch"). On the next page, Submit the Pull Request. 
* Once your Pull Request is opened, you will see a series of checks fire. The last one will say "netlify/goofy-bose-72cf26/deploy-preview" — when that one says "Deploy preview ready!" (it might take a few minutes), click "Details" to see a preview of your changes. 

Some Pull Request Etiquette:
* **Set a reviewer:** if you have someone in mind who you'd like to have review your changes, set them as the reviewer. Otherwise, set the reviewer to "Core Contributors"- this will go to the whole lab. 
* **Reviewing a Pull Request:** If you are reviewing someone else's pull reqest, always leave a review that is either "Request changes" or "Approve"- don't just leave a github comment or a message in Slack! Use the official review system so that it's clear what the coder should do. 
* **Merge!** Once someone approves your pull request, the coder/submitter (not the reviewer) gets to hit that big delicious green Merge button!


## FAQ

### My change isn't working. In the "checks" section of the Pull Request page, it says there are errors. 
To see the full error messages, you may need to log in to [Netlify](https://app.netlify.com/sites/goofy-bose-72cf26/overview), which is the service that builds our website. Log in with the Lab admin email to access it.

### I want to make a change to how the website looks. Where's the documentation for that?
This website is built with Hugo using the Academic Theme. Academic has excellent documentation, which you can find [here](https://sourcethemes.com/academic/docs/managing-content/).
