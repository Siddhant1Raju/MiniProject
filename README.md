

# Barcode Scanner

This project is a barcode scanner application built using Python and various computer vision libraries such as OpenCV, imutils, and pyzbar. It also utilizes the Streamlit library to provide a user-friendly web interface for the barcode scanner.

## Prerequisites

Before running this project, make sure you have the following dependencies installed:

- Python (3.6 or later)
- OpenCV (`opencv-python`)
- imutils
- pyzbar
- Streamlit

You can install the required Python packages using pip:

```
pip install opencv-python imutils pyzbar streamlit
```

## Usage

1. **Run the Application**: Execute the `app.py` script to start the Streamlit application.

```
streamlit run app.py
```

2. **Web Interface**: The application will launch a web interface in your default browser.

3. **Camera Access**: Grant the application access to your computer's camera when prompted.

4. **Barcode Detection**: Point the camera at a barcode. The application will detect and decode the barcode in real-time.

5. **Decoded Output**: The decoded barcode data (e.g., product code, URL, or any other information) will be displayed in the web interface.

6. **Exit**: Close the browser window or stop the Streamlit server to exit the application.

## Customization

You can customize various aspects of the project by modifying the `app.py` script:

- **Camera Settings**: Adjust the camera resolution, frame rate, or other camera-specific settings by modifying the `VideoCapture` parameters.
- **Detection Parameters**: Tweak the barcode detection parameters, such as the decoding type or localization settings, by modifying the `pyzbar.decode` function arguments.
- **Output Handling**: Customize how the decoded barcode data is processed or displayed by modifying the code in the `detect_barcodes` function.
- **Streamlit UI**: Enhance the user interface by modifying the Streamlit components and layouts within the `app.py` script.

## Examples

Here are a few examples of barcodes that can be used with this application:

- EAN-13 (e.g., product barcodes)
- QR codes
- Data Matrix codes
- PDF417 codes
- Aztec codes

## Contributing

Contributions to this project are welcome. If you find any issues or have suggestions for improvements, please open an issue or submit a pull request on the project's GitHub repository.

## License

This project is licensed under the [MIT License](LICENSE).

## Acknowledgments

- The OpenCV, imutils, pyzbar, and Streamlit libraries and their respective contributors.
- Any other relevant resources or datasets used in the project.
