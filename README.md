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


## Test locally, produce final HTML files and push to website

- run `hugo server` from the root of the repository to run the site locally in memory.
- run `hugo` from the root of the repository to produce the static site pages in `public/`.
- each push (`git push origin main`) will activate a webhook. The hook content is in the `cgi-bin/update.cgi` file and its URL is `https://2023.pass-the-salt.org/cgi-bin/update.cgi`. The webhook will check if updates exist on Github repo. If it is the case, it fetchs them to `/var/www/2023` directory on the server and then, rsync the content of the `public/` sub directory with the content of the website located in `/var/www/2023-passthesalt`.
