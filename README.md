# Sublime Hashids

Encode and decode hashids (hashids.org).

## Description

This plugin allows encoding and decoding ids using [hashids.org](http://hashids.org/) implementation.

## Usage

- initialize configuration (set salt)
  Project -> Hashids -> Add project settings
- encode/decode ids
- ...
- profit!

### Initialize configuration


```json
{
    "settings":
    {
        "hashids":
        {
            "salt": "your-salt-here"
        }
    }
}
```

## License

&copy; 2015 Marcin Kurzyna <[m.kurzyna@gmail.com](m.kurzyna@gmail.com)>.
MIT license, see the LICENSE file.
