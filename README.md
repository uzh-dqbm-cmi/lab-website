# Krauthammer Lab Website

## Contributing

This website is built with Hugo using the Academic Theme. Academic has excellent documentation, which you can find [here](https://sourcethemes.com/academic/docs/managing-content/).

Below is an overview of how to edit the content most relevant to our site.


### Write a Post, Project, or Opportunity Page
All of these pages function similarly. Their content is located in `lab-website/content/`+`post/`+`project/`+`opportunity/` respectively. For all of these kinds of content, each page has its own subdirectory within its respective page type. These page subdirectories hold all of the page's content and photos, namely: 

  * `index.md` contains the post content. There is excellent [documentation](https://sourcethemes.com/academic/docs/managing-content/) about writing posts and the metadata that can go in the front matter. 
  * `featured.jpg`: This image will be at the top of your post, and will serve as the icon on the front page. 
  * *additional photos:* To add additional images to your post, put the image files inside `lab-website/content/post/<post-name>/<image-name>.jpg`, and reference them in your post using `{{< figure src="<image-namme>.jpg" title="Your image title here." >}}`

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

