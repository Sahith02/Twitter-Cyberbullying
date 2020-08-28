# Twitter-Cyberbullying

<p align="center"><kbd><img src="https://github.com/Sahith02/Twitter-Cyberbullying/blob/master/static/CODS_logo.jpeg" width="128px" style="border-radius: 500px;"></kbd><p>


![Python](https://img.shields.io/badge/python-v3.6-blue.svg)
[![GitHub issues](https://img.shields.io/github/issues/Sahith02/Twitter-Cyberbullying)](https://github.com/Sahith02/Twitter-Cyberbullying/issues)
[![GitHub forks](https://img.shields.io/github/forks/Sahith02/Twitter-Cyberbullying)](https://github.com/Sahith02/Twitter-Cyberbullying/network)

This is an NLP text classifier based anti-cyberbullying system. It aims to build a strong foundation to a deployable product by building the core pipeline architecture. 

## Setup

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install requirements.

```bash
git clone https://github.com/Sahith02/Twitter-Cyberbullying.git
cd Twitter-Cyberbullying
pip install -r requirements.txt
python flask_backend.py
```

## Features

- Input twitter user handle and set max number of replies for latest tweet.
- Recursively retrieve the replies by using a function built on top of tweepy API.
- Preprocess each reply by a filtration system to keep only relevant information.
- Pass all the replies into the birdirectional LSTM pipeline trained on 20k samples of toxic comments.
- Display the toxicity level in a clean and crisp UI for understandability using Flask.


## Info
This project was done as part of the C.O.D.S Summer Project 2020 with a team of 4 mentees bulding the project and 3 guiding mentors. 

## Mentors

- Sahith Kurapati - [@Sahith02]( https://github.com/Sahith02 )
- Om Shreenidhi - [@om719]( https://github.com/om719 )
- Ananth Rastogi - [@ethereal-ux]( https://github.com/ethereal-ux )

## Mentees

- Shashank - [@Shashankhon1]( https://github.com/Shashankhon1 )
- Thilak - [@ThilakShekharShriyan]( https://github.com/ThilakShekharShriyan )
- Sudhanva - [@sudhanvarajesh]( https://github.com/sudhanvarajesh )
- Tushar - [@tush2001]( https://github.com/tush2001 )

