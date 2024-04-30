# Short UUIDs for Django

URL-friendly, random (enumeration-resistant) IDs for Django models.

## Dependencies

This snippet only depends on the `base58` package:

```
pip install base58  # if using PIP
poetry add base58   # if using Poetry
```

## Usage

1. Install the dependencies from above.
2. Copy the contents of the [fields.py](./shortuuid/models/fields.py) file into
   your project (a suitable location is under your core app's models package).
3. Add a `ShortUUIDField` to your models.
4. `makemigrations`, `migrate` and profit!

## Motivation

Random UUIDs provide resistance against enumeration attacks, and Django already
provides the `UUIDField` which can be easily used as a primary key. However, the
default hexadecimal representation of UUIDs used is not efficient, since each
UUID takes up 36 characters. An easy solution to this is to use a more dense
encoding, such as base 64 which is available as part of the standard library but
has the inconvenience of using hyphens (`-`) which introduce breakpoints when
selecting words in most operating systems. Try double-clicking the ID below and
you'll notice that the selection automatically extends only up to the hyphen:

```
uGRQNvcFTUukK-Mla2UTaQ
```

Instead, we can use base 58 and the Bitcoin alphabet, which also eliminates
ambiguous characters such as 0 and O. That encoding gives us 23-character long
strings which are URL friendly and can be selected at once just by double
clicking:

```
Q9oGv7rbFEExoSR4FFzgiL
```

## Prior art

- Python's own [UUID module](https://docs.python.org/3/library/uuid.html)
- KSUID implementations: [svix-ksuid](https://pypi.org/project/svix-ksuid/) and [cyksuid](https://pypi.org/project/cyksuid/)
- [ulid.py](https://pypi.org/project/ulid-py/)
- [timeflake](https://pypi.org/project/timeflake/)
- [snowflake-id](https://pypi.org/project/snowflake-id/)
- [cuid2](https://pypi.org/project/cuid2/)
- [django-extension's own ShortUUIDField](https://django-extensions.readthedocs.io/en/latest/field_extensions.html)

## Further reading

I've probably spent way too much time thinking about IDs both from the developer
and user experience perspectives, as well as from performance and security
standpoints and written a couple of blog posts about it:

- [Features of ID formats for web applications](https://hernandis.me/2023/02/26/features-of-id-formats-for-web-applications.html)
- [Benchmarking ID generation libraries in Python](https://hernandis.me/2023/03/06/benchmarking-id-generation-libraries-in-python.html)
