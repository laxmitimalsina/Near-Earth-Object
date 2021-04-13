import csv
import json


def write_to_csv(results, filename):
    """Write an iterable of `CloseApproach` objects to a CSV file.

    The precise output specification is in `README.md`. Roughly, each output row
    corresponds to the information in a single close approach from the `results`
    stream and its associated near-Earth object.

    :param results: An iterable of `CloseApproach` objects.
    :param filename: A Path-like object pointing to where the data should be saved.
    """
    fieldnames = (
        "datetime_utc",
        "distance_au",
        "velocity_km_s",
        "designation",
        "name",
        "diameter_km",
        "potentially_hazardous",
    )
    # TODO: Write the results to a CSV file, following the specification in the instructions.
    with open(filename, "w") as outfile:
        csvfile = csv.DictWriter(outfile, fieldnames=fieldnames)
        csvfile.writeheader()
        for row in results:
            csvfile.writerow(
                {
                    "datetime_utc": row.time,
                    "distance_au": row.distance,
                    "velocity_km_s": row.velocity,
                    "designation": row._designation,
                    "name": row.neo.name,
                    "diameter_km": row.neo.diameter,
                    "potentially_hazardous": row.neo.hazardous,
                }
            )


def write_to_json(results, filename):
    """Write an iterable of `CloseApproach` objects to a JSON file.

    The precise output specification is in `README.md`. Roughly, the output is a
    list containing dictionaries, each mapping `CloseApproach` attributes to
    their values and the 'neo' key mapping to a dictionary of the associated
    NEO's attributes.

    :param results: An iterable of `CloseApproach` objects.
    :param filename: A Path-like object pointing to where the data should be saved.
    """

    mylist = []
    for row in results:
        all_dict_items = {
            "datetime_utc": row.time_str,
            "distance_au": row.distance,
            "velocity_km_s": row.velocity,
            "neo": {
                "designation": row._designation,
                "name": row.neo.name,
                "diameter_km": row.neo.diameter,
                "potentially_hazardous": row.neo.hazardous,
            },
        }

        mylist.append(all_dict_items)

    with open(filename, "w") as outfile:
        jsonfile = json.dump(mylist, outfile, indent=2)
