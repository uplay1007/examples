def sizes(json_response):
    toponym = json_response["response"]["GeoObjectCollection"][
        "featureMember"][0]["GeoObject"]
    # Координаты центра топонима:
    toponym_coodrinates = toponym["Point"]["pos"]
    toponym_longitude, toponym_lattitude = toponym_coodrinates.split(" ")
    max_y = toponym["boundedBy"]["Envelope"]["upperCorner"].split()[1]
    max_x = toponym["boundedBy"]["Envelope"]["upperCorner"].split()[0]
    min_y = toponym["boundedBy"]["Envelope"]["lowerCorner"].split()[1]
    min_x = toponym["boundedBy"]["Envelope"]["lowerCorner"].split()[0]
    delta = max(abs(float(max_y) - float(min_y)), abs(float(max_x) - float(min_x)))
    return str(delta), toponym_coodrinates, toponym_longitude, toponym_lattitude