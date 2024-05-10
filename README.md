# TomlTool: A Python Library for Handling TOML Configuration Files

TomlTool is a simple and efficient Python library for working with TOML (Tom's Obvious, Minimal Language) file format. TOML files are an alternative to configuration files that are easy to write and easy to understand.

## Features

- **Loading TOML Data From a File** - TomlTool can load TOML data from the specified file and create a new instance of TomlTool.
- **Adding a New Item to the TOML Data** - You can add a new item (key-value pair) to the TOML data.
- **Removing an Item From the TOML Data** - You can remove an existing item from the TOML data.
- **Updating the Value of an Existing Item in the TOML Data** - If you need to change a value, TomlTool got that covered.
- **Converting Toml Data to JSON** - Easily convert TOML data to JSON string.
- **Create TomlTool instance from JSON file** - Not just TOML, work with JSON string or file and convert it to TOML.
- **Save the Modified TOML Data Back to the Original File** - Any changes you make can be saved back to the original file.

## How to Install

You can install `tomltool` via pip:

```bash
pip install tomltool
```

## Example Usage

Here's a basic example of how to use TomlTool:

```python
import tomltool

# Load TOML data from a file
toml = tomltool.TomlTool.load('config.toml')

# Add a new item to the TOML data
toml.add_item('section1.key1', 'value1')

# Remove an item from the TOML data
toml.remove_item('section1.key1')

# Update an existing item
toml.update_item('section1.key1', 'new_value')

# Save the changes back to the file
toml.save()
```

## Dependencies

tomlkit

## Contributing

Contributions are welcome! Please open an issue if you encounter any problems, or a pull request if you make a change.
Please note that this project is released with a Contributor Code of Conduct. By participating in this project you agree to abide by its terms.

## License

GNU GENERAL PUBLIC LICENSE
