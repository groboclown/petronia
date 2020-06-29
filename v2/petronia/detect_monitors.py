
import sys
from petronia.arch import funcs

FORMATS = {
    'yaml': [
        # Header
        "workgroups:\n- name: My Work Group\n  display:\n",
        # Per monitor
        (
            "  # screen {index} virtual position: ({left},{top}) -> ({right},{bottom})\n" +
            "  - width: {width}\n" +
            "    height: {height}"
        ),
        # Join the lines with:
        "\n",
        # Footer
        "\n"
    ],
    'json': [
        '"workgroups": [{\n  "name": "My Work Group",\n  "display": [\n',
        '    {b}\n      "width": {width}\n      "height": {height}\n    {e}\n',
        ",\n",
        "  ]\n}]\n"
    ],
    'py': [
        "",
        (
            "    # screen {index} virtual position: ({left},{top}) -> ({right},{bottom})\n" +
            "    config.MonitorResConfig({width}, {height})"
        ),
        ",\n",
        "\n"
    ]
}

if __name__ == '__main__':
    __format = 'yaml'
    if len(sys.argv) > 2 and sys.argv[1] == '-f':
        __format = sys.argv[2]
    if __format not in FORMATS:
        print("Unknown output format {0}".format(__format))
        sys.exit(1)

    print(FORMATS[__format][0])

    __lines = []
    __monitors = funcs.monitor__find_monitors()
    for __index in range(len(__monitors)):
        __monitor = __monitors[__index]
        __lines.append(FORMATS[__format][1].format(
            b='{', e='}',
            index=__index + 1,
            top=__monitor['top'],
            bottom=__monitor['bottom'],
            left=__monitor['left'],
            right=__monitor['right'],
            width=__monitor['right'] - __monitor['left'],
            height=__monitor['bottom'] - __monitor['top']
        ))

    print(FORMATS[__format][2].join(__lines))
    print(FORMATS[__format][3])
