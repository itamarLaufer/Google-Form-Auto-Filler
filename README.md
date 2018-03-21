# Google-Forms-Auto-Filler
filler Python library enables filling large amount Google form with multiple choice question (An update which will enable filling all the kind of question will be published soon) automatically and quickly with random answers or user's requested answers.

[A video demonstrating gow the library works:](https://drive.google.com/file/d/1twdch8YoZePCcT43jwZQOS9OcwnGU90U/view?usp=drivesdk)



## Getting Started

We still don't suuport PyPI because there are updates we want to make.
Copy the 2 Pyhton file to your repository.
* don't forget to credit!

### How To Use?

In the example we'll use the module to fill this [form](https://docs.google.com/forms/d/e/1FAIpQLSf3FklBI3vm6RLWDFqD1r3mRKxhPFbcshL2xOA-ZyFo1l-JOg/viewform)


```
import filler
import time

# time to sleep the code in order to manage to open the form
time.sleep(5)

filler.auto_filling(2, 250, [2,4,4,8], [3,-1,-1,3])
```

2 is the refreshing time of our browser (The time it takes it to submit)
250 is the amount of forms we want to be filled
[2,4,4,8] is a list containing the number of answer for each quaestion in the form
[3,-1,-1,3] is the ansers we want to be filled -> in question 1 the 3rd ansser in question 2 a random answer and so forth.

## Contributing

[keyboard Python library](hhttps://pypi.python.org/pypi/keyboard/)


## Built With

* [PyCharm](https://www.jetbrains.com/pycharm/) - The Python workspace


## Authors

* **Itamar Laufer** - *high scool student* - (https://github.com/itamarLaufer)
