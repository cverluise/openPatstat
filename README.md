[CEI]:https://www.college-de-france.fr/site/centre-economie-innovation/index.htm
[GHissues]:https://github.com/cverluise/openPatstat/issues
[GHpulls]:https://github.com/cverluise/openPatstat/pulls
[GHOP]:https://github.com/cverluise/openPatstat
[GBOP]:https://economics-of-innovation-lab.gitbook.io/open-patstat/
[GBlogo]:https://www.google.com/url?sa=i&rct=j&q=&esrc=s&source=images&cd=&cad=rja&uact=8&ved=2ahUKEwi269Gt8vHeAhWMz4UKHRrXAEkQjRx6BAgBEAU&url=https%3A%2F%2Ftwitter.com%2Fgitbookio&psig=AOvVaw3qrY-UcmDrgPTuMh6jGY0b&ust=1543316020829708

# Statement

The purpose of this project is to help disseminate Statistical Data on Patents (so called PatStat) 
to stimulate research on Patents and Innovation. To do so, we provide tools to load, build and explore 
this data using Google Cloud Platform. Google Cloud Platform offers a simple, yet powerful Big Data 
environment. 

This is an open source project hosted by the [Economics of Innovation ​Research Lab][CEI] at the Collège de France.
This is also meant to provide a place for sharing codes and good practices. Please, send [pull requests][GHpulls] and 
[issues][GHissues] directly to the [dedicated GitHub repository][GHOP]. 

> <font color='orange'>Version 0.1: This is a development release. Some features might be changed in backward-incompatible ways.</font>

# Documentation

[![alt text](https://gitlab.com/uploads/-/system/project/avatar/1058960/gitbook.png "Logo Title Text 1")][GBOP]

Please, visit our [GitBook][GBOP] for full documentation, examples and resources.   


# Installation 

## Clone/ Download the openPatstat repository

### Git

```bash
cd destination/path
git clone https://github.com/cverluise/openPatstat.git
````

### Download

1. Go to the [Open Patstat GitHub repository][GHOP]​
2. Click `Clone` or Download (top right)
3. Click `Download ZIP`

## Install the open_pastat python module

```bash
cd path/to/open_patstat
pip install -r requirements.txt
pip install -e .
```