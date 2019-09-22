# Inovoice extractor

Invoice extractor extract key value pairs from a invoice

## Getting Started

Here i'm used the East text detection model to detect the texts. after detecting the texts it will go throught the tesseract and extract the key values

### Prerequisites

* pytesseract

* flask

* pdf2img

* EAST text detection model




### Installing

```
pip install requirements.txt
```

```
python app.py
```

## Running the tests

The project is showing only 20% accuracy on test set. but it'can be improved by making a custom model for text detection,language support and tweaking the image preprocessing

## Deployment


* [Deployed on Google compute engine](http://35.226.34.234:5001/) - upload your pdf to test

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details


