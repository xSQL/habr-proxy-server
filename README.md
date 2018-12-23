# Habr.com proxy server

Simple proxy server to all pages & static files

# How to Use

1. Clone repo into apps folder of your projects

```bash
$git clone https://github.com/xSQL/habr-proxy-server.git ./habr
cd ./habr
```

2. Create & activate virtualenv

```bash
$pyvenv venv
$source venv/bin/activate
```

3. Install dependencies

```bash
(venv)$ pip install -r requirements
```

4. Run server

```bash
(venv)$ python server.py
```

5. Open into browser 127.0.0.1:8000 (port may be changed in settings.py)

# Testing

To test modified parser run

```bash
(venv)$ python -m unittest
```
