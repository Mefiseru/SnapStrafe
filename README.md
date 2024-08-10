# SnapStrafe

**SnapStrafe: Razer's Snap Tap Strafe technology for every keyboard**

SnapStrafe is a powerful tool designed to enhance gaming and productivity by implementing snap tap strafe technology for every keyboard. The project provides a seamless experience by automatically tapping the opposite key when a specified key is released, allowing for quick and efficient movements.

## Features

- Supports both Windows and Linux operating systems.
- Detects key releases and automatically taps the opposite key with a specified hold duration.
- Toggle functionality on/off with the 'N' key without exiting the program.
- Allows user control to override automatic taps with manual key presses. (BETA!)
- Easy installation and setup with automated scripts.
- Utilizes Python and C for optimal performance and responsiveness.

## Installation

To set up SnapStrafe on your system, follow these steps:

### Prerequisites

- Python 3.x installed on your system. (tested on Python 3.10.10)
- On Linux, ensure you have `sudo` privileges for installing system packages.

### Setup Instructions

1. **Clone the Repository** (or download the source code):

   ```bash
   git clone https://github.com/Mefiseru/SnapStrafe.git
   cd SnapStrafe/src
   ```

2. **Run the Setup Script**:

   The setup script will automatically install necessary dependencies, build the C extension, and prepare the project for use.

   ```bash
   python setup_project.py
   ```

   This script will:
   - Detect your operating system (Windows or Linux).
   - Install Python dependencies.
   - Install necessary system packages on Linux.
   - Build the C extension for keyboard interaction.

## Usage

Once the setup is complete, you can run the main script to start using SnapStrafe:

```bash
python main.py
```

### Key Features

- **Key Detection**: The script listens for the release of the 'A' and 'D' keys.
- **Automatic Opposite Tap**: When 'A' is released, 'D' is tapped, and vice versa, with a configurable hold duration.
- **Stop toggle** Toggle functionality on/off with the 'N' key without exiting the program.
- **Exit**: Use `Ctrl+C` in the terminal to exit the program.

## Configuration

You can customize the key hold duration by editing the `strafe_tapper.c` file:

- **Windows**: Modify the `Sleep` duration in milliseconds.
- **Linux**: Modify the `usleep` duration in microseconds (1000 microseconds = 1 millisecond).

Rebuild the extension after making changes to the C code by running:

```bash
python setup.py build_ext --inplace
```

## Contributing

Contributions are welcome! If you'd like to contribute to SnapStrafe, please fork the repository and create a pull request with your changes.

1. Fork the repository.
2. Create a new branch for your feature or bugfix.
3. Make your changes and commit them with descriptive messages.
4. Push your changes to your fork.
5. Open a pull request against the main repository.

## License

This project is licensed under the GPL-3 License. See the [LICENSE](LICENSE) file for more information.

## Support

If you encounter any issues or have questions, feel free to open an issue in the repository or contact the project maintainers.

## Acknowledgments

- Thanks to the open-source community for providing the tools and libraries used in this project.
- Inspired by the need for seamless keyboard interaction in gaming and productivity.
