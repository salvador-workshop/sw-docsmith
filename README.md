# docsmith

...

## Usage

### Cleaning

If a model named `whateverProjectName.stl` exists at `src/input/whateverProjectName/`, that can be cleaned by running:

`poetry run transform-clean --project "whateverProjectName"`

The output model would then be located at `output/whateverProjectName/whateverProjectName-cleaned.stl`

### Simplification

`poetry run transform-simplify --project "whateverProjectName"`
