# docsmith

...

## USAGE

### `poetry install`

Sets up the project

### `poetry run build-resume`

Builds a resume with the data in `input/resume/`, with completed resume data sent to `output/resume/`

### `poetry run process-image`

Processes images in `input/img`, with images sent to `output/img/`

`poetry run process-image --help`
`poetry run process-image --mode 3`

#### Operation Mode 5: Copy E-Book Images

This rips all the images from `.epub` files in `input/ebook`, with images sent to `output/whatever-ebook-name/`
