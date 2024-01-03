## Folder Creation Tool

### Overview
This Python script provides a graphical user interface (GUI) for creating sequences of folders within a selected directory. It now offers two modes: Monthly and Weekly folder creation. Users can specify naming conventions based on date ranges, year, and an optional detail, with flexibility in date formats and detail positioning.

### Dependencies
- **Python 3**
- **Tkinter** (typically included in standard Python installations)
- Standard Python libraries: **os**, **calendar**

### Functions Description

#### `create_monthly_folders(directory, start_month, end_month, year, detail, date_format, detail_position)`
Creates monthly folders in the specified directory.
- Parameters include the directory path, month range, year, detail, date format, and detail position.

#### `create_weekly_folders(directory, start_week, end_week, year, detail, detail_position)`
Creates weekly folders in the specified directory.
- Parameters include the directory path, week range, year, detail, and detail position.

#### `format_monthly_folder_name(month, year, date_format, detail, detail_position)`
Formats the name for monthly folders.
- Returns the formatted folder name as a string.

#### `format_weekly_folder_name(week, year, detail, detail_position)`
Formats the name for weekly folders.
- Returns the formatted folder name as a string.

#### `update_preview(start, end, detail, preview_list, year, date_format/detail_position, is_monthly)`
Updates the GUI's preview list to display folder names based on current inputs.
- Can handle both monthly and weekly folder previews.

### GUI Components
- **Start Menu**: Select between Monthly and Weekly folder creation.
- **Directory Selection**: Choose the target directory for folder creation.
- **Date/Week Range Inputs**: Dropdowns for selecting the start and end dates or weeks.
- **Year Selection**: Dropdown to select the year.
- **Date Format (Monthly Mode)**: Choose the format for dates in folder names.
- **Detail Position**: Specify the position of the additional detail (Beginning or End).
- **Additional Detail Input**: Enter any extra details to include in folder names.
- **Preview Display**: View how the folder names will appear based on current settings.
- **Action Buttons**: Update the preview, confirm folder creation, or clear inputs.
- **Navigation Button**: Return to the main menu or quit the application.

### Usage Instructions
1. Run the script in a Python environment.
2. From the main menu, choose between Monthly or Weekly folder creation.
3. Enter the folder creation parameters and select a directory.
4. Review the folder names in the preview area.
5. Confirm to create the folders or clear to reset inputs.

### Important Notes
- Existing folders with the same names will not be overwritten (uses `os.makedirs` with `exist_ok=True`).
- Offers a user-friendly interface for batch folder creation with customizable naming formats.