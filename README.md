# CS 340 — Grazioso Salvare Dashboard

A full stack web application dashboard built for Grazioso Salvare, a company that identifies and trains search-and-rescue dogs. The dashboard reads Austin Animal Center outcome records from a MongoDB database and lets staff filter them by rescue specialty.

## Artifacts

- `ProjectTwoDashboard.ipynb` — the dashboard application
- `CRUD_Python_Module.py` — reusable CRUD module for MongoDB
- `README.docx` — full project documentation with execution screenshots

## Reflection

### How do you write programs that are maintainable, readable, and adaptable?

The CRUD Python module from Project One is the clearest example of this in my work. Rather than scattering database calls through the dashboard code, I put all four operations behind a single `AnimalShelter` class with a consistent interface: every method takes a dictionary and returns either a boolean, a list, or a count. The dashboard never has to know about connection strings, authentication, or MongoDB cursors — it just calls `read()` and gets back something it can use.

The payoff showed up immediately in Project Two. The filter callback for the four rescue types is essentially one function with four different query dictionaries, all passed to the same `read()` method. Adding a fifth rescue category would mean adding one `elif` block, not writing new database code. I also used exception handling and guard clauses throughout, so a failed query returns an empty list instead of crashing the dashboard, and docstrings on each method so the inputs and return values are documented where someone would actually look for them.

Because the module is self-contained and takes credentials as constructor arguments, it could be reused against the same database by anything else — a reporting script, a command-line tool, a REST API, or a different front end entirely. Swapping the collection name would point it at a different data set without changing the method logic.

### How do you approach a problem as a computer scientist?

I started from the client's requirements rather than from the code. The Rescue Type and Preferred Dog Breeds table defined exactly what each filter needed to match on breed, sex, and age, so I translated that table directly into MongoDB queries before building any interface around them. That meant the data layer was correct and testable before the dashboard existed.

The main difference from previous coursework is that this project had a real separation of concerns imposed on it. In earlier classes I was usually writing one program that did one thing. Here I was working across an MVC stack — MongoDB as the model, Dash components as the view, callbacks and the CRUD module as the controller — and each layer had to work on its own terms. Building the database and indexes first, then the CRUD module, then the dashboard meant each layer could be verified before the next one depended on it. When something broke later, I usually knew which layer to look in.

For future client requests, I'd keep that order: understand the queries the client actually needs, index for those queries specifically, build a data access layer with a clean interface, and only then build the interface on top. I'd also keep testing each layer in isolation — the test notebook that exercised every CRUD method on both matching and non-matching cases caught problems that would have been much harder to diagnose through the dashboard.

### What do computer scientists do, and why does it matter?

Computer scientists take a problem that people are currently solving slowly, inconsistently, or not at all, and build something that solves it reliably and repeatedly. The technical work is a means to that end.

For Grazioso Salvare specifically, the underlying data already existed — the Austin Animal Center has been recording shelter outcomes all along. What it didn't have was a way to answer the question the company actually cares about: which dogs here are candidates for water rescue training? Answering that by hand means knowing the breed criteria, the age range in weeks, and how to query a database. This dashboard turns that into selecting a radio button. The staff who identify and train rescue dogs can spend their time on that work instead of on data retrieval, and the tool enforces the criteria consistently so candidates don't get missed because of a typo or a forgotten filter.

## Contact

Miniece Ragin
