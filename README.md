# Inovoice extractor

Invoice extractor extract key value pairs from a invoice

## Getting Started

Here i'm used the East text detection model to detect the texts. after detecting the texts it will go throught the tesseract and extract the key values

### Prerequisites

pytesseract

flask

pdf2img

EAST text detection model




### Installing

A step by step series of examples that tell you how to get a development env running

```
pip install requirements.txt
```

```
python app.py
```

## Running the tests

The project is showing only 20% accuracy on test set. but it'can be improved by making a custom model for text detection and tweaking the image preprocessing

​
39
​
40
​
41
​
42
```

## Deployment

Add additional notes about how to deploy this on a live system

## Built With

* [Dropwizard](http://www.dropwizard.io/1.0.2/docs/) - The web framework used
* [Maven](https://maven.apache.org/) - Dependency Management
* [ROME](https://rometools.github.io/rome/) - Used to generate RSS Feeds

## Contributing

Please read [CONTRIBUTING.md](https://gist.github.com/PurpleBooth/b24679402957c63ec426) for details on our code of conduct, and the process for submitting pull requests to us.

## Versioning

We use [SemVer](http://semver.org/) for versioning. For the versions available, see the [tags on this repository](https://github.com/your/project/tags). 

## Authors

* **Billie Thompson** - *Initial work* - [PurpleBooth](https://github.com/PurpleBooth)

See also the list of [contributors](https://github.com/your/project/contributors) who participated in this project.

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details

## Acknowledgments

* Hat tip to anyone whose code was used
* Inspiration
* etc

