from gkeepapi import Keep
import yaml
import json

keep = Keep()

try:
    with open("state", "r") as f:
        state = json.load(f)
        keep.restore(state)
        print("restored")
except FileNotFoundError:
    pass

with open("credentials.txt") as f:
    username, password = f.read().split(":")
    keep.login(username, password)


class Translator:
    def __init__(self, **kwargs):
        for k, v in kwargs.items():
            setattr(self, k, v)

    def from_md(md):
        raise NotImplementedError

    def from_keep(note):
        return Translator(
            labels=[label.name for label in note.labels.all()],
            title=note.title,
            text=note.text,
            id=note.server_id,
        )

    def to_md(self):
        res = ""
        res += "---\n"
        res += yaml.dump({
            "id": self.id,
            "labels": self.labels,
        })
        res += "---\n"
        if self.title:
            res += f"# {self.title}\n"
        if self.text:
            if self.title:
                res += "\n"
            res += self.text
        return res

    def to_keep(self):
        NotImplementedError


def get_public_md():
    public = keep.findLabel("public")
    for note in keep.find(labels=[public]):
        yield Translator.from_keep(note).to_md()


if __name__ == "__main__":
    for note in get_public_md():
        print(note)
        print("===")


with open("state", "w") as f:
    state = keep.dump()
    json.dump(state, f)
