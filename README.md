# Django snippets

A collection of utilities which I've used across several Django projects.

The motivation for this repository is to hold together a bunch of code snippets
which I've found useful in several Django projects, but which I don't think
warrant publishing yet another package. Sometimes because they require some fine
tuning for each specific project, and other times because they're just two
small.

Some of these already exist elsewhere, and with much more refined
implementations (see the README of each module for proper citations) but
sometimes I think it's just not worth the extra dependency. Also, this package
isn't intended to turn into something like
[django-extensions](https://github.com/django-extensions/django-extensions), I
prefer just coming back here and copying-pasting whatever I need when I need it
(most of the time it's just a single file, and these snippets are simple enough
that very, very rarely require an update).

## Snippets

- [ShortUUIDField](./shortuuid/README.md): a URL-friendly alternative to UUID fields.

## License

Released under the MIT License, see [LICENSE](./LICENSE) for a copy.

## Contributing

Contributions or comments are very welcome, feel free to open an issue or submit
a pull request.
