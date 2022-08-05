import os

from dynaconf import Dynaconf

HERE = os.path.dirname(os.path.abspath(__file__))

settings = Dynaconf(
    envvar_prefix="fastapifromtemplate",
    preload=[os.path.join(HERE, "default.toml")],
    settings_files=["settings.toml", ".secrets.toml"],
    environments=["development", "production", "testing"],
    env_switcher="fastapifromtemplate_env",
    load_dotenv=False,
)


"""
# How to use this application settings

```
from fastapifromtemplate.config import settings
```

## Acessing variables

```
settings.get("SECRET_KEY", default="sdnfjbnfsdf")
settings["SECRET_KEY"]
settings.SECRET_KEY
settings.db.uri
settings["db"]["uri"]
settings["db.uri"]
settings.DB__uri
```

## Modifying variables

### On files

settings.toml
```
[development]
KEY=value
```

### As environment variables
```
export fastapifromtemplate_KEY=value
export fastapifromtemplate_KEY="@int 42"
export fastapifromtemplate_KEY="@jinja {{ this.db.uri }}"
export fastapifromtemplate_DB__uri="@jinja {{ this.db.uri | replace('db', 'data') }}"
```

### Switching environments
```
fastapifromtemplate_ENV=production fastapifromtemplate run
```

Read more on https://dynaconf.com
"""
