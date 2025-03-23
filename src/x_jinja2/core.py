import io
from jinja2 import Environment
import csv, json5, jsonpath, jinja2


class XEnvironment(Environment):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._load_filters()

    def _load_filters(self):
        try:
            from jinja2_ansible_filters import core_filters

            self.filters.update(core_filters.FilterModule().filters())
        except ImportError:
            pass

        try:
            from ansible.plugins.filter import core as ansible_core_filters
            from ansible.plugins.filter import urls as ansible_urls_filters
            from ansible.plugins.filter import urlsplit as ansible_urlsplit_filters
            from ansible.plugins.filter import (
                mathstuff as ansible_mathstuff_filters,
            )

            self.filters |= ansible_core_filters.FilterModule().filters()
            self.filters |= ansible_urls_filters.FilterModule().filters()
            self.filters |= ansible_urlsplit_filters.FilterModule().filters()
            self.filters |= ansible_mathstuff_filters.FilterModule().filters()

            self.filters |= {
                "normalize_csv": self.__filter__normalize_csv,
                "jsonpath": jsonpath.jsonpath,
            }

        except ImportError:
            pass

    def __filter__normalize_csv(self, value):
        output = io.StringIO()
        csv_writer = csv.writer(output, quoting=csv.QUOTE_ALL)
        csv_writer.writerow([value])
        return str(output.getvalue().strip())

        pass


if __name__ == "__main__":
    output = (
        XEnvironment()
        .from_string("{{ data.foo | default('NULL') | normalize_csv }}")
        .render(
            data={
                "foo": "bar",
            },
        )
    )
    print(output)
    pass
