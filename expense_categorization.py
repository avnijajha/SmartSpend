def categorize_transaction(description):
    description = description.lower()
    food=["swiggy","zomato","restaurant","food","cafe","dominos","pizza hut","burger king","mcdonalds"]
    transport=["uber","ola","rapido","metro","bus","fuel"]
    shopping=["amazon","flipkart","myntra","nykaa","meesho","grocery","shopping","online shopping","mall","clothes"]
    entertainment=["netflix","jio hotstar","prime video","youtube","spotify","movie","cinema","bookmyshow","game"]
    bills=["electricity","water bill","gas bill","recharge","internet","phone bill"]
    education=[ "college","school","course","books","coaching"]
    for word in food:
        if word in description:
            return "Food"
    for word in transport:
        if word in description:
            return "Transport"
    for word in shopping:
        if word in description:
            return "Shopping"
    for word in entertainment:
        if word in description:
            return "Entertainment"
    for word in bills:
        if word in description:
            return "Bills"
    for word in education:
        if word in description:
            return "Education"
    return "Others"

def categorize_all_transactions(transactions):
    for transaction in transactions:
        transaction["category"] = categorize_transaction(transaction["description"])


def display_categories(transactions):
    for transaction in transactions:
        print(transaction["description"],"->",transaction["category"])
