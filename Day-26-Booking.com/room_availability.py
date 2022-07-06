"""
Expected Output:
[
    {
        "price": 250,
        "features": ["breakfast"],
        "availbility": 1
    },
    {
        "price": 260,
        "features": ["breakfast", "refundable"],
        "availbility": 3
    }
]

"""

availability = {
    176: [
        {
            "price": 120,
            "features": ["breakfast", "refundable"],
            "availbility": 5
        }
    ],
    177: [
        {
            "price": 130,
            "features": ["breakfast"],
            "availbility": 1
        },
        {
            "price": 140,
            "features": ["breakfast", "refundable", "wifi"],
            "availbility": 3
        }
    ],
    178: [
        {
            "price": 130,
            "features": ["breakfast"],
            "availbility": 2
        },
        {
            "price": 140,
            "features": ["breakfast", "refundable", "wifi"],
            "availbility": 10
        }
    ]
}


def get_all_property_that_satisfies_the_constraints(properties, features, rooms):
    res = []
    for p in properties:
        if p["availbility"] >= rooms and len(set(features).difference(set(p["features"]))) == 0:
            res.append(p)
    return res


def create_combinations(day1, day2):
    res = []
    for p1 in day1:
        for p2 in day2:
           res.append(
               {
                   "price": p1["price"] + p2["price"],
                   "features": list(set(p1["features"]).intersection(p2["features"])),
                   "availbility": min(p1["availbility"], p2["availbility"])
               }
           )
    return res if len(day2) != 0 else day1


def return_result(search):
    prev_day = []
    for date in range(search["checkin"], search["checkout"]):
        if len(availability.get(date)) > 0:
            curr_day = get_all_property_that_satisfies_the_constraints(availability.get(date), search["features"],
                                                                       search["rooms"])
            prev_day = create_combinations(curr_day, prev_day)
    return prev_day


if __name__ == '__main__':
    search = {
        "checkin": 176,
        "checkout": 178,
        "features": ["breakfast"],
        "rooms": 1
    }
    output = return_result(search)
    [print(o) for o in output]
