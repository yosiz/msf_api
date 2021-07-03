# msf_api

this is still very much work in progress,
the aim is to provide a simple python interface to the MSF Api.

## Usage

```
from msf_api import MsfApi

key="YOUR_API_KEY"
api = MsfApi(key)

# get character info
char_info = api.chars().get_character_info("AdamWarlock")


# get the total gear costs for a character to reach a gear level from a specified gear level
material_cost = api.get_gear_req("Nebula",10,15)
```

## Currently Implemented

- characters (Partial)
- Items (Partial)
- Raids (Partial)

## design decisions

- statically define the api endpoints instead of automatically generating stubs
  may change int he future.
- split each API endpoint into an independent sub module
  this way, each module can be expanded without any impact to the other modules.
  Also, Readability :)

## TODO

add the rest of the MSF API parts
add more higher level functions for accomplishing advanced logic

## Links

https://pypi.org/project/msf-api/0.0.1/
https://github.com/yosiz/msf_api
