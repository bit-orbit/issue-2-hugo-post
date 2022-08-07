# issue-2-repo

get an specific issue by its label and push it to the repo, this can be used by hugo
to create a blog post by issues.


### Description

in the static generator sites the worst problem is that you have not a good content
manager which provide an environment to edit and post each of your blogs.

i tried to use some of github features like CI/CD, Issues and Github Pages
to create that environment which make writing blogs easier.

**what this action will do?** well whenever you trigger this action, it will
download an specific issue by the label you defined in environment variable.
then you should `build` and `push` the the repo in local to the upstream.


### Usage

```bash
name: build-and-push-by-label
on:
  issues:
    types:
      - "labeled"

jobs:
  build-push:
    runs-on: ubuntu-latest
    steps:
    - uses: actions/checkout@v3
    - id: foo
      uses: bit-orbit/issue-2-hugo-post@master
      with:
        REPO: '<your repo name>'
        OWNER: '<the repo owner>'
        PUB_DIR: '<local publish directory>'
        DEBUG: True # verbose if True, otherwise quiet. default to False
```


### Example Action

this example will do all the stuff for you, such as:

1. check label of the issue.
2. download blog repo and then download the issue in to it.
3. setup hugo and build the blog.
4. push changes on main repo.
5. deploy ./docs directory on github pages.
6. close issue with specific comment.   


```bash

name: check-label-then-build-and-deploy
on:
  issues:
    types: [labeled]

jobs:
  checkLabel:
    runs-on: ubuntu-latest
    if: contains(github.event.issue.labels.*.name, 'post') || contains(github.event.issue.labels.*.name, 'blog')
    steps:
      - name: checkout the blog
        uses: actions/checkout@v3
        with:
          submodules: true
          fetch-depth: 0


      - uses: bit-orbit/issue-2-hugo-post@master
        with:
          REPO: 'test'
          OWNER: 'shabane'
          PUB_DIR: 'content'
          DEBUG: True # verbose if True, otherwise quiet. default to False
          LABELS: 'post:blog'

      - name: setup hugo
        uses: peaceiris/actions-hugo@v2
        with:
          hugo-version: 'latest'
          extended: true

      - name: build
        run: hugo --minify

      - name: Deploy
        uses: peaceiris/actions-gh-pages@v3
        if: github.ref == 'refs/heads/seprate'
        with:
          github_token: ${{ secrets.GITHUB_TOKEN }}
          publish_dir: ./docs

      - name: Commit files
        run: |
          git config --local user.email "John Doe@gmail.com"
          git config --local user.name "<John Doe>"
          git add --all
          git commit -m "Auto commiting changes"

      - name: Push changes
        uses: ad-m/github-push-action@master
        with:
          github_token: ${{ secrets.GITHUB_TOKEN }}
          branch: ${{ github.ref }}

      - name: Close Issue
        uses: peter-evans/close-issue@v2
        with:
          comment: Thanks for your contribution, we added this chapter to the book :)

```