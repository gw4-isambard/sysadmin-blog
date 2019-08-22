# Read me

## Build with Pelican

```
git clone CLONE_URL gw4-isambard
cd gw4-isambard
python3 -m venv .
. bin/activate
pip install -r requirements.txt
```

## Generate site

```
make html
```

## Add article

```
vi content/CATEGORY/YYYY-mm-dd-TITLE.md
  ---
  title: TITLE
  ---

  Insert interesting things here.
```

## Add static content (images)

Copy over and name your content

```
content/images/TITLE-IMG_NAME.jpg
```

Embed it in Markdown
```
<div class="gallery">
    <h2>Photos</h2>

    <a title="Title 1" href="{static}/images/image1.jpg">
        <img src="{static}/images/image1.jpg">
    </a>
    <a title="Title 2" href="{static}/images/image2.jpg">
        <img src="{static}/image2.jpg">
    </a>
</div>

```
