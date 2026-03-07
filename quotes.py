"""
quotes.py — Curated developer & productivity quotes for daily streak commits.
"""

import random

QUOTES = [
    # Coding & Engineering
    "The best code is no code at all. — Jeff Atwood",
    "First, solve the problem. Then, write the code. — John Johnson",
    "Any fool can write code that a computer can understand. Good programmers write code that humans can understand. — Martin Fowler",
    "Make it work, make it right, make it fast. — Kent Beck",
    "Code is like humor. When you have to explain it, it's bad. — Cory House",
    "Programs must be written for people to read, and only incidentally for machines to execute. — Harold Abelson",
    "Simplicity is the soul of efficiency. — Austin Freeman",
    "The most powerful tool we have as developers is automation. — Scott Hanselman",
    "Software is eating the world. — Marc Andreessen",
    "The function of good software is to make the complex appear to be simple. — Grady Booch",
    "Debugging is twice as hard as writing the code in the first place. — Brian W. Kernighan",
    "Talk is cheap. Show me the code. — Linus Torvalds",
    "One of my most productive days was throwing away 1000 lines of code. — Ken Thompson",
    "Always code as if the guy who ends up maintaining your code will be a violent psychopath who knows where you live. — John Woods",
    "Premature optimization is the root of all evil. — Donald Knuth",
    "Clean code always looks like it was written by someone who cares. — Robert C. Martin",
    "The best way to get a project done faster is to start sooner. — Jim Highsmith",
    "Continuous improvement is better than delayed perfection. — Mark Twain",
    "It's not a bug, it's an undocumented feature.",
    "A good programmer is someone who always looks both ways before crossing a one-way street. — Doug Linder",

    # Growth & Consistency
    "Small daily improvements over time lead to stunning results. — Robin Sharma",
    "Success is the sum of small efforts, repeated day in and day out. — Robert Collier",
    "We are what we repeatedly do. Excellence, then, is not an act, but a habit. — Aristotle",
    "The secret of getting ahead is getting started. — Mark Twain",
    "You don't have to be great to start, but you have to start to be great. — Zig Ziglar",
    "Fall seven times, stand up eight. — Japanese Proverb",
    "Done is better than perfect. — Sheryl Sandberg",
    "Every expert was once a beginner. — Helen Hayes",
    "Act as if what you do makes a difference. It does. — William James",
    "Consistency is more important than perfection.",
    "The only way to do great work is to love what you do. — Steve Jobs",
    "Dream big. Start small. Act now. — Robin Sharma",
    "Your limitation—it's only your imagination.",
    "Push yourself, because no one else is going to do it for you.",
    "Great things never come from comfort zones.",
    "It always seems impossible until it's done. — Nelson Mandela",
    "Strive for progress, not perfection.",
    "The harder you work for something, the greater you'll feel when you achieve it.",
    "Don't stop when you're tired. Stop when you're done.",
    "Wake up with determination. Go to bed with satisfaction.",

    # Open Source & Community
    "Given enough eyeballs, all bugs are shallow. — Linus Torvalds (Linus's Law)",
    "Open source is about collaborating; not competing. — Kelsey Hightower",
    "Software is a great combination of artistry and engineering. — Bill Gates",
    "The computer was born to solve problems that did not exist before. — Bill Gates",
    "The advance of technology is based on making it fit in so that you don't really even notice it. — Bill Gates",

    # Learning & Mindset
    "An investment in knowledge pays the best interest. — Benjamin Franklin",
    "Tell me and I forget. Teach me and I remember. Involve me and I learn. — Benjamin Franklin",
    "Learning is not attained by chance; it must be sought for with ardor and attended to with diligence. — Abigail Adams",
    "The more that you read, the more things you will know. — Dr. Seuss",
    "The capacity to learn is a gift; the ability to learn is a skill; the willingness to learn is a choice. — Brian Herbert",
    "In learning you will teach, and in teaching you will learn. — Phil Collins",
    "Education is not the filling of a bucket, but the lighting of a fire. — W.B. Yeats",
    "Live as if you were to die tomorrow. Learn as if you were to live forever. — Mahatma Gandhi",
    "The beautiful thing about learning is that nobody can take it away from you. — B.B. King",
    "The more I learn, the more I realize how much I don't know. — Albert Einstein",

    # Productivity & Focus
    "You miss 100% of the shots you don't take. — Wayne Gretzky",
    "Productivity is never an accident. It is always the result of a commitment to excellence. — Paul J. Meyer",
    "Focus on being productive instead of busy. — Tim Ferriss",
    "Either write something worth reading or do something worth writing. — Benjamin Franklin",
    "The key is not to prioritize what's on your schedule, but to schedule your priorities. — Stephen Covey",
    "Time is the scarcest resource, and unless it is managed, nothing else can be managed. — Peter Drucker",
    "If you spend too much time thinking about a thing, you'll never get it done. — Bruce Lee",
    "Do what you can, with what you have, where you are. — Theodore Roosevelt",
    "Take care of the minutes and the hours will take care of themselves. — Lord Chesterfield",
    "You will never find time for anything. If you want time, you must make it. — Charles Buxton",

    # Resilience & Perseverance
    "Failure is the condiment that gives success its flavor. — Truman Capote",
    "I have not failed. I've just found 10,000 ways that won't work. — Thomas Edison",
    "It does not matter how slowly you go as long as you do not stop. — Confucius",
    "Our greatest glory is not in never falling, but in rising every time we fall. — Confucius",
    "The difference between a successful person and others is not a lack of strength, but a lack of will. — Vince Lombardi",
    "Strength does not come from winning. Your struggles develop your strengths. — Arnold Schwarzenegger",
    "Life is 10% what happens to you and 90% how you react to it. — Charles R. Swindoll",
    "Believe you can and you're halfway there. — Theodore Roosevelt",
    "Problems are not stop signs, they are guidelines. — Robert H. Schuller",
    "Start where you are. Use what you have. Do what you can. — Arthur Ashe",

    # Tech Visionaries
    "The Internet is becoming the town square for the global village of tomorrow. — Bill Gates",
    "Just because something doesn't do what you planned it to do doesn't mean it's useless. — Thomas Edison",
    "Innovation distinguishes between a leader and a follower. — Steve Jobs",
    "Your time is limited, so don't waste it living someone else's life. — Steve Jobs",
    "Technology is best when it brings people together. — Matt Mullenweg",
    "The advance of technology is based on making it fit in so that you don't really even notice it. — Bill Gates",
    "The biggest risk is not taking any risk. — Mark Zuckerberg",
    "Move fast and break things. — Mark Zuckerberg",
    "The secret to successful hiring is this: look for the people who want to change the world. — Marc Benioff",
    "What we wish, we readily believe, and what we ourselves think, we imagine others think also. — Julius Caesar",

    # Programming Wisdom
    "There are only two kinds of languages: the ones people complain about and the ones nobody uses. — Bjarne Stroustrup",
    "Any sufficiently advanced technology is indistinguishable from magic. — Arthur C. Clarke",
    "Measuring programming progress by lines of code is like measuring aircraft building progress by weight. — Bill Gates",
    "The most dangerous phrase is: 'We've always done it this way.' — Grace Hopper",
    "A ship in harbor is safe, but that is not what ships are for. — John A. Shedd",
    "The best error message is the one that never shows up. — Thomas Fuchs",
    "Walking on water and developing software from a specification are easy if both are frozen. — Edward V. Berard",
    "No code is faster than no code.",
    "Make it work. Make it right. Make it fast.",
    "APIs are forever. Design them carefully.",
    "Commit often. Perfect later. Publish once.",
    "Every commit is a gift to your future self.",
    "Good code is its own best documentation.",
    "Refactor early, refactor often.",
    "Test it before you regret it.",
]


def get_quote() -> str:
    """Return a random quote from the curated list."""
    return random.choice(QUOTES)


def get_quote_seeded(seed: int) -> str:
    """Return a deterministic quote based on a seed (e.g., day of year)."""
    rng = random.Random(seed)
    return rng.choice(QUOTES)
