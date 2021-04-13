import csv
import json

from models import NearEarthObject, CloseApproach


def load_neos(neo_csv_path):
    """Read near-Earth object information from a CSV file.

    :param neo_csv_path: A path to a CSV file containing data about near-Earth objects.
    :return: A collection of `NearEarthObject`s.
    """
    neos = []
    with open(neo_csv_path) as infile:
        contents = csv.reader(infile)
        # a list to store column names found in the csv file
        headers = []
        for i, row in enumerate(contents):
            # if i is 0 then this is a header of CSV file
            if i == 0:
                headers = row
            else:
                row_dict = dict(zip(headers, row))
                designation = row_dict["pdes"]
                name = row_dict["name"]
                diameter = row_dict["diameter"]
                hazardous = row_dict["pha"]
                #                 print(row_dict)
                #                 break
                neo_list_info = NearEarthObject(designation, name, diameter, hazardous)
                neos.append(neo_list_info)
    return neos


def load_approaches(cad_json_path):
    """Read close approach data from a JSON file.

    :param neo_csv_path: A path to a JSON file containing data about close approaches.
    :return: A collection of `CloseApproach`es.
    """
    approaches = []
    # TODO: Load close approach data from the given JSON file.
    with open(cad_json_path) as infile:
        contents = json.load(infile)
        headers = contents["fields"]

        for row in contents["data"]:
            row_dict = dict(zip(headers, row))
            designation = row_dict["des"]
            time = row_dict["cd"]
            distance = row_dict["dist"]
            velocity = row_dict["v_rel"]
            ca = CloseApproach(
                designation=designation, time=time, distance=distance, velocity=velocity
            )
            approaches.append(ca)

    return approaches
