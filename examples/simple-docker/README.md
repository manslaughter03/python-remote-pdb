## PDB remote debugger in docker container

# Build simple python app docker image

```bash
make
```

# Run in debug mode by overloading docker entrypoint

```bash
docker run -it --rm -e "REMOTE_PDB_HOST=0.0.0" -e "REMOTE_PDB_PORT=5555" -p 5555:5555 --entrypoint "sh" example-pkg:0.0.1 -c 'apk update && apk add git && pip install git+https://github.com/manslaughter03/python-remote-pdb && python -m remote_pdb -m example_pkg'
```
