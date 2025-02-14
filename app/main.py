class Person:
    people: dict[str, "Person"] = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people[name] = self


def create_person_list(people: list) -> list:
    persons: [Person] = []
    for person_dict in people:
        name = person_dict["name"]
        age = person_dict["age"]
        persons.append(Person(name, age))
    for person_dict in people:
        item = Person.people[person_dict["name"]]
        if "wife" in person_dict and person_dict["wife"] is not None:
            item.wife = Person.people[person_dict["wife"]]
        if "husband" in person_dict and person_dict["husband"] is not None:
            item.husband = Person.people[person_dict["husband"]]

    return persons
