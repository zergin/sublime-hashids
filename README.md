# Sublime Hashids

Encode and decode hashids (hashids.org).

## Description

This plugin allows encoding and decoding ids using [hashids.org](http://hashids.org/) implementation.

## Instalation

 - via PackageControl: https://packagecontrol.io/packages/Hashids
 - or by cloning https://github.com/zergin/sublime-hashids.git into sublime package directory

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

### Using without project configuration

Plugin supports providing inline salt through key-value pairs in de/encoded strings. Examples:

```
salt=abc;ids=1,2,3 => G7CYSG
salt=abc;1,2,3 => G7CYSG
```

```
salt=abc;hash=G7CYSG => 1,2,3
salt=abc;G7CYSG => 1,2,3
```

## License

&copy; 2015 Marcin Kurzyna <[m.kurzyna@gmail.com](m.kurzyna@gmail.com)>.
MIT license, see the LICENSE file.
