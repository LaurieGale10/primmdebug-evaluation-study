gender_split: dict[str, int] = {
    "Female": 0,
    "Male": 0,
    "Non-binary": 0,
    "Other": 0,
    "Prefer not to say": 0
}
def get_gender_split() -> dict[str, int]:
    return gender_split

year_group_split: dict[str, int] = {
    "Year 7": 0,
    "Year 8": 0,
    "Year 9": 0,
    "Year 10": 0,
    "Year 11": 0
}
def get_year_group_split() -> dict[str, int]:
    return year_group_split

school_split: dict[str, int] = {
    "School A": 0,
    "School B": 0,
    "School C": 0,
    "School D": 0,
    "School E": 0
}

def get_school_split() -> dict[str, int]:
    return school_split

#PRIMMDebug challenge names?