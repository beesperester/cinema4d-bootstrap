from bootstrap import Description, DescriptionFlag, Layout, Group

SETTINGS_STRENGTH = Description(
    "SETTINGS_STRENGTH",
    {
        "strings_us": "Strength"
    },
    "REAL",
    [
        DescriptionFlag("MIN", 0.0),
        DescriptionFlag("MAX", 100.0)
    ]
)

SETTINGS_OFFSET = Description(
    "SETTINGS_OFFSET",
    {
        "strings_us": "Offset"
    },
    "VECTOR",
    []
)

layout = Layout(
    "Ttest",
    {
        "strings_us": "Test"
    },
    [
        DescriptionFlag("INCLUDE", "Tbase"),
        DescriptionFlag("INCLUDE", "Texpression")
    ],
    Group(
        "SETTINGS_GROUP",
        {
            "strings_us": "Settings"
        },
        [
            DescriptionFlag("DEFAULT", 1)
        ],
        [
            SETTINGS_STRENGTH,
            Group(
                "GROUP_LABEL_OFFSET",
                {
                    "strings_us": "Offset Settings"
                },
                [
                    DescriptionFlag("INCLUDE", "Tbase"),
                    DescriptionFlag("INCLUDE", "Texpression")
                ],
                [
                    SETTINGS_OFFSET
                ]
            )
        ]
    )
)

print(layout.GenerateStrings("strings_us"))
print(layout.GenerateHeaders())