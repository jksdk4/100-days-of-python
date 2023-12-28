# generate moar here: https://opentdb.com/api_config.php

from html import unescape
question_data = [
    [
        {"type": "boolean", "text": "A slug's blood is green.", "answer": "True"},
        {"type": "boolean", "text": "The loudest animal is the African Elephant.", "answer": "False"},
        {"type": "boolean", "text": "Approximately one quarter of human bones are in the feet.", "answer": "True"},
        {"type": "boolean", "text": "The total surface area of a human lungs is the size of a football pitch.", "answer": "True"},
        {"type": "boolean", "text": "In West Virginia, USA, if you accidentally hit an animal with your car, you are free to take it "
                 "home to eat.", "answer": "True"},
        {"type": "boolean", "text": "In London, UK, if you happen to die in the House of Parliament, you are entitled to a state funeral.",
         "answer": "False"},
        {"type": "boolean", "text": "It is illegal to pee in the Ocean in Portugal.", "answer": "True"},
        {"type": "boolean", "text": "You can lead a cow down stairs but not up stairs.", "answer": "False"},
        {"type": "boolean", "text": "Google was originally called 'Backrub'.", "answer": "True"},
        {"type": "boolean", "text": "Buzz Aldrin's mother's maiden name was 'Moon'.", "answer": "True"},
        {"type": "boolean", "text": "No piece of square dry paper can be folded in half more than 7 times.", "answer": "False"},
        {"type": "boolean", "text": "A few ounces of chocolate can to kill a small dog.", "answer": "True"}
    ],
    [
        {
            "type": "boolean", "difficulty": "easy", "category": "Geography",
            "text": "Toronto is the capital city of the North American country of Canada.",
            "answer": "False"
        },
        {
            "type": "boolean", "difficulty": "easy", "category": "Geography",
            "text": "There are no deserts in Europe.",
            "answer": "True"
        },
        {
            "type": "boolean", "difficulty": "easy", "category": "Geography",
            "text": "New Haven is the capital city of the state of Connecticut in the United States.",
            "answer": "False"
        },
        {
            "type": "boolean", "difficulty": "easy", "category": "Geography",
            "text": "Vatican City is a country.",
            "answer": "True"
        },
        {
            "type": "boolean", "difficulty": "easy", "category": "Geography",
            "text": "Hungary is the only country in the world beginning with H.",
            "answer": "False"
        },
        {
            "type": "boolean", "difficulty": "easy", "category": "Geography",
            "text": "The Republic of Malta is the smallest microstate worldwide.",
            "answer": "False"
        },
        {
            "type": "boolean", "difficulty": "easy", "category": "Geography",
            "text": "California is larger than Japan.",
            "answer": "True"
        },
        {
            "type": "boolean", "difficulty": "easy", "category": "Geography",
            "text": "Tokyo is the capital of Japan.",
            "answer": "True"
        },
        {
            "type": "boolean", "difficulty": "easy", "category": "Geography",
            "text": f"There is an island in Japan called \u014ckunoshima, A.K.A. " 
                    f"{unescape('&quot;')}Rabbit Island{unescape('&quot;')}, so named "
                    f"because of it{unescape('&#039;')}s huge population of rabbits.",
            "answer": "True"
        },
        {
            "type": "boolean", "difficulty": "easy", "category": "Geography",
            "text": "Nova Scotia is on the east coast of Canada.",
            "answer": "True"
        }
    ],
    [
        {"type": "multiple", "difficulty": "easy", "category": "Science: Computers",
         "text": "When Gmail first launched, how much storage did it provide for your email?",
         "answer": "1GB", "incorrect_answers": ["512MB", "5GB", "Unlimited"]},
        {"type": "multiple", "difficulty": "easy", "category": "Science: Computers",
         "text": "How many values can a single byte represent?",
         "answer": "256", "incorrect_answers": ["8", "1", "1024"]},
        {"type": "multiple", "difficulty": "easy", "category": "Science: Computers",
         "text": "According to the International System of Units, how many bytes are in a kilobyte of RAM?",
         "answer": "1000", "incorrect_answers": ["512", "1024", "500"]},
        {"type": "multiple", "difficulty": "easy", "category": "Science: Computers",
         "text": "How many kilobytes in one gigabyte (in decimal)?",
         "answer": "1000000",
         "incorrect_answers": ["1024", "1000", "1048576"]},
        {"type": "multiple", "difficulty": "easy", "category": "Science: Computers",
         "text": "Which computer hardware device provides an interface for all other connected devices to communicate?",
         "answer": "Motherboard",
         "incorrect_answers": ["Central Processing Unit", "Hard Disk Drive",
                               "Random Access Memory"]},
        {"type": "multiple", "difficulty": "easy", "category": "Science: Computers",
         "text": "In web design, what does CSS stand for?",
         "answer": "Cascading Style Sheet",
         "incorrect_answers": ["Counter Strike: Source", "Corrective Style Sheet",
                               "Computer Style Sheet"]},
        {"type": "multiple", "difficulty": "easy", "category": "Science: Computers",
         "text": "The C programming language was created by this American computer scientist. ",
         "answer": "Dennis Ritchie",
         "incorrect_answers": ["Tim Berners Lee", "al-Khw\u0101rizm\u012b",
                               "Willis Ware"]},
        {"type": "multiple", "difficulty": "easy", "category": "Science: Computers",
         "text": "HTML is what type of language?",
         "answer": "Markup Language",
         "incorrect_answers": ["Macro Language", "Programming Language",
                               "Scripting Language"]},
        {"type": "multiple", "difficulty": "easy", "category": "Science: Computers",
         "text": "The numbering system with a radix of 16 is more commonly referred to as ",
         "answer": "Hexidecimal",
         "incorrect_answers": ["Binary", "Duodecimal", "Octal"]},
        {"type": "multiple", "difficulty": "easy", "category": "Science: Computers",
         "text": "In any programming language, what is the most common way to iterate through an array?",
         "answer": f"{unescape('&#039;')}For{unescape('&#039;')} loops",
         "incorrect_answers": [f"{unescape('&#039;')}If{unescape('&#039;')} Statements",
                               f"{unescape('&#039;')}Do-while{unescape('&#039;')} loops",
                               f"{unescape('&#039;')}While{unescape('&#039;')} loops"]}
    ]

]
