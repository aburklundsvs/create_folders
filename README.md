## Folder Creation Tool

### Overview
This Python script offers a graphical user interface (GUI) for efficiently creating folder sequences within a selected directory. It features three modes: Monthly, Weekly, and the new Custom folder creation mode. Users can specify naming conventions based on date ranges, year, and optional details, with flexible date formats and detail positioning. The Custom mode allows for more personalized folder creation.

### Dependencies
- **Python 3**
- **Tkinter** (typically included in standard Python installations)
- Standard Python libraries: **os**, **calendar**

### Functions Description

#### Monthly and Weekly Folder Creation
- `create_monthly_folders(directory, start_month, end_month, year, detail, date_format, detail_position)`
  - Creates monthly folders in the specified directory.
- `create_weekly_folders(directory, start_week, end_week, year, detail, detail_position)`
  - Creates weekly folders in the specified directory.
- `format_monthly_folder_name(month, year, date_format, detail, detail_position)`
  - Returns the formatted name for monthly folders.
- `format_weekly_folder_name(week, year, detail, detail_position)`
  - Returns the formatted name for weekly folders.

#### Custom Folder Creation
- `generate_folder_names()`
  - Dynamically generates folder names based on static and range-based inputs provided in the Custom view.
  - Combines static text fields and dynamic numeric ranges, appending them to create unique folder names.

### GUI Components
- **Start Menu**: Select between Monthly, Weekly, and Custom folder creation modes.
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

#### Monthly Folder Creation
1. Select "Monthly" from the Start Menu.
2. Choose a directory for folder creation.
3. Enter the start and end months, year, date format, and additional details.
4. The "Update Preview" and "Confirm and Create" buttons will activate after selecting a directory.
5. Review the folder names in the preview area.
6. Click "Confirm and Create" to generate the folders.

#### Weekly Folder Creation
1. Select "Weekly" from the Start Menu.
2. Follow a similar process as in the Monthly mode for directory selection and inputting week ranges, year, and additional details.
3. The "Update Preview" and "Confirm and Create" buttons become available upon directory selection.
4. Review and confirm folder creation.

#### Custom Folder Creation
1. Choose "Custom" from the Start Menu.
2. Select a target directory.
3. Add static text fields and/or dynamic numeric range fields for folder names.
4. The "Update Preview" and "Confirm and Create" buttons will be enabled after a directory is chosen.
5. Preview the dynamically generated folder names.
6. Confirm to create the folders.

### Important Notes
- Existing folders with identical names won't be overwritten (`os.makedirs` with `exist_ok=True`).
- Provides a user-friendly interface for batch folder creation with customizable naming formats.

### Examples

### Example 1: Static, Dynamic, Static Fields

**Inputs**:
1. Static Text Field: "Project"
2. Dynamic Numeric Range Field: 1-3
3. Static Text Field: "Week_1"

**Folder Name Generation Process**:
1. The function first uses the static text "Project" to create an initial set of folder names. Since it's the first input, our initial folder names list is: `["Project"]`.
2. Next, it appends each number from the dynamic range (1-3) to this name. This process results in: `["Project_1", "Project_2", "Project_3"]`.
3. Finally, it appends the second static text "Week_1" to each of these names, resulting in: `["Project_1_Week_1", "Project_2_Week_1", "Project_3_Week_1"]`.

**Final Generated Folder Names**:
1. "Project_1_Week_1"
2. "Project_2_Week_1"
3. "Project_3_Week_1"

### Example 2: Static, Dynamic, Static, Dynamic Fields

**Inputs**:
1. Static Text Field: "Project"
2. Dynamic Numeric Range Field: 1-3
3. Static Text Field: "Week"
4. Dynamic Numeric Range Field: 1-2

**Folder Name Generation Process**:
1. Starting with "Project", our initial list is: `["Project"]`.
2. Appending numbers 1-3 from the dynamic range gives us: `["Project_1", "Project_2", "Project_3"]`.
3. Adding "Week" to each of these names results in: `["Project_1_Week", "Project_2_Week", "Project_3_Week"]`.
4. Finally, appending numbers 1-2 from the second dynamic range to each of the above, we get: `["Project_1_Week_1", "Project_1_Week_2", "Project_2_Week_1", "Project_2_Week_2", "Project_3_Week_1", "Project_3_Week_2"]`.

**Final Generated Folder Names**:
1. "Project_1_Week_1"
2. "Project_1_Week_2"
3. "Project_2_Week_1"
4. "Project_2_Week_2"
5. "Project_3_Week_1"
6. "Project_3_Week_2"

These examples illustrate how the function systematically builds folder names by sequentially appending static and dynamic field inputs, resulting in a structured and logical naming pattern that can be particularly useful for organizing files in a project or time-based manner.