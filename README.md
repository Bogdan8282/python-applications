# My Python programs
Instructions on how to download and run the programs I created. Make sure you have Python and pip module, then clone this repository to your desktop.

## Snake game
Good old game. To run this, you are going to need pygame module, which can be downloaded by printing this in your console:

```console
pip install pygame
```

Then just run the main.py file.

#### Controls:

| Keys    | Actions  |
|---------|----------|
| Arrows: | Movement |
| Key 1:  | Leave    |
| Key 2:  | Restart  |

Keys 1 and 2 work only after losing.

## Netflix data analysis
A study of changes in the length of films over the years. You are going to need matplotlib and pandas modules. Also, you must download Anaconda or identical application. Write this down in your console:

```console
pip install pandas
pip install matplotlib
```

If you are using Anaconda, run inside its environment this commands:

```console
conda activate base
cd path/to/folder
python main.py
```

plot.png is included into the folder, this is how the result of the code execution looks like.

## Weather scrapper
Program that performs parsing of weather information in the Kherson region from the website https://weather.com/. The information is displayed in Ukrainian.
This program also requires some modules, you can download them by printing this in your console:

```console
pip install Flask
pip install requests
pip install beautifulsoup4
```

Then just run this commands:

```console
cd path/to/folder
python app.py
```

After that, open http://127.0.0.1:5000/ in your browser

## Caesar Decipherer
Casual program, just download and run the main.py file. It receives an encrypted message and decrypts it. I am planning to modify it soon.
