# Inovoice extractor

Invoice extractor extract key value pairs from a invoice

## Getting Started

Here we have used the [East text detection model](https://arxiv.org/abs/1704.03155) to detect the texts. after detecting the texts it will go through the tesseract and extract the key values


### Prerequisites

* Pytesseract

* Flask

* OpenCV

* PILLOW

* Pdf2img

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


