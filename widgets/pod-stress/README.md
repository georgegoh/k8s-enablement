pod-stress
==========

Consume CPU and/or memory as required, to stress test these parameters in a pod.

This pod is a simple Flask app that accepts RESTful API calls:
* `GET /` : returns text "cpu_workers: N, mem_workers: M Mi".
* `POST /cpu_workers?value=N` : create `X` number of workers to stress the CPU.
* `POST /mem_workers?value=M` : create `M` number of workers to stress the memory.

See https://linux.die.net/man/1/stress to understand the utility that is used under the hood.

Running as a container
----------------------

If your network allows you to pull from docker.io, you can simply run the container like so:

```bash
docker run -p 8080:5000 georgegoh/pod-stress
```

And use curl to make API calls, .e.g.:

```bash
curl -X POST http://localhost:8080/cpu_workers\?value\=2
```

Examine the effect of your calls using the `docker stats` command.

Running in Kubernetes
---------------------

See the manifests in the `examples` directory for sample manifests.

Building
--------

To build the docker image locally:

```bash
make build
```

And run it like so:

```bash
make run
```