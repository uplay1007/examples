from math import sin, cos, sqrt, atan2, radians


def sizes(toponym_coodrinates, toponym, json_response):
    organization = json_response["features"][0]
    org_name = organization["properties"]["CompanyMetaData"]["name"]
    org_address = organization["properties"]["CompanyMetaData"]["address"]
    org_time = organization["properties"]['CompanyMetaData']['Hours']['text']
    point = organization["geometry"]["coordinates"]

    toponym_coodrinates = list(map(lambda x: float(x), toponym_coodrinates.split()))
    R = 6373.0
    lat1, lon1 = radians(toponym_coodrinates[0]), radians(toponym_coodrinates[1])
    lat2, lon2 = radians(point[0]), radians(point[1])
    dlon = lon2 - lon1
    dlat = lat2 - lat1
    a = sin(dlat / 2) ** 2 + cos(lat1) * cos(lat2) * sin(dlon / 2) ** 2
    c = 2 * atan2(sqrt(a), sqrt(1 - a))
    distance = R * c

    org_point = "{0},{1}".format(point[0], point[1])

    max_y = toponym["boundedBy"]["Envelope"]["upperCorner"].split()[1]
    max_x = toponym["boundedBy"]["Envelope"]["upperCorner"].split()[0]
    min_y = toponym["boundedBy"]["Envelope"]["lowerCorner"].split()[1]
    min_x = toponym["boundedBy"]["Envelope"]["lowerCorner"].split()[0]
    delta = max(abs(float(max_y) - float(min_y)), abs(float(max_x) - float(min_x)))
    return str(delta), org_point, org_address, org_name, org_time, "{:.2f}".format(distance)
