# 64×64 Pixel Drawing Web App

A simple Python-based web application that allows users to draw a 64×64 pixel image, select background and pen colors, and save the drawing as a PNG file.

Created with the help of Openai o1-preview model.

## Table of Contents

- [Features](#features)
- [Prerequisites](#prerequisites)
- [Installation](#installation)
- [Usage](#usage)
- [Project Structure](#project-structure)
- [Contributing](#contributing)
- [License](#license)

## Features

- **Drawing Canvas:** Draw on a 64×64 pixel canvas using your mouse.
- **Background Color Selection:** Choose a background color for your canvas.
- **Pen Color Selection:** Choose a pen color for drawing.
- **Save Functionality:** Save your drawing as a PNG image (`drawing.png`).
- **Clear Canvas:** Clear the canvas to start a new drawing.

## Prerequisites

- **Python 3.x**
- **pip** package manager

## Installation

1. **Clone the Repository**

   ```bash
   git clone https://github.com/donny-son/pixy.git
   cd pixy
   ```

2. **Create a Virtual Environment (Optional but Recommended)**

   ```bash
   python -m venv venv
   source venv/bin/activate   # On Windows use `venv\Scripts\activate`
   ```

3. **Install Dependencies**

   ```bash
   pip install flask flask-cors
   ```

## Usage

1. **Run the Application**

   ```bash
   python app.py
   ```

2. **Access the Web App**

   Open your web browser and navigate to:

   ```
   http://127.0.0.1:5000/
   ```

3. **Draw and Save**

   - Use the canvas to draw your image.
   - Select background and pen colors using the color pickers.
   - Click **Set Background Color** to apply the background color.
   - Click **Clear** to clear the canvas.
   - Click **Save** to save your drawing as `drawing.png`.

## Project Structure

```
your_repository/
├── app.py
└── templates/
    └── index.html
```

- **app.py:** The main Flask application file.
- **templates/index.html:** The HTML template containing the frontend code.

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request or open an Issue for any feature requests or bugs.

## License

This project is licensed under the MIT License.

