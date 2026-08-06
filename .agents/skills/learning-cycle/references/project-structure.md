# Standard Project Structure

For learning projects under `03.projects/`, use the following scaffold:

```
03.projects/<project-id>/
├── index.md                 # Project MOC
├── phase-<slug>/
│   ├── index.md             # Phase MOC
│   ├── week-01.md
│   ├── week-02.md
│   └── ...
├── resources/
│   ├── <topic>.md
│   └── ...
└── templates/
    ├── weekly-note.md
    ├── paper-reading.md
    └── project-retro.md
```

- `project-id`: kebab-case identifier
- `phase-<slug>`: lowercase hyphenated phase name
- `week-NN.md`: zero-padded week number
