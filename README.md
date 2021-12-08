# Mega-Sena Application

This project was created using the Django Framework.

The objective of this application is to check for the last result from the Mega-Sena lottery. Also, it generates six new numbers that the user can use to try and win the lottery pot.

## First Look

<img src="/app-look.png" alt="The look of the application" style="zoom:80%;" />

The interface of the application is written in Portuguese, from Brazil.

In the first box, we can see the latest result, and some more information like. The draw number, the date it was done, if it accumulated and the value of the next prize.

In the second box, we have the generate button, that will give us the six suggested numbers to be played for the next draw. At a first load, the numbers are not shown.

## API used

To make the project, it was needed to access an api, to fetch the latest result, and some more information.

The chosen api was the Loterias CAIXA API, that can be found on GitHub [here](https://github.com/guto-alves/loterias-api).

The base URL to work with this api to see the latest result is as follows:

> https://loteriascaixa-api.herokuapp.com/api/<lottery\>/latest

Just substitute ___lottery___ by the name of the lottery you want to see the latest result. Some options are __mega-sena__, __lotofacil__ and so on.

## Docker and Database

This application doesn't really need a database but I haven't remove it from the project settings.

This application has been dockerized, so, if you want to run this application locally without having to install all of it's dependencies, just run it with __docker-compose__.
