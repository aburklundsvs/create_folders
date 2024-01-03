## Folder Creation Tool

### Overview
This Python script offers a graphical user interface (GUI) to easily create a sequence of folders within a chosen directory. Users can specify the naming convention based on month range, year, an optional detail, and date format.

### Dependencies
- **Python 3**
- **Tkinter** (typically included in standard Python installations)
- Standard Python libraries: **os**, **calendar**

### Functions Description

#### `create_folders(directory, start_month, end_month, year, detail, date_format, detail_position)`
Creates folders in the designated directory.
- `directory`: The target directory path.
- `start_month`, `end_month`: Range of months (as integers) for folder naming.
- `year`: The year to be included in folder names.
- `detail`: A string for additional detail in the folder name.
- `date_format`: The format for the date in the folder name. Options: 'MM_YYYY', 'YYYY_MM', 'MMM_YYYY', 'YYYY_MMM'.
- `detail_position`: Where to place the additional detail ('Beginning' or 'End').

#### `format_folder_name(month, year, date_format, detail, detail_position)`
Formats the folder name according to the specified parameters.
- Returns: Formatted folder name as a string.

#### `update_preview(start_month, end_month, detail, preview_list, year, date_format, detail_position)`
Updates the GUI's preview list to display the folder names based on current inputs.

### Main Application
The `main()` function initializes the GUI and handles user interactions.

- **Nested Functions:**
  - `on_directory_selected()`: Activates buttons upon directory selection.
  - `on_confirm()`: Generates folders using the given inputs and closes the GUI.

### GUI Components
- **Directory Selection**: Field and button to choose the folder's destination.
- **Date Inputs**: Dropdowns for selecting the start month, end month, and year.
- **Date Format**: Dropdown to select the folder name's date format.
- **Detail Input**: Field for extra details and a dropdown for their position.
- **Preview Display**: Listbox showcasing the folder names as per current settings.
- **Action Buttons**: Buttons for updating the preview and confirming folder creation.

### Usage Instructions
1. Execute the script in a Python environment.
2. Use the GUI to enter the folder creation parameters and select a directory.
3. Review the folder names in the preview.
4. Press confirm to create the folders.

### Important Notes
- Folders with existing names will not be overwritten due to `os.makedirs` with `exist_ok=True`.
- The tool offers a convenient, user-friendly method for batch folder creation with custom naming formats.
