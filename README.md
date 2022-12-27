# 2023 website

All the code required to generate the website of the 2023 edition of Pass the SALT conference.

## Installation

`apt install hugo`

or visit https://gohugo.io/installation/linux/ and take the Extended edition.

## Modify content

- `config.toml`: contains global parameters of the site (title, logo, lang, top and bottom menu content).
- `data/en/homepage.yml`: Yaml parameters to inject into homepage through Vex theme templates.
- `themes/vex-hugo/layouts/`: several directories containing all HTML templates of the Vex theme.
- `themes/vex-hugo/layouts/index.html`: structure of the homepage which calls HTML snippets located in `partial` directory. If you want to add a section in the homepage, just add a call to a HTML snippet file and create the HTML file in the `partial` directory.  
- `content/`: Markdown content of individual pages.
- `static/`: images and files.
- `public/`: HTML pages generated by the `Hugo` engine.


## Test locally & produce final HTML files

`hugo server` to run the site locally in memory.

`hugo` to produce the static site pages in `public/`.

A webhook commits the content of `public/` on the website.
