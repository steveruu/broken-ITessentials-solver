# Cisco ITEssentials solver  
## written in python, broken  

### Description
- Solves *some of the* Cisco ITEssentials questions  
- Uses the itexamanswers.net website, where it scrapes the answer  

### Usage
```py
python3 string-formatter.py [question]  
```

### Example
```py
python3 string-formatter.py "Which two statements are true about the structure of an IPv6 address? (Choose two.)"
```

### Notes
- Broken because of the website's random-ass URL length limit
- The ITExamAnswers URLs cutout at random characters instead of having a set limit

